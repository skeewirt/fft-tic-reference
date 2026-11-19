# NxdDataConfigItemResolution

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 252
- **Rows:** 9 rows of 8 bytes
- **Keyed by:** one key: id (0..8)
- **Read by:** [ConfigMenu_DrawRowValue](../functions/ConfigMenu_DrawRowValue.md), [ConfigMenu_ReadSettings](../functions/ConfigMenu_ReadSettings.md), [UIAddonFFTOConfig_OnEvent](../functions/UIAddonFFTOConfig_OnEvent.md)
- **Row layout:** [NxdDataConfigItemResolutionRow](../structs/NxdDataConfigItemResolutionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Option list of the resolution setting (nine rows pointing at Resolution). Verdict: engine-data.

## Behavior

- V: 9 rows, one key id (0..8); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
