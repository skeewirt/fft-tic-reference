# Item_IsOwned

- **Address:** `0x140100F78`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `bool Item_IsOwned(uint16_t id)`
- **Callers:** sub_1401007E0 (one direct site)
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers whether the party owns an item, either in the inventory or equipped on one of the 54 units.

## Behavior

- V: the first argument register is not read; the id is the 16-bit value in dx, sign-extended, and anything above 0x104 is rejected.
- V: it looks up the Item-en row of the id (NXD table 45, 0x2D); when the row exists and its byte +44 (0x2C) is 0 the answer is false.
- V: a missing table or row skips that veto and continues with the inventory check.
- V: otherwise it reads byte_1411A7C00[id] and returns true when the byte is non-zero.
- V: if the inventory is empty it walks the 54 unit records (g_UnitSaveData, 600 bytes apart) and their seven equipment words at +14 (0xE), comparing each word with the id; a record whose byte +1 is 0xFF is skipped.
- V: the seven words are compared whether or not a slot is empty, with no per-slot marker byte.
- V: it calls three helpers and has a single direct caller.
- I: the sign-extension means ids above 32767 become negative before the 64-bit index, which is only safe while the 0x104 bound rejects them first.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)
- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Observed behaviours: [ItemRowGrammarBytesAndGates](../behaviors/ItemRowGrammarBytesAndGates.md)

## Notes

V: the Item column at +0x2C is named unknown2c in the table row structure; the only caller is the scenario condition of type 81, which answers 'item owned' only for items whose byte is non-zero.

The name is ours (IDB: sub_140100F78). The veto at row byte +44 is the reading the bytes support: the byte at +0x2C is tested after the row lookup and a zero returns false; every stock Item-en row has 0 in the column at +0x2C, so the meaning of the veto is still open.

## Open questions

What byte +44 of the Item-en row in memory is (the veto); why a stock row would veto every id.
