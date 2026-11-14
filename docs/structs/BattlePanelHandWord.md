# BattlePanelHandWord

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One hand word as the flag-aware panels read it: the item id in bits 0..8 and a two-bit value in bits 14..15. The carrier is a 64-byte copy of a party or battle record's +0x30..+0x6F, at 0x141876E90 (field) or 0x141D3B880 (battle), with the five words at +0x24; it is not a field at unit+0x1EC.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="item_id"></a>bits 0..8 | item_id | `uint16` | V | Item id of the slot, masked with 0x1FF by the panel loops (0x14032F160, 0x140399E0C). 0xFF means empty and a value of 0x105 or more ends the walk. |
| <a id="slot_flags"></a>bits 14..15 | slot_flags | `bits` | V | Two-bit value taken with shift 12 and mask 0xC (shr 0xC at 0x14032F178/0x140399E24, and 0xC at 0x14032F17D/0x140399E29) and stored in dword_14184B228 / dword_140D40978. On the session carriers only bit 15 is ever set; bit 14 exists on the shop/menu list entries. |
| <a id="unused"></a>bits 9..13 | unused | `bits` | I | No reader uses them; I: padding between the 9-bit panel id and the two flags. |

## Behavior

- V: the panels walk five words at carrier +0x24 (0x141876EB4 / 0x141D3B8A4), not at unit+0x1EC. The carrier is a copy: JobScreen_RefreshAfterChange copies record +0x30..+0x6F to 0x141876E90 (0x1402BD15D), PartyUnit_ReloadEquipment copies the live words to +0x24 (0x1402BDB42), and sub_14033E394 copies a battle record to 0x141D3B880 (0x14033E412).
- V: two panel variants extract the top two bits: sub_14032EDB8 (task 9 over g_EquipCandidates, task 10 over 0x141876E90) and sub_140399A64 (over 0x141D3B880).
- V: the id field is nine bits here, narrower than the party hand word, so the panel caps the id at 511 even before the flags are considered.

## Notes

V: the byte census of the equip session flags. The earlier placement at unit+0x1EC was wrong: the bytes show a record copy at 0x141876E90 with the hands at +0x24.

## Open questions

? what the two-bit value selects in the text draw, and whether a stock session ever leaves bit 14 set in the copied hand word.
