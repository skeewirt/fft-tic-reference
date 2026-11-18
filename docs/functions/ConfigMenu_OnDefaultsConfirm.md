# ConfigMenu_OnDefaultsConfirm

- **Address:** `0x140194C00`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_OnDefaultsConfirm(UIAddonFFTOConfig *addon, int *answer)`
- **Callers:** UIAddonFFTOConfig_Update (queued dialogs)
- **Callees:** ConfirmWindow_ShowHide, ConfigMenu_LockList, UIListGadget_RestoreFocus, UIGuide_Show, Input_PauseFor

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answer of the screen's own confirm window (0 = do it, anything else = cancel): hides the window and returns the screen to its list.

## Behavior

- V: on close: ConfirmWindow_ShowHide(window, 0, 0), ConfigMenu_LockList(addon, 0), +61 = 1, UIListGadget_RestoreFocus(list) (the list focuses its cursor row again; +61 keeps the cursor sound quiet), +48 = 0, +61 = 0, guide shown (UIGuide_Show 1), input pause 0.1 s, action 0x46 masked.

## State touched

- Calls: [ConfirmWindow_ShowHide](ConfirmWindow_ShowHide.md), [ConfigMenu_LockList](ConfigMenu_LockList.md), [UIListGadget_RestoreFocus](UIListGadget_RestoreFocus.md), [UIGuide_Show](UIGuide_Show.md), [Input_PauseFor](Input_PauseFor.md)

## Open questions

None recorded.
