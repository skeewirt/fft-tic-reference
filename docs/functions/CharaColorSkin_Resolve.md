# CharaColorSkin_Resolve

- **Address:** `0x1401E39BC`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int CharaColorSkin_Resolve(int value)`
- **Callers:** PreviewUnit_BuildRecord, PreviewUnit_BuildSpriteRecord, Unit_GetSpriteSetId, sub_1400FD0E4, sub_1401009E8, sub_140125F38, sub_1401E3A10, sub_1402AC520
- **Callees:** UITable_GetRowByKeys, UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves a CharCLUT chara_color_skin value to the skin to use.

## Behavior

- V: only the value 1 does anything: the CharaColorSkin (276) row (1, the selected skin: high byte of word_1411A7550) must pass UserSituation_IsMet on its +8; the function returns the selected skin.

## State touched

- Calls: [UITable_GetRowByKeys](UITable_GetRowByKeys.md), [UserSituation_IsMet](UserSituation_IsMet.md)

## Notes

Name is ours.

## Open questions

None recorded.
