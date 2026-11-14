# GUIFontSlotGroup_OnPartTableLoaded

- **Address:** `0x1403F40AC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIFontSlotGroup_OnPartTableLoaded(GUIFontSlotGroup *g)`
- **Callers:** GUIFontSlotGroup_Poll (when g+84 != 0 and its slot is loaded)
- **Callees:** sub_1403DA594, sub_1403DA918, sub_1403DA30C, allocator vtable +16 / +24 (g+16), GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Called by GUIFontSlotGroup_Poll once the group's part-table slot (g+84, the .utexpt file) is loaded: copies the table's part rectangles into the group's vector, requests the texture the table names and posts event 42.

## Behavior

- V: record = sub_1403DA594(g_GUIFontSlots, g+84). Only when the dword at record+80 is exactly 1 (else g+88 = g+89 = 1 and g+90 = 1: done, nothing loaded).
- V: blob = *(record+56). blob+0 = offset of the texture path string (relative to blob), blob+4 = offset of the entry array, blob+8 = entry count n. The part vector (g+24..+40) is cleared (end = begin) and grown to n * 16 bytes when needed.
- V: for each of the n entries (20 bytes each, array at blob + blob[1]): the four dwords at entry +4..+19 (skipping the first dword) are appended as one 16-byte vector element. So part i of the group = the four ints of the .utexpt record i (the rectangle).
- V: slot = sub_1403DA918(g_GUIFontSlots, blob + blob[0], ...) (request the texture by path, returns a slot id with type byte 2 and a 1-based index); the previous texture slot id g+80 is released with sub_1403DA30C when non-zero; g+80 = the returned slot id; g+89 = 1; when the returned id is 0 g+88 = 1 (nothing to wait for).
- V: event {42, 0, 0, 0} with ev+16 = *g is posted to the owners at g+96.

## State touched

- Calls: [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Referenced by

- Reads file formats: [TexturePartFile](../formats/TexturePartFile.md)

## Notes

The name is ours (IDB: sub_1403F40AC). This is the place where the atlas rectangles of a .utexpt (e.g. ui_job_tree_uitx.utexpt) enter the runtime: the vector built here is what UIImage part lookups index (part index = part - 1 per the UIB notes; the whole-texture rectangle then overwrites element 0 in GUIFontSlotGroup_OnTextureLoaded, which is I). Entry layout of the file (+0 dword not copied, +4..+19 four ints) is V from the copy loop; which of the four is x / y / w / h is not read here.

## Open questions

? the meaning of the skipped first dword of each 20-byte entry. ? x / y / w / h order of the four ints (the studio reads them as [x, y, w, h] from the file).
