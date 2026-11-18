# Battle_StatusApply

- **Address:** `0x14030CAA8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char Battle_StatusApply(int slot, int source)`
- **Callers:** `Battle_StatusResolve` (`0x14030C937`)
- **Callees:** `Status_FilterPendingSets`, `Battle_StatusRefresh`, `Unit_SetStatusCountdown`, `sub_1401FB064`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Converts the pending status sets of one unit's action result block into applied status bits, after filtering them
against the unit's innate/immunity sets. Handles the two team-changing statuses.

## Behavior

- V: the unit record is `rec = g_BattleUnitTable + 512*slot`; the result block is `rec + 0x1BE`, so pending sets
  are `rec+0x1DB..0x1DF` (result +29..33) and pending clears `rec+0x1E0..0x1E4` (result +34..38).
- V: for each of the 40 status bits set in the pending sets: skip it when the unit's `+0x1EF..0x1F3` already has
  it and a 16-byte filter table at `byte_140788DFC` says it is blocked; otherwise copy the corresponding 5-byte
  mask from `aDefghijklmnopq` into the pending clears, run `Status_FilterPendingSets(source)`, clear the effective
  status byte through `Battle_StatusRefresh`, set the bit in `+0x1EF..0x1F3`, call `Unit_SetStatusCountdown`, and
  play the status icon update `sub_1401FB064(status+1, on/off, slot)`.
- V: status 19 clears `rec[0x2E]`.
- V: statuses 9 and 34 (Charm/Recruit) copy the source unit's team bits: `rec[5]` bits 4..5 are set to the
  source's, and `rec[0x1EE] = (src[5] & 0x30) | (rec[0x1EE] & 0xC7)`; status 9 also zeroes result +16 and
  `rec[0x1EC]`.
- V: after the loop, `rec[0x61..0x65] = rec[0x57..0x5B] | rec[0x1EF..0x1F3]`.
- I: the two `dword_14186AF80` guards suppress the effect while an ability is being previewed.

## State touched

- Calls: [Battle_StatusRefresh](Battle_StatusRefresh.md), [sub_1401FB064](sub_1401FB064.md)

## Referenced by

- Called by: [Battle_StatusResolve](Battle_StatusResolve.md)
- Observed behaviours: [KoLeavesSomeStatusesOnTheUnit](../behaviors/KoLeavesSomeStatusesOnTheUnit.md), [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md), [StatusLoopsInflictCopyAndBattleTableLifetime](../behaviors/StatusLoopsInflictCopyAndBattleTableLifetime.md), [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md)
- Reads tables: [AbilityAux](../tables/AbilityAux.md), [AbilityKind6_PassiveIndex](../tables/AbilityKind6_PassiveIndex.md)

## Notes

The status ids here are 0-based (bit 0 = first status). `Unit_SetStatusCountdown` uses the same id, and for ids
24..39 writes a countdown byte at `rec+102+(id-24)`.

## Open questions

The id -> name table for the 40 statuses (not a string in the exe).
