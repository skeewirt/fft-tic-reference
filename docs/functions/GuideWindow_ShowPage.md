# GuideWindow_ShowPage

- **Address:** `0x14017D668`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GuideWindow_ShowPage(GuideWindow *w, unsigned int slot, unsigned int page)`
- **Callers:** ?
- **Callees:** sub_1400DB81C, UITable_GetRowByKeys, UITable_GetRowCount, GUITextNode_SetTextExpandedTemp, GuiImage_SetIconById, GUINode_FindState, GUINode_PlayState, sub_14017DA08

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows one page of an in-game guide: the GuidePage-en row (guide, page) gives the title, the text and an optional icon; the guide's page count is the size of its set.

## Behavior

- V: the guide key is dword +16 of the row sub_1400DB81C finds for the slot's id (w +1032 + 4 * slot, a 16-bit id; slot below w +1024).
- V: row = UITable_GetRowByKeys(188, guide, page) (nxd table 188 = GuidePage-en); the string at row +20 (relative to row +16) goes to the title text node (w +2256), the string at row +16 (relative to +16) to the body, the first element of the int array at +8 (when its count is above 0) is the icon (GuiImage_SetIconById), which picks the 'Image_Text' or 'Text' layout state.
- V: w +3060 = UITable_GetRowCount(188, guide) (the set's count), w +3056 = page; then sub_14017DA08(w, page, count).

## State touched

- Calls: [UITable_GetRowByKeys](UITable_GetRowByKeys.md), [UITable_GetRowCount](UITable_GetRowCount.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md), [GuiImage_SetIconById](GuiImage_SetIconById.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Notes

The page number is used as key2, and the page count is the set's record count: a guide's pages must be keys 0..n-1.

## Open questions

? which menu opens it (I: the help / guide window); ? what sub_14017DA08 draws (I: the page indicator).
