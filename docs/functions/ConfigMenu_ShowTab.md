# ConfigMenu_ShowTab

- **Address:** `0x14018EA74`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_ShowTab(UIAddonFFTOConfig *addon, int tab)`
- **Callers:** UIAddonFFTOConfig_BindNodes, UIAddonFFTOConfig_OnInput
- **Callees:** UIListGadget_SetCount

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the row list of a tab from its ConfigCategory and sets the tab states and header.

## Behavior

- V: walks the tab's ConfigCategory `config_items` and keeps only the item ids its code names (0..27, 30..33, 39, 46..56, in that code's order); in mode 1 only those whose ConfigItem byte +72 is set. A ConfigItem row the code does not name is never listed, whatever the table says.
- V: then sets the list count, the tab buttons' Active / Deactive states and the sub-header (+2888).

## State touched

- Calls: [UIListGadget_SetCount](UIListGadget_SetCount.md)

## Referenced by

- Called by: [UIAddonFFTOConfig_BindNodes](UIAddonFFTOConfig_BindNodes.md)
- Reads file formats: [ConfigCategoryTable](../formats/ConfigCategoryTable.md), [ConfigItemTable](../formats/ConfigItemTable.md)
- Reads tables: [NxdDataConfigCategory](../tables/NxdDataConfigCategory.md), [NxdDataConfigItem](../tables/NxdDataConfigItem.md)

## Open questions

None recorded.
