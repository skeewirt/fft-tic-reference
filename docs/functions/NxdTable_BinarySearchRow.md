# NxdTable_BinarySearchRow

- **Address:** `0x1403D4278`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `__int64 NxdTable_BinarySearchRow(__int64 entries, unsigned __int64 lo, unsigned __int64 hi, unsigned int id)`
- **Callers:** NxdTable_GetRowById (mode 1 without cache)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binary search over an array of 16-byte entries sorted by the first dword of the row each entry points to; returns the entry address or 0.

## Behavior

- V: entry i = entries + 16 * i. An entry is treated as empty when (qword[0] & 0x7FFFFFFFFFFFFFFF) == 0 and compared as key 0; otherwise the key is the dword at the pointer stored at entry+8. Equal key returns the entry address.
- V: standard half-open halving: mid = lo + ((hi - lo) >> 1); key <= id moves lo to mid + 1, key > id moves hi to mid. Returns 0 when the range is empty.

## Referenced by

- Called by: [NxdTable_GetRowById](NxdTable_GetRowById.md)
- Reads file formats: [NxdSingleKeyRows](../formats/NxdSingleKeyRows.md)

## Notes

The name is ours (IDB: sub_1403D4278). Returns the entry, not the row pointer; the caller uses the result as is.

## Open questions

? the high bit of qword[0] (masked out) is probably a flag (deleted / extended entry).
