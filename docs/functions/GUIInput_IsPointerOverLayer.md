# GUIInput_IsPointerOverLayer

- **Address:** `0x1400FE2D0`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `char GUIInput_IsPointerOverLayer(Widget *w, int layerId)`
- **Callers:** UIGadgetFFTOVScrollText_HandleScrollInput, UIAddonFFTOBraveStoryGlossary_vfunc_12, UIAddonFFTOTitlePlaymode_vfunc_22, sub_140112748 and 5 more
- **Callees:** GUILayerXform_MapPointFloat, GUIWidget_HitTestPoint, GUIVector32_Init, GUIVector32_Free

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells whether the mouse pointer is over a widget and hits a target tagged with the given id.

## Behavior

- V: returns 0 unless the UI core's pointer-enabled byte (g_GUICore+1909) is set.
- V: maps the pointer (g_GUICore +1880/+1884) through the layer transform of the widget's layer (w+60) with GUILayerXform_MapPointFloat, then hit-tests with GUIWidget_HitTestPoint.
- V: returns 1 when one of the hits has byte +143 equal to `layerId`.
- I: name and the meaning of byte +143 (layer or group id) are inferred; the function guards wheel scrolling of text/list gadgets.

## State touched

- Calls: [GUILayerXform_MapPointFloat](GUILayerXform_MapPointFloat.md), [GUIWidget_HitTestPoint](GUIWidget_HitTestPoint.md), [GUIVector32_Init](GUIVector32_Init.md), [GUIVector32_Free](GUIVector32_Free.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Referenced by

- Called by: [ListScroll_HandleStick](ListScroll_HandleStick.md)

## Notes

The stock wheel handler requires the pointer over its gadget through this check.

## Open questions

What byte +143 is.
