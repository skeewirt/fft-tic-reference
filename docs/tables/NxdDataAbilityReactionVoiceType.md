# NxdDataAbilityReactionVoiceType

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 330
- **Rows:** 4 rows of 48 bytes
- **Keyed by:** one key: id (0..3)
- **Row layout:** [NxdDataAbilityReactionVoiceTypeRow](../structs/NxdDataAbilityReactionVoiceTypeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Four rows of numeric voice-reaction parameters selected by an ability's reaction voice type; columns not decoded. Verdict: engine-data.

## Behavior

- V: 4 rows, one key id (0..3); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 12 of 12 columns not decoded (see the row layout)
