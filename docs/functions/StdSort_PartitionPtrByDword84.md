# StdSort_PartitionPtrByDword84

- **Address:** `0x1403C3AC8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `_QWORD *StdSort_PartitionPtrByDword84(_QWORD pair[2], _QWORD *first, unsigned __int64 last)`
- **Callers:** StdSort_LayersByKey (introsort loop called by UIRender_PrepareLayers)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same partition step as StdSort_PartitionPtrByDword12 with the key at object+84.

## Behavior

- V: identical structure (median-of-three / ninther, three-way partition, returns the equal range in pair); the key is the unsigned dword at *ptr + 84 instead of +12.

## Referenced by

- Called by: [StdSort_LayersByKey](StdSort_LayersByKey.md)

## Notes

Name proposed (IDB: sub_1403C3AC8).

## Open questions

The list is the UI layer list of UIRender_PrepareLayers (key +84 = the draw-order key; V).
