# GUINode_FindDescendant2

- **Address:** `0x140409214`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINode *GUINode_FindDescendant2(GUINode *root, UIName *outer, UIName *inner)`
- **Callers:** 36 call sites: MainTab_BindNodes ('MainTab' then 'Tab'; 'TextMask' then 'MaskNode00'), the world-map screen builder and many other screen builders
- **Callees:** GUINode_FindDescendant

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Two-step descendant lookup: the node `outer` under `root`, then the node `inner` under that.

## Behavior

- V: r = GUINode_FindDescendant(root, outer); returns 0 when r is 0, else GUINode_FindDescendant(r, inner).

## State touched

- Calls: [GUINode_FindDescendant](GUINode_FindDescendant.md)

## Referenced by

- Called by: [WorldMapScreen_BindNodes](WorldMapScreen_BindNodes.md)

## Notes

The name is ours; the game has no symbol for it.

## Open questions

None recorded.
