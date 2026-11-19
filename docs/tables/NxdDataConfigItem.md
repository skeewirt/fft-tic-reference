# NxdDataConfigItem

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 250
- **Rows:** 61 rows of 76 bytes
- **Keyed by:** one key: id (0..60)
- **Read by:** [ConfigMenu_DrawRowValue](../functions/ConfigMenu_DrawRowValue.md), [ConfigMenu_EnableRowWidgets](../functions/ConfigMenu_EnableRowWidgets.md), [ConfigMenu_ReadSettings](../functions/ConfigMenu_ReadSettings.md), [ConfigMenu_SetHelpText](../functions/ConfigMenu_SetHelpText.md), [ConfigMenu_ShowTab](../functions/ConfigMenu_ShowTab.md), [ConfigMenu_UpdateFooter](../functions/ConfigMenu_UpdateFooter.md), [UIAddonFFTOConfig_OnEvent](../functions/UIAddonFFTOConfig_OnEvent.md), [UIAddonFFTOConfig_OnInput](../functions/UIAddonFFTOConfig_OnInput.md), [UIAddonFFTOConfig_RefreshRowTexts](../functions/UIAddonFFTOConfig_RefreshRowTexts.md)
- **Row layout:** [NxdDataConfigItemRow](../structs/NxdDataConfigItemRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Settings menu rows (61): pad list, name and description UI text keys and value-kind parameters. Verdict: designer-data.

## Behavior

- V: 61 rows, one key id (0..60); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 15 of 18 columns not decoded (see the row layout)
