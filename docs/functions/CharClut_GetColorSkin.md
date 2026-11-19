# CharClut_GetColorSkin

- **Address:** `0x1401E3A10`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int CharClut_GetColorSkin(int key)`
- **Callers:** SceneUnit_BuildFromQueueEntry, sub_1401009E8
- **Callees:** NxdRegistry_Find, NxdTable_GetEntryByKeys2, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the chara_color_skin column (+0x10) of the CharCLUT row (key, 0) and resolves it.

## Behavior

- V: looks up CharCLUT row (key, 0), reads +0x10 and passes it to CharaColorSkin_Resolve.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Notes

Name is ours.

## Open questions

None recorded.
