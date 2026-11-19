# NxdDataRefinedVFXTexture

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 202
- **Rows:** 487 rows of 32 bytes
- **Keyed by:** one key: id (0..486)
- **Read by:** [EffectNxd_HasFlag24](../functions/EffectNxd_HasFlag24.md), [EffectNxd_HasFlag25](../functions/EffectNxd_HasFlag25.md), [EffectNxd_HasFlag28](../functions/EffectNxd_HasFlag28.md), [EffectNxd_LoadRow](../functions/EffectNxd_LoadRow.md), [Effect_TintByNxdScale](../functions/Effect_TintByNxdScale.md)
- **Row layout:** [NxdDataRefinedVFXTextureRow](../structs/NxdDataRefinedVFXTextureRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Effect textures (487) linked to depth bias and camera control. Verdict: engine-data.

## Behavior

- V: 487 rows, one key id (0..486); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 10 of 11 columns not decoded (see the row layout)
