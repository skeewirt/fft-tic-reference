# SDFFontBatch_SortCompare

- **Address:** `0x1403A8FB0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 SDFFontBatch_SortCompare(_DWORD *a, _DWORD *b)`
- **Callers:** SDFFontRenderer_Flush (0x1403A9B8A)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

qsort comparator for the text batch list: orders 8-byte entries by their first dword, never returns 0.

## Behavior

- V: body is `return *a1 < *a2 ? -1 : 1;` - only the first dword of each entry is read.
- V: equal keys return 1 (never 0), so the sort is not stable and a == b is reported as 'a after b'.
- V: single xref, SDFFontRenderer_Flush at 0x1403A9B8A (callback pointer for qsort).
- I: entries are (key dword, batch index dword) per the Flush sheet; this function does not touch geometry, only batch draw order.

## Notes

Leaf, 2 instructions of real work. No effect on UVs, kerning or scale.

## Open questions

? whether two batches can share a key (keys believed to be distinct draw sequence numbers; I).
