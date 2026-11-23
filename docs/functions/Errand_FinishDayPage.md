# Errand_FinishDayPage

- **Address:** `0x140379180`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char Errand_FinishDayPage(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 42)
- **Callees:** PagedText_Step, PagedText_Init, sub_1402CD304, sub_140378C74

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the page of an entry of list 41 (table index 42): shows the day text of the entry, then returns to the list.

## Behavior

- V: record dword 3 is the state (1 waits, 2 steps, 0 shows): at state 0 with the counter in dword 4 at 20 or more and the loading flag set it reads the entry's finish day from g_ErrandFinishDay, builds a text window with text id 47183 + the day and starts the widget (PagedText_Init).
- V: at the end it plays cue 2, pops, clears mask 0x10 of the windows below and calls sub_140378C74 to rebuild list 41.
- V: with language field 0 it only waits for confirm or cancel.

## State touched

- Calls: [PagedText_Step](PagedText_Step.md), [PagedText_Init](PagedText_Init.md)

## Open questions

None recorded.
