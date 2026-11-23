# UIGuide_Show

- **Address:** `0x1400EB5F4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIGuide_Show(void *a1, int show, int a3, int rows)`
- **Callers:** UIAddonFFTOConfig_BindNodes, ConfigMenu_OnDefaultsConfirm, TitleMenu_Build
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows or hides the guide bar (calls the guide agent's 0x14013C740).

## Behavior

- V: the General Options screen hides the bar when it opens its own confirm and shows it again when the confirm closes; TitleMenu_Build ends with show 0 (the title menu has no guide bar); the General Options bind ends with show 1.

## Referenced by

- Called by: [Battle_TimelineFocusCamera](Battle_TimelineFocusCamera.md), [BgmMode_ToggleTitleLanguage](BgmMode_ToggleTitleLanguage.md), [Book_ShowGuide](Book_ShowGuide.md), [Boot_Update](Boot_Update.md), [ConfigMenu_OnDefaultsConfirm](ConfigMenu_OnDefaultsConfirm.md), [JournalScreen_OnAction](JournalScreen_OnAction.md), [TavernMenu_OnCommand](TavernMenu_OnCommand.md), [TitleScene_Update](TitleScene_Update.md), [UIAddonFFTOConfig_BindNodes](UIAddonFFTOConfig_BindNodes.md), [sub_14013F71C](sub_14013F71C.md)
- Observed behaviours: [GuideBarLayout](../behaviors/GuideBarLayout.md)

## Open questions

None recorded.
