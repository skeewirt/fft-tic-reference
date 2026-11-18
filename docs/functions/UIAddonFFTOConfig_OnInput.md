# UIAddonFFTOConfig_OnInput

- **Address:** `0x1401892A8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOConfig_OnInput(UIAddonFFTOConfig *addon, uint8 *input)`
- **Callers:** UIAddon_OnEventBase (event 1)
- **Callees:** UIListGadget_IsAnimating, UIListGadget_OnInput, ConfigMenu_DrawRowValue, ConfigMenu_ConfirmDiscard

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input handler of the General Options screen (vtable slot 12): Back, restore defaults, tabs, value steps, then the row list's own input.

## Behavior

- V: with a confirm of its own open (+48 = 1..3) only that confirm reads input.
- V: action 0x1B Back closes the screen (asking first through UIDialog 63 when +55 / +56 are set: ConfigMenu_ConfirmDiscard) by calling the agent's vtable +48 with (agent, addon, 0, 0, 0); 0x46 asks UIDialog 61 (restore the tab's defaults); 0x2B / 0x2C select the previous / next tab (sound 109; the action codes are reached by a subtraction and a range test, so 0x2C and 0x46 are not immediates).
- V: input state bytes +0x3548 / +0x354C step the selected row's value by -1 and +0x354A / +0x354E by +1 (through ConfigMenu_DrawRowValue); offsets are relative to the input object passed in (`g_InputModule` + 8). I: they are Left and Right (from the step sign); which of each pair is the pad is not known.
- V: the handler ends, after Back, defaults, tabs and Left / Right, with the list's own input: when no value list is open (+2192 == 0) and the row list takes input (gadget +120), `if (!UIListGadget_IsAnimating(list)) UIListGadget_OnInput(list, input)`. The Left / Right branches return before it, so they never reach the list.
- V (seen live 2026-11-13): a screen of this class whose slot 12 does not make that call never moves its list cursor by pad or keyboard.

## State touched

- Calls: [UIListGadget_IsAnimating](UIListGadget_IsAnimating.md), [UIListGadget_OnInput](UIListGadget_OnInput.md), [ConfigMenu_DrawRowValue](ConfigMenu_DrawRowValue.md), [ConfigMenu_ConfirmDiscard](ConfigMenu_ConfirmDiscard.md)

## Referenced by

- Appears in flows: [GeneralOptionsOpenAndClose](../flows/GeneralOptionsOpenAndClose.md)
- Observed behaviours: [ListGadgetInputPath](../behaviors/ListGadgetInputPath.md)
- Reads tables: [NxdDataConfigCategory](../tables/NxdDataConfigCategory.md), [NxdDataConfigItem](../tables/NxdDataConfigItem.md)

## Open questions

None recorded.
