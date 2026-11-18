# UIListGadget_OnInput

- **Address:** `0x14028E188`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIListGadget_OnInput(UIListGadget *gadget, uint8 *input)`
- **Callers:** UIAddonFFTOConfig_OnInput
- **Callees:** UIListGadget_StepRow, UIListGadget_StepColumn, UIListGadget_RestoreFocus

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input of a list gadget: up / down / left / right moves of the cursor.

## Behavior

- V: does nothing unless the list component's byte +554 and the gadget's +120 are set and UIListGadget_IsAnimating says idle; then `ListScroll_HandleStick`; a cursor below 0 with a press (0x1400F1230) restores it (UIListGadget_RestoreFocus).
- V: input bytes +13640 / +13644 call UIListGadget_StepColumn(gadget, -1), +13642 / +13646 StepColumn(+1), +13641 / +13645 UIListGadget_StepRow(gadget, -1), +13643 / +13647 StepRow(+1); last 0x1400F1278(input).
- I: +13641 / +13645 are Up and +13643 / +13647 Down, +13640.. / +13642.. Left / Right; which byte of each pair is the pad is not known.

## State touched

- Calls: [UIListGadget_StepRow](UIListGadget_StepRow.md), [UIListGadget_StepColumn](UIListGadget_StepColumn.md), [UIListGadget_RestoreFocus](UIListGadget_RestoreFocus.md)

## Referenced by

- Called by: [UIAddonFFTOConfig_OnInput](UIAddonFFTOConfig_OnInput.md)
- Observed behaviours: [ListGadgetInputPath](../behaviors/ListGadgetInputPath.md)

## Open questions

None recorded.
