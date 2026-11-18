# PartyHandWord

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One equipment slot of a party unit: the item id in bits 0..9 and bit 15 as the Outfitter-session pending flag. Five of them sit at g_PartyUnits +0x54..+0x5C, one per slot.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="item_id"></a>bits 0..9 | item_id | `uint16` | V | Item id of the slot. Most consumers mask the word with 0x3FF; some compare the raw word (Item_CountEquippedByParty at 0x1402874D8, ShopEntry_Fill at 0x14036B4A3), so a flagged word is not seen as the same item there. |
| <a id="session_pending"></a>bit 15 | session_pending | `bit` | V | Set on a slot changed in the current Outfitter/shop session: sub_1402D7280 sets it when it stores id \| 0x8000 and adds the price to dword_143D1AC68 (0x1402D733A), and the apply loops copy a bit-15 candidate into the word. The commit handler sub_1402D65D4 strips it before the save is written. It is not the item-present flag: a committed item keeps the id with this bit clear. |
| <a id="cannot_equip"></a>bit 14 | cannot_equip | `bit` | V | Produced on list entries by Inventory_BuildEquipList (bts 0xE at 0x140288CAF) and Shop_BuildItemList (or 0x4000 at 0x140288FBD/0x140289061). sub_1402D7280 refuses a candidate that carries it (bt 0xE at 0x1402D72A0); sub_1402D5B6C and sub_1402D65D4 test it as part of a >= 0x4000 comparison. No stock writer sets it on a party word. |
| <a id="unused"></a>bits 10..13 | unused | `bits` | I | No writer sets them; sub_1402D65D4's 0x3FF strip would clear them on a word at or above 0x4000, but a word in 0x0400..0x3FFF is not stripped. I: padding between the 10-bit id and the two flag bits. |

## Behavior

- V: five words per party unit, at +0x54, +0x56, +0x58, +0x5A and +0x5C of the party record; 0 is empty, not 0xFF.
- V: a word at or above 0x8000 is treated as session-pending and its price is already in dword_143D1AC68; a word below 0x8000 is a plain 16-bit id and may still carry bit 14.
- V: the bit and the id share one 16-bit word, so the store cannot hold a 16-bit id without moving the session flag out of the word.

## Referenced by

- Observed behaviours: [OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag](../behaviors/OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag.md)

## Notes

V: layout, writers and readers come from the sheets sub_1402D6FB8, sub_1402D7280, sub_1402D6464, sub_1402D65D4 and sub_1402D5B6C. The earlier 'present' reading of bit 15 was wrong: the commit path strips it from an item that stays equipped.

## Open questions

? whether any session teardown other than the commit/cancel messages can leave bit 15 set on a party word.
