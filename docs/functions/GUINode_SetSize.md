# GUINode_SetSize

- **Address:** `0x1403EF6B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_SetSize(GUINode *n, int w, int h)`
- **Callers:** 34 functions incl. GUIComponent_UpdateNodeTree, GUINode_ApplyAnimChannels, GUITextBoardComponent_Update, GUIComponent_SetAllocatedSize, GUINode_BuildFromFile, GUIComponent_Ctor, GUIComponent_LoadProps
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets node size (+64 / +68), marks the node dirty, invalidates resolved pins and, unless the node has an explicit pivot, re-centres the pivot at size / 2.

## Behavior

- V: no change when (w, h) equals the stored size. Otherwise +64 = w, +68 = h, +149 (dirty) = 1.
- V: when (u8 +140 & 0xC) != 0 the cached right/bottom pin floats +124 and +128 are set to 0x7F7FFFFF (FLT_MAX, 'unresolved'), so GUINode_ResolvePins_* recompute them.
- V: when u8 +142 = 0 (pivot not explicit): pivot +72 = w / 2, +76 = h / 2 (C int division, truncation toward zero).

## Referenced by

- Called by: [CreditRoll_AddPictureLine](CreditRoll_AddPictureLine.md), [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md), [GUIComponent_LoadProps](GUIComponent_LoadProps.md), [GUIComponent_SetAllocatedSize](GUIComponent_SetAllocatedSize.md), [GuideBar_LayoutRow](GuideBar_LayoutRow.md), [UIGadgetFFTOVScrollText_Refit](UIGadgetFFTOVScrollText_Refit.md)

## Notes

The name is ours (IDB: sub_1403EF6B4). 13717 hits per 4 s. FLT_MAX (0x7F7FFFFF = 2139095039) is the 'pin not resolved yet' sentinel; GUINode_ResolvePins_Fraction tests |x - 3.4028235e38| <= 1.19e-7 to recognise it. Note the even-rounding of text boards happens in the caller, not here.

## Open questions

? What +142 is called in the editor (I: 'custom pivot').
