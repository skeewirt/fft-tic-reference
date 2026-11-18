# SpriteHdEntryRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One HD sheet entry number.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="entry"></a>`0x0` | entry | `uint32` | V | First HD sheet entry of the look in the g2d pack (the second sheet is the next entry); 0xFFFFFFFF = none. |

## Referenced by

- Described by tables: [SpriteHdEntryByShape](../tables/SpriteHdEntryByShape.md)

## Open questions

None recorded.
