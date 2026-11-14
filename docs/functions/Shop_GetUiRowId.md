# Shop_GetUiRowId

- **Address:** `0x1402ACA48`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Shop_GetUiRowId(int shop_id)`
- **Callers:** sub_140198E78, sub_14019F498, sub_1401AD6F8, sub_1401B0A7C, sub_1402AC878, Shop_Open
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, sub_1400DAA64, sub_1400FF8A4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a shop number to the UI table row that holds its name and description: the two special shops get fixed rows and every ordinary shop uses the common row.

## Behavior

- V: shop 100 returns 0x73 and shop 101 returns 0x72.
- V: shop 0x18F takes the special branch: it loads the shared UI object, checks a byte and returns 0x71 or 0x76.
- V: every other shop id returns 0x6E.
- V: the 0x18F branch calls the NXD registry and row accessors to test whether the special row is unlocked.
- V: the function does not read the shop table itself; it only chooses the UI row.
- V: the six callers are the shop, den and town menu screens.
- I: 0x6E is the generic shop tooltip row, and 100/101 are the two Poachers Den variants.
- ?: what the 0x18F id selects; the branch tests a table row but the row content was not read.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Called by: [Shop_Open](Shop_Open.md)

## Notes

Whole function read (171 bytes).

## Open questions

None recorded.
