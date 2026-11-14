# NameSlotTable_Lookup

- **Address:** `0x140089280`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `unsigned __int16 __fastcall NameSlotTable_Lookup(NameSlotTable *table, const char *name)`
- **Callers:** UIRender_CreateBuffers, UIRender_LoadShaders, SDFFontRenderer_CreateResources, FrequentUtilRenderer_CreateResources, CEGL2_SHADER_vfunc_1, CEGL2_SHADER_vfunc_6, CEGL2_SHADER_vfunc_7, sub_1400423E0, sub_1400424DC, sub_140042788, sub_140042874, sub_140042A24, sub_140042B38, sub_140042C68, sub_140042D54, sub_14009C1F8, sub_1400CCCA8, sub_1400CEB4C, sub_1403A33F0, sub_1403A7AD8, sub_1403A7B3C, sub_1403AE954, sub_1403B7C34, sub_1403C55E4, sub_1403CAFD0, sub_1403CC5D4, sub_1403E5B84
- **Callees:** EnterCriticalSection, LeaveCriticalSection, strcmp, sub_140025C74 (string assign), std::_Tree_val::_Insert_node

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns a shader resource name (constant buffer, texture or sampler) into a small dense slot id, adding the name to the table the first time it is seen.

## Behavior

- V: takes the critical section at table+32 on entry and leaves it on every path (a 40-byte CRITICAL_SECTION occupying +32..+71; the entry array pointer follows at +72).
- V: hashes the NUL-terminated name with a 32-bit FNV hash: start 0x811C9DC5 and, for every byte, hash = (hash * 0x01000193) XOR byte. This multiplies before the xor, which is the FNV-1 order (FNV-1a xors first). The length is found by scanning for the terminator.
- V: the index is an MSVC red-black tree (std::map layout): head node pointer at table+16, node count at table+24, the head's parent link is the root. Node layout (40 bytes, allocated through the allocator object at table+8, virtual slot +16): left link +0, parent +8, right link +16, colour byte +24, nil byte +25, key = the 32-bit hash at +28, slot id (16 bits) at +32.
- V: the search finds the run of nodes whose key equals the hash (the usual lower-bound and upper-bound walks) and visits the run in order, so different names that share a hash get separate nodes.
- V: for each node of the run the candidate name is read from the entry array: entry = (qword at table+72) + 40 * slot. An entry is a 40-byte allocator-aware string object: allocator pointer at +0, inline 16-byte buffer or heap pointer at +8, length at +24, capacity at +32 (the characters are inline when the capacity is below 16). The name is compared with strcmp; on a match the slot id of that node is returned.
- V: when no node matches: slot = the 16-bit count at table+80. When the dword capacity at table+84 is greater than the slot, the name is copied into entry[slot] (sub_140025C74, the string assign), a node {hash, slot} is allocated and linked at the position found by descending from the root (hash >= key goes right, otherwise left; the tree size is checked against 0xFFFFFFFF first), std::_Tree_val::_Insert_node links and rebalances it, the count is incremented and the new slot is returned.
- V: when the table is full (capacity not greater than the count) nothing is inserted and 0xFFFF (-1 as a 16-bit value) is returned.
- V: slot ids are dense and handed out in order of first use (0, 1, 2, ...); the count is never decremented here, so an id never changes. The same name always gives the same id, so every shader module that mentions g_Sampler shares one slot.
- V: there are three tables in the device globals qword_140C696A8: constant buffers at +5056, textures at +5064, samplers at +5072 (the callers load the table pointer from these fields just before the call). UIRender_CreateBuffers resolves cUIRenderRemap, cUIRender and cSDF from the first, tTexture0 from the second, g_Sampler and g_Sampler_tMaskBuffer from the third. 171 call sites were scanned: 168 load the table pointer from one of the three fields right before the call (the other three, in sub_1403A33F0, were not matched).
- V (UIRender_CreateBuffers, UICommandRing_Flush, UIRender_ApplyDrawState): the slot id is the index into the render context binding arrays: constant-buffer handles at context+328 + 8 * slot, texture handles at +1608 + 8 * slot, sampler words at +5704 + 4 * slot (RenderContext_ResetFrame clears 160, 512 and 64 entries of these arrays).
- V (live read 2026-10-30, the sampler table at qword_140C696A8 + 5072, 31 entries): 0..11 s_none1..s_none12, 12 ccc_ppn_sampler, 13 ccc_lln_sampler, 14 g_Sampler, 15 g_Sampler_tMaskBuffer, 16 ccc_lln_sampler_tMaskBuffer, 17 www_lln_sampler, 18 cwc_lln_sampler, 19 PointSampler, 20 LinearSampler, 21 LinearSampler_esgeTex, 22 LinearSampler_areaTex, 23 LinearSampler_searchTex, 24 LinearSampler_blendTex, 25 www_lll_sampler, 26 www_ppn_sampler, 27..30 sSampler0..sSampler3.
- I: the names follow a code: three address letters (c clamp, w wrap) and three filter letters (l linear, p point, n none; min, mag, mip). For ccc_lln that matches the word 0x26A that the Job Tree technique holds for slots 13 and 16 (clamp on all axes, min / mag linear, mip point; see GUILayer_BlurShadowPass and Sampler_DescFromWord). Basis: the names and that decoded word.
- I: the first twelve entries (s_none1..s_none12) look like placeholder names for unused sampler indices. Basis: the names only.

## State touched

- Reads: [NameSlotTable.tree](../structs/NameSlotTable.md#tree), [NameSlotTable.count](../structs/NameSlotTable.md#count), [NameSlotTable.capacity](../structs/NameSlotTable.md#capacity), [NameSlotTable.lock](../structs/NameSlotTable.md#lock) entered and left, [NameSlotTable.entries](../structs/NameSlotTable.md#entries)
- Writes: [NameSlotTable.entries](../structs/NameSlotTable.md#entries), [NameSlotTable.tree](../structs/NameSlotTable.md#tree), [NameSlotTable.count](../structs/NameSlotTable.md#count)

## Referenced by

- Called by: [UIRender_CreateBuffers](UIRender_CreateBuffers.md)
- Resolves registries: [SamplerSlots](../registries/SamplerSlots.md)

## Notes

The name is ours (IDB: sub_140089280 until applied). The sampler slot ids index the +5704 words of every render context: slot 14 (g_Sampler) is the one UIRender_ApplyDrawState writes with the UI draw's sampler word and the one the Job Tree shadow pixel shader reads (GUILayer_BlurShadowPass); slot 15 (g_Sampler_tMaskBuffer) is written with the same word. The 31 sampler names were read live from the running game and were not re-read here.

## Open questions

? the capacity stored at table+84 for each of the three tables (the context arrays hold 160 / 512 / 64 entries, probably the same limit, I). ? the contents of the constant-buffer and texture tables (only the sampler table was read live). ? where the entry strings' allocator pointers (entry+0) are set (not in this function).
