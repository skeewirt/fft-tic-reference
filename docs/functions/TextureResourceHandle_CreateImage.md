# TextureResourceHandle_CreateImage

- **Address:** `0x1403BBC64`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TextureResourceHandle_CreateImage(TextureResourceHandle *h, unsigned int *entry)`
- **Callers:** TextureResourceHandle_StreamStep (loop over the entries)
- **Callees:** sub_1400873D8, sub_14008757C, sub_1400876A8, sub_140087834

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the GPU image for one 32-byte TEX header entry by its type (low 2 bits of dword 0): 0 -> sub_1400873D8, 1 -> sub_14008757C, 2 -> sub_1400876A8, 3 -> sub_140087834, each building a faith::Graphics::Texture plus ShaderResourceView.

## Behavior

- V: dword 0 = e. Common: v4 = byte (info+6) (the flag byte passed on as the usage argument), depth / array fields from the entry words (u16 +8, +10, +12, +14), dword +4, and a 'srgb-like' byte = ((e >> 3) & 1) * 2 or 4.
- V: type 0 -> sub_1400873D8: view dimension 2 (or 3 when the array count u16 > 1) written as the byte before creation; i.e. D3D11_SRV_DIMENSION values TEXTURE1D (2) / TEXTURE1DARRAY (3) - I.
- V: type 1 -> sub_14008757C (view 4 / 5 = TEXTURE2D / 2DARRAY, I). When info+20 has bit 0x10 set it first creates with a flag byte 4 (a second texture), returns that result when non-zero, then creates the normal one.
- V: type 2 -> sub_1400876A8 (view 8 = TEXTURE3D, I). Type 3 -> sub_140087834 (view 9 / 10 = TEXTURECUBE / CUBEARRAY, I). Any other value returns 0.

## Referenced by

- Called by: [TextureResourceHandle_StreamStep](TextureResourceHandle_StreamStep.md)

## Notes

Name proposed (IDB: sub_1403BBC64). The dimension mapping to 1D / 2D / 3D / cube rests on the numeric view-type bytes in the four create functions (2/3, 4/5, 8, 9/10) matching the D3D11 SRV enum, hence I.

## Open questions

? the field meaning of the 32-byte entry beyond type (low 2 bits), the format bits at (dword >> 3) and the sizes (u16 +4 .. +14).
