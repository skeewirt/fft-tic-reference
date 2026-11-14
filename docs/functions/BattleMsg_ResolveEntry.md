# BattleMsg_ResolveEntry

- **Address:** `0x1401EBBF4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char *BattleMsg_ResolveEntry(BattleMsgObject *obj, void *a2, unsigned int slot)`
- **Callers:** sub_1401EC01C (walks up to 40 entries and resolves every entry whose kind is above 1)
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, ItemTable_GetRowById, PoachTable_GetRowById, UIText_Get, Str_Format, BattleMsg_IdFromDescriptor, CMesId_GetText, sub_1400FC85C, sub_1401E8B7C, sub_14002620C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Renders one battle message record entry: reads its kind and id, resolves the text for that kind and returns the entry's text buffer.

## Behavior

- V: a slot above 0x27 returns null; entry = obj + 8 + 0x20C * slot; kind = dword at entry+0.
- V: kind 1 formats the dword at entry+4 as '%d' through Str_Format.
- V: kind 2 names a unit record from g_UnitSaveData (600-byte stride, index below 0x36) using the name at +0xDC and the id at +0x230.
- V: kind 3 names a battle unit from g_BattleUnitTable (512-byte stride, index at most 0x14, used byte +1 not 0xFF) using +0x14C and +0x1FC.
- V: kind 4 masks the id to 0x7FF and calls ItemTable_GetRowById; kind 9 calls the same item-table accessor with the id unmasked (the bytes skip the mask on the kind-9 path).
- V: kind 5 uses NXD table 41 (0x29), cached in qword_143CDA2E0; kind 6 uses NXD table 39 (0x27, Ability-en), cached in qword_143CDA2D0.
- V: kind 7 builds a class 0 subtype 2 descriptor with kind 23 and the masked id, resolves it through BattleMsg_IdFromDescriptor and CMesId_GetText (base 23000).
- V: kind 8 builds the same descriptor with kind 10, resolves 10000 + id through BattleMsg_IdFromDescriptor and CMesId_GetText, and stores id + 10000 at entry+8.
- V: kind 10 also builds a kind-10 descriptor, but classifies it through sub_1400FC85C and maps the resulting class/kind to a table-172 base (2000, 3000, 6000, 7000, 8000, 9000, 10000, 11000, 14000, 16000, 17000, 18000, 22000 or 23000) plus the masked id.
- V: kind 11 uses PoachTable_GetRowById.
- V: every resolved string is copied into the 512-byte text at entry+0xC with a 511 cap.
- V: the 0x7FF mask is 11 bits and is not the banner truncation.
- I: the caller walks all 40 entries and resolves the ones with kind above 1, so the banner sees the text the dispatcher wrote.
- ?: what a2 is and what the entry+8 value is read by after kind 8 writes it.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [ItemTable_GetRowById](ItemTable_GetRowById.md), [PoachTable_GetRowById](PoachTable_GetRowById.md), [UIText_Get](UIText_Get.md), [Str_Format](Str_Format.md), [BattleMsg_IdFromDescriptor](BattleMsg_IdFromDescriptor.md), [CMesId_GetText](CMesId_GetText.md), [sub_1400FC85C](sub_1400FC85C.md), [sub_14002620C](sub_14002620C.md)

## Referenced by

- Called by: [sub_1401EC01C](sub_1401EC01C.md)
- Observed behaviours: [AbilityTextKeysPast2047](../behaviors/AbilityTextKeysPast2047.md)

## Notes

The name is ours (IDB: sub_1401EBBF4). The function is 0x425 bytes. Offsets are entry-relative; the record starts at object + 8, so entry+4 is object + 0xC. Read for kinds 4, 9, 10 and 11 during the item text research; the other kinds are from the earlier battle-message research. The bytes put the id + 10000 store on the kind-8 path, not kind 6.

- V: 0x1401EBF42 is a label inside this function (a branch target, not an entry; an earlier sheet named it `sub_1401EBF42`). What that path does:
  - V: the descriptor fields (class, subtype, kind, word) are handed to BattleMsg_IdFromDescriptor, which builds the message id.
  - V: the id is then looked up with CMesId_GetText, the table-172 accessor, and its result is what the function returns.
  - V: the only data the body touches is a small read-only table; there is no write to the message object.
  - I: this is the read-side twin of BattleMsg_Dispatch: a caller that holds a descriptor instead of a stored entry can ask for the same text.
  - ?: which callers pass a descriptor; the dispatch path builds entries, and the descriptor holders were not enumerated.

## Open questions

What the entry+8 value is read by; what a2 is; the full kind list and the producer of each; which kinds above 23 exist.
