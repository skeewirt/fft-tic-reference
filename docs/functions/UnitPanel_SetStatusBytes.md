# UnitPanel_SetStatusBytes

- **Address:** `0x14010A42C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 UnitPanel_SetStatusBytes(int64 panel, int which, _BYTE *set, __int128 *extra)`
- **Callers:** sub_1400E56A0 (from Battle_TimelineRefresh, Battle_UnitStatusFill, Battle_UnitStatusFillAlt, sub_1402DF374, all with the unit record +0x61)
- **Callees:** StatusList_BuildFromSet, sub_1400FAAB4, __security_check_cookie

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills a battle unit panel's status byte list (the icons on the panel) from a five-byte status set.

## Behavior

- V: which 0, 2, 3 use the list at panel +0x101A4 (count +0x101CC, a 16-byte copy of extra at +0x101D8); 1, 4, 5 and any other value the list at +0x10160 (count +0x10188, extra at +0x10194). Only 0x10160, 0x10194 and 0x101D8 are operands; the other offsets are built from them (lea rdi+28h, rax-0Ch, rax-34h).
- V: clears the 40-byte list and its count, lists the set with StatusList_BuildFromSet and keeps each status whose Status_ListCategory is 1 or 2, one byte each.

## State touched

- Calls: [StatusList_BuildFromSet](StatusList_BuildFromSet.md)

## Referenced by

- Observed behaviours: [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md)

## Notes

Name is ours. I: sub_14010A550 draws the list as icons (Icon row 0x16 with the byte), no names.

## Open questions

? which panel each which value is.
