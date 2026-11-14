# GUICore_IsFocusTarget

- **Address:** `0x1403D6E8C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUICore_IsFocusTarget(GUICore *core, __int64 widget, GUINode *node)`
- **Callers:** GUICore_FocusNode
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests whether (widget, node) is the current GUI focus: compares the three keys (widget+16, node+504, node+280) with the focus triple at core+1968 / +1984 / +2000.

## Behavior

- V: each key is compared by its cached hash when both hashes are non-zero (widget+24 vs core+1976, node+512 vs core+1992, node+288 vs core+2008), otherwise by string; any mismatch returns 0.

## Referenced by

- Called by: [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [GUICore_FocusNode](GUICore_FocusNode.md)

## Open questions

None recorded.
