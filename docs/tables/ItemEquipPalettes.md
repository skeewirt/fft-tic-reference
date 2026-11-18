# ItemEquipPalettes

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x140785CF0`
- **Rows:** 145 records of 2 bytes (ids 0..0x8F)
- **Keyed by:** item id (kinds 0 and 1)
- **Read by:** [Item_GetEquipPalette](../functions/Item_GetEquipPalette.md)
- **Row layout:** [ItemEquipPaletteRow](../structs/ItemEquipPaletteRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Palette selectors of weapons and shields.

## Behavior

- I: the extent of 145 rows is read from the bounds; two further rows for kinds 4 and 5 are at 0x140672B54.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
