# LegacyMenu_LoadRowList

- **Address:** `0x1402B29D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void *LegacyMenu_LoadRowList(void)`
- **Callers:** the legacy menu tasks
- **Callees:** BattleCommand_BuildScreen

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the row id list of the legacy menu named by the screen block into the live row array and starts the menu command screen.

## Behavior

- V: the menu id is the signed word at +872 of the active screen block; the row count comes from exe.ui.legacy_menu_row_counts and the list from exe.ui.legacy_menu_row_list_pointers.
- V: each row byte is turned into a text id by subtracting a fixed base and stored in the live row array; at most 7 rows are shown on a page (the first word is the count shown, the second the overflow).
- V: ends by calling the command screen builder BattleCommand_BuildScreen.

## State touched

- Calls: [BattleCommand_BuildScreen](BattleCommand_BuildScreen.md)

## Referenced by

- Reads tables: [LegacyMenuRowCounts](../tables/LegacyMenuRowCounts.md), [LegacyMenuRowListPointers](../tables/LegacyMenuRowListPointers.md)

## Notes

Name is ours; the existing name of the callee comes from an earlier pass.

## Open questions

None recorded.
