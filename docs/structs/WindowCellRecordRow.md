# WindowCellRecordRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of UiLegacyWindowCellLayoutBase.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="kind"></a>`0x0` | kind | `uint32` | I | cell kind (0xE0, 0x30, 0xB0, 0x20, 0x60 ...) |
| <a id="size"></a>`0x4` | size | `uint32` | I | width 0x10, height 0x18 (two words) |
| <a id="position"></a>`0x8` | position | `uint32` | I | x and y offset words (signed) |

## Referenced by

- Described by tables: [UiLegacyWindowCellLayoutBase](../tables/UiLegacyWindowCellLayoutBase.md)

## Open questions

None recorded.
