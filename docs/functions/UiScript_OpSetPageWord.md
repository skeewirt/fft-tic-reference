# UiScript_OpSetPageWord

- **Address:** `0x1403287FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpSetPageWord(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 12: composes the texture-page and blend attribute word of the following cells.

## Behavior

- V: bit 0 of +2 goes to bit 4 of the word, +3 >> 2 (4 bits) to bits 0..3, bits 4..5 of +2 to bits 5..6 and the low two bits of +4 to bits 7..8.
- I: the layout matches a graphics-chip page word (page column, page row, blend mode, colour depth).
- V: returns the pointer after the record.

## Notes

Same word as ClassicUi_OpSetBlendWord builds.

## Open questions

None recorded.
