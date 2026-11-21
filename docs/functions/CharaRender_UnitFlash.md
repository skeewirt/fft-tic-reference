# CharaRender_UnitFlash

- **Address:** `0x1400CC258`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void CharaRender_UnitFlash(void *block, unsigned slot, const float *distance)`
- **Callers:** sub_1402706BC
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Updates a drawing slot's 8-byte flash entry in the HD character renderer's per-slot block (+968 + 8 x slot): the highlight colour of a unit (kinds 1..3, a pulsing value that counts down unless paused) and the distance fade in its top byte.

## Behavior

- V: a slot of 16 or more is taken as slot 0 (the test at 0x1400CC26B).
- V: entry +0 the kind (3: brighter colour 255 / 160 / 100, else 240 / 140 / 80; 0: no flash), +1 the pulse counter (minus +2 per call, back to 32 below 0), +4 the resulting colour dword, whose top byte gets a fade from the distance (500..800 -> 223..32 + 32).

## Referenced by

- Observed behaviours: [TwentyOneUnitsNeedSixPerSlotStoresWidened](../behaviors/TwentyOneUnitsNeedSixPerSlotStoresWidened.md)

## Open questions

None recorded.
