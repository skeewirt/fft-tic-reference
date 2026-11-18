# LegacyCellRectsRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the LegacyCellRects table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="pad"></a>`0x0` | pad | `uint32` | V | zero |
| <a id="size_and_texture"></a>`0x4` | size_and_texture | `bytes[12]` | I | six halfwords: width, height, texture u, texture v, width, height (12, 14, 48, 144 ...) |
| <a id="flags"></a>`0x10` | flags | `uint32` | ? | 0x10, 0x3F, 0x1F, 0 (colour / mode bytes) |

## Referenced by

- Described by tables: [LegacyCellRects](../tables/LegacyCellRects.md)

## Open questions

None recorded.
