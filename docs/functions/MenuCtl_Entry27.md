# MenuCtl_Entry27

- **Address:** `0x140371F68`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MenuCtl_Entry27(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 27; pushed by sub_140371CAC)
- **Callees:** TimImage_Parse, ImageDissolve_Step, PagedText_Step, sub_14037270C, sub_140372C10, sub_140371984

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the page of a list entry that has a picture dissolve and a book progress word (table index 27).

## Behavior

- V: record dword 3 is the state: 1 waits for the window; 2 loads a picture (TimImage_Parse), places its window (position depends on the language) and goes to 3; 3 steps ImageDissolve_Step with a frame counter in dword 4 and goes to 0; 0 runs the page.
- V: the page runs the paged text widget at 0x140D49580; at its end it plays cue 2, restores the windows below and calls sub_140371984 (the list builder of kind 26).
- V: a button (action 0x1E, mask 16) sets record dword 2 from the byte table at 0x140692EC0 + 48 + entry, minus 1, and starts the close; after the close the step calls sub_14037270C when dword 2 is below 5 and the book progress word (0x1411A7536 + 56 x n) is nonzero, otherwise sub_140372C10.

## State touched

- Calls: [TimImage_Parse](TimImage_Parse.md), [ImageDissolve_Step](ImageDissolve_Step.md), [PagedText_Step](PagedText_Step.md)

## Open questions

? what the book progress word counts.
