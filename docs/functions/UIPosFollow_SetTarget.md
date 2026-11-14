# UIPosFollow_SetTarget

- **Address:** `0x1402AB394`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned __int64 UIPosFollow_SetTarget(UIPosFollow *f, int *pos)`
- **Callers:** sub_14011F69C, sub_14011F76C, sub_14012F7F4, sub_14012FC6C, JobList_OnCursorChanged
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts a position follow: target = base offset (f+40 / f+44) + pos (x, y); records the follower node's current position as the start.

## Behavior

- V: node = qword (f + 16). f[6] (float +24) = float(int f+40) + float(pos[0]); f[7] (+28) = float(int f+44) + float(pos[1]).
- V: when node != 0: f[8] (+32) = float(int low dword of node+56), f[9] (+36) = float(int high dword of node+56), i.e. the node's current (x, y).
- V: JobList_OnCursorChanged calls it twice (f = addon+8144 and addon+0x2000) with pos = (cell node + 56), the position of the cell the cursor moved to.

## Referenced by

- Called by: [JobList_SelectEntry](JobList_SelectEntry.md)

## Notes

Name proposed (IDB: sub_1402AB394); the role (the cursor / ring that glides to the hovered cell) is I, from the JobList_OnCursorChanged call pattern. The animation that moves it per frame was not traced.

## Open questions

? who interpolates f+32.. towards f+24.. each frame (not in this function). ? what f+40 / f+44 hold (a constant offset from the cell to the cursor).
