# WindowPattern_FillRow

- **Address:** `0x1403324F8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WindowPattern_FillRow(int unused, unsigned short *dest, int words, int templateBase)`
- **Callers:** WindowPattern_Build, sub_140331EEC, sub_140361B68, sub_140361F74
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills one row of a window frame pattern from a six-word template.

## Behavior

- V: writes template words 0 and 1 at the row start and words 6 and 7 at the row end, then repeats words 2, 3, 4 and 5 across the middle with a stride of four words (each word starting at its own offset).

## Referenced by

- Called by: [WindowPattern_Build](WindowPattern_Build.md)
- Reads tables: [WindowPatternTiles](../tables/WindowPatternTiles.md)

## Notes

Read in full.

## Open questions

?: the pixel meaning of the words.
