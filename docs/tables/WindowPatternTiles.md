# WindowPatternTiles

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B8260`
- **Rows:** 2088 rows of 2 bytes
- **Keyed by:** pattern word index (64 words per row type)
- **Read by:** [WindowPattern_Build](../functions/WindowPattern_Build.md), [WindowPattern_FillRow](../functions/WindowPattern_FillRow.md)
- **Row layout:** [WindowPatternWord](../structs/WindowPatternWord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Line patterns of the legacy window frames (borders and gradient rows) as 16-bit words, in a block of 2088 words. Verdict: designer-data.

## Behavior

- V: WindowPattern_Build (0x140332330): for each of up to 24 window rows picks a template base (multiples of 64 words, or 1078 + 64 x n) and copies it with WindowPattern_FillRow
- V: WindowPattern_FillRow (0x1403324F8): copies the two start words, the two end words and repeats four words across the row
- V: sub_140331EEC and sub_140361B68 and sub_140361F74: text window builders that call them
- V: readers use word [template + 0..9]; templates start every 64 words; the block runs 0x1050 bytes to the next symbol

## Notes

Our names. Tags: V reads and strides, I meaning of the words.

## Open questions

- ?: which template is which frame part
