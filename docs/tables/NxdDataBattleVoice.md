# NxdDataBattleVoice

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 183
- **Rows:** 53 rows of 44 bytes
- **Keyed by:** one key: id (0..52)
- **Row layout:** [NxdDataBattleVoiceRow](../structs/NxdDataBattleVoiceRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle voice cue definitions: numeric voice ids, group and probability parameters per cue. Verdict: designer-data.

## Behavior

- V: 53 rows, one key id (0..52); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 10 of 12 columns not decoded (see the row layout)
