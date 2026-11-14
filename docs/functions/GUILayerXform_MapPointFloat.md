# GUILayerXform_MapPointFloat

- **Address:** `0x1403F8C3C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUILayerXform_MapPointFloat(GUILayerXform *t, float pt[2])`
- **Callers:** GUICore_UpdateFrame
- **Callees:** sub_1403F8A20

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same transform as GUILayerXform_MapPointInt without rounding; used by GUICore_UpdateFrame to bring the pointer into UI coordinates before the hit test.

## Behavior

- V: same matrix layout as the int variant.

## Referenced by

- Called by: [GUICore_UpdateFrame](GUICore_UpdateFrame.md), [GUIInput_IsPointerOverLayer](GUIInput_IsPointerOverLayer.md)

## Open questions

None recorded.
