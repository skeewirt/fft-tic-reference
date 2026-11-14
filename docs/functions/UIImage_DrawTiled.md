# UIImage_DrawTiled

- **Address:** `0x1403E0E80`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `float UIImage_DrawTiled(UIRenderer *r, float *xform, int *rect, GUIFontSlot *part, int *uv, int tintRGBA, char mirror, unsigned layer)`
- **Callers:** UIImageNode_Draw
- **Callees:** UIDraw_SetStateFromSlot, UIRender_QueueImageDraw, sub_1403DCA04

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills a node rectangle with copies of a texture part, optionally mirroring every second column and row, emitting one quad (4 vertices of 24 bytes) per cell.

## Behavior

- V: cell size = part size (halved per axis when slot byte 35 is set), cols = ceil(width / cellW), rows = ceil(height / cellH); vertex space is reserved with UIRender_QueueImageDraw(4 * cols * rows).
- V: a cell UV rectangle is the part UV rectangle; with mirror set, odd columns swap u0/u1 and odd rows swap v0/v1; the last row/column is clipped and its far UV is interpolated by the covered fraction.
- V: vertices are the node rectangle positions transformed by the 2x3 matrix (xform[0..5]); nothing extends past the node rectangle (no glow quad); per vertex: x, y, z = 0, colour (4 bytes), u, v. Live check: the Job Tree ring = 2 cells, uv 2/204..110/204 by 2/196..106/196, second cell u-mirrored.

## State touched

- Calls: [UIDraw_SetStateFromSlot](UIDraw_SetStateFromSlot.md), [UIRender_QueueImageDraw](UIRender_QueueImageDraw.md)
- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Applies shader programs: [UIImage](../programs/UIImage.md)
- Called by: [GUINineGridNode_Draw](GUINineGridNode_Draw.md), [UIImageNode_Draw](UIImageNode_Draw.md)

## Notes

Verified against a live vertex-buffer read of the running game (read-only).

## Open questions

None recorded.
