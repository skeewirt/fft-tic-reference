# BannerWord_Draw

- **Address:** `0x140227AD8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BannerWord_Draw(int wordId, void *quads)`
- **Callers:** sub_140227558 (battle action display script task)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the gradient quads of one banner word image from its run of sprite cells.

## Behavior

- V: the run is [start, next start) of the banner word range table (0x1406724C0), the cells come from the banner cell table (0x140806A60, 12 bytes each; its address is an image-relative displacement added to the scaled run start, not an absolute operand).
- V: each cell gives four corners from its texture position, size and screen offset; the corner colours come from the banner colour table (0x1408073F4).
- V: with text language 2 the cells are shifted right (one special cell by the narrowest offset of the run, the others by 13).
- V: returns the cell count.

## Referenced by

- Reads tables: [BannerWordCells](../tables/BannerWordCells.md), [BannerWordColours](../tables/BannerWordColours.md), [BannerWordRanges](../tables/BannerWordRanges.md)

## Open questions

None recorded.
