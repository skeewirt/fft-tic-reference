# MapRenderer_ApplyVariationEffects

- **Address:** `0x1400CF2A8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 MapRenderer_ApplyVariationEffects(char *sub, const int *element)`
- **Callers:** MapRenderer_ApplyMapRow
- **Callees:** sub_1400D1AB8, EventCharaSprite_SetTable256Entry, sub_1400D24CC, sub_1400CE9FC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the four post-effect rows that a Map variation element names (glare, colour lookup, depth lookup, depth of field) into the renderer sub-object.

## Behavior

- V: the first argument is the sub-object that MapRenderer_ApplyMapRow passes (renderer + 148512), the second the 72-byte variation element.
- V: stores element +0x28 (post_effect_dof) at sub +4320, +0x14 (post_effect_glare) at +4324, +0x18 (post_effect_lut) at +4332 and +0x1C (post_effect_depth_lut) at +4328, and clears byte +4295.
- V: calls sub_1400D1AB8 with the depth-of-field key (it loads a PostEffectDOF row, table 227, through sub_1400D1F54), EventCharaSprite_SetTable256Entry with the glare key (PostEffectGlare, table 256), sub_1400D24CC with the colour lookup key (PostEffectLUT, table 285) and sub_1400CE9FC with the depth lookup key (PostEffectDepthLUT, table 284).
- V: after the LUT and depth LUT loads it copies the freshly loaded lookup values over the sub-object's current-value copies (the LUT block at +4232 from +4256 / +4264, the depth LUT block at +4128 from +4192 / +4208) and sets one word of each block to -1.0 (+4272 and +4228).
- I: the copy and the -1.0 words make the new rows take effect at once, without a fade (the words look like a no-fade-running marker).

## State touched

- Calls: [EventCharaSprite_SetTable256Entry](EventCharaSprite_SetTable256Entry.md)

## Referenced by

- Called by: [MapRenderer_ApplyMapRow](MapRenderer_ApplyMapRow.md)
- Observed behaviours: [MapVariationChosenBySceneVariables](../behaviors/MapVariationChosenBySceneVariables.md)

## Notes

Each key is the row key of its table; the value 0 is a valid key (the rows are looked up by key like any other).

## Open questions

? the contents of the four row types as used by the picture (only their loads were read).
