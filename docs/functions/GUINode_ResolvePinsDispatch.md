# GUINode_ResolvePinsDispatch

- **Address:** `0x1403EF860`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_ResolvePinsDispatch(GUINode *n)`
- **Callers:** GUIComponent_UpdateNodeTree, sub_140297FF8, sub_1403F0654, sub_14040BBF0, sub_14040C37C
- **Callees:** GUINode_ResolvePins_Fraction, GUINode_ResolvePins_Offset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses how a node's edge pins are resolved against its parent: pins as fractions (node+141 = 0) or as pixel offsets (node+141 = 1).

## Behavior

- V: node+140 = 0 -> nothing. Otherwise node+141 = 0 -> GUINode_ResolvePins_Fraction(n); node+141 = 1 -> GUINode_ResolvePins_Offset(n); any other value does nothing.

## State touched

- Calls: [GUINode_ResolvePins_Fraction](GUINode_ResolvePins_Fraction.md), [GUINode_ResolvePins_Offset](GUINode_ResolvePins_Offset.md)

## Referenced by

- Called by: [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md)

## Notes

The name is ours (IDB: sub_1403EF860). 30769 hits per 4 s: the single hottest helper on the Job Tree page (it runs for every node whose size or pins changed).

## Open questions

? What +141 values above 1 would mean (none dispatched).
