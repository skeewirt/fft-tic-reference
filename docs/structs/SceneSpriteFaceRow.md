# SceneSpriteFaceRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One face number.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="face"></a>`0x0` | face | `uint32` | V | Face number of a portrait code; 0xFFFFFFFF = none. Rows 160 and up hold fixed answers of the shape function (a few values name themselves). |

## Referenced by

- Described by tables: [SceneSpriteToFace](../tables/SceneSpriteToFace.md)

## Open questions

None recorded.
