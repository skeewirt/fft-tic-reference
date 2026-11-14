# Battle_ResolveTargets

- **Address:** `0x140281CE8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64_t Battle_ResolveTargets(int actorSlot, int64_t *outSummary)`
- **Callers:** `Battle_ExecuteAction` (`0x140206A55`), `sub_14038ABA4` (`0x14038AC2C`)
- **Callees:** `sub_14030A410` (reset result), `sub_140281A64`, `sub_140281C24`, `sub_140282754`, `Battle_ResolveAction` (`0x140281F0D`), `Action_SetWeaponItem`, `sub_140282234`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the target set for one action request and resolves the request against every target, producing one
result record per target plus a summary of the whole action.

## Behavior

- V: rejects actor slots >= 21; resets the actor's own result record at `record[actor]+0x1BE`
  (`sub_14030A410` at `0x140281D80`) and the shared working record `xmmword_14186AFC0`
  (`0x140281D9C`).
- V: builds a 21-byte target mask:
  - if `dword_14186AF9C` is set (charged/special action): `sub_140281A64(actor, out, &count, mask)`;
  - else if the request type is 0 or 6 and the ability id < 368: `sub_140281C24(request, mask)`;
  - otherwise `sub_140281C24` still handles the area.
- V: orders the targets by distance from the actor with `sub_140282754(mask, record[actor])` when the
  action is multi-target (`dword_1411A7024 != 0`).
- V: loops `j = 0..20`; for each mask byte != 0xFF calls `Battle_ResolveAction(request, j)` at
  `0x140281F0D`.
- V: fills the summary at `outSummary`: actor slot at +0, target count at +1, target list at +2,
  ability id at +20, result flags at +18/+24, hit count at +26.
- V: returns 1 when nothing was hit, 0 when at least one target was resolved, -1 on bad input.

## State touched

- Calls: [sub_140281A64](sub_140281A64.md), [Battle_ResolveAction](Battle_ResolveAction.md), [Action_SetWeaponItem](Action_SetWeaponItem.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [Battle_ExecuteAction](Battle_ExecuteAction.md)

## Notes

`sub_140282754` is the distance sort: it reads the actor's tile (`record+0x4F/+0x50`) and each
candidate's tile, and inserts them in ascending Manhattan distance.

## Open questions

- The distinction between the `dword_14186AF9C` path and the normal path (charged vs immediate action).
