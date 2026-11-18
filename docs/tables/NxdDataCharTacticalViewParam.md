# NxdDataCharTacticalViewParam

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 292
- **Rows:** 6 rows of 32 bytes
- **Keyed by:** two keys: id (1..3) x id2 (0..1)
- **Row layout:** [NxdDataCharTacticalViewParamRow](../structs/NxdDataCharTacticalViewParamRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Tactical-camera view parameters as float arrays per view and variant. Verdict: engine-data.

## Behavior

- V: 6 rows, two keys id (1..3) x id2 (0..1); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 3 of 5 columns not decoded (see the row layout)
