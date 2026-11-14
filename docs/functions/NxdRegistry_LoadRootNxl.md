# NxdRegistry_LoadRootNxl

- **Address:** `0x1403D33F0`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `int NxdRegistry_LoadRootNxl(NxdRegistry *reg, FileInfo *src, ...)`
- **Callers:** sub_1403D32DC
- **Callees:** Str_Format, sub_140011750 (allocator), sub_140037CA4, sub_140091124 (file open), sub_1400E1ADC (hash insert)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the table registry from the root.nxl list: one table object per listed table, keyed by table id, each pointing at its .nxd file. Every nxd table in the game (jobs, abilities, UI, scripted entries) is reachable through the registry this fills.

## Behavior

- V: skips the first 3 bytes of the file (byte-order mark), then walks CR/LF separated lines; any line whose first character is '#' is skipped, which drops the `#NXLT,1` header line.
- V: counts the remaining lines, then allocates one zeroed array of 80-byte table objects (count stored in the registry at +40, array at +32); returns an error code if the allocation fails.
- V: per line, splits on commas: field 1 is the table name, field 2 is the table id (parsed as a number). Only these two fields are read here; the row-count and kind columns are not consumed by this function.
- V: builds the data file name as `<directory>/<name>.nxd`, where the directory comes from the source file info, and asks the file manager to open it with a load callback pair.
- V: fills each table object: +0 owner, +8 id, +12 state = 1 (not yet loaded), +48 file object; then inserts (id -> object) into the registry's hash map.
- V: returns 0 on success.
- I: the table object's row array (+16), row count (+40) and data pointer (+56) are filled later when the file finishes loading, not here.

## State touched

- Calls: [Str_Format](Str_Format.md)
- Writes: [NxdTable.id](../structs/NxdTable.md#id), [NxdTable.state](../structs/NxdTable.md#state), [NxdTable.handle](../structs/NxdTable.md#handle)

## Referenced by

- Appears in flows: [NxdTableLoad](../flows/NxdTableLoad.md)
- Called by: [NxdHandle_OnLoaded](NxdHandle_OnLoaded.md)

## Notes

Table object layout used by the readers: +8 id, +12 state (2 or 3 = usable), +16 row array, +40 row count, +48 file object, +56 nxd data. A live walk of the registry found 246 entries whose ids and row counts match the lines of root.nxl. Localized tables share the id of their base name.

## Open questions

None recorded.
