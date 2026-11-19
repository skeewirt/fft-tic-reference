# NxdDataEventCharaDraw

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** NXD file
- **NXD table id:** 234
- **Rows:** 24 rows of 20 bytes
- **Keyed by:** two keys: id (14..489) x id2 (0..2)
- **Row layout:** [NxdDataEventCharaDrawRow](../structs/NxdDataEventCharaDrawRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Event character draw settings keyed by event and slot; a character control id and parameters. Verdict: designer-data.

## Behavior

- V: 24 rows, two keys id (14..489) x id2 (0..2); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 7 of 8 columns not decoded (see the row layout)
