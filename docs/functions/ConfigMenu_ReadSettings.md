# ConfigMenu_ReadSettings

- **Address:** `0x14018C72C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_ReadSettings(UIAddonFFTOConfig *addon)`
- **Callers:** UIAddonFFTOConfig_Update
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the game settings' values per ConfigItem id into +648 of the add-on, every frame.

## Behavior

- I: the add-on compares the copy with the shown values (+404) to redraw rows changed elsewhere.

## Referenced by

- Called by: [UIAddonFFTOConfig_Update](UIAddonFFTOConfig_Update.md)
- Reads tables: [NxdDataConfigItem](../tables/NxdDataConfigItem.md), [NxdDataConfigItemButtonType](../tables/NxdDataConfigItemButtonType.md), [NxdDataConfigItemCursorMoveType](../tables/NxdDataConfigItemCursorMoveType.md), [NxdDataConfigItemForwardEnabledType](../tables/NxdDataConfigItemForwardEnabledType.md), [NxdDataConfigItemResolution](../tables/NxdDataConfigItemResolution.md), [NxdDataConfigItemTextLanguage](../tables/NxdDataConfigItemTextLanguage.md), [NxdDataConfigItemVoiceLanguage](../tables/NxdDataConfigItemVoiceLanguage.md)

## Open questions

None recorded.
