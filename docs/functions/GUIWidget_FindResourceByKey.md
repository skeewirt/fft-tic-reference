# GUIWidget_FindResourceByKey

- **Address:** `0x1403FBDCC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `UIResource **GUIWidget_FindResourceByKey(GUIWidget *w, element *key)`
- **Callers:** GUINode_DrawKind10, sub_1403F495C
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Linear search of the widget's pointer vector (widget+256 .. +264) for the entry whose name key equals `key`; returns the entry or 0.

## Behavior

- V: for each element e of the vector: when e+8 (name hash) and key+8 are both nonzero they are compared; otherwise the name strings (the pointers at e+0 and key+0) are compared byte by byte up to the terminator.
- V: returns the first match, nullptr at the end of the vector. No caching and no mutation.

## Notes

The name is ours. The element's first 12 bytes use the same {char *name; int hash} layout as element. GUINode_DrawKind10 calls this vector the widget's resource vector.

## Open questions

The element type of the vector (what file section it comes from) was not read.
