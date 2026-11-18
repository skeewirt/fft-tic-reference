# ConfirmWindow_OnInput

- **Address:** `0x14029ECF8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfirmWindow_OnInput(ConfirmWindow *window, int *out, uint8 *input)`
- **Callers:** UIAddonFFTOConfig_Update
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input of the confirm window (its vtable +64).

## Behavior

- V: out[0] = the chosen button (0 the first, -1 nothing yet; 100 / 105 in its special modes). The screen answers it in ConfigMenu_OnDefaultsConfirm.

## Open questions

None recorded.
