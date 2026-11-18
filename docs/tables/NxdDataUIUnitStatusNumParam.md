# NxdDataUIUnitStatusNumParam

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 197
- **Rows:** 19 rows of 16 bytes
- **Keyed by:** one key: id (1..19)
- **Row layout:** [NxdDataUIUnitStatusNumParamRow](../structs/NxdDataUIUnitStatusNumParamRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Unit status number fields (19). Verdict: engine-data.

## Behavior

- V: 19 rows, one key id (1..19); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 3 of 4 columns not decoded (see the row layout)
