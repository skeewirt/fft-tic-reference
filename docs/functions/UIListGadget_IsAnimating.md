# UIListGadget_IsAnimating

- **Address:** `0x14028D44C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int UIListGadget_IsAnimating(UIListGadget *gadget)`
- **Callers:** UIAddonFFTOConfig_OnInput
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True while a 'Show', 'Slide_left' or 'Slide_right' state is running on the gadget's node +16, its list +24 or a visible slot component.

## Behavior

- V: tests the state byte +105 of those states (GUINode_PlayState sets it to 1).

## Referenced by

- Called by: [UIAddonFFTOConfig_OnInput](UIAddonFFTOConfig_OnInput.md)
- Observed behaviours: [ListGadgetInputPath](../behaviors/ListGadgetInputPath.md)

## Open questions

None recorded.
