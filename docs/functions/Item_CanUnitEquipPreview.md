# Item_CanUnitEquipPreview

- **Address:** `0x140396F1C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Item_CanUnitEquipPreview(short job, unsigned short id)`
- **Callers:** `sub_140396D08`, `sub_140396FEC`
- **Callees:** `sub_1402890C0` (Item_MenuCategory), `Item_GetRecord`, `sub_14039EA84`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The preview-record twin of the equip check: it decides whether the job shown in an equip preview could equip the candidate
item.

## Behavior

- V: The item id arrives in the second argument here, unlike the live check where it is first; the job is the first
  argument.
- V: It masks the id to ten bits, and a zero id returns 1 (true), the same value the live check returns for zero.
- V: The menu-category helper is asked for the id; menu category 5 returns -1 (false).
- V: It carries the same five special-cased ids as the live check, 262, 288, 293, 301 and 310, reached as the same chain
  of subtractions. For those ids it reads the job word at +0x24 of the preview unit record and returns 1 only for the two
  jobs 161 and 164; every other job gets -1.
- V: The generic path looks up the preview unit record in qword_141D3B7A0 by the unit argument, builds the equip-flag
  stream at record +0x73, reads the item record's category byte at +5 and reads one bit through `sub_14039EA84`; the bit
  set gives 1 and the bit clear gives -1.
- V: Two direct callers reach it; it calls the menu-category, record and bit-reader helpers rather than the live job row.
- I: Sharing the special-case table with the live check is what keeps the preview and the real equip decision from
  disagreeing.

## State touched

- Calls: [sub_1402890C0](sub_1402890C0.md), [Item_GetRecord](Item_GetRecord.md)
- Reads: [ItemRecord.equip_category](../structs/ItemRecord.md#equip_category)

## Referenced by

- Called by: [sub_140396D08](sub_140396D08.md), [sub_140396FEC](sub_140396FEC.md)

## Notes

- I: The special ids lie past the stock items (0..260); the same test is in Item_CanUnitEquip.

## Open questions

None recorded.
