# CharaRender_UnitLight

- **Address:** `0x1400CBB50`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `uint16_t CharaRender_UnitLight(void *block, unsigned slot, const void *light)`
- **Callers:** sub_1402705E0
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Updates a drawing slot's 40-byte light record in the HD character renderer's per-slot block (+328 + 40 x slot): its light values and a fade of the light factor toward 1.0 when the light changes.

## Behavior

- V: a slot of 16 or more is taken as slot 0 (the test at 0x1400CBB6C).
- V: record +0 a byte, +28 / +36 the light words, +2 / +4 the current and previous key, +8 / +12 / +16 / +20 the light's positions, +24 the factor (1.0 = settled; set to a tiny value when the light changes, then raised by 1 / dword_142E80194 (0.2 by default) per call).

## Referenced by

- Observed behaviours: [TwentyOneUnitsNeedSixPerSlotStoresWidened](../behaviors/TwentyOneUnitsNeedSixPerSlotStoresWidened.md)

## Open questions

None recorded.
