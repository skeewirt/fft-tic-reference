# KeyLongPress

- **Kind:** observed behaviour
- **Scope:** engine (input rows)
- **Area:** [Input](../areas/input.md)
- **Affects:** [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md), [InputRows_ApplyKeyBindings](../functions/InputRows_ApplyKeyBindings.md), [InputRows_ApplyPadLayout](../functions/InputRows_ApplyPadLayout.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A long-press binding reports pressed and held only after 1000 ms down: the pad flag 0x10000 and the key flag 0x80000.

## Behavior

- V: while the key is down, held and pressed stay 0 until the UI clock minus the press time reaches 1000 ms; then held is 1 and pressed is set for the frame in which the mark is crossed.
- M: the 9 UIKeyAssign rows with key_long_press set (70, 73, 93, 100, 106, 123, 173, 180, 251) all have the pad long-press flag of layout 1 set too, and no other row has the key flag; layout 1 has two more rows with the pad flag (114, 169).
- M: row 93 is the Space skip hold; row 94, also Space, has no long press.

## Notes

Actions with a long press are the hold-to-confirm ones (reset, retreat, achievements).

## Open questions

None recorded.
