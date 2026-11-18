# NxdDataUIColor

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 20
- **Rows:** 201 rows of 12 bytes
- **Keyed by:** one key: id (0..200)
- **Row layout:** [NxdDataUIColorRow](../structs/NxdDataUIColorRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Named UI colours (201). Verdict: engine-data.

## Behavior

- V: 201 rows, one key id (0..200); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id)
