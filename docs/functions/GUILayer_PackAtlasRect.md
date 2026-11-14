# GUILayer_PackAtlasRect

- **Address:** `0x1403B6A78`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 GUILayer_PackAtlasRect(UILayer *layer, __int64 targetObj)`
- **Callers:** UIRender_PrepareLayers
- **Callees:** AtlasShelf_Alloc

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides where a layer's pixels live in the layer atlas pages, allocates the integer rectangle there and rewrites the layer rectangle (+208..+220) and its offsets (+224..+236) to the packed position.

## Behavior

- V: layer +240..+252 (int rect) = ((int)x, (int)y, (int)(x + w), (int)(y + h)) from floats +208 / +212 / +216 / +220 (truncation toward zero, right / bottom edges truncated after the float sum); +224 / +228 = 0, +232 = 0, +492 = 0, +16 = +20 = -1 (page ids).
- V: only when layer byte +79 (culled) is 0. Atlas allocators are at UIRenderer+8616 (primary) and +8632 (secondary).
- V: fallback (no pack): when byte +179 is 0, dword +28 > 1, or bytes +78 / +486 / +488 are set, the allocation is for the whole target (rect 0,0,targetW,targetH from u16 +20 / +22) with margin 2 (which the allocator clamps to 0 for a full-page rectangle); +492 stays 0 and +208.. are unchanged. The result rectangle is discarded; only the primary page index (+16) is kept. A full-page rectangle always fails both fit tests, so every fallback layer takes a new page, and the next layer after it takes another new page (the cursor is left at the end of the row and page).
- V: packed path: margin = 2, or 32 when |float +500| > 3.2 or float +180 > 3.2 or float +188 > 3.2 (a blur is present). When byte +487: the secondary atlas gets the rect first, giving the packed rect P2 (the page index +20 = its page), and the primary allocation is repeated. The primary result P replaces the layer rectangle: +208 / +212 = (float)P.x0 / P.y0, +216 / +220 = (float)(P.x1 - P.x0) / (P.y1 - P.y0); +224 / +228 = P.x0 - (float)orig.x0, P.y0 - (float)orig.y0 with orig the int rect (+240 / +244, truncated, not the float rect); +232 / +236 = P2 - orig (ints, as floats) when +487 (otherwise +232 / +236 = +224 / +228); +492 = 1; +16 = the primary page index (+20 = the secondary page index only for +487). V: when byte +487 and the secondary page index changed, the primary shelf is moved to a new page first (row height 0, page + 1, cursor (0, 0)); the primary allocation always uses the int rect, the same margin and the original (x0, y0) as alignment key. V (live 2026-10-30): P and the page index +16 were reproduced for 63 layers of a running frame (no +487 layer among them: the secondary path is read in the code only).

## State touched

- Calls: [AtlasShelf_Alloc](AtlasShelf_Alloc.md)
- Reads: [GUILayer.rect](../structs/GUILayer.md#rect), [GUILayer.shadow_radius](../structs/GUILayer.md#shadow_radius), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md), [GUILayer.composited](../structs/GUILayer.md#composited), [GUILayer.layer_kind](../structs/GUILayer.md#layer_kind)
- Writes: [GUILayer.rect](../structs/GUILayer.md#rect), [GUILayer.atlas_offset](../structs/GUILayer.md#atlas_offset), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [GUILayer.packed](../structs/GUILayer.md#packed), [GUILayer.int_rect](../structs/GUILayer.md#int_rect)

## Referenced by

- Called by: [UIRender_PrepareLayers](UIRender_PrepareLayers.md)
- Observed behaviours: [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md)

## Notes

The name is ours (IDB: sub_1403B6A78). KEY for pixel-exact work: a layer's rectangle is not its design rectangle after this runs. It is truncated to integers, grown by the margin (2 px, 32 px with blur) inside the atlas, and the rectangle floats are then overwritten with integer atlas positions; the difference to the screen position is kept in +224 / +228 (and +232 / +236). A layer's content therefore lands on the screen at integer positions (floor toward zero of the unrounded float rect). The packed rectangle P is the content rectangle itself: the margin lies around it, so the content origin in the atlas is P.x0 / P.y0 and the atlas pixel of screen pixel (sx, sy) is (sx + P.x0 - x0, sy + P.y0 - y0) with (x0, y0) = the int rect origin.

## Open questions

Who writes the float rect first (the UI layout / animation step); what +500 / +180 / +188 are exactly (blur radii of the effect groups).
