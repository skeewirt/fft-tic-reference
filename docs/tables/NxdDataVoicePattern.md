# NxdDataVoicePattern

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 185
- **Rows:** 110 rows of 24 bytes
- **Keyed by:** one key: id (0..109)
- **Row layout:** [NxdDataVoicePatternRow](../structs/NxdDataVoicePatternRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Voice patterns (110). Verdict: designer-data.

## Behavior

- V: 110 rows, one key id (0..109); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 5 of 7 columns not decoded (see the row layout)
