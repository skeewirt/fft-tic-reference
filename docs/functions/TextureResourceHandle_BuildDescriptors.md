# TextureResourceHandle_BuildDescriptors

- **Address:** `0x1403BAFE4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TextureResourceHandle_BuildDescriptors(TextureResourceHandle *h)`
- **Callers:** TextureResourceHandle_StreamStep
- **Callees:** TexHeader_TableSize, sub_14006D730, TextureLoadInfo_Free, allocator

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For a TEX file whose entries carry per-slice records: builds the array of 96-byte upload descriptors (one for the inline payload and one per record) and hands it to the handle's consumer callback (state 1005 = finish).

## Behavior

- V: info = qword h+112; images = info+216, header = info+224. size/offset = TexHeader_TableSize when info[4] == 4, else 0; extra = (low + high) total and n = u16 info+10 entries.
- V: allocates 96 * (n + (inline extra != 0)) bytes (heap via sub_14001A2EC / A2C4), zeroes them and stores at info+240. When the inline extra is non-zero, record 0 = {+8 = size, +16 / +20 / +32 = extra, +24 = &images + (info+248 - extra), +64 = 0, +72 = 0, +80 = 0}.
- V: when (info[20] & 0xF) == 3 and n != 0: for each 16-byte file record (at header + 32 * N + 8): record i: +72 = (a / 4 != b), +8 = dword (rec - 8), +16 = dword(rec - 4) >> 2, +20 = dword rec, +32 = byte(rec + 4) & 0x7F, and by the low 2 bits of dword(rec - 4): 1 -> +64 = 3, +80 = the image object, +24 = the image's inner pointer (or its image view when the global byte 142C81C7A is 0 and the kind is 1 or 4); 0 -> sub_14006D730(record, image, count).
- V: state h+84 = 1005; h+92 &= ~0x100; h+56 = 0; calls the consumer at h+48 (vtable +56)(consumer, records, count); returns 0x96080017 (no consumer) otherwise. When the header is version != 4 it frees the info and returns 0x96120005.

## State touched

- Calls: [TexHeader_TableSize](TexHeader_TableSize.md), [TextureLoadInfo_Free](TextureLoadInfo_Free.md)

## Referenced by

- Called by: [TextureResourceHandle_StreamStep](TextureResourceHandle_StreamStep.md)

## Notes

Name proposed (IDB: sub_1403BAFE4); medium confidence on the name: the record meaning (96-byte upload descriptors) is I from how the array is passed to the consumer.

## Open questions

? the consumer behind h+48 (vtable +48 = read request, +56 = descriptors ready) and the record fields at +8 / +16 / +20 / +24 / +32 / +64 / +72 / +80.
