# GUITextNode_AlignVertical

- **Address:** `0x1403DE4D0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUITextNode_AlignVertical(GUITextLayout *layout, GUITextLayoutState *st)`
- **Callers:** GUITextNode_Layout
- **Callees:** GUITextNode_FinishLine, sub_1403DEE64 (bounds)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ends the layout of a text node: flushes the pending line and shifts every line's y by the vertical alignment offset of the node box (node+256), then computes the text bounds.

## Behavior

- V (arguments): layout and st as in GUITextNode_FinishLine. Locals: H = (float)(int32 node+68), n = number of line records ((layout+48 - layout+40) / 24), content = last line.y + last line.height (line record +4 and +12 of the last record).
- V: if there are no lines yet or st+64 (pending glyphs) is non-zero it first calls GUITextNode_FinishLine.
- V (offset o by node+256, only when n > 0): 0 top = 0; 1 middle = (H - content) * 0.5; 2 bottom = H - content; 3 distribute: step s = (H - content) / (n - 1) when n > 1, o = 0, and a single line gets (H - content) * 0.5; any other value = 0.
- V: line i (i = 0..n-1) gets y += o + i * s (s is 0 except for mode 3).
- V: then returns sub_1403DEE64(layout, st), which stores the text bounds at layout+104..116 (left = int(floor(min x) + 0.5), top = int(floor(min y) + 0.5), right = int(ceil(max x) + 0.5), bottom = int(ceil(max y) + 0.5), all ints; zeroed when empty or right <= left or bottom <= top; the extent uses each glyph's line.x + rec.x, line.y + rec.y and size * rec.f as the height).

## State touched

- Calls: [GUITextNode_FinishLine](GUITextNode_FinishLine.md)

## Notes

The name is ours (the IDB has sub_1403DE4D0). The offset is negative when the text is taller than the box (size 23 in H 20: bottom -3, middle -1.5), as in the live read of the Job Tree digit node. sub_1403DEE64 is not yet named in the IDB (proposed GUITextNode_ComputeBounds).

## Open questions

? who reads the bounds at layout+104..116 was not traced (sub_1403DCE74, called by GUITextNode_Layout after layout, is probably the consumer). ? the bounds formula was read from the decompile only, not checked live.
