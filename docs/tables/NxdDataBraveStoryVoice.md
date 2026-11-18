# NxdDataBraveStoryVoice

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 233
- **Rows:** 34 rows of 16 bytes
- **Keyed by:** two keys: id (0..11) x id2 (0..2)
- **Row layout:** [NxdDataBraveStoryVoiceRow](../structs/NxdDataBraveStoryVoiceRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Voice line references for the Brave Story scenes, keyed by scene and line; each row points at a packed audio entry and a timing float. Verdict: designer-data.

## Behavior

- V: 34 rows, two keys id (0..11) x id2 (0..2); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 4 columns not decoded (see the row layout)
