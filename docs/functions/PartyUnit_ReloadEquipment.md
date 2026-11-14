# PartyUnit_ReloadEquipment

- **Address:** `0x1402BD924`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `_OWORD *PartyUnit_ReloadEquipment(void)`
- **Callers:** `sub_1402BD740`, `sub_1402D58EC`, `sub_1402D5CC4`, `sub_1402D5FE4`, `sub_1402D6914`, `sub_140366A4C`
- **Callees:** `Item_GetRecord`, `PartyUnit_FillFromWork`, `UnitWork_BuildFromSaveIndex`, `Unit_ReloadFromJobRow`, `sub_140284998`, `sub_140287398`, `sub_140289894`, `__security_check_cookie`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the selected unit's work record from its save row and refreshes the three screen records: the 0x1407B27xx
party record, the 0x141876E90 panel block and the per-unit stat block. The live equipment words are copied into
the panel block raw.

## Behavior

- V: It builds a work record from the unit's save index (`UnitWork_BuildFromSaveIndex`) and fills seven equipment
  words at work +0x1BA..+0x1C6 with 0xFF before copying items.
- V: It masks the five live words with 0x3FF (0x1402BD9B9..0x1402BDA32) and sorts the two hand items by the
  record's equip category (19 goes to the shield slots); it then replaces 0, 0xFF and values at or above 0x105
  with 0xFF.
- V: It calls `PartyUnit_FillFromWork` to build the 64-byte record B (0x1402BDA97), then copies record B's
  +0x30..+0x3F to `xmmword_141876E90` (0x1402BDB20), and the live five words to a 32-byte stack value which is
  stored at `ymmword_141876EB0` (0x1402BDB42), i.e. the hand words land at block +0x24 (0x141876EB4).
- V: The live-word copy at 0x1402BDABB/0x1402BDAB7 is raw: the words are read as a qword and a word and are
  not masked before they are stored in the block, so a bit-15 word reaches the panel block.
- V: It computes the two-handed word with `sub_140284998` (0x1402BDACB) and stores it as the low word of
  `xmmword_141876EA0` (0x1402BDB37); the rest of that 16-byte value is not written in this function.
- V: It calls `sub_140287398(&xmmword_141876E90, unit+0x54)` (0x1402BDB57) to add the five items' stats to the
  block; that callee masks each id with 0x3FF and writes only the stat words.
- V: It sets eight refresh flags (`dword_14078CFAC`, `dword_141848B24`, ...) and ends through the stack cookie.
- I: The earlier "seven equipment words" description of the work record is right, but the panel block is not
  the work record: it is a 64-byte copy of the party record slice, and its hand words are the raw live words.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md), [PartyUnit_FillFromWork](PartyUnit_FillFromWork.md), [sub_140287398](sub_140287398.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md), [g_UnitSaveData](../globals/g_UnitSaveData.md)
- Writes: [xmmword_141876E90](../globals/xmmword_141876E90.md)

## Referenced by

- Appears in flows: [EquipPanelBlockFill](../flows/EquipPanelBlockFill.md), [EquipSessionFlagFlow](../flows/EquipSessionFlagFlow.md)
- Called by: [sub_1402D58EC](sub_1402D58EC.md), [sub_1402D5CC4](sub_1402D5CC4.md), [sub_1402D5FE4](sub_1402D5FE4.md), [sub_1402D6914](sub_1402D6914.md)

## Notes

V: the panel block writer. The five live words are copied raw (movsd 0x1402BDABB, word 0x1402BDAB7) and stored at block +0x24 (movaps 0x1402BDB42); the ids used for the work-list are masked with 0x3FF (0x1402BD9B9-0x1402BDA32).

## Open questions

- ?: the source and meaning of the uninitialised bytes in 0x141876EA0.
- ?: whether the panel expects the block's +0x10 word to be the two-handed value or the record's +0x40 word;
  the two writers disagree.
