# PaletteColour

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of a UI palette block.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="colour"></a>`0x0` | colour | `uint16` | V | 15-bit colour word (5 bits per channel; bit 15 clear in this table) |

## Referenced by

- Described by tables: [EquipScreenPalette](../tables/EquipScreenPalette.md), [PanelScreenPalette](../tables/PanelScreenPalette.md)

## Open questions

None recorded.
