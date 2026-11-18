# SectorAndSize

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the BattleSpriteFilesLanguage0 table and the tables that share its shape.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="sector"></a>`0x0` | sector | `uint32` | V | file sector of the sheet's battle sprite data (0 = none) |
| <a id="size"></a>`0x4` | size | `uint32` | V | byte size to read |

## Referenced by

- Described by tables: [BattleSpriteFilesLanguage0](../tables/BattleSpriteFilesLanguage0.md), [BattleSpriteFilesOtherLanguages](../tables/BattleSpriteFilesOtherLanguages.md)

## Open questions

None recorded.
