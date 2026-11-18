# GlyphAdvance

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the GlyphAdvanceWidths table: the advance width of one glyph.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="advance"></a>`0x0` | advance | `uint8` | V | pixel advance of the glyph with this index (6 for most glyphs, 4..10 for narrow and wide ones) |

## Referenced by

- Described by tables: [GlyphAdvanceExceptions](../tables/GlyphAdvanceExceptions.md), [GlyphAdvanceWidths](../tables/GlyphAdvanceWidths.md)

## Open questions

None recorded.
