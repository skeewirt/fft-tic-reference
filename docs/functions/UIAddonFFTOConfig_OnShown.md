# UIAddonFFTOConfig_OnShown

- **Address:** `0x14018A31C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOConfig_OnShown(UIAddonFFTOConfig *addon)`
- **Callers:** UIAddon_OnEventBase (event 5)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 7 of the General Options screen: after it is shown the row list focuses its cursor row and the shown flag is set.

## Behavior

- V: calls UIListGadget_RestoreFocus on the row list, then +59 = 1.

## Open questions

None recorded.
