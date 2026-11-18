# UIListGadget_RestoreFocus

- **Address:** `0x14028DAEC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIListGadget_RestoreFocus(UIListGadget *gadget)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Focuses the list's cursor row again.

## Behavior

- I: named from its callers (shown, confirm closed, cursor below 0).

## Referenced by

- Called by: [ConfigMenu_OnDefaultsConfirm](ConfigMenu_OnDefaultsConfirm.md), [UIListGadget_OnInput](UIListGadget_OnInput.md)

## Open questions

None recorded.
