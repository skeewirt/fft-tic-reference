# ListScroll_HandleStick

- **Address:** `0x14028E5D0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char ListScroll_HandleStick(ListScrollHelper *h, InputState *in)`
- **Callers:** list screen update methods (not traced)
- **Callees:** GUIComponentList_GetVScroll, GUIComponentList_GetHScroll, GUIInput_IsPointerOverLayer, ListScroll_Step, sub_14028E850, sub_14028D44C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Mouse wheel or right stick scrolls a component list by whole rows, independent of the cursor.

## Behavior

- V: acts only when the list component (h+24) is enabled (its +554), h+120 is set, sub_14028D44C(h) is 0 and the int at h+104 is negative.
- V: wheel (in+8 != 0), when h+126 is clear or the pointer is over the list layer 9: a vertical bar present -> ListScroll_Step, else a horizontal bar -> sub_14028E850; returns 1.
- V: otherwise, when h+122 is set: right stick vertical byte in+1227 != 0 with a vertical bar -> ListScroll_Step; right stick horizontal byte in+1226 != 0 with a horizontal bar -> sub_14028E850; returns 1 when either ran, else 0.

## State touched

- Calls: [GUIComponentList_GetVScroll](GUIComponentList_GetVScroll.md), [GUIComponentList_GetHScroll](GUIComponentList_GetHScroll.md), [GUIInput_IsPointerOverLayer](GUIInput_IsPointerOverLayer.md), [ListScroll_Step](ListScroll_Step.md)

## Referenced by

- Called by: [UIListGadget_ClassicInput](UIListGadget_ClassicInput.md)
- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

The name is ours (IDB: sub_14028E5D0). The Job Tree has no VScroll bar and no reader of the input state's bytes +1224 .. +1227 (a scan of every instruction with those displacements, 2026-11-10: no JobTree_* function among them), so the right stick does nothing there today.

## Open questions

? the flags at h+120 / +122 / +126 are named from use only; ? the callers (an addon update).
