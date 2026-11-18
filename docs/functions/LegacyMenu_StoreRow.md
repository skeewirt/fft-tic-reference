# LegacyMenu_StoreRow

- **Address:** `0x1402378C8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LegacyMenu_StoreRow(void)`
- **Callers:** sub_14022AFEC
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores the row chosen in the current legacy menu into the acting unit's row memory, for the menus that remember it.

## Behavior

- V: looks for the current menu id among the first 12 records of the menu row result table (0x1407DCFF0) and copies the node's row byte (+80) into the unit's 17-byte memory (0x1407DD1E0).

## Referenced by

- Reads tables: [LegacyMenuRowResults](../tables/LegacyMenuRowResults.md)

## Open questions

None recorded.
