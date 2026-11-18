# UIAddonFFTOConfig_RefreshRowTexts

- **Address:** `0x1401890E0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOConfig_RefreshRowTexts(UIAddonFFTOConfig *addon)`
- **Callers:** the add-on's vtable (slot 13)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vtable slot 13 of the General Options screen: sets every row's Title text again from its ConfigItem.

## Behavior

- V: the text id is ConfigItem +56.

## Referenced by

- Reads tables: [NxdDataConfigItem](../tables/NxdDataConfigItem.md)

## Open questions

None recorded.
