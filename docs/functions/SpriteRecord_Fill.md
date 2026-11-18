# SpriteRecord_Fill

- **Address:** `0x1400FB2A4`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `__int64 SpriteRecord_Fill(SpriteRecord *rec, int job, int shape, short palette, int a5, int a6, int slotArg, unsigned flagWord)`
- **Callers:** PreviewUnit_BuildRecord, sub_140172B70, sub_140177004, SceneUnit_FillSpriteRecord
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the sprite record fields and derives the pose id from the slot argument.

## Behavior

- V: +0 = job/party index, +4 = shape, +8 = palette, +10 = 0, +16 = 0, +20 = flagWord, +28 = -1 (word).
- V: +12 = (word_140672CF8[a5 % 4] & 2) != 0 (the record flag bit).
- V: +24 (pose / animation id) = word_140672D7A[4 * (a5 % 4)] when slotArg is 4, otherwise slotArg + word_140672D98[a5 % 4]. For the tree (a5 = 0, slotArg = 4) the pose is 2 and the record flag is 0.

## Referenced by

- Called by: [PreviewUnit_BuildRecord](PreviewUnit_BuildRecord.md), [SceneUnit_FillSpriteRecord](SceneUnit_FillSpriteRecord.md)
- Observed behaviours: [SpriteNumberStoreWidths](../behaviors/SpriteNumberStoreWidths.md)
- Reads tables: [SpriteDirection16MirrorFlags](../tables/SpriteDirection16MirrorFlags.md), [SpriteDirectionTables](../tables/SpriteDirectionTables.md)

## Notes

The table words (0x140672CF8, 0x140672D7A, 0x140672D98) are small selectors: for index 0 they read 0, 2 and 0.

## Open questions

None recorded.
