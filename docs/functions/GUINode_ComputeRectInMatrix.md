# GUINode_ComputeRectInMatrix

- **Address:** `0x1403F033C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_ComputeRectInMatrix(GUINode *node, int rect[4], const float m[6])`
- **Callers:** GUIWidget_HitTestSubtree, GUIWidget_HitTestChildren
- **Callees:** roundf

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Transforms the node's (0,0)-(w,h) corners by a 2x3 matrix and returns the rounded axis-aligned bounds {left, top, right, bottom}.

## Behavior

- V: w/h = node +64/+68; results through roundf of the min/max corner coordinates.

## Open questions

None recorded.
