# ItemList_GetPossessionIndex

- **Address:** `0x1402C437C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall ItemList_GetPossessionIndex(int a1, int a2)`
- **Callers:** sub_1402C4550
- **Callees:** Item_GetRecord, UITable_GetRowByKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a possession-list row to the item or UI table row behind it: it switches on the list text id, walks the list element, and treats an entry at or above 261 as a UI table 0xEC row rather than an item.

## Behavior

- V: the UI object is reached through the manager at 0x143CD9DA8 plus 0x10 and 0x158.
- V: the text id is switched on `text_id - 0xF82D`, with branches for 0xF82D and five later ids reached by chained subtractions, not as literals.
- V: the list branches walk an array at object +0x90..+0x98 with 48-byte elements and take the element at the row index.
- V: the element's first field is a dword but is read as a 16-bit word; an entry below 261 (`0x1402C4458`) goes to `Item_GetRecord` and is returned as an item.
- V: an entry at or above 261 is fetched through `UITable_GetRowByKey(0xEC, ...)` at element +24, so it is a UI row, not an item.
- V: an item whose record is missing or whose record byte +0xA is below 0x14 also takes the table-row path.
- V: the function returns the mapped index, or -1 when the id has no row.
- V: the `0x105` test is a discriminator between two entry kinds, not an item-id bound; an item id and a table row share the dword.
- I: the switch is on the panel that owns the list, because the six text ids are the six possession-list headings.
- ?: whether a list may hold ids above 260 at all.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Notes

- V: whole function read. The 48-byte element stride and the 0x105 discriminator are read in this function.

## Open questions

None recorded.
