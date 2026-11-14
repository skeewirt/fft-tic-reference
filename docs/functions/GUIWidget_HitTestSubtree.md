# GUIWidget_HitTestSubtree

- **Address:** `0x1403FD67C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUIWidget_HitTestSubtree(GUIHitQuery *q, GUIHitFrame *frame, GUINode *root)`
- **Callers:** GUIWidget_HitTestPoint, GUIWidget_HitTestComponent
- **Callees:** GUIWidget_HitTestChildren, Matrix2x3_Multiply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the hit test over a node's children (GUIWidget_HitTestChildren) under the accumulated transform.

## Behavior

- V: when the root has a transform (node +216) the node's matrix (+432) is combined with the query frame first.

## State touched

- Calls: [GUIWidget_HitTestChildren](GUIWidget_HitTestChildren.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Referenced by

- Called by: [GUIWidget_HitTestComponent](GUIWidget_HitTestComponent.md), [GUIWidget_HitTestPoint](GUIWidget_HitTestPoint.md)

## Open questions

None recorded.
