# GUICore_DrawOutsideBars

- **Address:** `0x1403E5258`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUICore_DrawOutsideBars(UIRenderer *r, const float m[6], const int rect[4], const uint32 screen[2], unsigned int color, unsigned int sortKey)`
- **Callers:** GUICore_CommitFrame (twice, for the two cursor-sized / border layers whose record flag +132 is 1)
- **Callees:** UIRender_QueueImageDraw, sub_1403DFE34, sub_1403DF670

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the part of the screen outside a transformed rectangle (the letterbox / pillarbox bars around the UI area) with a flat colour.

## Behavior

- V: the rect corners (rect[0], rect[1]) and (rect[2], rect[3]) are pushed through m (x' = m0*x + m2*y + m4, y' = m1*x + m3*y + m5) giving X1, Y1, X2, Y2; screen = {W, H} unsigned ints (r+184).
- V: when the rectangle lies completely outside the screen (X2 <= 0 or X1 >= W or Y2 <= 0 or Y1 >= H) the whole screen (0, 0, W, H) is filled through sub_1403DFE34 with the identity matrix.
- V: otherwise up to four flat quads (4 vertices each, colour = the dword, z = 0, queued with UIRender_QueueImageDraw): left bar if 0 < X1 < W (x 0..X1, y Y1..Y2), right bar if 0 < X2 < W (X2..W, Y1..Y2), top bar if 0 < Y1 < H (full width, y 0..Y1), bottom bar if 0 < Y2 < H (full width, Y2..H); the bounds are extended with sub_1403DF670 for (0,0) and (the far corner).

## State touched

- Calls: [UIRender_QueueImageDraw](UIRender_QueueImageDraw.md)
- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Notes

The name is ours (IDB: sub_1403E5258). colour comes from sub_1403D9570(g_ColorTable, 1), i.e. colour table entry 1. The rect argument in CommitFrame is {0, 0, layer.w, layer.h} (I).

## Open questions

? The bars use the plain bar corners without the half-pixel rule; bar overlap at the corners is not handled (not needed while the rect is inside the screen).
