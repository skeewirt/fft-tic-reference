# GUINode

- **Kind:** structure
- **Size:** 224 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Size from the 224-byte free in GUILayerNode's destructor.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="*name"></a>`0x8` | *name | `char` | V |  |  |  |
| <a id="*parent"></a>`0x18` | *parent | `GUINode` | V |  |  |  |
| <a id="*nextsibling"></a>`0x20` | *nextSibling | `GUINode` | V |  |  |  |
| <a id="*prevsibling"></a>`0x28` | *prevSibling | `GUINode` | V |  |  |  |
| <a id="objectid"></a>`0x30` | objectId | `int32` | V | copied from parent by GUINode_PropagateField48 (NOT a sprite part id) | [GUINode_PropagateField48](../functions/GUINode_PropagateField48.md) |  |
| <a id="kind"></a>`0x34` | kind | `int32` | V | 1 = container |  | [GUINode_ApplyAnimChannels](../functions/GUINode_ApplyAnimChannels.md), [GUINode_ClearVisibleSubtree](../functions/GUINode_ClearVisibleSubtree.md), [GUINode_DrawChildren](../functions/GUINode_DrawChildren.md), [GUINode_FindDescendant](../functions/GUINode_FindDescendant.md), [GUINode_FindNthPartByKindRec](../functions/GUINode_FindNthPartByKindRec.md), [GUINode_FindPartByName](../functions/GUINode_FindPartByName.md), [GUINode_PropagateField48](../functions/GUINode_PropagateField48.md), [GUINode_UpdateSubtree](../functions/GUINode_UpdateSubtree.md), [MainTab_BindNodes](../functions/MainTab_BindNodes.md), [ScrollHelper_Bind](../functions/ScrollHelper_Bind.md), [WorldMapScreen_BindNodes](../functions/WorldMapScreen_BindNodes.md) |
| <a id="x"></a>`0x38` | x | `int32` | V | the integer position; GUINode_SetPosition writes +0x38 / +0x3C and sets +0x95 (layout dirty); a state's position track (tag 5002) samples into it (GUINode_ApplyAnimChannels) |  |  |
| <a id="y"></a>`0x3C` | y | `int32` | V | see x |  |  |
| <a id="width"></a>`0x40` | width | `int32` | V | GUINode_SetSize (state size track) |  |  |
| <a id="height"></a>`0x44` | height | `int32` | V | see width |  |  |
| <a id="enabled"></a>`0x90` | enabled | `uint8` | V | a state's bool track writes it; 0 hides the node and its subtree (seen live on the deployment portrait boxes, 2026-11-21) |  |  |
| <a id="layoutdirty"></a>`0x95` | layoutDirty | `uint8` | V | set by GUINode_SetPosition and by a rotation change |  |  |
| <a id="*firstchild"></a>`0xD0` | *firstChild | `GUINode` | V |  |  |  |

## Notes

Source: vftable_faith::UISystem::GUINode (0x140721DD0).

## Open questions

None recorded.
