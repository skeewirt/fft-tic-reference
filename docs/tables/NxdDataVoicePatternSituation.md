# NxdDataVoicePatternSituation

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 196
- **Rows:** 18 rows of 16 bytes
- **Keyed by:** two keys: id (0..8) x id2 (0..2)
- **Row layout:** [NxdDataVoicePatternSituationRow](../structs/NxdDataVoicePatternSituationRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Voice pattern situations keyed by pattern and slot, with story-condition links. Verdict: designer-data.

## Behavior

- V: 18 rows, two keys id (0..8) x id2 (0..2); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 4 columns not decoded (see the row layout)
