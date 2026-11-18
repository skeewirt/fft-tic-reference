# ResourceHandle_FinishLoad

- **Address:** `0x1400965C4`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `void ResourceHandle_FinishLoad(ResourceHandle *h, int result)`
- **Callers:** ResourceHandle_LoadNow, sub_1400914EC, sub_140092304, sub_140095444
- **Callees:** ResourceHandle_ResolvedPath, sub_14041FB00

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ends a load: releases the reader, sets the final state, tags a localised file, and frees the resolved path string.

## Behavior

- V: state +84 = 1; on failure stores the error and calls vtable +80.
- V: on success with flag 8 set and 0x40000 clear: looks for '.ja.', '.en.', '.fr.', '.de.', '.cs.', '.ct.' or '.ko.' in the resolved path (ResourceHandle_ResolvedPath) and keeps flag 8 only when one is found.
- V: deletes the reader (+48) and, unless flag 0x4000, frees the resolved path object (+40).
- V: the file buffer (+56) is not freed here.

## State touched

- Calls: [ResourceHandle_ResolvedPath](ResourceHandle_ResolvedPath.md)

## Referenced by

- Appears in flows: [NxdTableLoad](../flows/NxdTableLoad.md)
- Called by: [ResourceHandle_LoadNow](ResourceHandle_LoadNow.md)
- Observed behaviours: [TextLanguage](../behaviors/TextLanguage.md)

## Notes

So the resolved path (with its language token) is readable during slot 8, and the buffer stays with the handle.

## Open questions

None recorded.
