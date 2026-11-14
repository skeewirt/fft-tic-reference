# UiLayerComposite

- **Kind:** flow
- **Area:** [Graphics](../areas/graphics.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One frame of UI, layer by layer, in the order the game does it: how a widget becomes layers, which target a layer's draws go to, when that target is cleared, what runs on it, and how it is blended onto the frame. Everything a software renderer needs for the Job Tree: draw each layer's pixels into a cleared layer target, then composite the layers onto the frame in order.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [GUIRenderer_ResetFrame](../functions/GUIRenderer_ResetFrame.md) | V | Start of the UI frame: 512 layer records (592 bytes) reset, layer count 0, current layer 0. |
| <a id="2"></a>2 | [GUICore_CommitFrame](../functions/GUICore_CommitFrame.md) | V | Widgets are drawn from the last entry of the widget vector to the first (the first entry is on top), each through GUICore_DrawWidget. |
| <a id="3"></a>3 | [GUICore_DrawWidget](../functions/GUICore_DrawWidget.md) | V | Builds the root draw context of the widget's main component and calls ComponentLayer_Begin with the force flag 0. |
| <a id="4"></a>4 | [ComponentLayer_Begin](../functions/ComponentLayer_Begin.md) | V | A layer is opened when the component has any enabled effect group (colour transform that is not the identity, offsets, single float, drop shadow, glow, the +186 group, the whole-layer blur group, clip, mask) or a blend type other than 0, or when the renderer feature byte (+606621, 1 from the initialiser) forces it: the widget root (widget byte +83 is 1 for every one of the 51 widgets read live) and any component with component byte +561 set. Component nodes of kind Layer (UIB 'Layer00', 'LayerRoot') are plain containers and open nothing. |
| <a id="5"></a>5 | [GUILayer_Select](../functions/GUILayer_Select.md) | V | Finds an existing layer record with the same layer id and equal effect settings (never when the id is 0) or builds a new one (GUILayer_BuildRecord) and makes it current; later draws are appended to the current layer. |
| <a id="6"></a>6 | [GUINode_DrawChildren](../functions/GUINode_DrawChildren.md) | V | The component's nodes are drawn last entry first; each UI draw appends its command to the current layer through UIRender_AppendCommand, which also marks the layer used (+76). A child component with effects opens its own record; when it ends GUILayer_Select(parent context) continues the parent in a NEW record with an incremented layer id, so the parent's later draws stay above the child's layer. |
| <a id="7"></a>7 | [UIRender_PrepareLayers](../functions/UIRender_PrepareLayers.md) | V | The used layers (list in slot order = creation order) get their order (overlap rule; the final pack order is the list sorted by the order key, see the behavior LayerAtlasPlacement) and each its rectangle in the layer atlas page (GUILayer_PackAtlasRect: the layer's integer screen rectangle plus a margin of 2 px, or 32 px when a blur radius is above 3.2); the atlas offset layer+224 / +228 = packed position - integer screen position. |
| <a id="8"></a>8 | [UIRender_SubmitFrame](../functions/UIRender_SubmitFrame.md) | V | For every used layer GUILayer_Composite packs the layer's commands; the commands of all contexts are then sorted by key and executed. |
| <a id="9"></a>9 | [LayerPassKeys](../registries/LayerPassKeys.md) | V | Clear: at the first layer of each atlas page GUILayer_Composite queues clears of the layer content target and its scratch targets (slots 26, 27, 28, 29; slot 3 when the layer has a drop shadow; slot 30 for a masked layer) to the colour (0, 0, 0, 0) (RenderCommand_ClearTarget; the 16 colour bytes of the command are zero). |
| <a id="10"></a>10 | [UICommand_ExecuteBatches](../functions/UICommand_ExecuteBatches.md) | V | Draw: the layer's own draws are replayed into the layer content target (RT 26) with the scissor rectangle = the layer's packed integer rectangle in atlas coordinates and the layer's constant buffer bound; vertices go through a pixel-to-clip matrix whose translation holds the atlas offset. |
| <a id="11"></a>11 | [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md) | V | Blend of the draws: the draw state's word, 0x79420a11 by default (source ONE, destination INV_SRC_ALPHA, add, alpha the same, write mask 0xF): the layer target holds premultiplied colour; the first draw into a cleared pixel stores round8(source). |
| <a id="12"></a>12 | [GUILayer_ApplyEffects](../functions/GUILayer_ApplyEffects.md) | V | Effects of the layer in fixed order on its pixels (mask, colour / offset passes, blur, drop shadow copy and blur), skipped for a plain layer; the layer's pixels stay in RT 26 unless a pass moved them. |
| <a id="13"></a>13 | [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md) | V | Blit: the layer quad (rect - atlas offset, the integer screen rectangle) is drawn with selector #9 (digit 0 = layer blend type); the pixel shader reads RT 26 at pixel + atlas offset (point read, exact texel) and does the blend by a read-modify-write of the frame target. |
| <a id="14"></a>14 | [LayerBlit](../programs/LayerBlit.md) | V | Blend type 0: frame = round8(layer.rgb x k + frame.rgb x (1 - layer.a)), alpha = round8(layer.a + frame.a x (1 - layer.a)), with k = cb8.z = 1 and the layer's colour transform (multiply 1, add 0 by default) applied to the layer pixels first. |
| <a id="15"></a>15 | [GUILayer_GlowPass](../functions/GUILayer_GlowPass.md) | V | Glow and shadow of the layer land after / before the blit as the existing flows describe (LayerGlowHalfSize, LayerDropShadow). |

## Behavior

- V: layers with no draws (+76 clear) are skipped by GUILayer_Composite and cost nothing; a layer with the cull flag (+79) draws and blits nothing.
- V: all UI draws, text included, are recorded into layer records; the pass order within one atlas page is clear, then every layer's draws, then every layer's blit (key order), so the layer target never holds more than the current page.
- I: the letterbox bars and the overlay quads (UIRender_DrawOverlayQuads) are drawn straight to the output, outside the layers.

## Referenced by

- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md), [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md), [LayerBlitOverFrameTarget](../behaviors/LayerBlitOverFrameTarget.md), [LayerContentDrawnIntoCleared8BitTarget](../behaviors/LayerContentDrawnIntoCleared8BitTarget.md), [WidgetRootsAreLayers](../behaviors/WidgetRootsAreLayers.md)

## Open questions

? the layer ids a UIB can assign (component +552), which merge several components into one record; the kind 2 layers (never produced by GUILayer_BuildRecord).
