# BannerWordCells

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140806A60`
- **Rows:** 204 rows of 12 bytes
- **Keyed by:** cell index (runs given by exe.ui.banner_word_ranges)
- **Read by:** [BannerWord_Draw](../functions/BannerWord_Draw.md)
- **Row layout:** [UiSpriteCell](../structs/UiSpriteCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite cells that build the 64 banner word images. Verdict: designer-data.

## Behavior

- V: 204 x 12 = 0x990; the next table starts at +0x994
- V: sub_140227AD8: builds one gradient quad per cell (colours from 0x1408073F4)

## Notes

Our names. Tags: V layout.

## Open questions

- ?: the words
