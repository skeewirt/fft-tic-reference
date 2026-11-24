# UIListGadget_ClassicInput

- **Address:** `0x14028E290`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char UIListGadget_ClassicInput(int64_t gadget, int64_t input, unsigned int keys, int16_t repeat, int forced)`
- **Callers:** sub_14022F868 (0x14023085A) and other list tasks
- **Callees:** UIListGadget_IsAnimating, ListScroll_HandleStick, sub_1400F6E50, UIListGadget_SetCursor, UIListGadget_RestoreFocus, sub_1400FC29C, sub_1400FC6D8, Input_TestAction, sub_14040D1AC, sub_14040D200

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input of a list gadget for the classic list tasks: stick scroll, row step with repeat and page jumps; returns 1 when the cursor moved.

## Behavior

- V: returns 0 when the gadget has no list component (+24), the component's byte +554 or the gadget's byte +120 is 0, or the gadget is animating.
- V: a stick scroll (ListScroll_HandleStick) returns 1.
- V: the row step is sub_1400F6E50(cursor +96, 0, count - 1, component dword 163, keys, repeat, 0); a change sets the cursor.
- V: with gadget byte +127 set and no row change, action 58 (mask 0x8000) jumps a page up and 59 (mask 0x2000) a page down, only when sub_1400FC29C() is 0 and the count is above 0; the step is min(rows above the first visible row, dword 175 / dword 173) upward and min(rows below the last visible row, dword 175 / dword 173) downward.
- V: a forced index >= 0 that differs from the result also sets the cursor.

## State touched

- Calls: [UIListGadget_IsAnimating](UIListGadget_IsAnimating.md), [ListScroll_HandleStick](ListScroll_HandleStick.md), [UIListGadget_SetCursor](UIListGadget_SetCursor.md), [UIListGadget_RestoreFocus](UIListGadget_RestoreFocus.md), [sub_1400FC29C](sub_1400FC29C.md), [sub_1400FC6D8](sub_1400FC6D8.md), [Input_TestAction](Input_TestAction.md)

## Notes

Actions 58 / 59 are the game's 'menu_left' / 'menu_right' rows bound to the keys '1' / '3' and the Left / Right arrows (LocationsListInputActions).

## Open questions

None recorded.
