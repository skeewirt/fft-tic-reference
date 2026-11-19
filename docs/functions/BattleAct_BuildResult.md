# BattleAct_BuildResult

- **Address:** `0x140281CE8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleAct_BuildResult(uint8 unit, uint8 *result)`
- **Callers:** BattleAct_Step, sub_14038ABA4
- **Callees:** sub_140281C24, sub_140282754, Battle_ResolveAction, Action_SetWeaponItem, sub_140281A64, sub_14030A410

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves the unit's queued action against its targets and fills the scene object's result record (obj +0x1A8): target list, flags and the effect word +0x14 the presentation is keyed by.

## Behavior

- V: the target scan (sub_140281C24, sub_140282754), then Battle_ResolveAction once per target; result +1 = target count, +2.. = targets.
- V: the effect word +0x14 (obj +0x1BC) = the queued action's ability word (unit +0x1A2, read at 0x14028211B and 0x140282185), or WORD4 of the formula state (a weapon spell, < 256) with +0x17 = 1, or 0 when byte_1407B078C is set.
- V: when xmmword_1407B0790's low byte is set (not negative, no weapon spell) it writes the sentinel 512 with +0x17 = 1 and +0x12 = 1 (0x1402821DD).
- V: rejects actor slots >= 21; resets the actor's own result record at record[actor] +0x1BE (sub_14030A410 at 0x140281D80) and the shared working record xmmword_14186AFC0 (0x140281D9C).
- V: builds a 21-byte target mask: sub_140281A64(actor, out, &count, mask) when dword_14186AF9C is set (a charged or special action), else sub_140281C24(request, mask); a multi-target action (dword_1411A7024 != 0) orders the targets by distance from the actor with sub_140282754.
- V: loops j = 0..20 and calls Battle_ResolveAction(request, j) at 0x140281F0D for each mask byte != 0xFF; the summary holds the actor slot at +0, the target count at +1, the target list at +2, the ability id at +20, result flags at +18 / +24 and the hit count at +26.
- V: returns 1 when nothing was hit, 0 when at least one target was resolved, -1 on bad input.

## State touched

- Calls: [Battle_ResolveAction](Battle_ResolveAction.md), [Action_SetWeaponItem](Action_SetWeaponItem.md), [sub_140281A64](sub_140281A64.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [BattleAct_Step](BattleAct_Step.md)

## Notes

In game 2026-10-30 an ability of id 512 reached this record as 512: the stock sentinel value. sub_140282754 is the distance sort: it reads the actor's tile (record +0x4F / +0x50) and each candidate's, in ascending Manhattan distance. Earlier sheet name: Battle_ResolveTargets.

## Open questions

What sets xmmword_1407B0790's low byte (the sentinel case): I, a reflected or bounced effect. The difference between the dword_14186AF9C path and the normal path (charged or immediate action).
