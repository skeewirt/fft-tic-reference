# BgmMode_OnTabButton

- **Address:** `0x1401C8250`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BgmMode_OnTabButton(void *screen, int button)`
- **Callers:** UIAddonFFTOBGMMode_vfunc_2
- **Callees:** sub_1400F4BCC, UIListGadget_SetCursor, UIListGadget_SetCount, UIListGadget_Show

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Switches the music player's list when a tab button is pressed.

## Behavior

- V: sets the current list index (screen +824) from the pressed tab button (button id - 100) and resizes the list gadget to that list.

## State touched

- Calls: [sub_1400F4BCC](sub_1400F4BCC.md), [UIListGadget_SetCursor](UIListGadget_SetCursor.md), [UIListGadget_SetCount](UIListGadget_SetCount.md), [UIListGadget_Show](UIListGadget_Show.md)

## Notes

Name is ours.

## Open questions

None recorded.
