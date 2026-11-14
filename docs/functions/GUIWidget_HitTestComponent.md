# GUIWidget_HitTestComponent

- **Address:** `0x1403FDB5C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUIWidget_HitTestComponent(GUIHitQuery *q, GUIHitFrame *frame, GUINode *refNode)`
- **Callers:** GUIWidget_HitTestChildren
- **Callees:** GUIWidget_HitTestSubtree, sub_1403F9938, Matrix2x3_Multiply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Descends into a component reference node (kind 12, e.g. one UnitJob panel) by looking up its component's own node tree and testing that under the reference node's transform.

## Behavior

- V: requires query +52 != 0; a component whose scale mode (+540) is 1 is rescaled by size ratio (node +64 over the component's +336).

## State touched

- Calls: [GUIWidget_HitTestSubtree](GUIWidget_HitTestSubtree.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Referenced by

- Called by: [GUIWidget_HitTestChildren](GUIWidget_HitTestChildren.md)

## Open questions

None recorded.
