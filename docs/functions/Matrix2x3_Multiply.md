# Matrix2x3_Multiply

- **Address:** `0x1403D82F0`
- **Area:** [Math](../areas/math.md)
- **Prototype:** `float *Matrix2x3_Multiply(float out[6], const float a[6], const float b[6])`
- **Callers:** UI hit test and render paths
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Concatenates two 2x3 affine matrices (a applied first, then b); the UI's node and layer transforms use this layout [m0 m1 m2 m3 tx ty].

## Behavior

- V: out0 = b0*a0 + b2*a1, out1 = a0*b1 + a1*b3, out2 = b0*a2 + b2*a3, out3 = a2*b1 + a3*b3, out4 = a4*b0 + a5*b2 + b4, out5 = a4*b1 + a5*b3 + b5.

## Referenced by

- Called by: [ComponentDrawContext_Build](ComponentDrawContext_Build.md), [ComponentDrawContext_ComputeMatrix](ComponentDrawContext_ComputeMatrix.md), [ComponentEffects_Collect](ComponentEffects_Collect.md), [ComponentLayer_DrawMaskComponent](ComponentLayer_DrawMaskComponent.md), [GUINineGridNode_Draw](GUINineGridNode_Draw.md), [GUINode_DrawKind10](GUINode_DrawKind10.md), [GUINode_DrawKind5](GUINode_DrawKind5.md), [GUINode_DrawKind7](GUINode_DrawKind7.md), [GUINode_DrawKind8](GUINode_DrawKind8.md), [GUINode_UpdateColourAndMatrix](GUINode_UpdateColourAndMatrix.md), [GUIRectNode_Draw](GUIRectNode_Draw.md), [GUIWidget_HitTestChildren](GUIWidget_HitTestChildren.md), [GUIWidget_HitTestComponent](GUIWidget_HitTestComponent.md), [GUIWidget_HitTestSubtree](GUIWidget_HitTestSubtree.md), [UIImageNode_Draw](UIImageNode_Draw.md)

## Open questions

None recorded.
