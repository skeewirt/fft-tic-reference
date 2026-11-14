# sub_14033DDFC

- **Address:** `0x14033DDFC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void sub_14033DDFC(int slot, int16_t *row_out, int16_t *scroll_out, uint16_t *list)`
- **Callers:** sub_14039297C, sub_140392DB8
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The cursor restore of the unit-pointer screens: the same job as sub_1402C0554, reading its saved entries (row, scroll, word) from the table at xmmword_143829E10.

## Behavior

- V: the saved entry is three words at xmmword_143829E10 + 6 * slot; the row and scroll go to the outputs.
- V: when the word at the saved row equals the saved word, it returns at once (there is no terminator count, unlike sub_1402C0554).
- V: otherwise it scans the list from row 0 to the first 0xFFFF for the first word that, masked with 0x3FF, equals the saved word; no match sets both outputs to 0.
- V: the saved word and the word at the saved row are read sign-extended; the scanned words zero-extended.

## Referenced by

- Called by: [sub_14039297C](sub_14039297C.md)

## Notes

- V: callers: sub_14039297C with slot 4 (the job list; its saver masks the word with 0x3FF at 0x140392B40) and sub_140392DB8 (the Learn list twin; saver mask at 0x140393077).

## Open questions

- ?: which screen the unit-pointer job and Learn lists belong to (not told apart live).
