# GUICore_SetCursorTarget

- **Address:** `0x1403D6A64`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUICore_SetCursorTarget(GUICore *core, __int64 widget, GUINode *node)`
- **Callers:** GUICore_FocusNode
- **Callees:** sub_1403D6B98, sub_1403D8870, sub_1403D87F4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Makes a node the GUI cursor target: stores its key triple in the core's cursor slot and sends it the cursor-enter virtual call (the old target gets the cursor-leave call).

## Behavior

- V: the current target comes from sub_1403D6B98; when it already is (widget, node) the call returns 1. Otherwise the three key strings at core+1920 / +1936 / +1952 are cleared and the old node's virtual +48 (cursor leave) runs.
- V: with a widget and a node whose byte +416 is set: when the node has an owner at node+576 the owner becomes the target; the keys (widget+16, node+504, node+280) are stored with sub_1403D87F4 and the node's virtual +40 (cursor enter, GUIComponentCustom_CursorEnter) runs; returns 1, else 0.

## Referenced by

- Called by: [FreeCursor_StepFromSticks](FreeCursor_StepFromSticks.md), [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [GUICore_FocusNode](GUICore_FocusNode.md)

## Notes

The cursor target and the focus (core+1968 triple, GUICore_SetFocusComponent) are separate key triples.

## Open questions

None recorded.
