# LegacyTask12_Build

- **Address:** `0x14039A518`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `long LegacyTask12_Build(void)`
- **Callers:** sub_14033E2C0, sub_14033E30C
- **Callees:** GradientWindow_ColourFromPaletteA, GradientWindow_ColourFromPaletteB, NumberFields_Draw, SceneTask_WaitFrame, sub_140242AFC, sub_140220450

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task 12: builds the plates and number fields of a battle-side panel from per-language cell lists.

## Behavior

- V: mode 12 reads the command block 0x140901300, any other mode 0x1409014E0; the cell block of the text language (0x140900EC0 language 0, 0x1409011F0 language 3, 0x1409010E0 language 2, 0x140900FD0 otherwise) supplies 17 six-word cells.
- V: colours its gradient windows with GradientWindow_ColourFromPaletteA / B, draws number fields with NumberFields_Draw and waits frames with SceneTask_WaitFrame.
- I: the name 'task 12' is the task id this function tests (12) before choosing its command block.

## State touched

- Calls: [GradientWindow_ColourFromPaletteA](GradientWindow_ColourFromPaletteA.md), [GradientWindow_ColourFromPaletteB](GradientWindow_ColourFromPaletteB.md), [NumberFields_Draw](NumberFields_Draw.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [sub_140242AFC](sub_140242AFC.md)

## Referenced by

- Reads tables: [LegacyTask12CommandsA](../tables/LegacyTask12CommandsA.md), [LegacyTask12CommandsB](../tables/LegacyTask12CommandsB.md), [LegacyTask12LayoutLang0](../tables/LegacyTask12LayoutLang0.md), [LegacyTask12LayoutLang1](../tables/LegacyTask12LayoutLang1.md), [LegacyTask12LayoutLang2](../tables/LegacyTask12LayoutLang2.md), [LegacyTask12LayoutLang3](../tables/LegacyTask12LayoutLang3.md)

## Open questions

?: which panel it builds.
