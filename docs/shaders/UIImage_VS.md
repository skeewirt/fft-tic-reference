# UIImage_VS

- **Kind:** shader
- **Stage:** vertex
- **Area:** [Graphics](../areas/graphics.md)
- **Technique file:** uirender.tec
- **Offset in file:** `0x001300`
- **DXBC hash:** `6a7a1a30381a082a68e9270e1b955d1f`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Vertex shader of the UI image program: position (x, y, z, w) times the projection in constant rows 0..3; colour and texture coordinate passed through (no snapping).

## Referenced by

- Observed behaviours: [RasterizerSnapsTo1_256Px](../behaviors/RasterizerSnapsTo1_256Px.md)
- Used in programs: [UIImage](../programs/UIImage.md)

## Open questions

None recorded.
