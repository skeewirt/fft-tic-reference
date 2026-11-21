# CharaRenderer_Init

- **Address:** `0x1400D4648`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `__int64 CharaRenderer_Init(CharaRenderer *r)`
- **Callers:** sub_140188FA4, sub_14025712C
- **Callees:** CharaRender_InitTargets, sub_1403CAC84 (load texture by name), sub_1400CCCA8, sub_1400CA3C0, sub_1400CAF20, sub_1400C7E2C, sub_1400D2D6C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the unit renderer: allocates its sub-objects, loads the textures it needs and creates the 256 slot targets.

## Behavior

- V: textures loaded by name: bg/textures/lut_chara.tga, bg/textures/lut_uichara.tga, bg/textures/weather.tga (stored in the object at +148104), char/shape_blank.tga, char/chara_shadow.tga, char/chara_ripples.tga (+148120), ui/ui_blank.tga, ui/direction.tga, ui/direction_select.tga, ui/sword.tga.
- V: +148128 = a 1104-byte LUT manager, +148136 = the 75864-byte target state (built by sub_1400CCCA8), +148144 = the 23568-byte config: size 256, ground x 128, ground y 192, scale 2.0f (0x40000000) followed by 256 slot entries of 92 bytes.
- V: calls CharaRender_InitTargets(state, config size, ground x, ground y).

## State touched

- Calls: [CharaRender_InitTargets](CharaRender_InitTargets.md)
- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md)

## Referenced by

- Observed behaviours: [TwentyOneUnitsNeedSixPerSlotStoresWidened](../behaviors/TwentyOneUnitsNeedSixPerSlotStoresWidened.md)

## Notes

The LUT used for the job tree is the second texture (lut_uichara), taken by CharaRender_DrawFrame when present.

## Open questions

The other sub-objects (+148080, +148096, +148112) were not traced (?).
