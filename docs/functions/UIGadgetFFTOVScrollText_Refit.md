# UIGadgetFFTOVScrollText_Refit

- **Address:** `0x1402AB174`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIGadgetFFTOVScrollText_Refit(UIGadgetFFTOVScrollText *g, int viewportHeight)`
- **Callers:** about 25 window methods (glossary, job windows, equipment windows ...) and UIGadgetFFTOJobDetailWindowWithButton_SetJobArgs
- **Callees:** sub_1403F1234, GUINode_SetSize, ScrollBar_SetPosition

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

After the text of a scroll-text gadget changed: lays the text out, sizes the text node to its laid-out height and sets up the scroll bar (range = text height, page = viewport height, position 0, bar visible only when the text is taller than the viewport).

## Behavior

- V: text = qword (g + 56); bar = qword (g + 24); arrow = qword (g + 32). Does nothing when text is null.
- V: sub_1403F1234(text) (re-lays out the text when dirty: the text-id refresh and GUITextNode_Layout), then GUINode_SetSize(text, width = text+64, height = text+436 - text+428), i.e. bottom - top of the layout bounds (GUITextNode_ComputeBounds output). The decompile lost the height in a register: it is r8d = [text+0x1B4] - [text+0x1AC].
- V: visible = textHeight > viewportHeight. bar: +652 = 0, +416 = visible, +660 = viewportHeight (page), +656 = max(1, textHeight) (range), +681 = 1, then ScrollBar_SetPosition(bar, 0, 1, 1). The arrow node's +416 = visible.

## State touched

- Calls: [GUINode_SetSize](GUINode_SetSize.md), [ScrollBar_SetPosition](ScrollBar_SetPosition.md)

## Referenced by

- Called by: [StatusScreen_SetCaption](StatusScreen_SetCaption.md)

## Notes

Name proposed (IDB: sub_1402AB174).

## Open questions

? the roles of bar+652 / +656 / +660 / +681 inside the scroll bar component (offsets as written).
