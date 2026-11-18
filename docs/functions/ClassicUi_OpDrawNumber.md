# ClassicUi_OpDrawNumber

- **Address:** `0x140390BA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpDrawNumber(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** sub_14038F3FC, sub_14032A204

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 13: draws a number or a row of gauge cells for a value supplied by the page.

## Behavior

- V: the value comes from the page's condition function at byte +3 (argument +9, or the list row in a list page).
- V: bit 29 of the value switches to a gauge: that many cells (+4) spaced by +5; otherwise the value is formatted with %d and its digits are drawn right aligned over +4 digit cells with spacing +5, blanks for the missing leading digits.
- V: bit 30 of the value selects an alternate colour word.

## Open questions

None recorded.
