# ConfigMenu_ConfirmDiscard

- **Address:** `0x14018E650`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_ConfirmDiscard(UIAddonFFTOConfig *addon)`
- **Callers:** UIAddonFFTOConfig_OnInput
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens UIDialog 63 when settings changes are pending and Back is pressed.

## Behavior

- V: used by the Back branch of UIAddonFFTOConfig_OnInput.

## Referenced by

- Called by: [UIAddonFFTOConfig_OnInput](UIAddonFFTOConfig_OnInput.md)

## Open questions

None recorded.
