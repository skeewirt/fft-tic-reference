# GUINode_BuildLocalMatrix

- **Address:** `0x1403F0270`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUINode_BuildLocalMatrix(GUINode *node, float out[6])`
- **Callers:** GUINode_UpdateColourAndMatrix
- **Callees:** sub_1403D83FC (2x3 rotate)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a node's local 2x3 matrix from scale (+80/+84), pivot (+72/+76), rotation (+88) and position (+56/+60).

## Behavior

- V: S = [sx 0 0 sy | tx = sx * (float)(-pivotX), ty = sy * (float)(-pivotY)] with sx = node+80, sy = node+84, pivotX = int node+72, pivotY = int node+76 (scale about the pivot, the pivot is moved to the origin first).
- V: sub_1403D83FC rotates all three row pairs by angle node+88: (m0,m1) -> (m0*cos - m1*sin, m0*sin + m1*cos), the same for (m2,m3) and for (tx,ty), with sinf / cosf of the raw float (radians).
- V: then tx += (float)(pivotX + posX), ty += (float)(pivotY + posY) with posX = int node+56, posY = int node+60 (the integer sums are formed first).
- V: result in the engine's row-vector layout [m0 m1 m2 m3 tx ty]: x' = m0*x + m2*y + tx, y' = m1*x + m3*y + ty. So a node point v (node-local, origin = top-left of the node box) maps to R(rot) * S * (v - pivot) + pivot + position, and the pivot is the point of the box that stays at position + pivot when the node is scaled or rotated.

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Called by: [GUINode_UpdateColourAndMatrix](GUINode_UpdateColourAndMatrix.md)
- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

The name is ours (IDB: sub_1403F0270). The pivot default set by the size setter (sub_1403EF6B4 when node+142 = 0) is size / 2 in integer division, so an unscaled node is simply translated by its position (pivot terms cancel). For the Job Tree text nodes this is the matrix GUITextNode_Draw multiplies glyph pen positions with.

## Open questions

None recorded.
