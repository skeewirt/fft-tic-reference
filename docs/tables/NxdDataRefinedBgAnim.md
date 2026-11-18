# NxdDataRefinedBgAnim

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 49
- **Rows:** 280 rows of 12 bytes
- **Keyed by:** two keys: id (0..116) x id2 (0..12)
- **Row layout:** [NxdDataRefinedBgAnimRow](../structs/NxdDataRefinedBgAnimRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Remastered background animations keyed by map and slot. Verdict: engine-data.

## Behavior

- V: 280 rows, two keys id (0..116) x id2 (0..12); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 3 of 3 columns not decoded (see the row layout)
