# NxdDataJobType

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** NXD file
- **NXD table id:** 200
- **Rows:** 124 rows of 16 bytes
- **Keyed by:** one key: id (1..124)
- **Row layout:** [NxdDataJobTypeRow](../structs/NxdDataJobTypeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per job look type (124): male and female icon ids. Verdict: designer-data.

## Behavior

- V: 124 rows, one key id (1..124); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id)
