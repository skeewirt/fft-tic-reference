# GUIWidget_HitTestPoint

- **Address:** `0x1403FD5D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUIWidget_HitTestPoint(GUIHitQuery *q, GUIWidget *w, float pt[2])`
- **Callers:** GUICore_UpdateFrame
- **Callees:** GUIWidget_HitTestSubtree

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Hit-tests one point against a widget's node tree and appends the hits to q.

## Behavior

- V: builds the query record (identity matrix at +24, point at +56/+60, mode at +52 = 0 meaning 'inverse-transform the point into each node'), finds the root layer node of the widget (first node with kind 1) and runs GUIWidget_HitTestSubtree.

## State touched

- Calls: [GUIWidget_HitTestSubtree](GUIWidget_HitTestSubtree.md)

## Referenced by

- Called by: [GUICore_UpdateFrame](GUICore_UpdateFrame.md), [GUIInput_IsPointerOverLayer](GUIInput_IsPointerOverLayer.md)

## Notes

Query flags set by GUICore_UpdateFrame: type filter array (query +32..+47) = 1 for every node kind except 13 (Collision), so ONLY Collision nodes can be hit; +53 = 0 stops at the first hit; +49/+52/+54 = 1.

## Open questions

None recorded.
