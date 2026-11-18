# NxdDataConfigPadAssign

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 270
- **Rows:** 4 rows of 20 bytes
- **Keyed by:** two keys: id (1..2) x id2 (1..2)
- **Read by:** [ConfigMenu_DrawRowValue](../functions/ConfigMenu_DrawRowValue.md)
- **Row layout:** [NxdDataConfigPadAssignRow](../structs/NxdDataConfigPadAssignRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pad button assignment presets keyed by two ids. Verdict: engine-data.

## Behavior

- V: 4 rows, two keys id (1..2) x id2 (1..2); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
