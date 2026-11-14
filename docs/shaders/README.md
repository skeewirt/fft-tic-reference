# Shaders

GPU shader programs from the game's technique files: stage, interface, bindings and what they compute (in words; no bytecode).

9 records. Format of a record: [kinds/shader.json](../../kinds/shader.json). Data: [data/shaders.jsonl](../../data/shaders.jsonl).

| Name | Stage | Technique file | Summary |
|---|---|---|---|
| [AlphaCopy_PS](AlphaCopy_PS.md) | pixel | uirender.tec | Copies a layer's alpha into the effect alpha target: writes (0, 0, 0, source alpha). |
| [FullscreenTriangle_VS](FullscreenTriangle_VS.md) | vertex | uirender.tec | Vertex shader of the alpha copy: an oversized triangle built from the vertex index, so no vertex buffer is bound. |
| [LayerBlendNormal_PS](LayerBlendNormal_PS.md) | pixel | uirender.tec | The layer blit pixel shader for blend type 0 (normal), offset variant 0: composites one layer's premultiplied pixels over the frame target by a read-modify-write of an unsigned-normalised UAV. It is the first of the 3... |
| [LayerBlendNormalOffsets_PS](LayerBlendNormalOffsets_PS.md) | pixel | uirender.tec | Blend type 0 with the offset variant (digit 1 = 1): the same over composite as LayerBlendNormal_PS with extra samples at the layer's three offset vectors (selected when any of them is non-zero). |
| [LayerQuadOffset_VS](LayerQuadOffset_VS.md) | vertex | uirender.tec | Vertex shader of the drop-shadow pass: moves the layer quad by the shadow offset and keeps its texture coordinates. |
| [LayerShadow_PS](LayerShadow_PS.md) | pixel | uirender.tec | Drop-shadow pass of a UI layer: darkens the target in place under the layer's blurred alpha, before the layer itself is drawn. |
| [MaskComposite_PS](MaskComposite_PS.md) | pixel | uirender.tec | Mask pass of a masked layer (the screen title): the layer's gradient times the mask buffer. |
| [UIImage_PS](UIImage_PS.md) | pixel | uirender.tec | The plain UI image pixel shader (UI technique program 0): every textured UI image (discs, the selection ring, the cursor glove, plates, floor tiles, line parts). |
| [UIImage_VS](UIImage_VS.md) | vertex | uirender.tec | Vertex shader of the UI image program: position (x, y, z, w) times the projection in constant rows 0..3; colour and texture coordinate passed through (no snapping). |
