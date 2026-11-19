# GuideIcon_ToGlyph

- **Address:** `0x1400F681C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GuideIcon_ToGlyph(void *text, int icon, int variant)`
- **Callers:** sub_1400F7378, sub_1400F74F4, sub_14028BE4C
- **Callees:** sub_1400F5490

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a guide-bar icon number (UIButtonGuide guide_icon / guide_icon_2) and a variant byte to a glyph and draws it.

## Behavior

- V: icons 1 and 2 go to sub_1400F5490 with 26 / 27.
- V: icons 13, 15, 16, 17, 18 map to glyphs 11, 16, 17, 18, 19 and icon 19 to glyph 13, whatever the variant byte.
- V: icons 3..12, 14, 20 and 21 map to glyphs 3, 1, 2, 4, 5, 8, 6, 9, 7, 10, 12, 14, 15 in that order, but only when the variant byte is 0; with a non-zero variant nothing is drawn.
- V: the glyph is drawn with sub_1403DC7BC.

## Notes

Name is ours. The two variant bytes are UIButtonGuide +0x24 and +0x26.

## Open questions

? what the variant byte stands for.
