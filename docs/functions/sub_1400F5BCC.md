# sub_1400F5BCC

- **Address:** `0x1400F5BCC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char sub_1400F5BCC(__int64 focusOwner, GUINode **nodes, int count, int cursor, _BYTE *opts)`
- **Callers:** sub_1402A9944 (the Active / Deactive tab switcher; it builds opts {x, x, 1} on the stack)
- **Callees:** GUICore_FocusNode, sub_1400F5674, sub_1400F5C78

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same as sub_1400F5B0C but takes the option struct as a pointer instead of two flags.

## Behavior

- V: identical focus logic to sub_1400F5B0C (valid = nodes && count > cursor && cursor >= 0; focus nodes[cursor] with sub_1400F5674 when focusOwner != 0 and valid; GUICore_FocusNode(0) when invalid and focusOwner == 0).
- V: loops i over 0..count-1 and calls sub_1400F5C78(node, opts, i == cursor) for every non-null node with the caller's opts (no copy).

## State touched

- Calls: [GUICore_FocusNode](GUICore_FocusNode.md), [sub_1400F5674](sub_1400F5674.md)

## Referenced by

- Called by: [TabBar_Select](TabBar_Select.md)

## Notes

Proposed name GUINodeList_SetCursorEx.

## Open questions

? see sub_1400F5B0C.
