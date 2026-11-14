# GUICollisionNode_EllipseContains

- **Address:** `0x1403FDD54`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUICollisionNode_EllipseContains(GUINode *node, float x, float y, float sweep, float innerRatio)`
- **Callers:** GUICollisionNode_ContainsPoint
- **Callees:** atan2f

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ellipse / ring-sector point test: normalises the point into [-1,1] over the node's size, rejects outside the unit circle or inside innerRatio, and for sweep > 0 rejects the angular part measured from 'up'.

## Behavior

- V: d2 = u^2 + v^2 with u = 2(x/w - 0.5), v = 2(y/h - 0.5); false if d2 > 1 or (innerRatio > 0 and innerRatio^2 > d2); angle = atan2(u, -v)/2pi (wrapped to 0..1) must be <= 1 - sweep.

## Referenced by

- Called by: [GUICollisionNode_ContainsPoint](GUICollisionNode_ContainsPoint.md)

## Open questions

None recorded.
