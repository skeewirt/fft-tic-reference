# UIAddonFFTOTitlePlaymode_Create

- **Address:** `0x1401CBA60`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `UIAddon *UIAddonFFTOTitlePlaymode_Create(UIAgentFFTOTitle *agent)`
- **Callers:** UITitle_ShowMenu
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the second add-on of `UITitle_ShowMenu`: the play mode screen (uiaddon row 245, `ffto_title_playmode.uib`).

## Behavior

- V: allocated, attached and loaded the same way as the menu add-on (flow ScreenAddonCreation).

## Referenced by

- Called by: [TitleScene_Update](TitleScene_Update.md), [UITitle_ShowMenu](UITitle_ShowMenu.md)

## Open questions

None recorded.
