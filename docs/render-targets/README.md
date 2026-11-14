# Render targets

GPU surfaces the renderer keeps by index: size, format and what each one holds at which point of the frame.

8 records. Format of a record: [kinds/render-target.json](../../kinds/render-target.json). Data: [data/render-targets.jsonl](../../data/render-targets.jsonl).

| Name | Index | Size | Format | Summary |
|---|---|---|---|---|
| [RT26_LayerContent](RT26_LayerContent.md) | RT 26 | output size | `R8G8B8A8_UNORM` | Layer content target: at the selection ring's glow pass it held the ring layer's own (sharp) pixels in its atlas place; the glow shader reads it as its second texture. |
| [RT27_GlowBlurred](RT27_GlowBlurred.md) | RT 27 | output size | `R8G8B8A8_UNORM` | Full-resolution blurred layer read by the glow pass (its first texture); for a half-size blur it is the bilinear upscale of RT32_HalfBlur. |
| [RT28_BlurScratch](RT28_BlurScratch.md) | RT 28 | output size | `R8G8B8A8_UNORM` | Scratch target of the UI blur's horizontal pass (UIBlur_Run gets 28 as its scratch index from the drop-shadow pass). |
| [RT30_MaskBuffer](RT30_MaskBuffer.md) | RT 30 | output size | `R8_UNORM` | Mask buffer of masked layers: the mask pass reads its red channel. |
| [RT32_HalfBlur](RT32_HalfBlur.md) | RT 32 | half output size (640 x 360 at 720p) | `R8G8B8A8_UNORM` | Half-size blur target: first the 2 x 2 box downsample of the layer, finally the vertically blurred result. |
| [RT37_HalfBlurTemp](RT37_HalfBlurTemp.md) | RT 37 | half output size (640 x 360 at 720p) | `R8G8B8A8_UNORM` | Half-size blur scratch: holds the horizontal pass of the half-size blur. |
| [RT3_EffectAlpha](RT3_EffectAlpha.md) | RT 3 | output size (1280 x 720 at 720p) | `R8G8B8A8_UNORM` | Effect alpha atlas: each layer with a drop shadow copies its alpha here (inside its atlas rectangle), the UI blur blurs it in place, and the shadow pass samples it. |
| [UITarget_Frame](UITarget_Frame.md) | per-type slot 2 (Renderer +0x5CB8 + 800 x type) | output size (1280 x 720 at 720p) | `UNORM (8 bits per channel by the captures)` | The UI frame target: the render target every layer blit composites onto (GUILayer_BlitFinal, GUILayer_BlurShadowPass and the glow pass take it from the same per-type table entry, slot 2 of the 800-byte row of the laye... |
