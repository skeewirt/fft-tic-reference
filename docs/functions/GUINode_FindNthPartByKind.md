# GUINode_FindNthPartByKind

- **Address:** `0x1403F081C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINode *GUINode_FindNthPartByKind(GUINode *n, unsigned kind, int index)`
- **Callers:** ComponentEffects_Collect, sub_14010E950, sub_140118438, sub_140125414, sub_1401332A0, sub_14015CB04, sub_14015F2F4, sub_14019CD24, sub_1401AE728 and 8 more
- **Callees:** sub_1403F0850

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the index-th (0-based) descendant part of the given kind in depth-first order; the worker is sub_1403F0850.

## Behavior

- V: wrapper: copies index to the stack and calls GUINode_FindNthPartByKindRec(n, kind, &index).
- V: worker: for each child c (first child n+208, next c+32): when c+52 = kind: v = (*counter)--; v <= 0 returns c (so the counter counts down to 0). When c+52 = 1 (container) recurses into it; a non-null result is returned. Returns 0 when exhausted.

## Referenced by

- Called by: [ComponentEffects_Collect](ComponentEffects_Collect.md), [GUITabButton_Deselect](GUITabButton_Deselect.md), [GUITabButton_Select](GUITabButton_Select.md), [sub_1401332A0](sub_1401332A0.md), [sub_1403456D4](sub_1403456D4.md)

## Notes

The name is ours (IDB: sub_1403F081C and the recursive worker sub_1403F0850). 29 hits per 4 s each. The children of a container of the same kind count too, in tree order (container itself first when kind = 1).

## Open questions

None recorded.
