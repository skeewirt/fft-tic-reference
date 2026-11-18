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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 4 columns not decoded (see the row layout)
