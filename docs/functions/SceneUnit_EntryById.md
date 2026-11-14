# SceneUnit_EntryById

- **Address:** `0x1402EFF34`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void *SceneUnit_EntryById(unsigned id)`
- **Callers:** Unit_GetSpriteSetId, SceneUnit_FillSpriteRecord, sub_1402C1628
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns a scene unit entry of the selector scenes (564 bytes each at 0x1408E6CB0) by its id, or null.

## Behavior

- V: id 0 to 15 and a scene id word (0x141848BB0) of 21, 43, 44 or 51 give 0x1408E6CB0 + 564 * id; anything else null.

## State touched

- Reads: [g_SceneIdWord](../globals/g_SceneIdWord.md)

## Referenced by

- Called by: [SceneUnit_FillSpriteRecord](SceneUnit_FillSpriteRecord.md), [Unit_GetSpriteSetId](Unit_GetSpriteSetId.md), [sub_1402C1628](sub_1402C1628.md)

## Notes

The name is ours (IDB: sub_1402EFF34).

## Open questions

? the screens of scene ids 21, 43, 44 and 51.
