# NxdDataFacilityVoicePattern

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 203
- **Rows:** 7 rows of 20 bytes
- **Keyed by:** one key: id (0..6)
- **Row layout:** [NxdDataFacilityVoicePatternRow](../structs/NxdDataFacilityVoicePatternRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Facility voice sound file paths (seven patterns). Verdict: designer-data.

## Behavior

- V: 7 rows, one key id (0..6); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 4 columns not decoded (see the row layout)
