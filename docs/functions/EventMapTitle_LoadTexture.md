# EventMapTitle_LoadTexture

- **Address:** `0x140302B68`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventMapTitle_LoadTexture(void)`
- **Callers:** EventScript_Run (the 0x91 handler, call at 0x14023DA81, made before SceneTask_Start); sub_14020E578 (call at 0x14020E7E7).
- **Callees:** SceneVar_Read, `sub_1402202C8`, `sub_1400D5A50`, `sub_140010F50`, `sub_1403D2004`, `sub_1403D21F0`, `sub_1403D21C8`, `sub_14041FB00`, `sub_1403D2358`, `sub_14025FA60`, `sub_1402203AC`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the map-title texture file chosen by scene variable 51 (maptitle_%03d.tex) into a 10,240-byte buffer, unless the enhanced-build test says it is not needed; the 0x91 handler calls it before starting the sweep task.

## Behavior

- V: reads scene variable 51 with SceneVar_Read and subtracts 1. The result is the index.
- V: the index is kept when it is 119 or less. The comparison is signed, so a scene value of 0 gives an index of -1, which is kept and printed as a negative number. Any larger value gives index 0.
- V: when dword_1407D453C is not zero, the index is stored in DWORD1 of xmmword_142E7FCE0. The load is skipped when that flag is not zero and the float at dword_142C81554 is 2.0 or more. When the flag is zero the load always happens.
- V: allocates a 10,240-byte buffer with sub_1402202C8.
- V: formats the file name fftpack/tex/maptitle/maptitle_%03d.tex with the index into a 260-byte local buffer (through sub_1400D5A50).
- V: allocates a zeroed 32-byte loader object with sub_140010F50 and opens the file name with sub_1403D2004 (the loader is null when the allocation fails).
- V: calls sub_1403D21F0 on the loader. When it returns 1, the loader is released with sub_1403D21C8 and sub_14041FB00 (size 32) and nothing else is done; the 10,240-byte buffer is not freed on this path.
- V: otherwise it copies the file data into the buffer with sub_1403D2358 (source offset 0, length taken from the dword at +64 of the loader's data block, or 0 when there is no block), releases the loader with sub_1403D21C8 and sub_14041FB00, and, when DWORD2 of xmmword_142FF9E24 is not 1, calls sub_14025FA60 twice: once with the string table unk_1408EBA28 when the language dword at +8 of g_LanguageInfo is non-zero or g_LanguageInfo is null (unk_1408EB938 otherwise) and the buffer, and once with qword_1408EBB18 and byte_1408F25D8.
- V: then frees the buffer with sub_1402203AC. This happens on the copy path only.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Observed behaviours: [PlaceTextOfAMapIdComesFromTheMapRowAndTheTownRow](../behaviors/PlaceTextOfAMapIdComesFromTheMapRowAndTheTownRow.md)

## Notes

The routine takes no meaningful arguments; the 0x91 handler calls it with whatever the registers hold.

## Open questions

What sub_1403D2004, sub_1403D21F0, sub_14041FB00 and sub_14025FA60 do with the data (only the calls here were read); what xmmword_142E7FCE0 is read for; why the buffer is not freed when the loader reports 1; whether a scene value of 0 (index -1) is reached in practice.
