# NxdDataConfigCategory

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 249
- **Rows:** 16 rows of 16 bytes
- **Keyed by:** one key: id (0..15)
- **Read by:** [ConfigMenu_DrawRowValue](../functions/ConfigMenu_DrawRowValue.md), [ConfigMenu_SetTabTitles](../functions/ConfigMenu_SetTabTitles.md), [ConfigMenu_ShowTab](../functions/ConfigMenu_ShowTab.md), [UIAddonFFTOConfig_OnEvent](../functions/UIAddonFFTOConfig_OnEvent.md), [UIAddonFFTOConfig_OnInput](../functions/UIAddonFFTOConfig_OnInput.md)
- **Row layout:** [NxdDataConfigCategoryRow](../structs/NxdDataConfigCategoryRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Settings menu categories: the item ids each contains and a UI text key for the title. Verdict: designer-data.

## Behavior

- V: 16 rows, one key id (0..15); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 3 columns not decoded (see the row layout)
