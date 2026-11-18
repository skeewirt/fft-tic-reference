# NxdDataConfigPadList

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 273
- **Rows:** 4 rows of 20 bytes
- **Keyed by:** one key: id (0..3)
- **Read by:** [ConfigMenu_DrawRowValue](../functions/ConfigMenu_DrawRowValue.md), [UIAddonFFTOConfig_OnEvent](../functions/UIAddonFFTOConfig_OnEvent.md)
- **Row layout:** [NxdDataConfigPadListRow](../structs/NxdDataConfigPadListRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Four pad lists used by settings rows. Verdict: engine-data.

## Behavior

- V: 4 rows, one key id (0..3); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 4 columns not decoded (see the row layout)
