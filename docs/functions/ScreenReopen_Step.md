# ScreenReopen_Step

- **Address:** `0x1403797F8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t ScreenReopen_Step(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 49; pushed by sub_1403793DC)
- **Callees:** EventTask_Start, sub_140371CAC, sub_140374B50, EventViewer_OpenEntry, sub_140318860, sub_140319218, sub_1403196DC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a short controller (table index 49) that waits a few frames, then re-opens the screen whose kind is in its first dword.

## Behavior

- V: it clears the fade mode; record dword 4 counts down, then when dword 5 is 0 it draws a fade rectangle once (sub_14025FC38) and sets dword 5.
- V: when the count has finished it pops itself and, by the kind in dword 0, starts event task 14 with a message (text id 47176, 47325 for kinds 43 to 45) and calls the builder of that screen: kind 27 sub_140371CAC, 28 sub_140374B50, 29 EventViewer_OpenEntry, 43 sub_140318860, 44 sub_140319218, 45 sub_1403196DC.

## State touched

- Calls: [EventTask_Start](EventTask_Start.md), [EventViewer_OpenEntry](EventViewer_OpenEntry.md)

## Notes

The helper sub_1403793DC pushes this kind with the kind to re-open (V from the callers' arguments 27, 28, 29, 43, 44, 45).

## Open questions

None recorded.
