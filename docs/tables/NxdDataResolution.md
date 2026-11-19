# NxdDataResolution

- **Kind:** table
- **Area:** [Display](../areas/display.md)
- **Storage:** NXD file
- **NXD table id:** 257
- **Rows:** 9 rows of 16 bytes
- **Keyed by:** one key: id (1..9)
- **Read by:** [ConfigMenu_DrawRowValue](../functions/ConfigMenu_DrawRowValue.md), [UIAddonFFTOConfig_OnEvent](../functions/UIAddonFFTOConfig_OnEvent.md)
- **Row layout:** [NxdDataResolutionRow](../structs/NxdDataResolutionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The nine selectable resolutions (width and height). Verdict: engine-data.

## Behavior

- V: 9 rows, one key id (1..9); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 4 columns not decoded (see the row layout)
