# UITitle_ShowMenu

- **Address:** `0x1401C2BCC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UITitle_ShowMenu(UIAgentFFTOTitle *agent)`
- **Callers:** not recorded
- **Callees:** UIAddonFFTOTitle_Create, UIAddonFFTOTitlePlaymode_Create, TitleMenu_Build

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the title agent's three add-ons and builds the menu.

## Behavior

- V: creates the menu add-on (0x1401CB9B4), the play mode add-on (0x1401CBA60) and a third add-on (0x1401CA6C4, row 256 `ffto_saving.uib`), stored at agent +64, +72, +80.
- V: calls `TitleMenu_Build`.

## State touched

- Calls: [UIAddonFFTOTitle_Create](UIAddonFFTOTitle_Create.md), [UIAddonFFTOTitlePlaymode_Create](UIAddonFFTOTitlePlaymode_Create.md), [TitleMenu_Build](TitleMenu_Build.md)

## Open questions

None recorded.
