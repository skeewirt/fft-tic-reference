# GUITextBoardComponent_Update

- **Address:** `0x14040E3F0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUITextBoardComponent_Update(GUIComponent *comp, float time, char force)`
- **Callers:** vtable entry (sub_140721F88 and data xref 0x143D42D90)
- **Callees:** sub_14040E59C, sub_14040AAC0, sub_1403F1234, sub_1403EF6B4, GUINode_SetPosition, GUIComponent_Update

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Update override of a text-board component class: fits the board's text node (kind 3 part named by qword_143CDA2A0+5000) to the text's extent, sizes the component to text plus margins (rounded up to even), and aligns the board inside the rectangle it was given, then runs the base update.

## Behavior

- V: sub_14040E59C(comp) caches once (comp+684 flag) the text node's authored box: +648 = node x (+56), +652 = y (+60), +656 = x + w, +660 = y + h, +664 / +668 = the component's authored width / height (+336 / +340). The text node T is sub_14040AAC0 = GUINode_FindPartByName(comp+272, name) with kind 3 required; none = skip to the base update.
- V: when comp+672 (a text id) is nonzero and differs from T+248, T+248 = it and T+316 (text dirty) = 1; when T+316 is set the text is re-laid-out at once (sub_1403F1234).
- V (size): textW = T+432 - T+424, textH = T+436 - T+428 (the text's measured extent, int); w = max(textW, authored box width +656 - +648), h = max(textH, +660 - +652). Text node size = ((w + 1) & ~1, (h + 1) & ~1) via sub_1403EF6B4. Component root (comp+272) size = ((w + left + (authW - boxRight) + 1) & ~1, (h + top + (authH - boxBottom) + 1) & ~1) with left = +648, top = +652, boxRight = +656, boxBottom = +660, authW/authH = +664/+668. So every size is the content size plus the authored margins, rounded UP to an even integer.
- V (alignment inside the allocated rectangle comp+528 x comp+532, which GUIComponent_UpdateNodeTree sets from the reference node's size): horizontal mode comp+676: 0 or other = 0, 1 or 3 = (comp+528 - compW) / 2 (C integer division, truncation toward zero), 2 = comp+528 - compW; vertical comp+680 likewise with comp+532 and compH. The component root's position is set to that (GUINode_SetPosition(comp+272, x, y)).
- V: finally tail-calls GUIComponent_Update(comp, time, force).

## State touched

- Calls: [GUINode_SetPosition](GUINode_SetPosition.md), [GUIComponent_Update](GUIComponent_Update.md)

## Notes

The name is ours (IDB: sub_14040E3F0). 8036 hits per 4 s. This is where a Job Tree text board's text node gets its size and the board its alignment offset; text pen y still follows GUITextNode_Layout / GUITextNode_Draw inside that node size (H = node+68 here is the even-rounded content height, so for a vertical-bottom node the 'H - size' term uses this rounded H, not the file H).

## Open questions

Which text id / name the +5000 global is (likely 'Title', not read); whether the Job Tree digit boxes are instances of this class (the 8036 count suggests the text boards of the tab / row labels).
