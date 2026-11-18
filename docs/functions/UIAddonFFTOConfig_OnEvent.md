# UIAddonFFTOConfig_OnEvent

- **Address:** `0x14018A344`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOConfig_OnEvent(UIAddonFFTOConfig *addon, int *event, void *a3)`
- **Callers:** the add-on's vtable (slot 2)
- **Callees:** UIAddon_OnEventBase, ConfigMenu_DrawRowValue, ConfigMenu_SetHelpText

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Node event handler of the General Options screen (vtable slot 2): draws rows, tracks the cursor, applies switches, sliders and tab clicks.

## Behavior

- V: calls `UIAddon_OnEventBase` first (the call at 0x14018A38A).
- V: events by id (id at [0], index at [1]): 0x1E draw row [1] (posted by the list for every visible row); 0x20 a row got the cursor (node = the row, its index at node +648; sound 105 when the screen is shown and idle); 0x1C decide on a row (node = the list component at +1768); 0x1A a slider moved; 21 / 22 a switch went on / off (node = the switch, its row at node +548); 24 a tab clicked; 16 / 17 a click on a node (17: the Select arrows); 23 may the screen close (answer at [3]).
- V: event 0x1E sets the row's `Title` text from ConfigItem +56, shows the row's Select / Slider / Swich state by item type, registers the widget to the add-on (listener slots +584, row index at +548) and draws the value through ConfigMenu_DrawRowValue.

## State touched

- Calls: [UIAddon_OnEventBase](UIAddon_OnEventBase.md), [ConfigMenu_DrawRowValue](ConfigMenu_DrawRowValue.md), [ConfigMenu_SetHelpText](ConfigMenu_SetHelpText.md)

## Referenced by

- Observed behaviours: [UIAddonBaseEventRouting](../behaviors/UIAddonBaseEventRouting.md)
- Reads tables: [NxdDataConfigCategory](../tables/NxdDataConfigCategory.md), [NxdDataConfigItem](../tables/NxdDataConfigItem.md), [NxdDataConfigItemResolution](../tables/NxdDataConfigItemResolution.md), [NxdDataConfigItemTextLanguage](../tables/NxdDataConfigItemTextLanguage.md), [NxdDataConfigPadList](../tables/NxdDataConfigPadList.md), [NxdDataResolution](../tables/NxdDataResolution.md)

## Open questions

None recorded.
