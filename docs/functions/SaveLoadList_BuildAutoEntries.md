# SaveLoadList_BuildAutoEntries

- **Address:** `0x1401859A8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void *SaveLoadList_BuildAutoEntries(int64_t addon, int64_t descriptors)`
- **Callers:** sub_1401838F0 (0x14018393E, agent state 4 phase 0)
- **Callees:** SaveLoadList_ClearAutoEntries (0x1401859CA), Mem_Alloc (0x140185A26), memset (0x140185A42), std::vector _Xlen (0x140185CA9, length error path)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds vector B, the auto-row list of the save/load add-on, from the agent's five 264-byte resume descriptors. Each accepted descriptor becomes one 240-byte row carrying the summary fields and six 32-byte preview records.

## Behavior

- V: begins by clearing vector B through `SaveLoadList_ClearAutoEntries`, so every call rebuilds the auto rows from scratch.
- V: walks exactly five descriptors, 264 bytes apart; they are the five resume summaries the agent copied into its own block at +256.
- V: a descriptor is accepted only when its first dword is the FFTI marker, its +4 dword is 122 and its +12 dword is below 2; a rejected descriptor produces no row.
- V: an accepted descriptor allocates a 240-byte row from the UI allocator and zero-fills it.
- V: the row's +0 dword is the descriptor's ordinal 0..4. The summary fields come from descriptor +38 (row +8), +42 (row +4), +45 (row +16), +64 (row +12) and the 64-bit value at +56 (row +32).
- V: row +20 receives descriptor +44 when descriptor +46 is nonzero and descriptor +41 otherwise. `SaveLoadList_FillItem` reads +20 as the location id and +234 as the flag that selects the world-map place lookup instead of the UITable 0x34 row.
- V: rows +24 and +28 stay zero.
- V: the six 32-byte preview records at descriptor +68, +100, +132, +164, +196 and +228 are copied into the row at +40..+231; each copied record's first dword is then replaced with -1.
- V: the row flags are: +232 = 0, +233 = 1 (auto row), +234 = descriptor +46, +235 = 1 only for descriptor ordinal 1 when +46 is nonzero, +236 = descriptor +43 nonzero, +237 = descriptor +47 is 1, and +238/+239 = 0.
- V: the row pointer is appended to vector B (+480 begin, +488 end, +496 capacity); a full vector grows through the allocator at +472 and copies the existing eight-byte pointers.
- V: there is no sort here; vector B keeps the descriptor order. The sort at the end of `SaveLoadList_BuildEntries` runs on vector A after any copy from vector B.
- I: for an auto row the +0 number is a resume-descriptor ordinal rather than a cache slot (rests on the selection handler forwarding row +233 with the row number, and on state 5 choosing the resume loader when that auto flag is set).
- ?: what +235 marks, and what descriptor +41 and +44 identify beyond their use as location ids.

## State touched

- Calls: [SaveLoadList_ClearAutoEntries](SaveLoadList_ClearAutoEntries.md), [Mem_Alloc](Mem_Alloc.md)
- Writes: [UIAddonFFTOSaveLoad](../structs/UIAddonFFTOSaveLoad.md)

## Referenced by

- Called by: [UISaveLoad_StateEnter](UISaveLoad_StateEnter.md)

## Notes

Whole body read (775 bytes). The accept test, the field stores, the six-record copy and the vector growth were checked. The meanings of row +4/+8/+12/+16/+20/+32 come from `SaveLoadList_FillItem`. The descriptor array itself is filled by agent state 3 (`sub_14018373C`).

## Open questions

? what row +235 means; ? what descriptor +41 and +44 identify beyond serving as location ids; ? whether the five descriptor ordinals have fixed roles (save slot, checkpoint, ...).
