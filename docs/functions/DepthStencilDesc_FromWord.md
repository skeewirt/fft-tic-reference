# DepthStencilDesc_FromWord

- **Address:** `0x140051438`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int DepthStencilDesc_FromWord(D3D12_DEPTH_STENCIL_DESC *desc, unsigned __int64 word)`
- **Callers:** sub_140051508 (pipeline state creation)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Unpacks the packed depth-stencil word of a pipeline state into the Direct3D 12 depth-stencil description.

## Behavior

- V: DepthEnable = w & 1, DepthWriteMask = (w & 2) != 0, DepthFunc = ((w >> 2) & 7) + 1, StencilEnable = (w >> 25) & 1, StencilReadMask = byte 6, StencilWriteMask = byte 7; front face: StencilFailOp = (w >> 29) + 1 (bits 29..31), StencilDepthFailOp = ((w >> 34) & 7) + 1, StencilPassOp = ((w >> 37) & 7) + 1, StencilFunc = ((w >> 26) & 7) + 1.
- V: with bit 33 set the back face has its own fields (fail = ((w >> 16) & 7) + 1, depth fail = ((w >> 19) & 7) + 1, pass = ((w >> 22) & 7) + 1, func = ((w >> 13) & 7) + 1); otherwise it repeats the front face.
- V: called by the pipeline-state builder sub_140051508 with the qword at key+48, next to BlendDesc_FromWords (blend) and sub_140051324 (rasteriser).
- I: the draw-state qword at ts+104 is this word: a program entry's mask bit 0x80 replaces its low 5 bits (depth enable, write, comparison: ShaderProgram_ApplyState), and the reset constant 0xFFFF00001C000000 (RenderContext_ResetFrame) decodes as stencil masks 0xFF / 0xFF with KEEP operations and ALWAYS. Used to read the SDFFont programs (SDFFontRenderer_Flush).

## Notes

Comparison values are D3D12_COMPARISON_FUNC (1 NEVER, 2 LESS, 3 EQUAL, 4 LESS_EQUAL, 5 GREATER, 6 NOT_EQUAL, 7 GREATER_EQUAL, 8 ALWAYS).

## Open questions

None recorded.
