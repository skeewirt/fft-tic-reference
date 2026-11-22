# BattleRetriesRestoreTheirOwnCapture

- **Kind:** observed behaviour
- **Scope:** the battle System Menu's Retry choices
- **Area:** [Save data](../areas/save-data.md)
- **Affects:** [Battle_SaveCapture](../functions/Battle_SaveCapture.md), [Battle_RestoreCapture](../functions/Battle_RestoreCapture.md), [SceneUnits_SaveRestore](../functions/SceneUnits_SaveRestore.md), [sub_1401EE9B4](../functions/sub_1401EE9B4.md), [Deployment_PlaceUnitAtCursor](../functions/Deployment_PlaceUnitAtCursor.md), [Battle_JoinUnitAndLoad](../functions/Battle_JoinUnitAndLoad.md), [Battle_AddJoinedUnit](../functions/Battle_AddJoinedUnit.md), [sub_1400C4360](../functions/sub_1400C4360.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Both Retry choices rebuild the battle from a battle capture, not from the battle as it stands: 'Change Formation and Retry' restores a capture taken after the battle's own units were built and before any party unit joined, then runs the deployment setup and re-places the locked unit on its old tile; 'Retry from Start of Battle' restores the capture taken after Commence. The game keeps one capture region and several autosave entries of it, and restores the one the choice needs.

## Behavior

- V (seen live 2026-11-22, a trace of Change Formation and Retry in a story battle): SceneUnit_Release once for every drawn unit, then Battle_RestoreCapture, then the deployment setup sub_1401EE9B4, then Deployment_PlaceUnitAtCursor for the locked unit at its old tile (no unit standing there), which joins it through Battle_JoinUnitAndLoad and Battle_AddJoinedUnit.
- V (seen live 2026-11-22): the capture Change Formation restored held the battle's own units and no party unit (it was taken while the deployment screen opened, before the first placement); the capture Retry from Start of Battle restored held the placed party (taken after Commence). Both rebuild the battle's own entries first (Battle_BuildEntryUnits runs again).
- V: the capture region starts at 0x1408167A0; Battle_SaveCapture copies the 21 unit records into it at 0x140898134 (region +0x81994); a battle autosave entry's payload is the region after a 340-byte header, so its unit records sit at payload +0x81AE8.
- V: the entry names come from sub_1400C4360: 'resume_en%02d_%s.sav' for points 2..4 (en00..en02) with the part names main, world, attack, fturn, 'resume_enbtl_%s.sav' for point 1, 'resume_enwm_main.sav' for point 0; loading a mid-battle save reads every entry of the battle (main, attack, fturn, world) at once (seen live).
- V: Battle_JoinUnitAndLoad sets the deployment state's +0x18 only when it finds the joined unit's drawn unit, and Deployment_PlaceUnitAtCursor reads through it with no test: a Change Formation whose restored drawing slots are all in use faults at 0x1401F330F and the game freezes on the deployment screen (seen live 2026-11-22).
- I: which Battle_SaveCapture call (the battle state 75 one or the 'J' step one in sub_140210AF0) takes each capture.

## Open questions

? which entry the game copies into the region for each Retry choice; ? the 'world' entry's role in a battle.
