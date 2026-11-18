# ConfirmWindow_SetDialog

- **Address:** `0x14029C6E0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfirmWindow_SetDialog(ConfirmWindow *window, int dialog_row, int keep, int force)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads a UIDialog row into the confirm window gadget.

## Behavior

- V: the message text id goes to +192, the option text ids to the button text nodes at +72 / +80 / +88 (text id at node +248), and the row's flags (+429.., `ShowBlack` / `HideBlack`, the `Button<n>` layout by the number of options).

## Notes

Struct: UIGadgetFFTOConfigConfirmWindow (vtables 0x140712448 / 0x1407124A0).

## Open questions

None recorded.
