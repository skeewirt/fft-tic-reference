# EffectLabelRectRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of BattleEffectLabelRectsLang0.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="uv"></a>`0x0` | uv | `uint16` | I | packed texture position of the label picture (low bits x, high bits y) |
| <a id="width"></a>`0x2` | width | `uint8` | I | width of the label in pixels |
| <a id="height_flags"></a>`0x3` | height_flags | `uint8` | I | height and page flags |

## Referenced by

- Described by tables: [BattleEffectLabelRectsLang0](../tables/BattleEffectLabelRectsLang0.md), [BattleEffectLabelRectsLang1](../tables/BattleEffectLabelRectsLang1.md), [BattleEffectLabelRectsLang2](../tables/BattleEffectLabelRectsLang2.md), [BattleEffectLabelRectsLang3](../tables/BattleEffectLabelRectsLang3.md)

## Open questions

None recorded.
