# GUICollisionNode_ContainsPoint

- **Address:** `0x1403FDCC8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUICollisionNode_ContainsPoint(GUINode *node, float localX, float localY)`
- **Callers:** GUIWidget_HitTestChildren
- **Callees:** GUICollisionNode_EllipseContains

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The Collision node's shape test, in the node's local space.

## Behavior

- V: shape 0 (node +208): the rectangle 0 <= x < w and 0 <= y < h (w, h = node +64/+68 ints), comparisons x >= 0 and w > x: left/top edge inside, right/bottom edge outside.
- V: shape 1: GUICollisionNode_EllipseContains (inner radius +212, sweep +216).
- V: a node of kind 7 (ellipse) uses the same ellipse test with its own parameters (+232/+228).

## State touched

- Calls: [GUICollisionNode_EllipseContains](GUICollisionNode_EllipseContains.md)

## Referenced by

- Called by: [GUIWidget_HitTestChildren](GUIWidget_HitTestChildren.md)

## Notes

The job tree panel's UnitJob/Layer00/Collision00 is shape 0 (file bytes: shape 0, ratio 0, sweep 0), 100x140 at (-20,-34): the hover zone is exactly that rectangle.

## Open questions

None recorded.
