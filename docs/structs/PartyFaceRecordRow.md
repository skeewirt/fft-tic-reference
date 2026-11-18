# PartyFaceRecordRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One portrait rectangle record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="x"></a>`0x0` | x | `uint16` | V | Atlas x of the portrait rectangle; the job change preview shifts it by 2 bits and adds the page base. |
| <a id="y"></a>`0x2` | y | `uint16` | V | Atlas y of the portrait rectangle. |
| <a id="width"></a>`0x4` | width | `uint16` | V | Portrait width; the portrait is centred on it. |
| <a id="height"></a>`0x6` | height | `uint16` | V | Portrait height; the portrait is centred on it. |
| <a id="variant"></a>`0x8` | variant | `uint16` | I | Packed job-derived portrait variant (base << 6) \| low 6 bits (base 224 for generic jobs); the face record getter overwrites it for most indices. |
| <a id="page"></a>`0xA` | page | `uint16` | I | Atlas page or palette selector; the job change preview branches on 100, 101 and 28. |

## Referenced by

- Described by tables: [PartyFaceRecords](../tables/PartyFaceRecords.md)

## Open questions

None recorded.
