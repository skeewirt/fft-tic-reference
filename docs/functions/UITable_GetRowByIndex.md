# UITable_GetRowByIndex

- **Address:** `0x1403DBDF4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char *UITable_GetRowByIndex(int tableId, unsigned int key, unsigned int index)`
- **Callers:** sub_1403DBB00, sub_1402EE994, sub_1402A876C, UIAddonFFTOSaveLoad_vfunc_12, sub_14013CA80 and about ten more
- **Callees:** NxdRegistry_Find, sub_1403D3A10, sub_1403D3A34, sub_1403D3C98, sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the index-th sub-row of a key in a multi-row UI table, or null.

## Behavior

- V: same registry / type / state checks as UITable_GetRowCount; additionally index must be < sub_1403D3A34(table, key) (the count).
- V: the row comes from sub_1403D3C98(table, key, index); a null result returns null; a row whose first qword is negative returns the constant block unk_1406F5ED0 (a default / deleted-row placeholder); otherwise sub_1403D2FD8(row) converts the row to its data pointer.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md)

## Notes

The name is ours (IDB: sub_1403DBDF4).

## Open questions

? what unk_1406F5ED0 contains.
