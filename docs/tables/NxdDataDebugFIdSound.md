# NxdDataDebugFIdSound

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 89
- **Rows:** 691 rows of 8 bytes
- **Keyed by:** one key: id (0..690)
- **Row layout:** [NxdDataDebugFIdSoundRow](../structs/NxdDataDebugFIdSoundRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Debug sound id list (691 rows). Verdict: engine-data.

## Behavior

- V: 691 rows, one key id (0..690); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id)
