# NxdDataEventFlag

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** NXD file
- **NXD table id:** 219
- **Rows:** 1024 rows of 8 bytes
- **Keyed by:** one key: id (0..1023)
- **Row layout:** [NxdDataEventFlagRow](../structs/NxdDataEventFlagRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Index of 1024 event flag slots; rows carry only a designer comment slot. Verdict: engine-data.

## Behavior

- V: 1024 rows, one key id (0..1023); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id)
