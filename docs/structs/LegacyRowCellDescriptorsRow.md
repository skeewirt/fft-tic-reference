# LegacyRowCellDescriptorsRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the LegacyRowCellDescriptors table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="zero"></a>`0x0` | zero | `uint32` | I | zero |
| <a id="rects"></a>`0x4` | rects | `int16[8]` | I | two rectangles x, y, width, height |
| <a id="pad"></a>`0x14` | pad | `uint32` | I | zero |

## Referenced by

- Described by tables: [LegacyRowCellDescriptors](../tables/LegacyRowCellDescriptors.md)

## Open questions

None recorded.
