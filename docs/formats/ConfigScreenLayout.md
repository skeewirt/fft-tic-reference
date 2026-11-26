# ConfigScreenLayout

- **Kind:** file format
- **Extension:** `.uib`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Read by:** [UIAddonFFTOConfig_BindNodes](../functions/UIAddonFFTOConfig_BindNodes.md), [ConfigMenu_SetTabTitles](../functions/ConfigMenu_SetTabTitles.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

`ffto_config_enhanced_ver02.uib` and `ffto_config_parts.uib` (pack 0008): the layout of the settings screen and its row, switch, select and slider parts.

## Behavior

- V: `Widget` = ConfirmWindowAll, MainTab, Config; `Config` = LayerRoot {TabAll (150, 110), ConfigList (150, 188), SelectList (1090, 188), LayerImg {DepthOfField, Gamma}, TextArea (0, 936)} and Black (a full-screen Reference); textures ui_button_dummy, ui_unit_tex_02, ui_config_parts, ui_unit_tex.
- V: `TabAll` = ButtonGuideL / R, TabButton01..07, states HomePosition, Show, Hide, Tab04, Tab05 and two more (the tab layouts by count; no layout below four tabs). `ListItem` (912 x 68) = Title text, references Select / Slider / Swich, states Enable, Disable, CursorOver, CursorOut, Select, Slider, Swich (each of the last three shows its widget and hides the other two: opacity key 5009).
- V: parts file: `Swich` (Knob, NineGrid00, Collision00), `Select` (Text00 text, ArrowL, ArrowR; states among them Arrow and List), `Slider` (Num, Knob, Bar, Base).
- V (seen live 2026-11-25): a `ListItem` whose `Select` state is played shows its `Select` part; with that part's `Arrow` state played (and `List` stopped) the row draws its Text00 value between ArrowL and ArrowR, as the stock value rows do; with `List` played and `Arrow` stopped it draws the value without arrows.
- V: `Widget` Show plays `MainTab` and `Config` Show (track 5028); `Config` Show / Hide play `TabAll`, `TextArea` and `Black` states (5028) and move `LayerImg`; `TabAll` Show / Hide animate only its `LayerRoot` position and opacity (Show: y -20 -> 0, opacity 0 -> 1 in 10 frames; Hide: opacity 1 -> 0, y 0 -> -10 in 6); `HomePosition` sets it to (0, 0), opacity 1. No state of `Config` or `TabAll` has a bool (enabled) track. I: tag 5028 = play the child's state of the same name; so a `TabAll` Hide played after the bind is undone by the screen's own Show, and the node's enabled byte (+144) stays as set.

## Open questions

None recorded.
