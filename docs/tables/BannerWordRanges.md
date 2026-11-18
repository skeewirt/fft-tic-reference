# BannerWordRanges

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1406724C0`
- **Rows:** 65 rows of 4 bytes
- **Keyed by:** banner word id 0..63 (the next entry gives the end)
- **Read by:** [BannerWord_Draw](../functions/BannerWord_Draw.md)
- **Row layout:** [BannerWordRange](../structs/BannerWordRange.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

For each of 64 banner word images, which run of sprite cells builds it. Verdict: designer-data.

## Behavior

- V: 65 monotonic entries 0..204 then -1; 204 = the cell count of 0x140806A60
- V: sub_140227AD8 (banner word draw): start = table[id], count = table[id + 1] - start, cells from 0x140806A60

## Notes

Our names. Tags: V layout, ? meaning of ids.

## Open questions

- ?: which in-game words the 64 ids are (the id comes from word_1407DCF86, set by sub_140236468 from tile data and an event value)
