# EventVarEditor_Open

- **Address:** `0x14036DB30`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t EventVarEditor_Open(void)`
- **Callers:** ClassicMenu_HubStep
- **Callees:** EventVarEditor_DrawPage, WorldMenu_AllocOverlayRecord, WorldMenu_AllocWindowRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the event variable editor: creates its window and pushes kind 11.

## Behavior

- V: creates two windows (WorldMenu_AllocOverlayRecord, WorldMenu_AllocWindowRecord), marks the list window busy, calls EventVarEditor_DrawPage and pushes kind 11 with the cursor at an offset of (8, 12) from the list window.

## State touched

- Calls: [EventVarEditor_DrawPage](EventVarEditor_DrawPage.md), [WorldMenu_AllocOverlayRecord](WorldMenu_AllocOverlayRecord.md), [WorldMenu_AllocWindowRecord](WorldMenu_AllocWindowRecord.md)

## Referenced by

- Called by: [ClassicMenu_HubStep](ClassicMenu_HubStep.md)

## Notes

It lists event variables and lets a value be changed. Its original opener (read in the functions named, not in this body) was row 8 of the old main world menu: node 15 runs LegacyWorldMenu_RequestEventVarEditor, which sets word_143749F38 = 1; LegacyWorldMenu_FrameStep turns it into mask 0x800000 of 0x141D32E14 and ClassicMenu_HubStep calls this function (0x14080D008, 0x14080D748, 0x14080DE88 and 0x14080E5C8 are the +48 task fields of node 15 in the four language tables, whose records start at 0x14080CFD8, 0x14080D718, 0x14080DE58 and 0x14080E598).

## Open questions

? whether play can still reach it: the old main world menu's task confirms only its roster row (LegacyWorldMainMenuRows).
