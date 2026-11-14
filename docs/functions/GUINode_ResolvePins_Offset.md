# GUINode_ResolvePins_Offset

- **Address:** `0x1403EFBE4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_ResolvePins_Offset(GUINode *node)`
- **Callers:** UI layout pass (not traced)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves edge pins stored as pixel offsets from the parent edges (same flag bits as GUINode_ResolvePins_Fraction).

## Behavior

- V: right/bottom pins are parent size minus the stored offset; both pins on one axis scale the node's size by the stored ratio (+132/+136).

## Referenced by

- Called by: [GUIComponent_UpdateNodeTree](GUIComponent_UpdateNodeTree.md), [GUINode_ResolvePinsDispatch](GUINode_ResolvePinsDispatch.md)

## Open questions

See GUINode_ResolvePins_Fraction.
