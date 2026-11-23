# UIAddon_LoadByRow

- **Address:** `0x1401D1A00`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddon_LoadByRow(UIAddon *addon, int row)`
- **Callers:** every screen creator
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads a screen's layout: row of UI table 24 (`uiaddon.nxd`), whose `path` names the layout file.

## Behavior

- V: looks the row up in UI table 24 and, when it exists, loads the layout with `sub_1401D1A3C` using the row's `path`.

## Referenced by

- Appears in flows: [ScreenAddonCreation](../flows/ScreenAddonCreation.md)
- Called by: [Boot_Update](Boot_Update.md), [Guide_OpenWindow](Guide_OpenWindow.md), [TitleScene_Update](TitleScene_Update.md), [UISaveLoad_StateEnter](UISaveLoad_StateEnter.md), [sub_140183658](sub_140183658.md)
- Resolves registries: [UIAddonRows](../registries/UIAddonRows.md)

## Notes

Flow: ScreenAddonCreation. Registry: UIAddonRows.

## Open questions

None recorded.
