# ConfigMenu_SetTabTitles

- **Address:** `0x14018E6CC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_SetTabTitles(UIAddonFFTOConfig *addon)`
- **Callers:** UIAddonFFTOConfig_BindNodes
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the tab button titles from the ConfigCategory rows and the MainTab header.

## Behavior

- V: calls `MainTab_BindNodes(addon + 2848, root)` and `MainTab_SelectTab(addon + 2848, 2)` (the title board and the second board), puts UI text 2209 (General Options, mode 1) or 2613 (Settings, mode 0) in +2880 (MainTab +32, the `TextMask/MaskNode00` Title) and clears +2888 (MainTab +40 = `TextBoard02` Title).
- V: ConfigMenu_ShowTab then sets +2888 to the tab's ConfigCategory name id, so '<header> > Gameplay' is TextBoard02. `MainTab_SelectTab` index 1 ('Hide02') shows the title board alone (the Job Tree uses it).

## Referenced by

- Called by: [UIAddonFFTOConfig_BindNodes](UIAddonFFTOConfig_BindNodes.md)
- Reads file formats: [ConfigCategoryTable](../formats/ConfigCategoryTable.md), [ConfigScreenLayout](../formats/ConfigScreenLayout.md)
- Reads tables: [NxdDataConfigCategory](../tables/NxdDataConfigCategory.md)

## Open questions

None recorded.
