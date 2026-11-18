# TitleMenu_MoveCursor

- **Address:** `0x1401C4154`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void TitleMenu_MoveCursor(void *part, int delta)`
- **Callers:** not recorded
- **Callees:** GUICore_FocusNode

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves the current row by a delta, wrapping when its flag is set, and focuses the row's button node.

## Behavior

- V: second vtable (the +48 part), slot 3; the row count and current row are seen from this part at +168 / +172 (add-on +216 / +220).
- V: focuses the new row's button node with `GUICore_FocusNode`.
- V: count = part +168 - 1, current = part +172; wrap (r8b): past the end -> 0, below 0 -> last; else clamped to 0..last; on a change `GUICore_FocusNode(*(part + 24 * (row + 1)))` = the button at add-on +72 + 24 * row. The current row is set by the focus event (19: +220 = node +548), not here.
- V: the part's count and current row at +168 / +172 are the title add-on's +216 / +220 (the +48 part is a `UIFFTOMenuFunctionBase`, vtable 0x14070A460, entry 3 = this function, entry 1 0x1402AB584; both addresses are data / neighbours, not in this body).

## State touched

- Calls: [GUICore_FocusNode](GUICore_FocusNode.md)

## Referenced by

- Called by: [UIMenuFunction_OnInput](UIMenuFunction_OnInput.md)
- Observed behaviours: [TitleMenuRowStorage](../behaviors/TitleMenuRowStorage.md)

## Open questions

None recorded.
