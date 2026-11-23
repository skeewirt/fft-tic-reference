# SaveLoadList_ClearAutoEntries

- **Address:** `0x140185CB0`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveLoadList_ClearAutoEntries(int64_t addon)`
- **Callers:** SaveLoadList_BuildAutoEntries (0x1401859CA), sub_140184DB0 (0x140184DDA)
- **Callees:** sub_1401862BC (0x140185CE7)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Releases every row of vector B, the auto-row list, and resets the vector's end pointer. The pointer array itself stays allocated.

## Behavior

- V: counts vector B in eight-byte pointer slots as (end - begin) / 8.
- V: calls `sub_1401862BC` once for each row pointer.
- V: `sub_1401862BC` releases one 240-byte row: for each of its six preview records it calls `sub_1400EDC68` with `g_CharaRenderMgr` and the record, erases the record's node from the add-on map at +544, and then frees the row.
- I: `sub_1400EDC68` is the release counterpart of `CharaRender_RegisterSlot` (rests on the two calls acting on the same preview record in `SaveLoadList_FillItem` and here).
- V: after the loop it stores +480 into +488, so the vector becomes empty. The storage at +480 and the capacity at +496 are untouched.
- V: called by `SaveLoadList_BuildAutoEntries` before a rebuild, and by the add-on destructor `sub_140184DB0` (0x140184DDA) before the pointer array is freed.
- V: the destructor releases vector A's rows through `sub_140186240`, then vector B's rows through this function, then the preview map and the helper subobjects, and only then frees vector C's storage, vector B's storage and vector A's storage, in that order.
- I: the vector owns only its pointer array; each row is a separate allocation owned by the list (rests on the per-row free here and on the separate array release in the destructor).
- ?: what render handle the map stores for each preview record.

## State touched

- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [UIAddonFFTOSaveLoad](../structs/UIAddonFFTOSaveLoad.md)
- Writes: [UIAddonFFTOSaveLoad](../structs/UIAddonFFTOSaveLoad.md)

## Referenced by

- Called by: [SaveLoadList_BuildAutoEntries](SaveLoadList_BuildAutoEntries.md)

## Notes

Whole body read (107 bytes). The per-row release, the map erase and the end-pointer reset were checked in this function and in the destructor. Vector C holds the same row pointers as vector A's filtered view, so it is not released per row.

## Open questions

? what the render handle stored per preview record refers to.
