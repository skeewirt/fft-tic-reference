# GUITextNodeStringSource

- **Kind:** observed behaviour
- **Scope:** where a text node's string comes from: the UI table or the code
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [GUITextNode_SetString](../functions/GUITextNode_SetString.md), [GUITextNode_UpdateLayout](../functions/GUITextNode_UpdateLayout.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A text node shows the string of its UI table text id while that id is not 0; with text id 0 it keeps a string set in code.

## Behavior

- V: `GUITextNode_SetString` (0x1403F0F8C) copies the string into the node.
- V: `GUITextNode_UpdateLayout` re-reads the text from the UI table only while the node's text id (+248) is not 0, so a text node with text id 0 keeps a string set in code.

## Open questions

None recorded.
