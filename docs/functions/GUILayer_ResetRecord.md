# GUILayer_ResetRecord

- **Address:** `0x1403E73A0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUILayer_ResetRecord(UIRenderer *r, int index)`
- **Callers:** GUIRenderer_ResetFrame, GUILayer_Select
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets one layer record to its defaults (full target size, identity colour transform, every effect group off).

## Behavior

- V: +0 / +2 = target size (r+184 / r+188), blend type 0, colour multiplier (1,1,1,1), add (0,0,0,0), flag words +153/+154/... cleared, rectangle (0, 0, w, h), opacity 1.0f at +552; all effect pointers and group flags zero.
- V (disassembly, 2026-10-30): the dword at record+152 (layer+176) is set to 0x01000000: the three effect flags +176 / +177 / +178 become 0 and the byte layer+179 becomes 1; layer+179 is the 'composited' byte (GUILayer_Composite and GUILayer_PackAtlasRect only act on layers where it is set), cleared only by GUINode_DrawKind10. The dword at layer+486 (flags +486..+489) is zeroed and the kind dword layer+28 is set to 0.

## State touched

- Writes: [GUILayer.offset_vectors](../structs/GUILayer.md#offset_vectors), [GUILayer.rect](../structs/GUILayer.md#rect), [GUILayer.composited](../structs/GUILayer.md#composited), [GUILayer.layer_kind](../structs/GUILayer.md#layer_kind)

## Referenced by

- Called by: [ComponentLayer_DrawMaskComponent](ComponentLayer_DrawMaskComponent.md), [GUICore_DrawWidget](GUICore_DrawWidget.md), [GUILayer_Select](GUILayer_Select.md), [GUIRenderer_ResetFrame](GUIRenderer_ResetFrame.md)

## Open questions

None recorded.
