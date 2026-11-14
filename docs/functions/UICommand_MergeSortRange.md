# UICommand_MergeSortRange

- **Address:** `0x1403AE788`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `_UNKNOWN **__fastcall UICommand_MergeSortRange(int unused, __int64 dst, __int64 src, int lo, int hi)`
- **Callers:** UIContext_SortCommands, itself (V)
- **Callees:** memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Recursive stable merge sort over 16-byte records [lo, hi] keyed by the first qword (unsigned), ping-ponging between two buffers, with insertion sort for short ranges.

## Behavior

- V: if hi - lo >= 7: mid = (lo + hi) >> 1; recursively sorts both halves with the buffer arguments swapped (a3, a2), then merges them from src into dst. Merge takes the right element only if left.key > right.key (strict), so equal keys keep order (stable). Leftover tail is memmove'd (16 * remaining bytes).
- V: if hi - lo < 7 (7 or fewer elements): copies src[lo] to dst[lo] and insertion-sorts dst in place using the same strict > comparison on the first qword.
- V: record = 16 bytes; key = first qword, unsigned compare. Argument a1 is unused.
- I: key is the UI command sort key (layer / depth | order) and the second qword the command index or pointer; UIContext_SortCommands calls it.

## Referenced by

- Called by: [UIContext_SortCommands](UIContext_SortCommands.md)

## Notes

The classic JDK-style mergesort with insertion cutoff 7.

## Open questions

? what the 64-bit key encodes (see UICommand_Append / UIContext_SortCommands).
