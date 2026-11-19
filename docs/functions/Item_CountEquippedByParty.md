# Item_CountEquippedByParty

- **Address:** `0x1402874D8`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `__int64 __fastcall Item_CountEquippedByParty(__int16 id_word)`
- **Callers:** `ShopEntry_InitFromList`, `sub_140332C8C`, `Item_CountTotal`
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counts how many party units hold a given item id in their five equipment words.

## Behavior

- V: It masks the argument with 0x3FF (`v2 = a1 & 0x3FF` in the export) and walks `g_PartyCount` units and five
  words per unit.
- V: The comparison is a raw word equality (`*v5 == v2`), not a masked compare. A word with bit 15 set does not
  equal the masked id, so a session-pending item is not counted as equipped.
- V: It returns 0 when the argument masks to zero.
- I: The function is used by the shop row count; during a session a pending purchase therefore reads as "not
  equipped" until the commit strips the bit.

## State touched

- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Called by: [Inventory_AddWithOverflow](Inventory_AddWithOverflow.md), [Item_CountTotal](Item_CountTotal.md), [PoachList_Build](PoachList_Build.md), [ShopEntry_InitFromList](ShopEntry_InitFromList.md), [sub_140332C8C](sub_140332C8C.md), [sub_1403358FC](sub_1403358FC.md), [sub_14036A95C](sub_14036A95C.md)

## Notes

V: compares each raw party word with the masked argument (0x1402874D8); a bit-15 word is not counted as equipped.

## Open questions

- ?: whether the shop UI wants a pending word counted as equipped; the current code does not.
