# GUINode_SetPivot

- **Address:** `0x1403EF704`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_SetPivot(GUINode *n, int x, int y)`
- **Callers:** CharaRender_PlaceSlotImage, GUINode_BuildFromFile, sub_1401389C4, sub_14013ABCC, sub_140161F80
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the node pivot (+72 / +76), marks the node dirty and invalidates the resolved pivot pins.

## Behavior

- V: no change when equal. Otherwise +72 = x, +76 = y, +149 = 1; when u8 +140 != 0 the floats +132 and +136 are set to 0x7F7FFFFF (unresolved).

## Notes

The name is ours (IDB: sub_1403EF704). 1131 hits per 4 s. Unlike GUINode_SetSize it does not touch byte +142; I: the file loader sets the explicit-pivot flag itself.

## Open questions

None recorded.
