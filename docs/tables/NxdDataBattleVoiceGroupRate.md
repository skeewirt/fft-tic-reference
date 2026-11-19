# NxdDataBattleVoiceGroupRate

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 184
- **Rows:** 6 rows of 208 bytes
- **Keyed by:** one key: id (0..5)
- **Row layout:** [NxdDataBattleVoiceGroupRateRow](../structs/NxdDataBattleVoiceGroupRateRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Six rows of 50 percentage weights, one per battle voice group, choosing how often each voice group plays. Verdict: designer-data.

## Behavior

- V: 6 rows, one key id (0..5); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
