# AtlasShelf_Alloc

- **Address:** `0x1403B6D68`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__m128i *AtlasShelf_Alloc(unsigned int *shelf, __m128i *outRect, __int64 targetObj, __m128i *inRect, int margin, int *origXY)`
- **Callers:** GUILayer_PackAtlasRect, UIRender_PrepareLayers
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shelf (row) allocator for the layer atlas page: places a rectangle plus margin and returns the packed integer rectangle.

## Behavior

- V: shelf state = { x cursor, y row start, row height, page index }; page size = u16 +20 / +22 of targetObj. Empty or inverted input rect returns the input unchanged.
- V: margin m = clamp(min(margin, (pageW - w) / 2), 0..) for x (the division truncates toward zero), and the same for y with (pageH - h) / 2; the padded size is w + 2m by h + 2m.
- V: when x + paddedW + 3 > pageW the shelf moves to the next row (y += rowHeight, x = 0, rowHeight = 0); when y + paddedH + 3 > pageH it opens a new page (page index + 1, cursor = (0, 0), rowHeight = 0; the cursor value is the zero pair qword_143D12018, which the database shows as -1 because it is uninitialised data but which reads 0 at runtime, live 2026-10-30). Each test is a signed int compare; the x test is made first, so a row break and a page break can both happen in one call (then x = 0, y = 0 on the new page).
- V: the content origin is cursor + m; when the original x (origXY[0]) is a multiple of 4 and the packed x is not, the packed x is rounded up to the next multiple of 4 (same for y with origXY[1]); the extra pixels are added to the cursor advance. Output = (x, y, x + w, y + h) of the unpadded content, with no margin (the margin lies outside the returned rectangle); the row height becomes max(rowHeight, paddedH + padY); the x cursor becomes cursor + padX + paddedW. The rounding applies only when the packed value is > 0 and the original coordinate is a multiple of 4 (test on the original int rect x0 / y0, which the callers pass in origXY). V (live 2026-10-30): the whole algorithm reproduces x, y and page of all 63 layers of a running Job Tree frame (5 pages) exactly.

## Referenced by

- Called by: [GUILayer_PackAtlasRect](GUILayer_PackAtlasRect.md), [UIRender_PrepareLayers](UIRender_PrepareLayers.md)
- Observed behaviours: [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md)

## Notes

The name is ours (IDB: sub_1403B6D68). The 4-pixel alignment only applies to coordinates whose original value is a multiple of 4 (then the packed value is a multiple of 4 when it is > 0); every other position gets whatever the cursor gives, so its parity follows the widths of the rectangles placed before it in the row (padded width = w + 2 m, plus the alignment pads), not the parity of the original position. The cursor starts at (0, 0) on every page: the first rectangle of a page with margin 32 and a 4-aligned original x lands at x = 32; with margin 2 and an unaligned x at x = 2. See the behavior LayerAtlasPlacement for the recipe.

## Open questions

Why the +3 slack in the fit tests (I: guard against 4-pixel alignment growth). No page-count limit is tested here (the sort key keeps 6 bits of the page index).
