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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 6 of 8 columns not decoded (see the row layout)
