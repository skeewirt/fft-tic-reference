# ConfigMenu_SetHelpText

- **Address:** `0x1401928AC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_SetHelpText(UIAddonFFTOConfig *addon, int item)`
- **Callers:** UIAddonFFTOConfig_OnEvent
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the help line (the Text part of Config/TextArea) from the item's help text id.

## Behavior

- V: `GUITextNode_SetTextExpandedTemp`, then text id 0; the id is ConfigItem +64 in mode 1 and +68 in mode 0; called on event 0x20.

## Referenced by

- Called by: [UIAddonFFTOConfig_OnEvent](UIAddonFFTOConfig_OnEvent.md)
- Reads file formats: [ConfigItemTable](../formats/ConfigItemTable.md)
- Reads tables: [NxdDataConfigItem](../tables/NxdDataConfigItem.md), [NxdDataConfigItemCursorMoveType](../tables/NxdDataConfigItemCursorMoveType.md), [NxdDataUI](../tables/NxdDataUI.md)

## Open questions

None recorded.
