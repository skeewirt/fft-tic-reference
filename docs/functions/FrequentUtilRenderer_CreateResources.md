# FrequentUtilRenderer_CreateResources

- **Address:** `0x1403AAA84`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char sub_1403AAA84(__int64 r)  // r = FrequentUtilRenderer*`
- **Callers:** sub_1403A143C (0x1403A1774), data 0x143D401BC
- **Callees:** sub_1403A7AD8, sub_140091124, sub_140037CA4, sub_1403A7B08, sub_140086F64, sub_140086D28, sub_140087318, sub_1400879F4, sub_140086E9C, sub_14003E120 / sub_14003E228, sub_140089280, sub_1403AB2CC, sub_14003AD5C, sub_14003ABD0, sub_140095E88

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

FrequentUtilRenderer set-up: loads shader/FrequentUtil.tec, creates six small constant buffers, loads 16 blue-noise textures, builds a 36-index buffer, looks up 18 texture slots and 10 constant-buffer slots, then creates 16 + 16 small buffers with views.

## Behavior

- V: sub_1403A7AD8() first (cMaterial slot at r+16); shader = sub_140091124('shader/FrequentUtil.tec') into r+24 (an old r+24 is released first, sub_140095E88); null -> release via vtable slot 2 and return 0.
- V: six constant buffers (sub_140086F64, flags 66563) into r+40 (64 bytes), r+56 (288), r+200 (32), r+216 (128), r+232 (32), r+240 (48); each replaces (releases) a previous object; any null aborts to the slot-2 release path.
- V: a loop of 16 over the pointer table off_1406C5E60 (strings 'system/graphics/texture/noise/bn_64_00.tex' .. 'bn_64_15.tex', i.e. 64x64 blue-noise textures, I: from the names) loads each with sub_140091124 into r+64+8i and appends it to the owner list with sub_1403A7B08.
- V: r+224 = sub_140086E9C(72-byte index buffer, 16-bit indices, kind 22) is mapped and filled with 36 words (a 36-index mesh list) and unmapped. I: a small box / cube mesh for the utility passes; not read where drawn.
- V: slot ids by name: r+252..+286 = 'tTexture0'..'tTexture17'; r+288..+306 = cFrequentUtil, cCopyParam, cGaussianBlurPS, cGenerateFlatMipmap, cPredicateQuery, cCopyRangeVS, cCopyModelBufferParam, cOffsetMatrixParam, cCopyModelBufferParamArray, cOffsetMatrixParamArray; r+248 dword = *(qword_140C696A8 + 5088) (a count, I: frame / backbuffer count).
- V: sub_1403AB2CC(r) builds a *(r+248)-sized array of 32-byte constant buffers at *(r+312) (and more). On success two loops of 16: 64-byte buffers (flags 2049, stride 16) with views at r+392+8i, then 64-byte buffers (flags 34817) with views (sub_1400879F4) at r+520+8i. Returns 1 when both loops finish.
- V: no sampler / blend state is created in this function.

## State touched

- Reads: [g_RenderDevice](../globals/g_RenderDevice.md)

## Notes

Proposed name: FrequentUtilRenderer_CreateResources. Companion of SDFFontRenderer_CreateResources (sub_1403A87EC); both are called from sub_1403A143C (0x1403A1764 / 0x1403A1774).

## Open questions

? what the 36-index mesh draws. ? sub_1403AB2CC contents. ? what the two 16-buffer sets hold (I: per-pass parameter ring).
