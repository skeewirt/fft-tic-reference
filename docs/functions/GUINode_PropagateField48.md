# GUINode_PropagateField48

- **Address:** `0x1403F0610`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_PropagateField48(GUINode *node, int value)`
- **Callers:** sub_1403F0654
- **Callees:** itself

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Recursively assigns `value` to child->+48 for the node's children (linked via +32), descending when child kind (+52) == 1.

## Behavior

- V: used when a node is attached to a parent (sub_1403F0654): the child inherits the parent's +48.
- V: this is why every 'Unit' gadget +0x30 equals its component root's object id.

## State touched

- Reads: [GUINode.kind](../structs/GUINode.md#kind)
- Writes: [GUINode.objectId](../structs/GUINode.md#objectid)

## Notes

Do not treat +0x30 as sprite part data.

## Open questions

None recorded.
