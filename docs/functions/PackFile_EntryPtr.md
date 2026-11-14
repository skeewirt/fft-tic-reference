# PackFile_EntryPtr

- **Address:** `0x1403D2668`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `unsigned __int64 PackFile_EntryPtr(PackFile *pack, int index)`
- **Callers:** PackFile_ReadEntry, sub_14041E05C
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the in-memory address of a loaded pack entry: from one of the 8 cached entry slots when index is cached, else base + (offset[index] - offset[first loaded]).

## Behavior

- V: cache check over 8 slot ids at pack+456; chunk table at pack+16 (16 bytes per entry: offset at +0).

## Referenced by

- Called by: [PackFile_ReadEntry](PackFile_ReadEntry.md), [sub_14041E05C](sub_14041E05C.md)

## Open questions

None recorded.
