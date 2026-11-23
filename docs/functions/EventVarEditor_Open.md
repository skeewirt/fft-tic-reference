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

It lists event variables and lets a value be changed.

## Open questions

? whether play starts it: mask 0x800000 of 0x141D32E14 is set only by sub_1402B4710 when word_143749F38 is 1; that word is set only by the event-task entry sub_1402B3D1C, which four data records reference (0x14080D008, 0x14080D748, 0x14080DE88, 0x14080E5C8). Whether play starts that task is unknown.
