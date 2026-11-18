# Job

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** NXD file
- **NXD table id:** 46
- **Keyed by:** job id
- **Read by:** [JobTable_GetRow](../functions/JobTable_GetRow.md), [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md)
- **Row layout:** [NxdDataJobRow](../structs/NxdDataJobRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The job rows (the Job-en table), read through JobTable_GetRow. The stock job table in the executable is a separate table.

## Behavior

- V: JobTable_GetRow caches table 46 (0x2E); it returns null when the row is missing.

## Notes

NXD tables are loaded through the shared registry (NxdRegistry_Find by table id) and read with NxdTable_GetRowById or a key lookup; the file format is described by the NXD format records.

## Open questions

None recorded.
