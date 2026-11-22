# Deployment_PlaceUnitAtCursor

- **Address:** `0x1401F3128`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Deployment_PlaceUnitAtCursor(DeploymentState *state, char check_commands)`
- **Callers:** sub_1401EF0D8, sub_1401F5CEC
- **Callees:** sub_1402607E4, sub_1403033CC, sub_140217630, SceneVar_Read, sub_140152494, SceneObject_FindBySlot, SceneUnit_Release, SceneTask_WaitFrame, Deployment_CompactPlaced, sub_1401F3858, Deployment_CountPlaced, Battle_JoinUnitAndLoad

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Places the deployment candidate under the carousel glove on the cursor tile: frees the unit standing there, joins the candidate and adds it to the placed list.

## Behavior

- V: the candidate index is state +0x730; it returns 0 when that is negative or not below the candidate count +0x724; the candidate's roster index is the dword at state +0x49C + 12 x index.
- V: the unit standing on the cursor tile (dword_140C6AFB8 / dword_140C6ADAC / dword_140C6AFBC) is the scene object sub_1402607E4 finds there; its roster index is its record's +2 when the record's slot byte is not 0xFF.
- V: when sub_1403033CC finds the candidate already placed it returns 1 if that unit is the one on the tile, else it shows message 0x77 and returns -1.
- V: with check_commands set, sub_140217630 must accept the candidate (its battle commands) or it returns -2.
- V: with a unit on the tile: when scene variable 511 is set and that unit is roster index 0 it shows message 116 (0x74) and returns 0; otherwise it frees that unit's drawn unit (SceneObject_FindBySlot, SceneUnit_Release), sets its record's slot byte and +0x1B5 to 0xFF, waits 4 frames and drops its roster index from the placed list (Deployment_CompactPlaced, sub_1401F3858).
- V: with no unit on the tile it shows message 118 (0x76) and returns 0 when the placed count (Deployment_CountPlaced) has reached the capacity +0x40.
- V: then Battle_JoinUnitAndLoad(state, roster index, -1), the cursor tile into +0x65..+0x67, and the joined unit's roster index read through state +0x18 (its scene object) +0x148 (its record) +2 at 0x1401F330F, with no test of +0x18, into the first free entry of the placed list (+0x44), whose index goes to +0x10.
- V (seen live 2026-11-22): when the join builds no drawn unit (every drawing slot in use) +0x18 is 0 and the read at 0x1401F330F faults inside a game task; the game freezes on the deployment screen. In 'Change Formation and Retry' the deployment re-places the locked unit through this function (sub_1401EF0D8) right after the setup (record BattleRetriesRestoreTheirOwnCapture).

## State touched

- Calls: [sub_140217630](sub_140217630.md), [SceneVar_Read](SceneVar_Read.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [SceneUnit_Release](SceneUnit_Release.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [Deployment_CompactPlaced](Deployment_CompactPlaced.md), [sub_1401F3858](sub_1401F3858.md), [Deployment_CountPlaced](Deployment_CountPlaced.md), [Battle_JoinUnitAndLoad](Battle_JoinUnitAndLoad.md)

## Referenced by

- Observed behaviours: [BattleRetriesRestoreTheirOwnCapture](../behaviors/BattleRetriesRestoreTheirOwnCapture.md)

## Notes

Name is ours.

## Open questions

None recorded.
