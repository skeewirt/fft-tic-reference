# UiRect

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One screen or VRAM rectangle of a panel.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="x"></a>`0x0` | x | `int16` | V | x |
| <a id="y"></a>`0x2` | y | `int16` | V | y |
| <a id="w"></a>`0x4` | w | `int16` | V | width |
| <a id="h"></a>`0x6` | h | `int16` | V | height |

## Referenced by

- Described by tables: [EquipPanelRects](../tables/EquipPanelRects.md)

## Open questions

None recorded.
