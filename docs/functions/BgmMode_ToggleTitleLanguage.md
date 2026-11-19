# BgmMode_ToggleTitleLanguage

- **Address:** `0x1401C8438`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BgmMode_ToggleTitleLanguage(void *screen)`
- **Callers:** UIAddonFFTOBGMMode_vfunc_12
- **Callees:** Input_IsActionMapped, Input_PauseFor, sub_1400F4BCC, UIGuide_Show, UIListGadget_RefreshVisible

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Toggles the alternate track titles of the music player.

## Behavior

- V: only when g_LanguageInfo +8 is 2 or 3 and action 195 is mapped: toggles the screen's title-language dword (+896), plays UI sound 0x12F, shows guide text 21012 or 21013 and refreshes the list.
- V: language 2 is French and 3 German (registry TextLanguageCodes).

## State touched

- Calls: [Input_PauseFor](Input_PauseFor.md), [sub_1400F4BCC](sub_1400F4BCC.md), [UIGuide_Show](UIGuide_Show.md), [UIListGadget_RefreshVisible](UIListGadget_RefreshVisible.md)
- Writes: [BgmModeScreen.title_alt](../structs/BgmModeScreen.md#title_alt)

## Notes

Name is ours.

## Open questions

None recorded.
