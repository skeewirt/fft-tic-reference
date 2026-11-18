# SpriteLookAttributes

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140673300`
- **Rows:** 170 rows of 4 bytes
- **Keyed by:** look (sprite shape) number; no bound in the code (row 170 is the next table)
- **Read by:** [BattleAnim_SelectMotion](../functions/BattleAnim_SelectMotion.md), [CharaAnim_ReadStep](../functions/CharaAnim_ReadStep.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md), [CharaRender_DrawFrame](../functions/CharaRender_DrawFrame.md), [CharaRender_SetSlotRequest](../functions/CharaRender_SetSlotRequest.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [SceneUnits_SaveRestore](../functions/SceneUnits_SaveRestore.md)
- **Row layout:** [SpriteLookAttributeRow](../structs/SpriteLookAttributeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per look: which frame file and animation sequence file kind it uses, the pose remap flag and a scale byte.

## Behavior

- V: read by about twenty functions of the sprite renderer and animation code.
- V: 20 functions read this table (cross-references in the database); the first ten are linked.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: what scale_byte measures
