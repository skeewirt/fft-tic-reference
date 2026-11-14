# FullscreenTriangle_VS

- **Kind:** shader
- **Stage:** vertex
- **Area:** [Graphics](../areas/graphics.md)
- **Technique file:** uirender.tec
- **Offset in file:** `0x034080`
- **DXBC hash:** `562d13f1fca3e875076406b14dec36b8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Vertex shader of the alpha copy: an oversized triangle built from the vertex index, so no vertex buffer is bound.

## Behavior

- I: built from SV_VertexID (the pass binds no vertex buffer; the shader reads row 11.xy as a uv scale).

## Referenced by

- Used in programs: [LayerAlphaCopy](../programs/LayerAlphaCopy.md)

## Open questions

None recorded.
