# NxdDataUIAddon

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 24
- **Rows:** 264 rows of 36 bytes
- **Keyed by:** one key: id (0..263)
- **Row layout:** [NxdDataUIAddonRow](../structs/NxdDataUIAddonRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

UI add-on definitions (264): UI file path and flags. Verdict: engine-data.

## Behavior

- V: 264 rows, one key id (0..263); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 22 of 24 columns not decoded (see the row layout)
