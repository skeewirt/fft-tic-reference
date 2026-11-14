# UIGadget_GetOwnerWidget

- **Address:** `0x1402A7A84`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIGadget_GetOwnerWidget(UIGadget *g)`
- **Callers:** vtables only: UIGadgetFFTOJobDetailWindowWithButton_140716E50 slot 1, ...WithGuide_140716E68 slot 1, ...JobDetailWindowBase_140716F78 slot 1
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the owning widget of the gadget's owner node: node = *(g + 8); returns node + 496 (0 when there is no node).

## Behavior

- V: v1 = qword (a1 + 8); returns 0 when null, else the qword at (v1 + 496).
- V (context): node+496 is the owning widget of a GUI node (GUICore_FocusNode reads it that way).

## Notes

Name proposed (IDB: sub_1402A7A84); the same trivial getter is shared by the three job detail window classes.

## Open questions

? what the slot 1 virtual is called by (likely the focus / cursor owner lookup).
