# ClutBank_CopyRow

- **Address:** `0x1402F7594`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void ClutBank_CopyRow(const uint16_t *src, unsigned bank, unsigned row, int all)`
- **Callers:** SceneUnit_BuildFromQueueEntry, SceneUnit_RunPlacement, SceneUnit_BuildPalette, ItemSprite_LoadPalettes, BattleLoad_StepFresh, MapBlock_RunCommand
- **Callees:** sub_1402F74D8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a 16-colour row (or, with all = 1, all 16 rows) into a bank of the palette manager: its words, its 7-byte colour entries and the uploaded image, unless the bank is held.

## Behavior

- V: does nothing when the bank's second flag byte (g_ClutManager + 8 + 2450 x bank + 1) is set; else clears the row's header byte (all 16 headers with all = 1), copies through sub_1402F74D8 and marks the manager changed (dword 0 = 1).
- V: callers pass a drawing slot as the row for the per-slot banks: SceneUnit_BuildFromQueueEntry (bank 4, the raw copy of the unit's colours), SceneUnit_RunPlacement, SceneUnit_BuildPalette, ResultLabel_ShowNext and others; a row of 16 or more lands in the next part of the bank (its colour entries, then the next bank's flags and headers).

## State touched

- Calls: [sub_1402F74D8](sub_1402F74D8.md)

## Referenced by

- Observed behaviours: [TwentyOneUnitsNeedSixPerSlotStoresWidened](../behaviors/TwentyOneUnitsNeedSixPerSlotStoresWidened.md)

## Open questions

None recorded.
