# UiScript_OpDrawNumber

- **Address:** `0x140328920`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpDrawNumber(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table), sub_14021C620 (four direct calls)
- **Callees:** sub_14032A204 (formats the number), sub_14031DA24, the row callback

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slots 13, 25, 26 and 27: draws a number or a gauge for a value supplied by a row callback.

## Behavior

- V: record: +2 digit size (1, 0 or other), +3 callback index, +4 digit count, +5 spacing, +6 alternate-palette flag, +7 x of the first digit, +8 y, +9 immediate argument. The y gets the list row offset in list mode. A null callback entry makes the argument itself the value.
- V: the value is signed: the sign is kept and the magnitude used; bit 30 of the magnitude (cleared before use) switches to a second alternate palette word; bit 29 switches to the gauge. +6 non-zero selects the first alternate palette word.
- V: number: formatted as decimal and drawn right aligned over the digit count with the given spacing; digits are texture cells laid side by side (size 1: 8 x 14, size 0: 6 x 11). Other sizes draw no digits in this table. A minus sign cell (6 x 11) takes the first position when negative; opcode 26 puts it at a fixed x.
- V: leading positions: opcode 25 leaves them blank; opcodes 13, 26 and 27 draw a zero glyph there (sizes 0 and 1 only); opcode 26 draws those zeros with the alternate palette except on the last position.
- V: opcodes 25 and 27 pass the shared tint colour record to the cell queue, 13 and 26 pass none (the opcode is read from the record's first byte).
- V: gauge: draws the digit-count number of small 6 x 3 cells spaced by +5 from x +7, whatever the value's low bits.
- V: returns the pointer after the record.

## Notes

Registered at four slots. The item-page twin ClassicItemUi_OpDrawNumber has one slot, draws digits for the third size too (in two texture rows) and puts the gauge cells 1 pixel further left.

## Open questions

?: what the pages use bit 29 for (only the flag is read).
