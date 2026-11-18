# TitleScreenLayout

- **Kind:** file format
- **Extension:** `.uib`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Read by:** [UITitleMenu_BindNodes](../functions/UITitleMenu_BindNodes.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

`ffto_title_enhanced.uib` (pack 0008): the title screen behind the menu: backdrop, logo, version, copyright and the `Menu` component with its six buttons.

## Behavior

- V: `Widget` = Rect00 (1920 x 1080, #e9e6d8) and TitleEnhanced; `TitleEnhanced` = LayerRoot {Menu (872, 770; 300 x 240), Logo (0, 0; 1920 x 800), Version (1784, 1000), Copyright (0, 1000), BG (1920 x 1080)}; textures ui_title_enhanced_parts, ui_logo_fft_enhanced, ui_title_enhanced_bg.
- V: its Hide fades LayerRoot to opacity 0 in 10 frames (and plays Menu's Hide), so hiding the title add-on takes the backdrop (BG) with it: behind another screen the title is then black (seen live 2026-11-13).
- V: component `Menu` = LayerButton {MenuButton01..06, References to `MenuButton`}, the six at (0, 41), (0, 91), (0, 141), (0, 108), (0, 152), (0, 196) in the file; states HomePosition, Show, Hide (only LayerButton: position and opacity) and Menu3..Menu6 (1 frame each, keys 5002 position and 5009 opacity per button): Menu3 rows 1..3 at y 41 / 91 / 141, 4..6 opacity 0; Menu4 at 16 / 66 / 116 / 166, 5 and 6 at 222 opacity 0; Menu5 at 4 / 48 / 92 / 136 / 180, 6 opacity 0; Menu6 at -24 / 20 / 64 / 108 / 152 / 196. `TitleEnhanced` Menu3..Menu6 each play the `Menu` state of the same name (5028). Component `MenuButton` (300 x 60) = Layer00, Glow, Title, Collision00; states HomePosition, Enable, Disable, CursorOver, CursorOut, Down, Up, Click.

## Referenced by

- Observed behaviours: [TitleBackdropAndInputFlag](../behaviors/TitleBackdropAndInputFlag.md), [TitleMenuRowStorage](../behaviors/TitleMenuRowStorage.md)

## Open questions

None recorded.
