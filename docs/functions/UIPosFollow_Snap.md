# UIPosFollow_Snap

- **Address:** `0x1402AB3F0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIPosFollow_Snap(UIPosFollow *f)`
- **Callers:** sub_14011A20C, sub_14012F7F4, sub_14012FC6C
- **Callees:** GUINode_SetPosition

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finishes a position follow at once: puts the follower node at the target (int casts) and makes current = target.

## Behavior

- V: x = float +24, y = float +28; node = qword (f + 16). When node != 0: GUINode_SetPosition(node, (int)x, (int)y). Then f[8] = x, f[9] = y (current = target, also when there is no node).

## State touched

- Calls: [GUINode_SetPosition](GUINode_SetPosition.md)

## Referenced by

- Called by: [JobList_SelectEntry](JobList_SelectEntry.md)

## Notes

Name proposed (IDB: sub_1402AB3F0). Pair of UIPosFollow_SetTarget.

## Open questions

? as UIPosFollow_SetTarget.
