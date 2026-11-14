# UI_GetHelpSlotState

- **Address:** `0x1402BB604`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int UI_GetHelpSlotState(void)`
- **Callers:** sub_1402BBBCC, Shop_Open
- **Callees:** sub_140303EC8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides whether the shared help-description slot is visible and returns a masked UI state word for the caller.

## Behavior

- V: it calls sub_140303EC8 for the base state and keeps the result in r9d.
- V: any of the three mode bytes at 0x140D408F2, 0x140D40903 and 0x142FEC532 being non-zero returns 0.
- V: when the object loaded through the global pointer at 0x14078D5D8 has a non-zero qword at +0x890, the mode word at 0x141811424 is compared with 4: equal applies the mask, anything else returns the base state.
- V: when that field is zero, a non-zero dword at 0x1418736B4 applies the mask, and with 0x1418736B4 zero a non-zero dword at 0x1418736B0 applies it while a zero one returns the base state.
- V: the masked value is the base state with 0xF0FF applied.
- V: the two callers are the shop open path and the sell-list builder.
- I: the help slot is the shared item-description id, so this function is the gate that hides the help panel when the slot is empty.
- ?: what each of the three mode bytes suppresses; only the zero test is read.

## State touched

- Reads: [g_HelpIdSlot](../globals/g_HelpIdSlot.md)

## Referenced by

- Called by: [Shop_Open](Shop_Open.md)

## Notes

Whole function read (101 bytes). The help slot is the S5 carrier.

## Open questions

None recorded.
