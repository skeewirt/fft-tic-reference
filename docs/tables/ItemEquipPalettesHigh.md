# ItemEquipPalettesHigh

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x140672B54`
- **Rows:** 2-byte rows, count not established
- **Keyed by:** item kinds 4 and 5 (index base not established)
- **Read by:** [Item_GetEquipPalette](../functions/Item_GetEquipPalette.md)
- **Row layout:** [ItemEquipPaletteRow](../structs/ItemEquipPaletteRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Palette selectors read by Item_GetEquipPalette for the kinds 4 and 5.

## Behavior

- I: layout as ItemEquipPalettes.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: extent, index base and meaning of the rows
