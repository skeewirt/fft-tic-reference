# PoachItem

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** NXD file
- **NXD table id:** 236
- **Keyed by:** poach type id
- **Read by:** [PoachTable_GetRowById](../functions/PoachTable_GetRowById.md), [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md), [UIText_ResolveCategoryRow](../functions/UIText_ResolveCategoryRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The poach rows (the PoachItem-en table), read through PoachTable_GetRowById.

## Behavior

- V: UIText_ResolveCategoryRow sends the category 'PoachItem' to table 0xEC (236).

## Notes

NXD tables are loaded through the shared registry (NxdRegistry_Find by table id) and read with NxdTable_GetRowById or a key lookup; the file format is described by the NXD format records.

## Open questions

None recorded.
