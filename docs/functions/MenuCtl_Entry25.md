# MenuCtl_Entry25

- **Address:** `0x14037472C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MenuCtl_Entry25(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 25; pushed by sub_140374484)
- **Callees:** TimImage_Parse, PagedText_Step, sub_1403741C4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the detail page of a list entry with a picture (table index 25): sets the picture up, runs the paged text, then returns to the list.

## Behavior

- V: record dword 3 is the state: 1 waits for the window (mask 0x100 clear) and goes to 2; 2 waits for the counter 0x141856AB4 to be 0, loads the picture (TimImage_Parse, two texture uploads) into a window at position (-116, -34) and goes to 3; 3 waits for the window and goes to 0; 0 runs the paged text widget at 0x140D49580 and, when it finishes, unmarks the windows and calls sub_1403741C4, which rebuilds the list.
- V: when the language field is 0 a confirm or cancel ends the page directly.

## State touched

- Calls: [TimImage_Parse](TimImage_Parse.md), [PagedText_Step](PagedText_Step.md)

## Open questions

None recorded.
