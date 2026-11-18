# UIAddonFFTOConfig_BindNodes

- **Address:** `0x140188878`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOConfig_BindNodes(UIAddonFFTOConfig *addon)`
- **Callers:** the add-on's vtable (slot 4)
- **Callees:** ConfigMenu_SetTabTitles, ConfigMenu_ShowTab, UIListGadget_Bind, UIGuide_Show

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Node binding of the General Options screen (vtable slot 4): picks the tabs by mode and binds Config, TabAll, ConfigList, SelectList, TextArea and ConfirmWindowAll.

## Behavior

- V: mode byte +52 = 1 (the mode select's General Options) uses the ConfigCategory tabs 11, 8, 10, 9; mode 0 (in game) uses 5, 3, 4, 0, 2, 1.
- V: the bind ends with the guide bar shown (UIGuide_Show, 1).

## State touched

- Calls: [ConfigMenu_SetTabTitles](ConfigMenu_SetTabTitles.md), [ConfigMenu_ShowTab](ConfigMenu_ShowTab.md), [UIListGadget_Bind](UIListGadget_Bind.md), [UIGuide_Show](UIGuide_Show.md)

## Referenced by

- Appears in flows: [GeneralOptionsOpenAndClose](../flows/GeneralOptionsOpenAndClose.md)
- Reads file formats: [ConfigScreenLayout](../formats/ConfigScreenLayout.md)

## Open questions

None recorded.
