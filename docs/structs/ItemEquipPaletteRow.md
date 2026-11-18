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
| <a id="palettes"></a>`0x0` | palettes | `uint8` | V | Two 4-bit indices of 32-byte palettes at 0x140D35750 loaded into palette slots 5 (high nibble) and 6 (low nibble); I: the weapon and shield sprite palettes. |
| <a id="byte1"></a>`0x1` | byte1 | `uint8` | ? | No reader found. |

## Referenced by

- Described by tables: [ItemEquipPalettes](../tables/ItemEquipPalettes.md), [ItemEquipPalettesHigh](../tables/ItemEquipPalettesHigh.md)

## Open questions

None recorded.
