# LayerPassKeys

- **Kind:** registry
- **Area:** [Graphics](../areas/graphics.md)
- **Resolved by:** [GUILayer_Composite](../functions/GUILayer_Composite.md)
- **Values stored in:** [RenderContext.sort_key](../structs/RenderContext.md#sort_key)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The pass constants OR-ed into the 64-bit sort key of the layer commands. Commands execute in key order: target type, then atlas page, then pass number (bits 9..14 of the constant), then the layer's order. The id is the pass number (constant >> 9 & 0x3F).

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="clear"></a>1 | `clear` | `0x6AC00200` | V | GUILayer_Composite: the clear commands of an atlas page (clear to (0, 0, 0, 0)). |
| <a id="draw"></a>2 | `draw` | `0x6AC00400` | V | UICommand_ExecuteBatches: the layer's own UI draws into the layer target (RT 26). |
| <a id="copy offset region"></a>7 | `copy offset region` | `0x6AC00E00` | V | GUILayer_CopyOffsetRegion and the GUILayer_Composite effect-entry key. |
| <a id="+484 pass"></a>8 | `+484 pass` | `0x6AC01000` | V | GUILayer_ApplyEffects: the pass of the +484 group (sub_1403AEE0C). |
| <a id="base copy / +486 pass"></a>14 | `base copy / +486 pass` | `0x6AC01C00` | V | UIRender_ResolveBase (when its xmmword condition is set) and the +486 pass of GUILayer_ApplyEffects. |
| <a id="shadow alpha copy"></a>15 | `shadow alpha copy` | `0x6AC01E00` | V | GUILayer_ApplyEffects before GUILayer_CopyToTarget and GUILayer_BlurShadowPass (the drop shadow of the layer). |
| <a id="shadow blur"></a>16 | `shadow blur` | `0x6AC02000` | V | GUILayer_BlurShadowPass: the blur of the drop shadow. |
| <a id="blit and effects"></a>59 | `blit and effects` | `0x6AC07600` | V | GUILayer_BlitFinal, the glow pass and the drop-shadow draw: the layer onto the frame target. |
| <a id="end"></a>63 | `end` | `0x6AC07E00` | V | Left in the state at the end of GUILayer_Composite. |

## Behavior

- V: key layout read from GUILayer_Composite: (order & 0x1FF | ((page & 0x3F | target type << 18) << 15) | constant) << 10, so the target type is the most significant field, then the constant's high bits, the page, the pass and last the order.

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Observed behaviours: [LayerCompositeOrder](../behaviors/LayerCompositeOrder.md)

## Open questions

None recorded.
