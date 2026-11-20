# NxdDataGeneralJob

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** NXD file
- **NXD table id:** 189
- **Rows:** 21 rows of 124 bytes
- **Keyed by:** one key: id (0..20)
- **Read by:** [GameState_ResetJobFlags](../functions/GameState_ResetJobFlags.md), [Job_GetJpForLevel](../functions/Job_GetJpForLevel.md)
- **Row layout:** [NxdDataGeneralJobRow](../structs/NxdDataGeneralJobRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per general job (21): arrays of required jobs, levels, positions and experience, and tree placement parameters. Verdict: designer-data.

## Behavior

- V: 21 rows, one key id (0..20); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
