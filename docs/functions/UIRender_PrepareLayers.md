# UIRender_PrepareLayers

- **Address:** `0x1403B85B0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UIRender_PrepareLayers(__int64 g_Renderer)`
- **Callers:** sub_1403A2774 (frame begin)
- **Callees:** UILayer_GetTarget, GUILayer_PackAtlasRect, AtlasShelf_Alloc, StdSort_LayersByOrder, StdSort_LayersByKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame layer setup: collects the used layers, finds overlaps, assigns draw order and atlas pages, then packs every layer's rectangle.

## Behavior

- V: resets both atlas allocators (UIRenderer+8616 / +8632 = cursor (0, 0), row height 0, page 0; the cursor value is qword_143D12018, 0 at runtime), clears dword_140906B58..68 = -1, and collects the layers of the 512 entries (+216) whose byte +76 is set into the list at +4312 (count +172).
- V: walking the list from the back: layer+20 = 0; when +489 is set the nearest lower layer with +487 is found, its +8 copied to this +36 and, when the two rectangles do not overlap (float compares on +208 / +212 / +216 / +220, strict), byte +79 (culled) is set. The list is sorted (sub_1403C2930).
- V: for every layer with +487, +179 set, +28 != 2, +78 / +486 / +488 clear: the int rect (truncation) is allocated in a temporary atlas with margin 2 or 32 (|+500|, +180, +188 > 3.2); when the temporary page changes (the breaking layer is not counted on the new page: the cursor is reset to (0, 0) after it), +20 of this layer and of every later layer in the list is set to this layer's +12 (its order at that moment), not to a page number; the temporary pass only exists for these +487 layers. Further passes compute the draw order +12 as 1 + the order of the nearest overlapping lower layer, and the key +84 = mode | (4 * (+12) + 4) with mode = 1 when +28 == 0 and +177 or +178 is set, else 2 when +28 == 0, else 0; sorted again (sub_1403C2B00); +12 is renumbered densely by key change.
- V: finally calls UILayer_GetTarget and GUILayer_PackAtlasRect for each layer in order.
- V (read in full 2026-10-30): the order +12 starts as the layer's index (GUIRenderer_ResetFrame). Walking from the top of the list down, a layer whose float rectangle (+208..+220) overlaps (strictly) the nearest lower layer gets +12 = (+20, the page base) + that layer's current +12 + 1; a layer with no overlapping lower layer keeps its index (0 when +487). A further pass sets +12 = lower + 1 only where the nearest overlapping lower layer is a masked layer (+487 with +179, kind != 2 and +78, +486, +488 clear). The sort key +84 = mode | (4 x +12 + 4) with mode 1 for a kind 0 layer with +177 or +178, 2 for another kind 0 layer, 0 otherwise; the list is sorted by it (StdSort_LayersByKey, sub_1403C2B00: an MSVC std::sort introsort, a stable insertion sort up to 32 elements, partition based and not stable above) and +12 renumbered densely by key change, starting at 1 (equal keys share a number). The pack order of GUILayer_PackAtlasRect is this final list order. V (live 2026-10-30, 63 layers): keys, list order (including a tie broken against the slot order) and every packed position were reproduced; the first sort (by +12, whose values are the slot indices, already ascending) changes nothing. A layer that overlaps a lower layer q gets the order idx(q) + 1 (idx = the slot index), at most its own index, so it can be packed before layers created between q and itself.

## State touched

- Calls: [UILayer_GetTarget](UILayer_GetTarget.md), [GUILayer_PackAtlasRect](GUILayer_PackAtlasRect.md), [AtlasShelf_Alloc](AtlasShelf_Alloc.md), [StdSort_LayersByOrder](StdSort_LayersByOrder.md), [StdSort_LayersByKey](StdSort_LayersByKey.md)
- Reads: [GUILayer.rect](../structs/GUILayer.md#rect), [GUILayer.index](../structs/GUILayer.md#index), [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.used](../structs/GUILayer.md#used)
- Writes: [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.culled](../structs/GUILayer.md#culled)

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Observed behaviours: [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md), [LayerCompositeOrder](../behaviors/LayerCompositeOrder.md)

## Notes

The name is ours (IDB: sub_1403B85B0). Only the loops' arithmetic is V; the intent of each pass (layer order, page assignment, overlap) is I. Overlap tests are strict float compares of the unrounded rectangles.

## Open questions

Why overlap decides +12 (I: layers that overlap are blended in order, so the later one must not be ordered before the earlier one). The +487 flag is written by ComponentLayer_DrawMaskComponent (V, 2026-10-30: the mask component of a component whose property block has a mask is drawn into a fresh record and the flag is set when it produced draws; live in a Job Tree frame).
