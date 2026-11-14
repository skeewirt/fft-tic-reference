# TurnPanel_FillUnitEntry

- **Address:** `0x14010C1FC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool TurnPanel_FillUnitEntry(int64 panel, int index, ... (19 arguments), _BYTE *set /* arg 16 */, _BYTE *countdowns /* arg 17 */, ...)`
- **Callers:** sub_1400E5910 (from TurnPanel_SetUnitPanel with the unit record +0x61 and +0x66), sub_140106C54
- **Callees:** sub_14002620C, StatusList_BuildFromSet, sub_1400FAAB4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills one entry (448 bytes at panel + 448 x index) of a battle turn panel: the unit's numbers, name and its status byte list.

## Behavior

- V (status part): the entry keeps a copy of the set (+38712) and of the 16 countdown bytes (+38717); its status byte list at +0x95C8 (count +0x95C4) is cleared, then the set is listed with StatusList_BuildFromSet and every status whose Status_ListCategory is 1 or 2, except 23, is kept as one byte.
- V: the list is then compared with the one drawn last (+0x24C0 further on, count +0xBA84): a different count or byte marks the entry for redraw.
- I: sub_14010C624 draws the bytes as icons (Icon row 0x16 with the byte), no names.

## State touched

- Calls: [sub_14002620C](sub_14002620C.md), [StatusList_BuildFromSet](StatusList_BuildFromSet.md)

## Referenced by

- Observed behaviours: [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md)

## Notes

Name is ours. Read for its status list only (the other fields are copied from the arguments). The status set is the stack argument at rsp+0x128 (a point after the list loop and before the compare is 0x14010C533).

## Open questions

? the meaning of the other 17 arguments.
