# UnitPanelCellsLanguage2

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F4930`
- **Rows:** 18 rows of 12 bytes
- **Keyed by:** panel cell 0..17
- **Row layout:** [UiSpriteCell](../structs/UiSpriteCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite cells of the unit status page, language 2 (18 cells). Verdict: designer-data.

## Behavior

- V: sub_14033054C (unit panel page task, event task 59): 18 cells placed through the cell placer; language 2 table
- V: loop of 18 with a 12-byte stride; 0xE0 bytes up to the next table: 216 of cells then an 8-byte rectangle; the first 216 bytes are also stored at 0x1408F8760 for the battle variant

## Notes

Our names. Tags: V layout.

## Open questions

None recorded.
