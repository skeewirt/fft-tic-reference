# JobCommand

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** NXD file
- **NXD table id:** 41
- **Keyed by:** command id
- **Read by:** [JobCommandTable_GetRow](../functions/JobCommandTable_GetRow.md), [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md), [UIText_ResolveCategoryRow](../functions/UIText_ResolveCategoryRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The job command rows (the JobCommand-en table), read through JobCommandTable_GetRow.

## Behavior

- V: JobCommandTable_GetRow caches table 41 (0x29); UIText_ResolveCategoryRow sends the category 'JobCommand' to the same id.

## Notes

NXD tables are loaded through the shared registry (NxdRegistry_Find by table id) and read with NxdTable_GetRowById or a key lookup; the file format is described by the NXD format records.

## Open questions

None recorded.
