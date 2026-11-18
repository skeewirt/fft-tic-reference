# LegacyJobScreenLayoutLang0Row

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 6592 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the LegacyJobScreenLayoutLang0 table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="header"></a>`0x0` | header | `bytes[52]` | I | 13 dwords of row sizes / tile counts (0x40, 0x2C, 0x2C, 0x4A, 0x2C, 0x36 ...) |
| <a id="grid"></a>`0x34` | grid | `bytes[6540]` | ? | grid of small cell codes (0..0x12 per cell) drawn by the screen |

## Referenced by

- Described by tables: [LegacyJobScreenLayoutLang0](../tables/LegacyJobScreenLayoutLang0.md)

## Open questions

None recorded.
