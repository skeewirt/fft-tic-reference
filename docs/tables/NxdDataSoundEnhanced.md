# NxdDataSoundEnhanced

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 280
- **Rows:** 254 rows of 24 bytes
- **Keyed by:** one key: id (0..253)
- **Read by:** [EventSoundEntry_Append](../functions/EventSoundEntry_Append.md)
- **Row layout:** [NxdDataSoundEnhancedRow](../structs/NxdDataSoundEnhancedRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Enhanced music cue definitions (254) linked to sound resources. Verdict: engine-data.

## Behavior

- V: 254 rows, one key id (0..253); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 5 of 6 columns not decoded (see the row layout)
