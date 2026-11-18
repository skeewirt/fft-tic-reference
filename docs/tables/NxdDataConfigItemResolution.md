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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
