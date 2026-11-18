# LegacyMenuRowResults

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407DCFF0`
- **Rows:** 31 rows of 16 bytes
- **Keyed by:** menu node id (key at +0)
- **Read by:** [LegacyMenu_StoreRow](../functions/LegacyMenu_StoreRow.md)
- **Row layout:** [LegacyMenuRowResultRecord](../structs/LegacyMenuRowResultRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per legacy menu, the result code of each row (and which menus remember the row per unit). Verdict: designer-data.

## Behavior

- V: 31 records x 16 bytes to 0x1407DD1E0; loops of 12 and of 31
- V: sub_1402346D0 (legacy menu open): the first 12 menus restore the row each unit last chose (per-unit bytes at 0x1407DD1E0, 17 per unit)
- V: sub_1402378C8: stores the chosen row of those 12 menus back
- V: sub_140237FA4: maps the current menu and row to the result code (searches all 31)

## Notes

Our names. Tags: V layout, ? codes.

## Open questions

- ?: meaning of the result codes
