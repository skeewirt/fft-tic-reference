# GUICore_IsCursorTarget

- **Address:** `0x1403D6BFC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUICore_IsCursorTarget(GUICore *core, __int64 widget, GUINode *node)`
- **Callers:** GUICore_FocusNode
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same comparison as GUICore_IsFocusTarget against the cursor-target triple at core+1920 / +1936 / +1952.

## Behavior

- V: hashes at core+1928 / +1944 / +1960, strings at +1920 / +1936 / +1952.

## Referenced by

- Called by: [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [GUICore_FocusNode](GUICore_FocusNode.md), [sub_14022F868](sub_14022F868.md)

## Open questions

None recorded.
