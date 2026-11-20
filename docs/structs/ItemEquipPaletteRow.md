# ItemEquipPaletteRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Palette selector of one item.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="palettes"></a>`0x0` | palettes | `uint8` | V | Two 4-bit indices of 32-byte palettes at 0x140D35750 loaded into palette slots 5 (high nibble) and 6 (low nibble) by ItemSprite_LoadPalettes; I: the weapon and shield sprite palettes. |
| <a id="sheet_row"></a>`0x1` | sheet_row | `uint8` | V | Row of the item picture in the equipment sprite sheet, in steps of 8 pixels: EquipSprite_BuildPieces adds it to the row of every piece it builds for the held item (piece v = 8 * (this + the frame row)). I: one picture per item, from the stock values. |

## Referenced by

- Described by tables: [ItemEquipPalettes](../tables/ItemEquipPalettes.md), [ItemEquipPalettesHigh](../tables/ItemEquipPalettesHigh.md)

## Open questions

None recorded.
