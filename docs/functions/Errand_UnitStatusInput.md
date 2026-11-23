# Errand_UnitStatusInput

- **Address:** `0x1403787A4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t Errand_UnitStatusInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 40; pushed by sub_1403781F4)
- **Callees:** StatusGlossary_Open, sub_1403783F0, sub_140377E9C, EventTask_Start

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of a unit's status page for an errand in progress (table index 40): two direction presses page through the units of the errand.

## Behavior

- V: Input_RepeatDirection() drives the paging: the first call moves record dword 5 to the next unit (wrapping) and sets the arrow style 105, the second call moves to the previous unit and sets 103; each redraws the page with sub_1403783F0 for the unit id stored in the errand's active entry (byte 5 of the 9-byte entry g_ErrandActive + 9 x errand index, dword 4); a single-unit errand does nothing.
- V: when neither of the actions 0x2D and 0x2E is down the two arrow windows are reset to styles 102 and 104.
- V: the help action calls StatusGlossary_Open; confirm or cancel starts the close, and when the close ends it pops, starts event task 14, prints text id 47177 with the errand's text number and calls sub_140377E9C to rebuild the list.

## State touched

- Calls: [StatusGlossary_Open](StatusGlossary_Open.md), [EventTask_Start](EventTask_Start.md)

## Open questions

None recorded.
