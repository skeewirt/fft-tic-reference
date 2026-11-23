# Errand_UnitListInput

- **Address:** `0x14037808C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t Errand_UnitListInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 39; pushed by sub_140377E9C)
- **Callees:** sub_1403781F4, MenuCtl_ListCursorStep

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of a list of entries (table index 39): confirm opens the page of the entry (kind 40).

## Behavior

- V: cancel clears 0x140D49678, lowers the window counters and pops; confirm stores the row in 0x140D49678, lowers the counters and starts the close.
- V: after the close it pops and calls sub_1403781F4 with record dword 4 and the row, which pushes kind 40.
- V: otherwise the row cursor moves (MenuCtl_ListCursorStep, offset by dword 3).
- I: the errand name rests on the kind it opens (40 reads g_ErrandActive).

## State touched

- Calls: [MenuCtl_ListCursorStep](MenuCtl_ListCursorStep.md)

## Open questions

None recorded.
