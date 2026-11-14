# EquipSessionFlagLifecycle

- **Kind:** observed behaviour
- **Scope:** the five party equipment words, the override array and the candidate array during an Outfitter or shop session
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [EquipSetBlock](../structs/EquipSetBlock.md), [EquipPanelBlock](../structs/EquipPanelBlock.md), [dword_143D1AC68](../globals/dword_143D1AC68.md), [qword_141801100](../globals/qword_141801100.md), [sub_1402D7280](../functions/sub_1402D7280.md), [sub_1402D65D4](../functions/sub_1402D65D4.md), [sub_1402D5B6C](../functions/sub_1402D5B6C.md), [sub_140287D9C](../functions/sub_140287D9C.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Bit 15 marks a slot changed in the current session and priced into dword_143D1AC68; bit 14 is a list-entry 'cannot equip' mark. The commit strips bit 15 (and any bit 14) from every party word before the save is written; the cancel restores the override words.

## Behavior

- V: the bit-15 writers are sub_140287D9C (four candidate words, 0x140288544), sub_1402D7280 (the unit word, 0x1402D733A) and the apply loops of sub_1402D5CC4 and sub_1402D6914, which copy a flagged candidate into the unit word.
- V: the bit-15 readers treat the word as signed or compare it against 0x8000: sub_1402D58EC (0x1402D5A6C, 0x1402D5ACD), sub_1402D5FE4 (0x1402D6129 js), sub_1402D6464 (0x1402D6490), sub_1402D65D4 (0x1402D6621), sub_1402D5CC4 (0x1402D5EFA jns), sub_1402D6FB8 (0x1402D704C shr), sub_1402D7584 (0x1402D75E1 jge).
- V: the bit-14 producers are Inventory_BuildEquipList (bts 0xE at 0x140288CAF) and Shop_BuildItemList (or 0x4000 at 0x140288FBD and 0x140289061); both write list entries, not party or candidate words.
- V: sub_1402D7280 refuses a bit-14 candidate (bt 0xE at 0x1402D72A0), but the two apply loops test only bit 15 (0xFFFF8000), so a bit-14 candidate would be stored if one ever reached them.
- V: after commit, sub_1402D65D4 masks every word at or above 0x4000 with 0x3FF and returns the override item to the inventory; bits 10..13 are not stripped but no writer sets them.

## Open questions

? whether a session teardown other than the commit/cancel messages can leave bit 15 set in a party word.
