# NxdDataUIAnnounce

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 68
- **Rows:** 123 rows of 28 bytes
- **Keyed by:** one key: id (0..3005)
- **Row layout:** [NxdDataUIAnnounceRow](../structs/NxdDataUIAnnounceRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Announcement banner definitions (123). Verdict: designer-data.

## Behavior

- V: 123 rows, one key id (0..3005); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 5 of 7 columns not decoded (see the row layout)
