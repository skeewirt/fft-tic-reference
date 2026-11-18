# EffectFileLocatorRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of EffectFileLocatorsLangOther.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="pack_file_number"></a>`0x0` | pack_file_number | `uint32` | V | file number in the game's data pack (900 / 901 based) |
| <a id="size"></a>`0x4` | size | `uint32` | V | size of the effect file in bytes (0xB000, 0xB800, 0x14000 ...) |

## Referenced by

- Described by tables: [EffectFileLocatorsLang0](../tables/EffectFileLocatorsLang0.md), [EffectFileLocatorsLangOther](../tables/EffectFileLocatorsLangOther.md)

## Open questions

None recorded.
