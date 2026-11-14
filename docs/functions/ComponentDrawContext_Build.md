# ComponentDrawContext_Build

- **Address:** `0x1403EDCA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 ComponentDrawContext_Build(int a1, ComponentCtx *out, ComponentCtx *parent, GUINode *ref, GUIComponent *comp)`
- **Callers:** GUIComponentRef_Draw
- **Callees:** sub_14040A914, Matrix2x3_Multiply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the child draw context of a component: copy of the parent (0x258 bytes), composed matrix, opacity and colour.

## Behavior

- V: out+496 = comp; matrix out+504 = parent matrix * the component's own transform (sub_14040A914 with the reference node); out+528/+532 scaled by the component's scale; out+536 += comp+192 (opacity add); out+540 = byte-wise product of the parent colour and comp+196; out+544 += ref+200 (order); ++out+552 (depth); out+548 = comp+552 << 16 when set (layer id).

## State touched

- Calls: [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Referenced by

- Called by: [GUIComponentRef_Draw](GUIComponentRef_Draw.md), [GUINode_DrawKind10](GUINode_DrawKind10.md)

## Open questions

None recorded.
