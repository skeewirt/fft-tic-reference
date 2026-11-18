# PanelScreen_InitVram

- **Address:** `0x14033D88C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int PanelScreen_InitVram(void)`
- **Callers:** sub_14033D9E4
- **Callees:** VramPage_CopyRect, sub_14025FC38

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Uploads the palette and strips of the second panel screen to VRAM.

## Behavior

- V: the same upload sequence as EquipScreen_InitVram with the other palette block (0x1408F9370): the staging block at x 256, the 64 x 4 word palette at (256, 250) and two small strips.
- V: then clears an eight-word state block and one dword; there is no inventory snapshot or order list work.

## State touched

- Calls: [VramPage_CopyRect](VramPage_CopyRect.md), [sub_14025FC38](sub_14025FC38.md)

## Referenced by

- Reads tables: [PanelScreenPalette](../tables/PanelScreenPalette.md)

## Notes

IDA carried a wrong library name for this function.

## Open questions

?: which screen sub_14033D9E4 starts.
