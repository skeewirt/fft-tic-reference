# ConfigMenu_DrawRowValue

- **Address:** `0x140190194`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_DrawRowValue(UIAddonFFTOConfig *addon, int row, int delta, int flag, int redraw)`
- **Callers:** UIAddonFFTOConfig_OnEvent, UIAddonFFTOConfig_OnInput
- **Callees:** GUISwitch_SetOn, GUISwitch_SetOff

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a row's value by item type, optionally stepping it first.

## Behavior

- V: ConfigItem column `Unknown4` is the row type: 1 a value with arrows (Select), 2 a slider, 3 an On / Off switch (Swich), 4 a value from a list (SelectList), 5 a key to press (UIDialog 232).
- V: for a switch a non-zero delta flips the value (sound 133), then the switch is set on or off through GUISwitch_SetOn / GUISwitch_SetOff.

## State touched

- Calls: [GUISwitch_SetOn](GUISwitch_SetOn.md), [GUISwitch_SetOff](GUISwitch_SetOff.md)

## Referenced by

- Called by: [UIAddonFFTOConfig_OnEvent](UIAddonFFTOConfig_OnEvent.md), [UIAddonFFTOConfig_OnInput](UIAddonFFTOConfig_OnInput.md)
- Reads file formats: [ConfigItemTable](../formats/ConfigItemTable.md)
- Reads tables: [NxdDataConfigCategory](../tables/NxdDataConfigCategory.md), [NxdDataConfigItem](../tables/NxdDataConfigItem.md), [NxdDataConfigItemResolution](../tables/NxdDataConfigItemResolution.md), [NxdDataConfigPadAssign](../tables/NxdDataConfigPadAssign.md), [NxdDataConfigPadList](../tables/NxdDataConfigPadList.md), [NxdDataResolution](../tables/NxdDataResolution.md)

## Open questions

None recorded.
