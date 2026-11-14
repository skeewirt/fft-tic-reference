# GUIComponent_SetAllocatedSize

- **Address:** `0x1403F2EF8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponent_SetAllocatedSize(RefNode *ref, GUIComponent *comp)`
- **Callers:** GUIComponent_UpdateNodeTree, sub_14012F138, sub_1402A4DB4, sub_14040BBF0 and two vtable entries
- **Callees:** GUINode_SetSize (sub_1403EF6B4)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores the size taken from a reference node (ref+64 / +68) as the component's allocated size comp+528 / +532, swapped for the rotated layout mode, and resizes the component root when it asks for it.

## Behavior

- V: (w, h) = ints at ref+64 / ref+68. When comp+536 = 7 and comp+664 = 0 the pair is swapped (w <-> h); otherwise unchanged.
- V: when comp+540 = 2: GUINode_SetSize(comp+272, w, h) (sub_1403EF6B4). Always comp+528 = w, comp+532 = h.

## State touched

- Calls: [GUINode_SetSize](GUINode_SetSize.md)

## Referenced by

- Called by: [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md)

## Notes

The name is ours (IDB: sub_1403F2EF8). 13862 hits per 4 s. This is the 'allocated rectangle' that the text board and the alignment code (GUITextBoardComponent_Update) read.

## Open questions

? Meaning of comp+536 = 7 (I: a rotated/portrait layout kind) and comp+540 = 2 (I: 'fit root to reference').
