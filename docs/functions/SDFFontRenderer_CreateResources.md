# SDFFontRenderer_CreateResources

- **Address:** `0x1403A87EC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char sub_1403A87EC(__int64 r)  // r = SDFFontRenderer*`
- **Callers:** sub_1403A143C (0x1403A1764), data 0x143D4012C / 0x143D40138
- **Callees:** sub_1403A7AD8, sub_14001A2C4, sub_140011750 (alloc), sub_1403C043C, sub_140037CA4, sub_140091124 (resource load), sub_1403A7B08, sub_140086D28 / sub_140087318 / sub_140086F64 / sub_140086DE4 / sub_140086E9C (create buffer / SRV / cbuffer / VB / IB), sub_140089280 (slot lookup by name), sub_14008C5D8 (input layout), sub_14003E120 / sub_14003E228 (map / unmap)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

SDFFontRenderer set-up: fills the CPU palette array with 512 default entries, loads shader/SDFFont.tec, creates the palette buffer + its view, the constant buffer, the vertex / index buffers for the glyph quads, looks up the shader slots (tTexture0..12, cSDFConstant), and allocates the CPU vertex buffer.

## Behavior

- V: first sub_1403A7AD8() (sets r+16 = slot of constant buffer 'cMaterial', returns 1); returns 0 if it fails. Every later failure also returns 0 (no cleanup here; callers use the destructor slot).
- V: CPU palette: r+9560 = allocation of 98304 bytes (= 512 entries x 192 bytes). 512 times it writes one 192-byte default entry at stride 192 (layout below). The same 98304 figure is the GPU palette buffer size.
- V: palette default entry: bytes 0..63 = 4x4 identity matrix (copied from xmmword_140906C20 through the transposing copy sub_1403C043C; the source reads 1,0,0,0 / 0,1,0,0 / 0,0,1,0 / 0,0,0,1). Then 16-byte vectors: +64 (0.5, 0.25, 2.8, 128.0); +80 (6.0, -6.0, 0.8, 0.4); +96 (0.1, 1.0, 0, 0); +112 (0, 0, 0, 1); +128 (0, 0, 0.2, 1); +144 (1, 1, 1, 1); +160 (0.2, 0.5, 0.9, 1); +176 (0, 0.75, 0, 0).
- V (combined with the SDFFontRenderer_Flush rewrite list, which names those offsets): +64 = 0.5 is the threshold T (contour at 0.75 - T/2 = 0.5), +68 = 0.25 the outline term, +76 = 128 becomes 1/128, +80 = 6.0 is the shadow width field Flush tests, +88 = 0.8 and +92 = 0.4 are rewritten ((1-x-.5)*.5+.5 and x*.5), +96 = 0.1 is the value Flush multiplies by 0.005 (the K = 0.1 * 0.005 * g * S constant of fonts.md; 0.1 is exactly this default), +128 is the colour Flush substitutes for +112 when the shadow width is 0, +188 -> 1 - x.
- I: roles of +112 = (0,0,0,1) (shadow colour, black), +128 = (0,0,0.2,1) (alternate shadow colour, dark blue), +144 white, +160 = (0.2, 0.5, 0.9, 1) (a colour) and the values +72 = 2.8, +84 = -6.0, +100 = 1.0 were not read where they are used here.
- V: shader: sub_140091124(qword_143CD9B88, 'shader/SDFFont.tec', hash from sub_140037CA4, 0, &zeroed 32-byte out) -> r+24; null -> return 0. sub_1403A7B08(r, shader) appends it to the owner list at *(r+8) (vector push_back).
- V: palette GPU buffer r+48 = sub_140086D28(descriptor {size 0x18000 = 98304, flags 0x10802, stride 192}, kind 20); r+56 = sub_140087318 (shader resource view of that buffer, descriptor words {0, 1, 0x20000000000}); r+40 = sub_140086F64 constant buffer, descriptor {128 bytes, 66563 = 0x10403}, kind 20 (contents not read here; I: per-frame transform / screen constants).
- V: slot ids: r+160..+182 words = sub_140089280(table at *(qword_140C696A8 + 5064), 'tTexture1'..'tTexture12'); r+184 = 'tTexture0'; r+186 = sub_140089280(table at *(qword_140C696A8 + 5056), 'cSDFConstant'). r+9528 word = 8.
- V: vertex layout r+192 = sub_14008C5D8(*(qword_140C696A8 + 5016), 5 element descriptors {0xB24100000240000, 0xDA128000C222000, 0xE200000}, 5) = a 5-element input layout (I: matches the 48-byte vertex EmitGlyph writes: position, alpha dword, UV, float4, colour).
- V: glyph VB r+200 = sub_140086DE4(size 786432 = 0xC0000 = 4096 quads x 4 vertices x 48 bytes, flags 65794); glyph IB r+208 = sub_140086E9C(size 49152 = 4096 x 6 x 2 bytes, flags 513). The IB is mapped (sub_14003E120), then for quad n (0..4095) six 16-bit indices 4n, 4n+1, 4n+2, 4n+3, 4n+3, 4n+4 are written, then unmapped (sub_14003E228): a triangle strip per quad with a degenerate join to the next quad's first vertex.
- V: CPU vertex buffer r+9552 = allocation of 786432 bytes (EmitGlyph writes 4 x 48-byte vertices per glyph into it, quad n at 4n); null -> return 0.
- V: second small geometry set: layout r+216 = sub_14008C5D8(..., {2228224}, 1) (one element); VB r+224 = sub_140086DE4(size 6144, flags 65794); IB r+232 = sub_140086E9C(size 1536 = 192 x 4 x 2, flags 513) filled with strip indices 4n..4n+3 for n in 0..191 (0xC0 quads, no degenerate join). I: 6144 = 192 quads x 4 vertices x 8 bytes, a corner table (the 'quad UV corner table' of Flush); what it draws was not read.
- V: no sampler state, blend state, rasteriser or depth object is created or described anywhere in this function; the only palette-like GPU object is the 98304-byte buffer + view, and cSDFConstant is looked up as a slot id only (r+186). Nothing here touches UV derivatives (that is pixel-shader work).
- V: returns 1 on success.

## State touched

- Reads: [g_RenderDevice](../globals/g_RenderDevice.md)

## Notes

Proposed name: SDFFontRenderer_CreateResources. The cSDFConstant here is only the slot id at r+186 (I: Flush binds the palette buffer to it; the binding is in Flush, not read now) and is a different thing from the 'cSDF' 32-byte buffer of UIRender_ApplyDrawState. Default palette numbers fit fonts.md: T 0.5, K factor 0.1 x 0.005.

## Open questions

? the 5 vertex element semantics / formats (descriptor words not decoded). ? what the 8-byte-vertex second geometry set is drawn for. ? exact contents of the 128-byte constant buffer at r+40. ? blend and sampler state (not here; see Flush / ApplyDrawState).
