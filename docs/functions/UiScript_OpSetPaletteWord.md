# UiScript_OpSetPaletteWord

- **Address:** `0x140328734`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpSetPaletteWord(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 9: sets the palette word of the following cells.

## Behavior

- V: the word is (+3 and 0x3F) | (nine-bit value << 6) with the nine-bit value (+2 << 8) + +4 wrapped to 0x1FF; it is stored in the palette word global that the cell handlers pass to the cell queue.
- V: returns the pointer after the record.

## Notes

Same packing as ClassicUi_OpSetTexturePageA.

## Open questions

None recorded.
