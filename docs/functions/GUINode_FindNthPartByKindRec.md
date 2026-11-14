# GUINode_FindNthPartByKindRec

- **Address:** `0x1403F0850`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINode *GUINode_FindNthPartByKindRec(GUINode *n, unsigned kind, int *remaining)`
- **Callers:** GUINode_FindNthPartByKind, itself
- **Callees:** itself

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Recursive worker of GUINode_FindNthPartByKind (see that sheet).

## Behavior

- V: depth-first over children via +208 / +32, matching node+52 = kind, decrementing *remaining on each match and returning the node when it was <= 0 before the decrement; recursing into kind 1 containers.

## State touched

- Reads: [GUINode.kind](../structs/GUINode.md#kind)

## Notes

The name is ours (IDB: sub_1403F0850).

## Open questions

None recorded.
