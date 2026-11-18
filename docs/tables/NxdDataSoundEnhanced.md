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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 6 columns not decoded (see the row layout)
