# SortieScreen_SetArea1Face

- **Address:** `0x1401480D4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void SortieScreen_SetArea1Face(UIAddonFFTOBattleSortie2 *screen, int position, int face, int variant)`
- **Callers:** sub_1401F3858 (the column and its hide loop)
- **Callees:** UIName_Key, GUINode_StopState, GUINode_FindState, GUINode_PlayState, FaceNumber_Remap, FaceTexture_FormatName

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows one portrait box of the deployment screen's second area with a unit's face, or hides it (face -1); SortieScreen_SetArea0Face without the lock icon.

## Behavior

- V: returns when the screen's root (+0x48) is 0 or the position is above 3; the box at +0x328 + 0x30 x position (node, Eye, Mouth).
- V: face -1 plays HideUnit, otherwise ShowUnit and the face texture on Eye and Mouth, as SortieScreen_SetArea0Face.
- V: reads only +0x18, +0x48 and the boxes of the screen object.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [FaceNumber_Remap](FaceNumber_Remap.md), [FaceTexture_FormatName](FaceTexture_FormatName.md)

## Referenced by

- Observed behaviours: [DeploymentPortraitColumnBoxes](../behaviors/DeploymentPortraitColumnBoxes.md)

## Open questions

None recorded.
