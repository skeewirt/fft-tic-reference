# Battle_ApplyActionResult

- **Address:** `0x14030A488`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_ApplyActionResult(int slot)`
- **Callers:** `Battle_ApplyActionResults` (`0x1402067DF`), `sub_1402029DC` (`0x140202A53`, `0x140202AA6`), `sub_14020435C`, `sub_14020BFD4`, `sub_14030C1C4`,
- **Callees:** `Battle_StatusResolve`, `Status_FilterPendingSets`, `Battle_AwardActorJp`, `sub_140278C1C`,

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the pending action result of one unit to that unit: HP/MP damage and healing, stat changes, Brave/Faith
changes, EXP/level changes, status sets/clears and the death check. This is the function that moves live HP.

## Behavior

- V: `slot` must be 0..20 and `rec[1] != 0xFF`; it sets `qword_14186AF68 = rec` and
  `qword_14186AF70 = rec + 0x1BE` (the result block).
- V: reads `curHP = u16(rec+0x30)`, `maxHP = u16(rec+0x32)`, `curMP = u16(rec+0x34)`, `maxMP = u16(rec+0x36)`.
- V: `newHP = clamp(curHP + i16(result+8) - i16(result+6), 0, maxHP)`, then capped at 999; writes it back to the HP field at
  `0x14030A62F`.
- V: `newMP = clamp(curMP + i16(result+12) - i16(result+10), 0, maxMP)`, capped 999; writes at
  `0x14030A638`.
- V: applies result byte +20 to `+0x3A` Speed (cap 50), +21 to `+0x41` (cap -1 = none), +22 to `+0x38` PA,
  +23 to `+0x39` MA (cap 99), +24 to `+0x2B` Brave (cap 100, sign in bit 7), +25 to `+0x2D` Faith (cap 100).
- V: result +42 is applied to `+0x28` (EXP) as a signed byte (bit 7 = subtract); afterwards `sub_140278AD8` is
  called: at 100 EXP the level byte `+0x29` goes up by one (cap 99) and EXP resets to 0.
- V: result +43 != 0 calls `Battle_AwardActorJp`; result +18 bit 7 = level down, bit 8 = level up (handled
  through `sub_140278C1C`).
- V: result +18 bit 1 = "clear all statuses": clears `+87..91`, `+92..96`, `+97..101`, the countdown area
  `+102..117`, `+495..499`.
- V: `Battle_StatusResolve` + `Status_FilterPendingSets` handle `result+29..33` (sets) and `result+34..38`
  (clears); `+0x1EF..0x1F3` changes are folded into `+0x61..0x65` by `Battle_StatusRefresh`.
- V: when `newHP == 0` and the unit has none of `+97 & 0x60` / `+98 & 1`, it increments `+0x18C`, calls
  `sub_14030C110(2)` and returns -1 when `rec+0x1B4` bit 7 is set (death).
- V: result message ids 440/444/446/450/451/452 select the follow-up (item return, steal, etc.) in the first half.
- V (from the action-flow review): after the HP/MP write it sets `[rec+0x1F5] = 0xFF` (HP/MP changed flag) and applies the six
  stat/status bytes through `sub_14030C080`; result `[+18]` bit 0x8000 subtracts HP damage from a shield pool (`qword_14186B020`,
  indexed by `(rec[+0x1EE] >> 4) & 3`), bit 0 refills that pool to max HP, bit 3 (0x8) returns an item, bit 0x4000 runs `sub_140271C50`
  (death/stone check); `sub_14030C87C(slot, 0/1)` at `0x14030A518` refreshes status and clears HP on petrify (`+97 & 0x20`).
- V: returns -1 when `rec+0x1B4` is negative (KO/removed target), else 0.
- I: `+0x1B4` bit 7 marks a unit whose 0 HP is final (monster/guest); the exact rule is not decoded.
- V (2026-11-10): the after-damage reaction chain is the tail of this function (its helper calls are at 0x14030AB03 and 0x14030AB2C). Unless the formula result's type byte (0x1407B0788) is 7 or sub_14030AF88 answers non-zero, it tests the passive bits of the unit held in g_BattleActingUnit in a fixed order: +0x94 bit 0x80 gives reaction 422, 0x40 gives 423, 0x20 gives 424, 0x02 gives 428; +0x95 bit 0x40 gives 431, 0x20 gives 432, 0x10 gives 433, 0x08 gives 434 (through sub_14030BE68); +0x96 bit 0x40 gives 439 and 0x10 gives 441. The first bit found goes to the Brave-roll helper sub_14030BE18 with that id; only one reaction is chosen.
- V: sub_14030BE18 needs the action block's flag byte +39 bit 7, skips the roll in a simulation, and stores the reaction id at block word +16 and copies the HP result (word +6) to word +40; sub_14030BE68 also needs status byte +0x63 mask 0x01. The executor that runs the chosen reaction is sub_1403095E4 (called from Battle_ResolveAction); see AfterDamageReactionChain and PassiveAbilitiesAreAPerUnitBitMap.

## State touched

- Calls: [Battle_StatusResolve](Battle_StatusResolve.md), [Battle_AwardActorJp](Battle_AwardActorJp.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [Battle_ApplyActionResults](Battle_ApplyActionResults.md), [sub_14020435C](sub_14020435C.md), [sub_14020BFD4](sub_14020BFD4.md), [sub_14030C704](sub_14030C704.md)
- Observed behaviours: [AfterDamageReactionChain](../behaviors/AfterDamageReactionChain.md), [PoisonAndRegenActAtTheEndOfTheUnitsTurn](../behaviors/PoisonAndRegenActAtTheEndOfTheUnitsTurn.md)

## Notes

The other half of the result pipeline is `Battle_ResolveAction` (fills the result block) and
`Battle_StatusApply` (status side). `Battle_ApplyActionResult` must run after both.

## Open questions

What `+0x1B4` bit 7 means exactly, and whether the `+0x1B4` bit 6 "no-target" rule is the guest/ally rule.
- The six `sub_14030C080` destinations (+0x2B, +0x2D, +0x38, +0x39, +0x3A, +0x41) beyond the ones named above, and the owner of the shield pool `qword_14186B020`.
