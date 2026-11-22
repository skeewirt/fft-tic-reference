# SortieScreen_SetArea0Face

- **Address:** `0x140147D94`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void SortieScreen_SetArea0Face(UIAddonFFTOBattleSortie2 *screen, int position, int face, int variant, bool lock)`
- **Callers:** sub_1401F3858 (the column and its hide loop)
- **Callees:** UIName_Key, GUINode_StopState, GUINode_FindState, GUINode_PlayState, FaceNumber_Remap, FaceTexture_FormatName, GUIWidget_EnsureSlotGroup, UIName_Assign

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows one portrait box of the deployment screen's first area with a unit's face, or hides it (face -1).

## Behavior

- V: returns at once when the screen's root (+0x48) is 0 or the position is above 4; reads the box node, Eye and Mouth at +0x310 + 0x30 x position and returns when any is 0.
- V: face -1: stops ShowUnit and plays HideUnit on the box. Otherwise plays ShowUnit, formats the face texture name (FaceNumber_Remap, FaceTexture_FormatName) and, when it differs, assigns it to the Eye and Mouth parts (the screen's widget +0x18 gets the slot group first).
- V: then ShowLock or HideLock by `lock`.
- V: reads only +0x18, +0x48 and the boxes of the screen object.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [FaceNumber_Remap](FaceNumber_Remap.md), [FaceTexture_FormatName](FaceTexture_FormatName.md), [GUIWidget_EnsureSlotGroup](GUIWidget_EnsureSlotGroup.md), [UIName_Assign](UIName_Assign.md)

## Referenced by

- Observed behaviours: [DeploymentPortraitColumnBoxes](../behaviors/DeploymentPortraitColumnBoxes.md)

## Open questions

None recorded.
