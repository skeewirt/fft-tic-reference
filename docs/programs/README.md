# Shader programs

Engine shader programs: a selector and program index resolved to its vertex and pixel shader, and the passes that use it.

4 records. Format of a record: [kinds/program.json](../../kinds/program.json). Data: [data/programs.jsonl](../../data/programs.jsonl).

| Name | Selector | Program index | Summary |
|---|---|---|---|
| [LayerAlphaCopy](LayerAlphaCopy.md) | UI manager selector #10 | 0 | First step of a layer's drop shadow: copies the layer alpha into RT3_EffectAlpha inside the layer's atlas rectangle. |
| [LayerBlit](LayerBlit.md) | UI manager selector #9 | 0 | The layer blit: draws one layer's quad (rect - atlas offset) with the layer blend type as selector digit 0 and the offset-vector flag as digit 1. |
| [LayerShadow](LayerShadow.md) | UI manager selector #10 | 1 | The drop-shadow draw: the layer quad moved by the offset, darkening the target under the blurred alpha. |
| [UIImage](UIImage.md) | UI technique (UIRender_ApplyDrawState) | 0 | Draws every textured UI image: program 0 of the UI technique (shader objects 1 and 10). |
