# GuideBarLayout

- **Kind:** observed behaviour
- **Scope:** the footer button guide bar
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [UIGuide_Set](../functions/UIGuide_Set.md), [UIGuide_Show](../functions/UIGuide_Show.md), [UIGuide_GetKey](../functions/UIGuide_GetKey.md), [GuideBar_SetPage](../functions/GuideBar_SetPage.md), [GuideBar_Layout](../functions/GuideBar_Layout.md), [GuideBar_LayoutRow](../functions/GuideBar_LayoutRow.md), [UIButtonGuideKeysOfGeneralOptions](../registries/UIButtonGuideKeysOfGeneralOptions.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The guide bar shows one UIButtonGuide key at a time: up to 8 slots, left ones first then right ones from x 1920; a sub-row mask hides sub-rows.

## Behavior

- V: UIGuide_Set jumps to the guide agent (agents array entry 14, +112) when it is active (its vtable +16); its add-on +64 gets GuideBar_SetPage(addon, key, rows), which stores the key at +2224 and a sub-row mask at +2228 and lays the bar out.
- V: GuideBar_Layout reads UI table 33 (`UIButtonGuide`): rows of the key, left ones, then right ones; GuideBar_LayoutRow skips sub-row i when bit i of the mask is clear and a row whose text id (+12) is 0; byte +37 (`Unknown25`) = right side.
- V: UIGuide_Show(_, show, 0, rows) calls the guide agent's 0x14013C740; the settings screen hides the bar when it opens its own confirm and shows it again when the confirm closes; TitleMenu_Build ends with show 0.

## Open questions

None recorded.
