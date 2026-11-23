# SaveLoadList_BuildEntries

- **Address:** `0x140185D1C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveLoadList_BuildEntries(int64_t addon)`
- **Callers:** SaveLoadList_Refresh (0x140187BF0)
- **Callees:** sub_140186240, sub_140186390, CardSlot_IsValid, sub_1401CCE78, Mem_Alloc, memset, sub_140031D7C (vector grow), std::vector _Xlen (error path)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds vector A, the row list the screen shows for the current tab: the tab-specific extra rows, one 240-byte row per selected cache slot, then a sort of the pointer array.

## Behavior

- V: first releases the previous rows through `sub_140186240`: each vector A row is freed through `sub_1401862BC`, the vector A end pointer is reset, and vector C is emptied by setting its end pointer to its begin pointer.
- V: tab 0 first creates one blank row through `sub_140186390`, sets its +232 byte and appends it to vector A.
- I: that blank row is the save list's "new save" row; the selection handler treats a row with +232 set as "save into the first free cache slot" (rests on the handler's `CardSlot_IsValid` scan and on its save event).
- V: tab 1 copies every vector B row into a new 240-byte row (a complete 240-byte copy, six preview records included) and appends it to vector A.
- V: tab 2 adds neither the blank row nor a copy of vector B.
- V: all three tabs then scan the 50 cache slots. A slot is appended when `CardSlot_IsValid` returns 0 (I: 0 means valid, the `SC` magic test; the callee is not shown in this body); on tab 2 the slot must also have a nonzero byte at +0x119 and a situation at +0x11A of 0 or 5.
- V: a manual row receives: +0 slot, +4 byte +0x118 (language variant), +8 byte +0x113 (level), +12 dword +0x120 (progress), +16 byte +0x11B (play mode), +20 byte +0x116 (location), +24 byte +0x11A (situation), +28 word +0x11C, +32 qword +0x44 (timestamp), +236 byte +0x119 nonzero (clear mark) and +237 byte +0x11E == 1 (New Game mark). Its +232 and +233 bytes stay zero.
- V: +28 is read by `SaveLoadList_FillItem` only when the situation at +24 is 1, where it selects an NXD 156 row that leads to an NXD 230 place name.
- V: the row reserves six 32-byte records at +40..+231. All six are initialized with -1 in their first dword. The manual builder copies four records from slot +0x124..+0x1A3; the tab-1 copy and the auto builder fill all six.
- V: the three vector field triples are: A at +440 (allocator), +448 (begin), +456 (end), +464 (capacity); B at +472, +480, +488, +496; C at +504, +512, +520, +528.
- V: A holds every row built for the tab, B holds the auto rows and C holds the visible rows after the +436 filter (the list the item callback and the cursor read).
- V: ends with `sub_1401CCE78` (0x14018621B), a sort over vector A.
- V: no job byte or job text is read (the list shows no class).

## State touched

- Calls: [CardSlot_IsValid](CardSlot_IsValid.md), [Mem_Alloc](Mem_Alloc.md)

## Referenced by

- Appears in flows: [SaveLoadScreenFlow](../flows/SaveLoadScreenFlow.md)
- Called by: [SaveLoadList_Refresh](SaveLoadList_Refresh.md)

## Notes

Whole body was read (1314 bytes). Earlier versions of this reference said four 32-byte preview records at +40..+167 and a single "+232 auto-slot flag"; the code shows six records at +40..+231 (four is only the manual builder's copy count) and two separate markers: +232 is the tab-0 blank row and +233 is the auto row.

## Open questions

- ? the on-screen names of tabs 0, 1 and 2 (the code only has indices and mode bits).
- ? whether the tab-2 situations 0 and 5 are world-map and cleared saves.
- ? what the +235 byte marks on auto rows.
