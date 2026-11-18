# NxdDataGuidePage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 188
- **Rows:** 409 rows of 24 bytes, text in 7 languages
- **Keyed by:** two keys: id (0..3277) x id2 (0..7)
- **Read by:** [GuideWindow_ShowPage](../functions/GuideWindow_ShowPage.md)
- **Row layout:** [NxdDataGuidePageRow](../structs/NxdDataGuidePageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Guide pages keyed by guide id and page index: icon id arrays and text slots. Verdict: designer-data.

## Behavior

- V: 409 rows, two keys id (0..3277) x id2 (0..7); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 5 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
