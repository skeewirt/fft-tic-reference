# GUINode_DrawKind10

- **Address:** `0x1403ED7D0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_DrawKind10(UIRenderer *r, DrawCtx *ctx, GUINode *node)`
- **Callers:** GUINode_DrawChildren (kind 10)
- **Callees:** sub_1403FBDCC, sub_1403F96CC, ComponentDrawContext_Build, ComponentLayer_Begin, GUILayer_Select, Matrix2x3_Multiply, sub_1403E6440, sub_1403E9A2C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draw hook for runtime node kind 10 (file type 11): resolves the node's two names, opens a component layer for the referenced component and queues an 80-byte draw record.

## Behavior

- V: skipped when node+204 (visible) is 0 or node+145 (hidden) is set. The resource named by the key at node+208 is looked up in the widget's resource vector (sub_1403FBDCC over widget +256..+264, compared by name key); a miss ends the call.
- V: the component named by the key at node+224 is looked up in the widget's component map (sub_1403F96CC, widget +136). When it is found, loaded (component +416) and visible (+192 = 0 or opacity +188 > 0), a draw context is built (ComponentDrawContext_Build) and ComponentLayer_Begin(r, ctx, 1) opens a layer; the layer's texture size is read from the layer record.
- V: either way a record is appended to the renderer's list at r+606688 (80 bytes: the widget, the resource, the node, the matrix from Matrix2x3_Multiply(node+160, ctx+504), the node colour (+196) times the context colour (ctx+540) per channel, and the layer index).

## State touched

- Calls: [ComponentDrawContext_Build](ComponentDrawContext_Build.md), [ComponentLayer_Begin](ComponentLayer_Begin.md), [GUILayer_Select](GUILayer_Select.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)
- Reads: [g_Renderer](../globals/g_Renderer.md)

## Notes

The name is ours. No node of kind 10 appears in the Job Tree screen (node census: Mask 1, Effect 0, Model 0).

## Open questions

What the kind 10 resource and the queued record are (the record's consumer was not read); the file-format name of type 11.
