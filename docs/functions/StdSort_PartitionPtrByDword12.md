# StdSort_PartitionPtrByDword12

- **Address:** `0x1403C37EC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `_QWORD *StdSort_PartitionPtrByDword12(_QWORD pair[2], _QWORD *first, unsigned __int64 last)`
- **Callers:** StdSort_LayersByOrder (the introsort loop), which UIRender_PrepareLayers calls
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Introsort partition step on an array of object pointers keyed by the dword at object+12: median-of-three (or Tukey ninther for more than 41 elements) pivot choice and three-way partition; returns the equal range [lo, hi) in pair.

## Behavior

- V: size <= 41 elements: median of first / middle / last; larger: median of medians of three groups spaced n >> 3 apart (n = the element count; the first group starts at the first element, the last ends at the last). Keys are the unsigned dwords at *ptr + 12.
- V: then expands the pivot run left and right over equal keys and partitions the rest into < pivot, == pivot, > pivot, stable only up to the usual std::sort swaps; returns pair[0] = end of the lower part, pair[1] = start of the upper part.

## Referenced by

- Called by: [StdSort_LayersByOrder](StdSort_LayersByOrder.md)

## Notes

Name proposed (IDB: sub_1403C37EC). This is MSVC's _Partition_by_median_guess_unchecked specialised for the key at +12 (the layer sort key). Same code as StdSort_PartitionPtrByDword84 with a different key offset.

## Open questions

The list is the UI layer list of UIRender_PrepareLayers (key +12 = the layer's order, initially its slot index; V).
