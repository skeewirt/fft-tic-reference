# NxdDataDifficultyLevel

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 111
- **Rows:** 3 rows of 28 bytes
- **Keyed by:** one key: id (0..2)
- **Row layout:** [NxdDataDifficultyLevelRow](../structs/NxdDataDifficultyLevelRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The three play modes: UI text key and numeric parameters. Verdict: designer-data.

## Behavior

- V: 3 rows, one key id (0..2); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 4 of 7 columns not decoded (see the row layout)
