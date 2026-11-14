# RootSignature_CreateWithSampler

- **Address:** `0x140042E64`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall RootSignature_CreateWithSampler(__int64 unused1, RootSigRecord *out, int shaderVisibility, int numRootConstants, __int64 unused5, int numUavs, unsigned int samplerWord)`
- **Callers:** sub_140042018 (four calls), sub_14004318C, sub_1400435C4, sub_14004386C
- **Callees:** Sampler_DescFromWord, D3D12SerializeRootSignature, sub_140084744 (device error report), sub_140026BD4 (error log helper, returns its third argument)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds one Direct3D 12 root signature (optional root constants, one SRV descriptor table, optional UAV descriptor table, at most one static sampler decoded from a sampler word), serialises and creates it on the device, and stores the interface pointer and a 64-bit hash of the serialised blob.

## Behavior

- V: arguments in order: the first (rcx) and the fifth (the first stack slot) are never read. out (rdx) is a 16-byte record, [0] = the ID3D12RootSignature pointer and [8] = the blob hash; a null out gives the error result without doing anything. shaderVisibility (r8) goes into the ShaderVisibility field of every root parameter and into the static sampler. numRootConstants (r9), numUavs (the sixth argument) and samplerWord (the seventh; read as a dword, the decompile types it as 16 bits) are described below.
- V: the root signature flags are 0x1D: allow input assembler input layout, deny hull, deny domain and deny geometry shader root access (vertex and pixel access are not denied).
- V: the parameters, in this order: (1) only when numRootConstants != 0: 32-bit root constants, ShaderRegister 0 (b0), RegisterSpace 0, Num32BitValues = numRootConstants; (2) always: a descriptor table with one range, type SRV, 1 descriptor, base register 0 (t0), space 0, offset 0; (3) only when numUavs != 0: a descriptor table with one range, type UAV, numUavs descriptors from register 0 (u0), space 0, offset 0. The parameter count is therefore 1 to 3, with the SRV table at index 0 or 1.
- V: static sampler: unless (samplerWord & 0x3C0) == 0x380 (bits 6..9 equal to 0xE) the one sampler is Sampler_DescFromWord(&desc, &samplerWord, ..., shaderVisibility), which decodes filter, address modes, LOD and comparison from the word and stores the visibility at +48 of the description; its ShaderRegister and RegisterSpace (+40 / +44) are 0, so it is s0, space 0. With the 0x380 pattern the root signature has no static sampler (NumStaticSamplers 0).
- V: it calls D3D12SerializeRootSignature with the version-1 description, then creates the object through the device at (qword_140C696A8 + 3504) with vtable slot +128 (CreateRootSignature: node mask 0, the blob pointer and size, the root signature interface id, the result pointer).
- V: on success out[0] = the new interface pointer and out[8] = a 64-bit hash of the serialised blob bytes (start 0xCBF29CE484222325 and, for every byte, hash = (hash * 0x100000001B3) XOR byte: the FNV-1 order with the 64-bit constants); both blobs are released and 0 is returned.
- V: on a null out, a failed serialise or a failed CreateRootSignature it releases both blobs and returns 0x96100001 (the value sub_140026BD4 returns after logging); the serialise and create failures also report the HRESULT through sub_140084744 first. Every caller tests the sign of the result.
- V: the seven call sites (out slot offset in the owner object; shaderVisibility, numRootConstants, numUavs, samplerWord): sub_140042018 +0x88: 0 (all), 8, 1, 0x26A; +0x98: 0, 4, 1, 0x2A; +0xC8: 0, 0, 2, 0x3AA; +0xD8: 0, 48, 1, 0x3AA. sub_14004318C +0x78: 5 (pixel), 4, 0, 0x3AA. sub_1400435C4 +0xA8: 5, 4, 0, 0x2A. sub_14004386C +0xB8: 0, 4, 4, 0x3AA.
- V (Sampler_DescFromWord decode): the 0x3AA words select no static sampler; 0x26A is clamp on all axes with min / mag linear and mip point; 0x2A is clamp on all axes with point filtering.
- V (sub_140039E24): the records filled by the four sub_140042018 calls are passed to sub_140039E24 right after each call; it reads record[8] and uses it in a lookup key (the hash plus 31 times a dword read through the shader object) in a cache guarded by an SRW lock, creating the cached object with sub_1400511BC on a miss.
- I: that cached object is a compute pipeline state and the hash identifies the root signature in its cache key. Basis: the call order and the shape of sub_140039E24; the shaders behind these signatures were not read.

## State touched

- Calls: [Sampler_DescFromWord](Sampler_DescFromWord.md)
- Reads: [g_RenderDevice](../globals/g_RenderDevice.md)

## Notes

The name is ours (IDB: sub_140042E64 until applied). The parameters are laid out as the 32-byte D3D12_ROOT_PARAMETER (type, then the union at +8 and +16, visibility at +24), the ranges as the 20-byte D3D12_DESCRIPTOR_RANGE, the static sampler as the 52-byte D3D12_STATIC_SAMPLER_DESC.

## Open questions

? what the pipelines behind the +0x88 / +0x98 / +0xC8 / +0xD8 signatures compute (sub_140042018 and its shaders were not read). ? what sub_14004318C, sub_1400435C4 and sub_14004386C build with their signatures (two pixel-visibility signatures with 4 root constants, one with and one without a point sampler, and a 4-UAV signature). ? the first and fifth arguments (unused).
