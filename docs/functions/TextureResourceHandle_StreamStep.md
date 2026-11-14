# TextureResourceHandle_StreamStep

- **Address:** `0x1403BB25C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TextureResourceHandle_StreamStep(TextureResourceHandle *h, __int64 arg)`
- **Callers:** vtable only: TextureResourceHandle_1407203C8 slot 17
- **Callees:** TextureLoadInfo_Alloc, TextureLoadInfo_Free, TexHeader_TableSize, TexHeader_ValidateCopy, TextureResourceHandle_CreateImage, TextureResourceHandle_BuildDescriptors, TextureResourceHandle_FinishLoad, sub_14003E638, sub_14003E674, sub_14003E6D0, sub_14003E5D8, sub_14003E6A8, sub_14003E604, sub_14003E7C4, sub_140069C28, consumer callback h+48

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 17 of TextureResourceHandle: the incremental TEX file loader. Each call consumes the bytes the previous read produced and requests the next read: header, header table, then the pixel data of every image, mip and slice, until the images are complete.

## Behavior

- V: state = atomic dword h+84. States: 1000 allocate the TextureLoadInfo (TextureLoadInfo_Alloc, failure 0x96120001), state = 1001, request min(h+64, info+252) bytes of header into the info header buffer (info+224); h+92 |= 0x100; h+56 = the buffer; the read request is the consumer callback at h+48 (vtable +48); no consumer returns 0x96080017.
- V: 1001 (first chunk): requires >= 8 bytes with dword 0x20584554 ('TEX '), byte +4 == 4, byte +5 bit 0x01, >= 0x28 bytes and a non-zero entry count at +8 (else TextureLoadInfo_Free and 0x96120002). Copies the 8-byte magic block to info+0 and the first 32-byte entry to info+8. When the count > 1 or info+12 / +16 are non-zero it sizes the payload (info+248 = info+12 + info+16 + ((2N + 7) & 0x3F8) + 8N), allocates the image array (info+216, 8N bytes, filled with the 0xFFFF id area) and, when info+16 != 0, records the payload tail in h+96 / h+104. Then uses TexHeader_TableSize to find how much more header there is; when the first chunk already holds it, validates with TexHeader_ValidateCopy, otherwise allocates a larger header buffer (info+252), copies what it has, sets state 1002 and requests the rest.
- V: 1002 (rest of the header, or after 1001 completes): TexHeader_ValidateCopy again (a non-zero result gives 0x96120002); h+120 bits 0 / 1 / 2 = (dword header >> 2 / >> 4 / >> 5) & 1; h+128 = header dword +24; then for each of the N entries calls TextureResourceHandle_CreateImage (failure 0x96120005, info freed); finally, when (info[20] & 0xF) != 0 it calls TextureResourceHandle_BuildDescriptors, else (when the table has an inline payload) goes to state 1004 with info+256 = the first entry's size and requests it, else straight to the pixel-data setup.
- V: 1004 / pixel data setup: sub-resource buffer = sub_14003E6D0(image, mip + slice * mips); null frees the info and returns 0x96120006. Size = ((w >> mip) * (h >> mip) * bytes-per-pixel (sub_140069C28), 4x4 block compressed formats use (w + 3) >> 2) rounded up to 8; state = 1003, the read is requested with h+56 = the buffer; info+256 += size.
- V: 1003 (one image slice's data arrived): uploads it (sub_14003E7C4 with the slice index = mip + slice * mipCount), then advances the counters in order: info+268 (mip) up to the mip count (sub_14003E638), info+272 (slice) up to the slice count (sub_14003E674), info+264 (image) up to the entry count; between images info+256 = the next entry's size; when everything is done calls TextureResourceHandle_FinishLoad. Otherwise continues at the pixel data setup.
- V: 1005 calls TextureResourceHandle_FinishLoad; any other state returns 0.

## State touched

- Calls: [TextureLoadInfo_Alloc](TextureLoadInfo_Alloc.md), [TextureLoadInfo_Free](TextureLoadInfo_Free.md), [TexHeader_TableSize](TexHeader_TableSize.md), [TexHeader_ValidateCopy](TexHeader_ValidateCopy.md), [TextureResourceHandle_CreateImage](TextureResourceHandle_CreateImage.md), [TextureResourceHandle_BuildDescriptors](TextureResourceHandle_BuildDescriptors.md), [TextureResourceHandle_FinishLoad](TextureResourceHandle_FinishLoad.md)

## Notes

Name proposed (IDB: sub_1403BB25C). Read from the decompile only: the file layout is this loader's, the registers lost in Hex-Rays (the image width, height and format of the size computation: sub_14003E5D8 / E6A8 / E604) were not recovered, hence the exact size formula is I. Error codes: 0x96120001 out of memory, 0x96120002 bad header, 0x96120005 image create failed, 0x96120006 sub-resource missing, 0x96080017 no consumer.

## Open questions

? the file format fields beyond those listed (+6 byte passed on, the dword at header +24 stored in h+128, flags bits). ? the consumer interface at h+48. ? the sub_14003Exxx image accessors by name.
