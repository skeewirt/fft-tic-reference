# NxdDataUIAddonPriority

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 81
- **Rows:** 8 rows of 12 bytes
- **Keyed by:** one key: id (0..7)
- **Row layout:** [NxdDataUIAddonPriorityRow](../structs/NxdDataUIAddonPriorityRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

UI add-on priorities (8). Verdict: engine-data.

## Behavior

- V: 8 rows, one key id (0..7); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 2 of 3 columns not decoded (see the row layout)
