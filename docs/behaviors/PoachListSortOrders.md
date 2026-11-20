# PoachListSortOrders

- **Kind:** observed behaviour
- **Scope:** engine (poacher screens)
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [sub_1401CAB50](../functions/sub_1401CAB50.md), [sub_1401CAFE0](../functions/sub_1401CAFE0.md), [sub_1401CAC8C](../functions/sub_1401CAC8C.md), [sub_1402A6710](../functions/sub_1402A6710.md), [PoachList_Build](../functions/PoachList_Build.md), [PoachRow_SetMonsterIcon](../functions/PoachRow_SetMonsterIcon.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The poacher lists are sorted by one of two insertion sorts: by the PoachItem sort_name string, or by the sort_order byte; the list labels use a notice form by two other columns.

## Behavior

- V: sub_1401CAB50 (24-byte entries) and sub_1401CAFE0 (48-byte PoachListEntry) compare the sort_name strings of the PoachItem rows (UI table 0xEC) of the entries; ties fall back to the id.
- V: sub_1401CAC8C compares the sort_order byte (+0x35); the entry with the larger byte comes first (the code reads this way), ties fall back to the smaller id.
- V: sub_1402A6710 shows text line 2098 for a row, or 2099 when the item record's shop progress byte is 0x14 or more or the PoachItem notice_mark byte (+0x36) is set.
- V: the monster icon plays 'Rare' by PoachItem rare (+0x34) and its Icon part frame is PoachItem icon (+0x30) (PoachRow_SetMonsterIcon).

## Open questions

? which screen uses which sort; why three rows have notice_mark set.
