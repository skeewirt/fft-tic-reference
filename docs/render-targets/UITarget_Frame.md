# UITarget_Frame

- **Kind:** render target
- **Area:** [Graphics](../areas/graphics.md)
- **Index:** per-type slot 2 (Renderer +0x5CB8 + 800 x type)
- **Size:** output size (1280 x 720 at 720p)
- **Format:** `UNORM (8 bits per channel by the captures)`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The UI frame target: the render target every layer blit composites onto (GUILayer_BlitFinal, GUILayer_BlurShadowPass and the glow pass take it from the same per-type table entry, slot 2 of the 800-byte row of the layer's target type). Type 0 is the type of the main UI target.

## Behavior

- V (live read 2026-10-30): the row of type 0 holds four target objects (slots 0..3); slot 0 is the layer draw target (RT 26's resource), slot 2 is a two-dimensional array view (the frame), slots 1 and 3 other views of the same size (1280 x 720).
- V: UIRender_SubmitFrame reads the page count from slot 2's view (array size) to clear and transition one atlas texture per page.
- I: slot 2 is the frame the finished UI is presented from: the blits write it, UIRender_ResolveBase copies the base surface into it first. Not traced to the swap chain here.

## Referenced by

- Bound in shaders: [LayerBlendNormal_PS](../shaders/LayerBlendNormal_PS.md)
- Observed behaviours: [LayerBlitOverFrameTarget](../behaviors/LayerBlitOverFrameTarget.md)

## Open questions

? the DXGI format of the resource (the shader sees it as a UNORM float4 UAV); how slot 2 reaches the swap chain.
