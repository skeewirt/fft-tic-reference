# EquipPanelCellsLanguage0V0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F3790`
- **Rows:** 19 rows of 12 bytes
- **Keyed by:** panel cell 0..18
- **Read by:** [sub_14032EDB8](../functions/sub_14032EDB8.md), [sub_14032F410](../functions/sub_14032F410.md), [sub_14032F9F8](../functions/sub_14032F9F8.md)
- **Row layout:** [UiSpriteCell](../structs/UiSpriteCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite cells of the equip screen panel, language 0, variant 0 (19 cells). Verdict: designer-data.

## Behavior

- V: loop of 19 with a 12-byte stride in all three equip panel tasks; selected by text language 0 and panel variant 0
- I: the table follows the rectangle list of the equip panels; it is not a candidate of its own (the candidate 0x1408F3778 lies in the rectangle list before it)

## Notes

Our names. Found beside the table at 0x1408F3778; tags V layout.

## Open questions

None recorded.
