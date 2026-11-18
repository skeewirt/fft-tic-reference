# TitleMenuRowStorage

- **Kind:** observed behaviour
- **Scope:** where the title add-on keeps its rows and what lies after them
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [UIAddonFFTOTitle](../structs/UIAddonFFTOTitle.md), [TitleMenu_AddEntry](../functions/TitleMenu_AddEntry.md), [TitleMenu_MoveCursor](../functions/TitleMenu_MoveCursor.md), [TitleMenu_Build](../functions/TitleMenu_Build.md), [TitleMenu_FocusCurrent](../functions/TitleMenu_FocusCurrent.md), [TitleScreenLayout](../formats/TitleScreenLayout.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The title add-on stores six 24-byte rows at +72; the count, current row, last input tick and flags follow at +216..+230, and no instruction of the title code touches +231..+239, so a seventh row would overlap those fields.

## Behavior

- V: `UIAddonFFTOTitle` is 240 bytes (`Mem_Alloc(240)` in UIAddonFFTOTitle_Create 0x1401CB9B4, +72..+215 and +216..+230 cleared): +64 the TitleEnhanced node; +72 six rows of 24 bytes {button node, text node, kind byte at +16}; +216 count, +220 current row, +224 last input tick, +228 a save exists, +229 cleared, +230 idle timeout armed.
- V: a row's kind byte is read at +88 + 24 * index; row index 6 would have its kind byte at +232, its button node at +216 (the count) and its text node at +224 (the last input tick).
- V: the +48 part (`UIFFTOMenuFunctionBase`) reads the row count and current row at its +168 / +172, which are the add-on's +216 / +220 (menu code shared with other menus).
- V: the layout file has the row states Menu3..Menu6 only; GUINode_ApplyStateAtFrame with a name the file lacks (Menu7) changes nothing.
- V (seen live 2026-11-13): with seven rows set up, the title menu drew three rows: writing the node fields of the components returned by GUINode_FindDescendant does not move the rows (the parent's states animate the Reference parts).

## Open questions

None recorded.
