# UIPartRef_GetResource

- **Address:** `0x1403DCA6C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void *UIPartRef_GetResource(UIPartRef *ref)`
- **Callers:** GUILayer_BuildRecord, UIDraw_SetStateFromSlot
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the resource record of a part reference: the first element of its resource list, or a table entry by id, or the fallback pointer.

## Behavior

- V (disassembly 1403DCA9C..1403DCACB, checked 2026-10-28): with no resource pointer and ref+33 set, the table slot (qword_143CDA098+37936 + 16 * (id + 541)) is returned only when ref+28 < 1, i.e. id 0; any other id returns 0. The decompile is right; the first impression of an inverted test was wrong.
- V: ref[0] set: the first element of the small vector at record+112 (inline element when (u16 +120 & 0xFFF8) == 8 and u32 +124 == 0, else **(record+112)).
- V: ref[0] null and byte ref+33 != 0: when dword ref+28 = 0 returns the 8-byte entry at (*(g_GUICore-ish ptr qword_143CDA098 + 37936)) + 16 * (ref+28 + 541), otherwise 0. Byte ref+33 = 0: returns ref[2].

## State touched

- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [GUILayer_BuildRecord](GUILayer_BuildRecord.md)

## Notes

The name is ours (IDB: sub_1403DCA6C). 6004 hits per 4 s. The decompile tests ref+28 = 0 before indexing with ref+28 + 541, so the table path is only taken for id 0 (slot 541): I: a built-in default texture. This looks odd and was transcribed literally.

## Open questions

? Whether the 'id = 0 only' test is inverted in the decompile (read the disassembly before relying on the table path).
