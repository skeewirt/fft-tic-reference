# UnitSprite_DepthSort

- **Address:** `0x14026D9C8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void UnitSprite_DepthSort(void *sceneObject, ...)`
- **Callers:** sub_140207880, sub_14020BCF0, sub_14020CC50, sub_14020DC78, sub_14020E174, sub_140210AF0
- **Callees:** sub_140261F60, cos, sin, sub_1400D31CC, sub_140249000, sub_140261E28, sub_140261D9C, sub_140283AB8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Computes the depth value of a unit sprite for sorting.

## Behavior

- V: for a scene object whose dword +0x15C has bit 4 set it adds the render object's byte +964 (the CharShape unknown_2d column, signed, copied there by sub_14027032C) to the unit's y before the depth value is computed.
- V: the same flag makes BattleFormation_DrawUnits use the alternate height (CharShape height_2).

## Notes

Name is ours.

## Open questions

? what scene object flag +0x15C bit 4 marks.
