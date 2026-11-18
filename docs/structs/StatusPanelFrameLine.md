# StatusPanelFrameLine

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 7 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the StatusPanelFrameLines table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="rgb"></a>`0x0` | rgb | `bytes[3]` | V | primitive colour red, green, blue |
| <a id="x"></a>`0x3` | x | `uint8` | V | x offset added to the panel origin |
| <a id="y"></a>`0x4` | y | `uint8` | V | y offset added to the panel origin |
| <a id="width"></a>`0x5` | width | `uint8` | V | line width (1) |
| <a id="height"></a>`0x6` | height | `uint8` | V | line height |

## Referenced by

- Described by tables: [StatusPanelFrameLines](../tables/StatusPanelFrameLines.md)

## Open questions

None recorded.
