# SpriteHdEntryByShape

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x1407151F0`
- **Rows:** 170 rows of 4 bytes
- **Keyed by:** sprite shape id (ids above 169 are rejected)
- **Read by:** [CharaRender_BuildAtlasTexture](../functions/CharaRender_BuildAtlasTexture.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [Unit_GetFaceIndex](../functions/Unit_GetFaceIndex.md), [sub_140260CF0](../functions/sub_140260CF0.md), [sub_14026C2E8](../functions/sub_14026C2E8.md)
- **Row layout:** [SpriteHdEntryRow](../structs/SpriteHdEntryRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

First HD sheet entry of every look in the g2d pack.

## Behavior

- V: the monster face index table is addressed through a virtual base 0x140715378, 392 bytes inside this table.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
