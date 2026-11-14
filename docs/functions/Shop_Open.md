# Shop_Open

- **Address:** `0x1402C35FC`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void Shop_Open(int shop_id)`
- **Callers:** sub_140345FE4
- **Callees:** __alloca_probe, sub_1402F4238, EventVar_Read, sub_1400FF6B8, sub_1402C4880, sub_1401E2CB8, sub_140260688, sub_14033EA08, sub_1402F41D0, sub_14025FE14, sub_1402F3888, sub_14025FC38, sub_14032A5D0, Shop_GetUiRowId, sub_1400D6DAC, sub_1400EDEE0, sub_1400EDD30, sub_1402B1C84, sub_1402BC46C, sub_14032A230, sub_14032A8A0, Resource_GetSlotObject, EventTask_Start, sub_1402C40BC, sub_1402B1D94, sub_1402B1F08, sub_140303B10, sub_14031E300, sub_140329E1C, sub_1402BD740, sub_1402D7954, UI_GetHelpSlotState, sub_140330E34, sub_1402BC3C4, sub_1402B1E74, sub_1400ECE30, sub_1401E2D64, sub_140285A6C, sub_1402B340C, sub_14033E898, sub_14025FA60, sub_1402F3A04, sub_14041FAE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the shop screen for a shop number: it stores the id, resolves the real shop from the event variable when the id is not special, builds the list and the panels and starts the shop task.

## Behavior

- V: the argument is stored in the screen shop word at 0x141811684.
- V: shop ids outside 100 and 101 are not taken literally: the function reads event variable 0x31 (49) after the screen opens and uses that as the effective shop id.
- V: ids 100 and 101 are the two hardcoded Poachers Den shops and skip the event-variable read.
- V: the UI row id for the shop comes from Shop_GetUiRowId, which maps 100, 101 and 0x18F to their own rows (0x18F is a callee-side constant; this body passes only the screen shop word).
- V: the routine allocates the screen buffers, builds the list callbacks and fills the shop, item and help panels.
- V: the shop task is started through EventTask_Start and the screen state is written into the shop object.
- V: the single caller is the town shop event command, so the screen is event-driven.
- I: the event variable holds the town-specific shop number because the town record itself only names the shop command.
- ?: what the extra unlock test at 0x1402C378F..0x1402C37A5 distinguishes between shops 100 and 101; the two texts differ but the condition is not decoded.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [sub_14025FC38](sub_14025FC38.md), [Shop_GetUiRowId](Shop_GetUiRowId.md), [Resource_GetSlotObject](Resource_GetSlotObject.md), [EventTask_Start](EventTask_Start.md), [UI_GetHelpSlotState](UI_GetHelpSlotState.md), [sub_140285A6C](sub_140285A6C.md)
- Reads: [g_HelpIdSlot](../globals/g_HelpIdSlot.md)
- Writes: [g_SelectedShopIndex](../globals/g_SelectedShopIndex.md)

## Notes

Whole function read (2323 bytes).

## Open questions

None recorded.
