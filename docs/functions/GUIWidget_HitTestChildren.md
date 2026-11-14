# GUIWidget_HitTestChildren

- **Address:** `0x1403FD844`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUIWidget_HitTestChildren(GUIHitQuery *q, GUIHitFrame *frame, GUINode *parent)`
- **Callers:** GUIWidget_HitTestSubtree, itself
- **Callees:** GUIWidget_HitTestComponent, GUICollisionNode_ContainsPoint, Matrix2x3_Invert, Matrix2x3_Multiply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Depth-first walk of a node's children (first child at +208, next sibling at +32): layer nodes (kind 1) recurse, component nodes (kind 12) descend through GUIWidget_HitTestComponent, every other node whose kind is not filtered is tested.

## Behavior

- V: nodes with +144 = 0 or +204 = 0 are skipped when query +49 is set; the node's matrix (+160, 2x3 affine) is multiplied into the frame (Matrix2x3_Multiply).
- V: point mode 0: the frame matrix is inverted (Matrix2x3_Invert), the point is transformed into the node's local space and tested with GUICollisionNode_ContainsPoint; hits are appended as 32-byte entries (frame, node, local x/y).
- V: with query +53 = 0 the walk returns as soon as one hit exists, so the FIRST Collision node in tree order wins.

## State touched

- Calls: [GUIWidget_HitTestComponent](GUIWidget_HitTestComponent.md), [GUICollisionNode_ContainsPoint](GUICollisionNode_ContainsPoint.md), [Matrix2x3_Invert](Matrix2x3_Invert.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Referenced by

- Called by: [GUIWidget_HitTestSubtree](GUIWidget_HitTestSubtree.md)

## Notes

Rectangle mode 1 (query +52 = 1) instead overlaps the node's rounded rectangle (GUINode_ComputeRectInMatrix) with a point/box; not used by hover.

## Open questions

None recorded.
