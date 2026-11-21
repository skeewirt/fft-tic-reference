# UnitClut_TintRow

- **Address:** `0x1402F7628`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int16_t UnitClut_TintRow(int mode, uint16_t *row, int unused, unsigned slot, int unused2, int16_t dr, int16_t dg, int16_t db, int now)`
- **Callers:** SceneUnit_TintOwnRow, UnitClut_TintRowPlain
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The battle side's tint rule: turns one 16-colour palette row into a unit slot's colours in bank 3 of the palette manager.

## Behavior

- V: loops over the 16 colours of the row; a colour word of zero gives red, green and blue 0 and skips the mode and the offsets.
- V: mode 5 takes each channel halved to 4 bits (word bits 1..4, 6..9, 11..14); mode 6 puts (blue + 3 green + 2 red) / 6 in all three channels; mode 7 the same sum / 12; every other mode value (the callers pass 4 and 8) takes the channels as they are.
- V: adds dr, dg, db to red, green, blue, limits each to 31, and puts a channel below 1 to 0.
- V: when all three channels are 0 and the low 15 bits of the source word are not, blue becomes 1.
- V: writes the word (bit 15 kept from the source) to word_140C6D770[16 * slot + i], the base row of bank 3, and sets the manager's first dirty dword.
- V: with `now` non-zero it also writes the word to word_140C74170[16 * slot + i] (bank 3 of the final image) and, when the slot's byte at 0x140C6CFE0 + 9 * slot is 0, the four state bytes red, green, blue, bit 15 of the colour (7 bytes per colour from 0x140C6D070).

## Referenced by

- Called by: [SceneUnit_TintOwnRow](SceneUnit_TintOwnRow.md), [UnitClut_TintRowPlain](UnitClut_TintRowPlain.md)
- Observed behaviours: [SixteenSceneUnitsComeOnlyFromTheLookQueue](../behaviors/SixteenSceneUnitsComeOnlyFromTheLookQueue.md), [TwentyOneUnitsNeedSixPerSlotStoresWidened](../behaviors/TwentyOneUnitsNeedSixPerSlotStoresWidened.md), [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md)

## Notes

The name is ours (IDB: sub_1402F7628). Structure: ClutBank. The same four modes and the same offset, limit and blue-1 lines are inline in CharaRender_BuildAtlasTexture for the menus.

## Open questions

? what the third and fifth arguments are for (not read by the body).
