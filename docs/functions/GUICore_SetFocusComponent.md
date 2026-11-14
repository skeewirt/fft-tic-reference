# GUICore_SetFocusComponent

- **Address:** `0x1403D6CE0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUICore_SetFocusComponent(GUICore *core, GUIWidget *widget, GUINode *node)`
- **Callers:** GUICore_UpdateFrame, JobTree_HandleInput area (sub_1401D1F7C, sub_1401D2240), sub_14040CB60
- **Callees:** virtual +96 / +104 of the node

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves focus to a component node: the old focus node gets virtual +104 (focus lost, event 20), the new one virtual +96 (focus gained, event 19); stores the new key triple at core+1968.

## Behavior

- V: returns 1 without change when the node already has focus.

## Referenced by

- Called by: [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [GUICore_FocusNode](GUICore_FocusNode.md), [GUICore_UpdateFrame](GUICore_UpdateFrame.md)

## Open questions

None recorded.
