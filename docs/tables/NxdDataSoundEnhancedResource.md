# NxdDataSoundEnhancedResource

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 279
- **Rows:** 110 rows of 12 bytes
- **Keyed by:** one key: id (0..109)
- **Read by:** [EventSoundEntry_Append](../functions/EventSoundEntry_Append.md)
- **Row layout:** [NxdDataSoundEnhancedResourceRow](../structs/NxdDataSoundEnhancedResourceRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sound resource file paths (110). Verdict: engine-data.

## Behavior

- V: 110 rows, one key id (0..109); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
