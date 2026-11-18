# NxdDataUnitVoice

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 204
- **Rows:** 10 rows of 28 bytes
- **Keyed by:** one key: id (0..9)
- **Row layout:** [NxdDataUnitVoiceRow](../structs/NxdDataUnitVoiceRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Unit voice type definitions (10). Verdict: designer-data.

## Behavior

- V: 10 rows, one key id (0..9); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 5 of 7 columns not decoded (see the row layout)
