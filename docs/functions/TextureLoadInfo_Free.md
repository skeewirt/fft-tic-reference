# TextureLoadInfo_Free

- **Address:** `0x1403BAB84`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void TextureLoadInfo_Free(TextureLoadInfo **pp)`
- **Callers:** TextureResourceHandle_FinishLoad, TextureResourceHandle_BuildDescriptors, TextureResourceHandle_StreamStep, TextureResourceHandle_Unload
- **Callees:** sub_14003ABD0, sub_140011804, sub_140088674

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Releases a TextureLoadInfo: releases its images, returns its ids to the id allocator, frees the arrays and the record, and clears *pp.

## Behavior

- V: images: for i < byte info+8 (the entry count): sub_14003ABD0(info+216 [i]) (release) and the slot set to 0; then the image array is freed (sub_140011804) unless it is the inline slot at +208.
- V: the header buffer (+224) is freed unless it is the inline +40. The u16 id array (+232, count u16 +276): each id != 0xFFFF is returned with sub_140088674(qword_140C696A8, id) and reset; the array freed. The single id u16 +278 likewise. The descriptor array +240 is freed. Finally the record itself and *pp = 0.

## State touched

- Reads: [g_RenderDevice](../globals/g_RenderDevice.md)

## Referenced by

- Called by: [TextureResourceHandle_BuildDescriptors](TextureResourceHandle_BuildDescriptors.md), [TextureResourceHandle_FinishLoad](TextureResourceHandle_FinishLoad.md), [TextureResourceHandle_StreamStep](TextureResourceHandle_StreamStep.md), [TextureResourceHandle_Unload](TextureResourceHandle_Unload.md)

## Notes

Name proposed (IDB: sub_1403BAB84).

## Open questions

? sub_140088674 / qword_140C696A8 (an id allocator for GPU image handles; see TextureResourceHandle_RegisterImages for the other side).
