# SceneUnit_Release

- **Address:** `0x14026E0F4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void SceneUnit_Release(SceneObject *unit)`
- **Callers:** EventScript_Run (the case that takes a unit off: slot byte 0xFF), sub_1401F0948, sub_1401F22D0, sub_1401F3128 (deployment: a unit taken back off its cell), SceneUnits_ReleaseAll, SceneObjects_StepStates
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Frees a drawn unit's scene unit (drawing slot) and, when no other drawn unit uses the same look pool record, frees that record too.

## Behavior

- V: clears the in-use dword of scene unit [unit+8] (0x140D30030 + 1352 x index).
- V: walks g_SceneObjectList for another node with the same pool index (byte +9) whose scene unit is still in use; when none is found it clears the pool record's first byte (g_LookPool + 13014 x pool), freeing it; then unlinks the node.

## Referenced by

- Called by: [SceneObjects_StepStates](SceneObjects_StepStates.md), [SceneUnits_ReleaseAll](SceneUnits_ReleaseAll.md)

## Notes

Behavior: SixteenSceneUnitsComeOnlyFromTheLookQueue.

## Open questions

None recorded.
