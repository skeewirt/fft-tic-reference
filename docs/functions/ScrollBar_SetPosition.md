# ScrollBar_SetPosition

- **Address:** `0x14040B994`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ScrollBar_SetPosition(GUIComponentScrollBar *bar, int pos, char snap, char clamp)`
- **Callers:** not recorded
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Game setter for the native scroll bar component (vtable 0x140722238, kind 8 at node+536).

## Behavior

- V: position at +648, lower bound +652, upper bound +656, viewport size +660; smooth floats +672/+676 ease the knob when snap is 0.
- V: the Knob and Base parts carry a visible flag at +144 (used to hide the bar for short lists).
- V: raw writes to +656/+660 are the wrong layout for this class; always use this setter. The node's scale (instance +0x18) controls its drawn length.

## State touched

- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUIComponentList_SetScrollX](GUIComponentList_SetScrollX.md), [GUIComponentList_SetScrollY](GUIComponentList_SetScrollY.md), [UIGadgetFFTOVScrollText_HandleScrollInput](UIGadgetFFTOVScrollText_HandleScrollInput.md), [UIGadgetFFTOVScrollText_Refit](UIGadgetFFTOVScrollText_Refit.md)

## Open questions

None recorded.
