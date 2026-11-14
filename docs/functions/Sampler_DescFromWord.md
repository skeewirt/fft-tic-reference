# Sampler_DescFromWord

- **Address:** `0x140068D54`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `D3D12_STATIC_SAMPLER_DESC *Sampler_DescFromWord(D3D12_STATIC_SAMPLER_DESC *out, unsigned *word, __int64 a3, __int64 a4, int shaderVisibility)`
- **Callers:** RootSignature_CreateWithSampler (sub_140042E64; called when (samplerWord & 0x3C0) != 0x380)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decodes a 32-bit packed sampler word (the words kept in the draw state at +5704 + 4 * slot) into a D3D12 static sampler description.

## Behavior

- V: filter: if bits 6..9 are all set the filter is anisotropic (0x55); otherwise bit 6 = MIN linear (0x10), bit 9 = MAG linear (0x04), bit 8 = MIP linear (0x01); bit 27 adds the comparison flag (0x80). Bit 7 is only read for the anisotropic test.
- V: address modes: AddressU = (word & 3) + 1, AddressV = ((word >> 2) & 3) + 1, AddressW = ((word >> 4) & 3) + 1 (1 wrap, 2 mirror, 3 clamp, 4 border, 5 mirror once).
- V: MipLODBias = (signed 10-bit field word bits 10..19) * 0.03125 (the shift pair (word << 12) >> 22); MaxAnisotropy = {1, 2, 4, 6, 8, 10, 12, 16}[(word >> 24) & 7]; ComparisonFunc = ((word >> 28) & 7) + 1; MinLOD = (word >> 20) & 0xF; MaxLOD = FLT_MAX when bit 7 or bit 8 is set (mips enabled), otherwise MinLOD; BorderColor = 0 (transparent black); the 52-byte description is completed with ShaderRegister = 0 and RegisterSpace = 0 (+40 / +44) and ShaderVisibility = a5 (+48).
- V (IDB image): the default word dword_141D8BC7C holds 0xFFFFFFFF in the database. That value decodes as anisotropic with the comparison flag, BORDER addressing on all axes and MinLOD 15 (the contexts store it masked with 0x7FFFFFFF, which drops bit 31). It is not the runtime value.
- V (live read 2026-10-30, x/1wx 0x141D8BC7C = 0): the default word is 0 at runtime. It decodes as point filtering, WRAP addressing on all axes, MinLOD = MaxLOD = 0, with MaxAnisotropy 1 and ComparisonFunc NEVER (unused: the comparison filter flag is clear). Every slot a fresh context or a reset context stores from the default (RenderContext_ResetFrame for all 64 slots, sub_14003A048) therefore holds 0.
- V (xref list of the IDB): all 15 references to dword_141D8BC7C are reads (sub_14003A048, RenderContext_ResetFrame, sub_1400CEB4C, sub_1400CF9BC, UICommandRing_Flush, UIRender_ApplyDrawState, sub_1403CB56C, PostTarget_DrawFitted, CharaRender_SubmitQuads). No direct xref writes it; the code that changes it from the IDB value to 0 was not found statically.
- V (live read 2026-10-30; names on the NameSlotTable_Lookup sheet): the slot index of a word in the +5704 array is the id from the sampler name table: 12 ccc_ppn_sampler, 13 ccc_lln_sampler, 14 g_Sampler, 15 g_Sampler_tMaskBuffer, 16 ccc_lln_sampler_tMaskBuffer, up to 30 sSampler3 (31 entries, the full list is on that sheet). The UI draw word goes to slots 14 and 15 (UIRender_ApplyDrawState); the technique defaults for the Job Tree shadow are slots 13 and 16 (GUILayer_BlurShadowPass).
- V (live read 2026-10-28, ShaderSelector_Apply entry with r8 = 2 = the SDF font renderer's call, 300 records on the Job Tree: slots 0..7 of state+5704 all 0x26A): the SDF text atlas sampler is min / mag linear, mip point, CLAMP on U / V / W, MinLOD = MaxLOD = 0, i.e. plain bilinear with clamping. The generic UI draw word (UIRender_ApplyDrawState a2+4, 368 of 400 records) is 0x2C0: min / mag linear, mip point, WRAP, MinLOD 0, MaxLOD FLT_MAX; the rest are 0 (point, wrap). The UI .tex headers carry one mip, so the mip fields do not matter on this screen.
- V (with CharaRender_SubmitQuads): the chara atlas slot clears bits 6..9 (point filtering, MinLOD = MaxLOD = 15) and the three LUT slots have bits 6 and 9 set with 7 and 8 clear (0x240 pattern): min / mag linear, mip POINT, MinLOD = MaxLOD = 15 (i.e. the last mip that exists), BORDER addressing. So the LUT is sampled bilinearly (as render_chara models), and the atlas with a point filter.

## Referenced by

- Called by: [RootSignature_CreateWithSampler](RootSignature_CreateWithSampler.md)

## Notes

The name is ours (IDB: sub_140068D54). Bits 6..9 equal to 0xE (a7 & 0x3C0 == 0x380 in the caller) select 'no static sampler' (the shader samples through a descriptor-table sampler instead).

## Open questions

? the code that makes dword_141D8BC7C 0 at runtime (all 15 references read it, none writes it). Which bit pattern selects the descriptor-table path in the caller (0x380), and whether any UI slot uses it; whether the LUT texture really has a single mip (MinLOD 15 would force a 1 x 1 level otherwise).
