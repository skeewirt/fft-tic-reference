# GUINode_FindGadgetPart

- **Address:** `0x140409134`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINode *GUINode_FindGadgetPart(GUINode *root, const char *gadgetName, const char *partName)`
- **Callers:** JobTree_RefreshAddon (0x1337D9, 'Unit'/'Unit'), and many other UI addons
- **Callees:** GUINode_FindDescendant, GUINode_FindPartByName

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a named part inside a named gadget: looks up the gadget node, then searches the gadget's component layer for the part.

## Behavior

- V: node = GUINode_FindDescendant(root, gadgetName); null -> null.
- V: returns GUINode_FindPartByName(node + 272, partName); +272 is the GUIComponent layer node embedded in the gadget.

## State touched

- Calls: [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUINode_FindPartByName](GUINode_FindPartByName.md)

## Referenced by

- Called by: [MainTab_BindNodes](MainTab_BindNodes.md), [ScrollHelper_Bind](ScrollHelper_Bind.md), [WorldMapScreen_BindNodes](WorldMapScreen_BindNodes.md)

## Notes

Only resolves an existing gadget; creating it is the caller's job (JobTree_RefreshAddon creates the 'Unit' gadget before this lookup).

## Open questions

None recorded.
