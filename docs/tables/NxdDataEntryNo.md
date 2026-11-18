# NxdDataEntryNo

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 109
- **Rows:** 512 rows of 28 bytes
- **Keyed by:** one key: id (0..511)
- **Row layout:** [NxdDataEntryNoRow](../structs/NxdDataEntryNoRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per entry number (512): link to the sortie confirmation row plus parameters. Verdict: designer-data.

## Behavior

- V: 512 rows, one key id (0..511); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 2 of 5 columns not decoded (see the row layout)
