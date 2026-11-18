# ConfigMenu_LockList

- **Address:** `0x140193958`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_LockList(UIAddonFFTOConfig *addon, int lock)`
- **Callers:** UIAddonFFTOConfig_OnInput, ConfigMenu_OnDefaultsConfirm
- **Callees:** ConfigMenu_EnableRowWidgets

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns the row list's input off or on (gadget +128, the rows' widgets, the tab collisions).

## Behavior

- V: the rows' widgets go through ConfigMenu_EnableRowWidgets.

## State touched

- Calls: [ConfigMenu_EnableRowWidgets](ConfigMenu_EnableRowWidgets.md)

## Referenced by

- Called by: [ConfigMenu_OnDefaultsConfirm](ConfigMenu_OnDefaultsConfirm.md)

## Open questions

None recorded.
