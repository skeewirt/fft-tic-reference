# NxdDataConfigItemCursorMoveType

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 268
- **Rows:** 2 rows of 20 bytes
- **Keyed by:** one key: id (0..1)
- **Read by:** [ConfigMenu_ReadSettings](../functions/ConfigMenu_ReadSettings.md), [ConfigMenu_SetHelpText](../functions/ConfigMenu_SetHelpText.md)
- **Row layout:** [NxdDataConfigItemCursorMoveTypeRow](../structs/NxdDataConfigItemCursorMoveTypeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Option values for the cursor-movement setting. Verdict: engine-data.

## Behavior

- V: 2 rows, one key id (0..1); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 4 of 5 columns not decoded (see the row layout)
