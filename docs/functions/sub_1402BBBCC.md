# sub_1402BBBCC

- **Address:** `0x1402BBBCC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char __fastcall sub_1402BBBCC(__int64 a1, __int64 a2, __int64 a3, __int64 a4)`
- **Callers:** not in the exported set; the equip screen's confirm handler
- **Callees:** `PartyUnit_WriteBackToSave`, `sub_1402C17F4`, `sub_14032A230`, `sub_1400ECFF0`, `sub_1400ECF28`, `sub_1400ECF8C`, `sub_14011B438`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The equip screen's confirm/refresh path. On the confirm message it toggles the unit's locked byte, saves the
unit, then copies record +0x30..+0x6F into the panel block and renders.

## Behavior

- V: On message 1008 it reads and toggles the unit's +0x174 byte and calls `PartyUnit_WriteBackToSave` (0x1402BBEE7).
- V: It then copies the record's first 0x30 bytes to the 0x1407B27xx fields, record +0x30..+0x6F to
  `xmmword_141876E90` (0x1402BBF68..0x1402BBF90), and record +0x70 onward to the 0x141876C80 region.
- V: The block copy is raw; the hand words at record +0x54..+0x5C land at block +0x24..+0x2C and reach the
  renderers and the panel task with their flags.
- V: It calls `sub_1402C17F4`/`sub_1402C19EC` on the block to render the equip screen.
- I: Because the save write happens before the block copy, a flagged word would reach both the save and the
  panel; the only guard is the earlier commit strip.
- V: the same copy into the preview record at 0x141876C10 from the selected party unit (g_PartyUnits[g_SelectedUnitIndex] + 112).

## State touched

- Calls: [PartyUnit_WriteBackToSave](PartyUnit_WriteBackToSave.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)
- Writes: [g_UnitSaveData](../globals/g_UnitSaveData.md), [xmmword_141876E90](../globals/xmmword_141876E90.md)

## Referenced by

- Appears in flows: [JobScreenFrame](../flows/JobScreenFrame.md)

## Notes

V: on the confirm message it calls PartyUnit_WriteBackToSave (0x1402BBEE7) before copying record +0x30..+0x6F to the panel block; a flagged word would reach both the save and the block.

## Open questions

- ?: the exact message ids around 1008 and whether the save write can be interrupted before the strip.
