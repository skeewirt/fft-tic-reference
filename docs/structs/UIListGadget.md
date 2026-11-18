# UIListGadget

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The row list gadget used by General Options (constructor 0x14028C458, bound by 0x14028C5C4 with tag 151 and the part name `List`).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="node"></a>`0x10` | node | `GUINode *` | V | The gadget's node (animated by Show / Slide_left / Slide_right). |
| <a id="list"></a>`0x18` | list | `GUIComponentList *` | V | The list component; GUIComponentList_GetItemComponent(list, index) returns an item node (kind 10 at +536). |
| <a id="cursor_row"></a>`0x60` | cursor_row | `int32` | V | The cursor row. |
| <a id="takes_input"></a>`0x78` | takes_input | `uint8` | V | Tested by the list input. |
| <a id="input_lock"></a>`0x80` | input_lock | `uint8` | V | Turned off / on by ConfigMenu_LockList. |

## Behavior

- V: functions: UIListGadget_SetCount, _Show, _SetCursor, _RefreshVisible, _OnInput, _IsAnimating.

## Open questions

None recorded.
