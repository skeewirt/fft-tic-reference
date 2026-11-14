# SDFFontRenderer_CloseBatch

- **Address:** `0x1403A8FBC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 SDFFontRenderer_CloseBatch(SDFFontRenderer *r, int newKey, GUINodeRecord *newNode)`
- **Callers:** SDFFontRenderer_Flush (0x1403A9B6D with key 0 / node 0 to flush the last batch), GUITextNode_Draw (0x1403EA1E8, when the draw sequence number changes; at most 0xC0 batches per node record list)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Closes the glyph batch being built (all quads emitted since the last close) and starts a new one: stores its quad range, bounding box, node record and sort key in the batch table.

## Behavior

- V: only when r+32 (the device) is set. old key = r+7952, old node = r+240; r+7952 = newKey, r+240 = newNode, and newNode+76 = 1 (marks the node record used).
- V: batch slot k = r+7944 (count); the 40-byte record at r+248+40*k: +0..15 = the 16-byte bounding box r+7928..7940 (minX, minY, maxX, maxY, built by SDFFontRenderer_AccumulateBounds), +16 = first quad (old r+7948), +20 = quad count (r+9520 - old r+7948), +24 = old node, +32 = old key. r+7948 = r+9520 (the running quad count); r+7928..7943 are zeroed for the next batch.
- V: when the closed batch has quads (count != 0) it appends the sort entry (key = old key at r+7956+8*k, index k at r+7960+8*k) and increments r+7944. Empty batches are not listed.

## Notes

The name is ours (IDB: sub_1403A8FBC). In SDFFontRenderer_Flush the bounding box floats are divided by the renderer's +9544 / +9548 before they are written to the per-batch GPU buffer. The key is the GUI layer's draw sequence number + 1 (a1+606596 + 1 in GUITextNode_Draw).

## Open questions

? the use of the bounding box on the GPU side (probably a scissor / culling rectangle; not read).
