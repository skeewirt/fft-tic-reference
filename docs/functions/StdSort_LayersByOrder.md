# StdSort_LayersByOrder

- **Address:** `0x1403C2930`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 StdSort_LayersByOrder(UILayer **first, UILayer **last, __int64 ideal, char pred)`
- **Callers:** UIRender_PrepareLayers
- **Callees:** StdSort_PartitionPtrByDword12, StdSort_PopHeapHolePtrByDword12, memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The introsort loop of MSVC's std::sort for an array of layer pointers, keyed by the unsigned dword at layer+12 (the layer's order); UIRender_PrepareLayers sorts the collected layer list with it before it computes the draw order.

## Behavior

- V: loop on the range [first, last): up to 32 elements (256 bytes) it runs an insertion sort; with more elements and ideal > 0 it calls StdSort_PartitionPtrByDword12 and sets ideal = (ideal >> 2) + (ideal >> 1), then recurses into the smaller side and loops on the larger one (the lower part is recursed when it is smaller, otherwise the upper part); with ideal <= 0 it falls back to a heap sort (make-heap loop from the middle down, then pop the largest to the end repeatedly) using StdSort_PopHeapHolePtrByDword12. The initial ideal is the element count.
- V: insertion sort: for each element, a key below the first element's key moves the whole prefix up by one (memmove) and takes the first slot; otherwise it is inserted by shifting while its key is below the previous one's (strict less-than, so equal keys keep their order: stable). Keys are compared as unsigned dwords.
- V: the call from UIRender_PrepareLayers passes the list at UIManager+4312 and its end (count at +172). The keys at that time are the slot indices (GUIRenderer_ResetFrame writes layer+12 = index for every record each frame) and the list was filled in slot order, so the array is already ascending with distinct keys and the sort changes nothing (V live: the first 63 entries of a running frame, slots 0..62).

## State touched

- Calls: [StdSort_PartitionPtrByDword12](StdSort_PartitionPtrByDword12.md), [StdSort_PopHeapHolePtrByDword12](StdSort_PopHeapHolePtrByDword12.md)

## Referenced by

- Called by: [UIRender_PrepareLayers](UIRender_PrepareLayers.md)
- Observed behaviours: [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md)

## Notes

Name proposed (IDB: sub_1403C2930). Identical in structure to StdSort_LayersByKey (key at +84). With the ideal depth halving by 3/4 per level the heap fallback needs more than 20 partition levels for the largest list (512 layers) and is not expected to run.

## Open questions

None recorded.
