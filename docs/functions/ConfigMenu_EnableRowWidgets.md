# ConfigMenu_EnableRowWidgets

- **Address:** `0x140193A20`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_EnableRowWidgets(UIAddonFFTOConfig *addon, int row, int enable)`
- **Callers:** ConfigMenu_LockList
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Enables or disables a row's arrows, slider and switch collisions.

## Behavior

- I: the prototype comes from the call in ConfigMenu_LockList.

## Referenced by

- Called by: [ConfigMenu_LockList](ConfigMenu_LockList.md)
- Reads tables: [NxdDataConfigItem](../tables/NxdDataConfigItem.md)

## Open questions

None recorded.
