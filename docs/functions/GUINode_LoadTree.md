# GUINode_LoadTree

- **Address:** `0x1403F6C70`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_LoadTree(UILoader *ld, int *fileNode, GUIWidget *w, GUINode *node)`
- **Callers:** sub_1403F5910
- **Callees:** GUINode_BuildFromFile, sub_1403F5910, sub_1403F0654, sub_1403F4BA8, sub_1403FA344, sub_1403D87F4, sub_1403DC750

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds one node from its file record and, for a Layer, its children; a Reference node gets its component by name from the file's component array.

## Behavior

- V: GUINode_BuildFromFile(ld, fileNode, node) first.
- V: Layer (type 1): children from the table at fileNode + int(+0x90), int(+0x94) entries (offsets relative to the table), each built by sub_1403F5910 and linked in order.
- V: Reference (type 10), when ld+32 is set: the file header is ld+8, the component array header + int(header+4) with int(header+8) records of 64 bytes; each record's name (record + int(record+0)) is compared byte by byte with the node's component name (fileNode + int(+0x70)); the FIRST match is instantiated (sub_1403F4BA8 -> GUIComponent_LoadDef), registered (sub_1403FA344) and its name key copied to node+208.
- V: type 13 (Mask) is resolved after it the same way (not read further).

## State touched

- Calls: [GUINode_BuildFromFile](GUINode_BuildFromFile.md)

## Notes

The name is ours. The lookup is a linear search over every record of the file; names must be unique, the first match wins.

## Open questions

-
