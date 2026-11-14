# AtlasShelf

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The state of one layer atlas allocator (a shelf / row packer): the cursor in the current row, the start of the row, the height of the row and the page. The UI manager holds two, the primary at +8616 and the secondary (masked layers only) at +8632; UIRender_PrepareLayers resets both every frame, GUILayer_PackAtlasRect and AtlasShelf_Alloc advance them.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="cursor_x"></a>`0x0` | cursor_x | `int32` | V | Next free x in the current row (0 at the start of a page and of a row). Advances by the padded width plus the alignment pad. |
| <a id="row_y"></a>`0x4` | row_y | `int32` | V | Top of the current row (0 at the start of a page). Grows by the row height when a row is closed. |
| <a id="row_height"></a>`0x8` | row_height | `int32` | V | Height of the tallest rectangle in the current row, margins and alignment pad included; 0 for a new row. |
| <a id="page"></a>`0xC` | page | `int32` | V | Page index (0 at the start of the frame); +1 each time a rectangle does not fit below the current row. |

## Behavior

- V: the starting state of both shelves is {0, 0, 0, 0}: UIRender_PrepareLayers and the UI renderer constructor copy the zero pair g_ZeroPair into cursor_x / row_y and clear the row height (the page index is cleared by the same stores).
- V (live 2026-10-30, after the Job Tree frame): the primary shelf read {674, 239, 251, 4}: page 4, row top 239, row height 251, cursor 674. That is the state after the last layer of the list (slot 62, integer rectangle 610 x 187, margin 32, the first layer of its row: cursor 0 + 610 + 64 = 674, row top 239, row height 187 + 64 = 251); a model of the placement reproduces the whole state. The secondary shelf read {0, 0, 0, 0} (no masked layer in the frame).

## Referenced by

- Observed behaviours: [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
