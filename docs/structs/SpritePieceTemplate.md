# SpritePieceTemplate

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the WorldMapSpritePieceTemplates table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="d0"></a>`0x0` | d0 | `int32` | I | first template dword |
| <a id="d1"></a>`0x4` | d1 | `int32` | I | second template dword |
| <a id="d2"></a>`0x8` | d2 | `int32` | I | third template dword (0 marks an empty piece) |
| <a id="d3"></a>`0xC` | d3 | `int32` | I | fourth template dword |
| <a id="d4"></a>`0x10` | d4 | `int32` | I | fifth template dword (width of the piece) |
| <a id="d5"></a>`0x14` | d5 | `int32` | I | sixth template dword (height of the piece) |

## Referenced by

- Described by tables: [SpritePieceTemplates](../tables/SpritePieceTemplates.md)

## Open questions

None recorded.
