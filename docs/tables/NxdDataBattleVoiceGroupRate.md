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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 50 of 52 columns not decoded (see the row layout)
