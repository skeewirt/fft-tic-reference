# TexHeader_TableSize

- **Address:** `0x1403BA9B0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `unsigned __int64 TexHeader_TableSize(const unsigned char *hdr, const unsigned char *hdr8)`
- **Callers:** TextureResourceHandle_BuildDescriptors (sub_1403BAFE4), TextureResourceHandle_StreamStep (sub_1403BB25C)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Size of the sub-image table of a TEX file header: returns (low dword = bytes of the table after the 40-byte header start, high dword = 40), or 0 for a header that is not version 4.

## Behavior

- V: returns 0 when hdr[4] != 4 (version). flags = hdr[5]. size = 32 * hdr8[0] (hdr8 = hdr + 8; hdr8[0] = number of 32-byte entries N).
- V: when flags bit 0x01 is set and (hdr8[12] & 0xF) == 3: size += 16 * u16(hdr8 + 2). When bit 0x01 is clear and bit 0x10 is set and (hdr8[12] & 0xF) != 0: size += 24 * u16(hdr8 + 2). High dword of the return = 40 (the header start offset of the table).

## Referenced by

- Called by: [TextureResourceHandle_BuildDescriptors](TextureResourceHandle_BuildDescriptors.md), [TextureResourceHandle_StreamStep](TextureResourceHandle_StreamStep.md)

## Notes

Name proposed (IDB: sub_1403BA9B0). The TEX header layout (I, from this and the loader): +0 'TEX ' (0x20584554), +4 version 4, +5 flags, +6 byte (copied as an argument to the image create call), +8.. a first 32-byte entry whose first byte is the entry count.

## Open questions

? the semantics of the flag bits 0x01 / 0x10 and of the 16 / 24-byte extension records (I: per-array-slice or per-mip records).
