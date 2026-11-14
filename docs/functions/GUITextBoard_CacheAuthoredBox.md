# GUITextBoard_CacheAuthoredBox

- **Address:** `0x14040E59C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUITextBoard_CacheAuthoredBox(__int64 comp)`
- **Callers:** GUITextBoardComponent_Update (and one apparent mis-named region at 0x14040E3EA)
- **Callees:** GUITextBoard_FindTextNode

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Once per component, snapshots the text node's authored rectangle and the component's authored size, the baseline GUITextBoardComponent_Update uses when it refits the board around the text.

## Behavior

- V: runs only if byte comp+684 != 0 (the 'not yet cached' flag) and GUITextBoard_FindTextNode(comp) returns non-null.
- V: with n = text node dwords: comp+648 = n[14] (x, node +56); comp+652 = n[15] (y, +60); comp+656 = n[16] + n[14] (right = w + x, node +64); comp+660 = n[15] + n[17] (bottom = y + h, node +68).
- V: comp+664 = comp+336 (dword); comp+668 = comp+340 (dword): the component's authored width / height (I: +336/+340 are size).
- V: comp+684 = 0 afterwards, so it is cached once.
- V: callers GUITextBoardComponent_Update (0x14040E40E) and one more reference at 0x14040E3EA inside an exception-thunk-named region.

## State touched

- Calls: [GUITextBoard_FindTextNode](GUITextBoard_FindTextNode.md)

## Notes

Rect order is left, top, right, bottom in comp+648..+660 (I from the arithmetic).

## Open questions

? confirm that node +56..+68 are x, y, w, h (inferred from the sums).
