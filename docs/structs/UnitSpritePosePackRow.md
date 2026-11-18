# UnitSpritePosePackRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the UnitSpritePosePack table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="header"></a>`0x0` | header | `uint32` | ? | first dword = 1 (pack version / count), then a u16 = 2 |
| <a id="record_offset"></a>`0x6` | record_offset | `int16` | V | byte offset of a 28-byte pose record, counted from the u16 at +4 (0xD8, 0xF4, 0x110 ... step 0x1C) |

## Referenced by

- Described by tables: [UnitSpritePosePack](../tables/UnitSpritePosePack.md)

## Open questions

None recorded.
