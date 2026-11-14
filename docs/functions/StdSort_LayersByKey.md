# StdSort_LayersByKey

- **Address:** `0x1403C2B00`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 StdSort_LayersByKey(UILayer **first, UILayer **last, __int64 ideal, char pred)`
- **Callers:** UIRender_PrepareLayers
- **Callees:** StdSort_PartitionPtrByDword84, StdSort_PopHeapHolePtrByDword84, memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The introsort loop of MSVC's std::sort for an array of layer pointers keyed by the unsigned dword at layer+84 (the draw-order key); the final sort of UIRender_PrepareLayers, whose result is the order in which GUILayer_PackAtlasRect places the layers.

## Behavior

- V: same loop as StdSort_LayersByOrder with the key at +84: insertion sort up to 32 elements (stable), above that partition steps (StdSort_PartitionPtrByDword84, median of three up to 41 elements, Tukey ninther above, three-way partition around the pivot run), recursion into the smaller side, heap fallback (StdSort_PopHeapHolePtrByDword84) when the ideal depth reaches 0.
- V: above 32 elements the sort is therefore not stable: layers with equal keys can leave their creation order. Live (2026-10-30, 63 layers): keys 74 (slots 17 and 25) and 206 (slots 51 and 58) are ties; the slots 17, 25 keep their order and the slots 58, 51 come out reversed. A model of the partition code that follows the decompile reproduces the whole list order of the frame (checked on the sorted list kept at UIManager+4312).
- V: the key is mode | (4 x order + 4) with the order from UIRender_PrepareLayers (see that sheet), so ties are layers of equal order and mode.

## State touched

- Calls: [StdSort_PartitionPtrByDword84](StdSort_PartitionPtrByDword84.md), [StdSort_PopHeapHolePtrByDword84](StdSort_PopHeapHolePtrByDword84.md)

## Referenced by

- Called by: [UIRender_PrepareLayers](UIRender_PrepareLayers.md)
- Observed behaviours: [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md)

## Notes

Name proposed (IDB: sub_1403C2B00). The sorted pointer array stays in memory after the frame (UIManager+4312); the count at +172 is cleared by UIRender_ClearLayerFlags, so a reader after the frame must take the entries up to the first null or use the slot order.

## Open questions

None recorded.
