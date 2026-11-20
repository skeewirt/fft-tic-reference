# ItemObtainedPanel_Fill

- **Address:** `0x1401A4A40`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ItemObtainedPanel_Fill(void *panel, ...)`
- **Callers:** not recorded
- **Callees:** UITable_GetRowByKey, GuiImage_SetIconById, FormatArgs_Push

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the 'obtained' panel for a book or a collection entry (part read).

## Behavior

- V: kind 1 uses text 1929, kind 2 text 1928.
- V: for kind 1, ids found in the 5-entry list at 0x140671EF0 are books: the Book row (table 148) key is (id - 17). Other ids are Collection (table 121) rows.
- V: in both cases the title is the row's string at +0x14 and the body the string at +0x1C (read as dword index 7 of the row; the string at +0x18 when +0x1C is empty); the icon is the dword at row +0x28 (icon_2) through GuiImage_SetIconById at +2784.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [GuiImage_SetIconById](GuiImage_SetIconById.md), [FormatArgs_Push](FormatArgs_Push.md)
- Reads: [tbl_ObtainedBookIds](../globals/tbl_ObtainedBookIds.md)

## Referenced by

- Called by: [sub_1401A4188](sub_1401A4188.md)

## Notes

Only the part that reads the Book row was read.

## Open questions

None recorded.
