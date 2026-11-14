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
| <a id="*firstchild"></a>`0xD0` | *firstChild | `GUINode` | V |  |  |  |

## Notes

Source: vftable_faith::UISystem::GUINode (0x140721DD0).

## Open questions

None recorded.
