# EquipPanelCellsLanguage3V2

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F44F0`
- **Rows:** 19 rows of 12 bytes
- **Keyed by:** panel cell 0..18
- **Read by:** [sub_14032EDB8](../functions/sub_14032EDB8.md), [sub_14032F410](../functions/sub_14032F410.md), [sub_14032F9F8](../functions/sub_14032F9F8.md)
- **Row layout:** [UiSpriteCell](../structs/UiSpriteCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite cells of the equip screen panel, language 3, variant 2 (19 cells). Verdict: designer-data.

## Behavior

- V: sub_14032EDB8 (equip panel task, five words), sub_14032F410 (two-row variant) and sub_14032F9F8 (detail variant): 19 cells placed through the cell placer with the panel origin; selected by text language 3 and panel variant 2
- V: loop of 19 with a 12-byte stride in all three readers; selection by language record (+8) and a variant of 0..3; the 12 bytes after the cells (rectangle) are a separate table

## Notes

Our names. Tags: V layout, I variant meaning.

## Open questions

None recorded.
