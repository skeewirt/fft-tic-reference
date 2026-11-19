# GUITextNode_SetTextExpanded

- **Address:** `0x1403F109C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUITextNode_SetTextExpanded(__int64 node, _QWORD *text, __int64 args)`
- **Callers:** GUITextNode_SetTextById, GUITextNode_SetTextExpandedTemp, sub_140108828, sub_140109134, sub_1401442FC, sub_1401527C0 and many more
- **Callees:** GUIText_Expand, GUITextNode_SetString

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Expands placeholders in text using args into a temporary std::string, then sets the result on the node; uses the raw text if expansion reports nothing.

## Behavior

- V: builds a std::string temp on the stack: allocator = qword_143CDAA80[+32] (or 0), size 0, capacity 15 (v9 = 15, SSO).
- V: if GUIText_Expand(&alloc, text, args) != 0, the string to set is the temp (heap pointer v8[0] when capacity >= 16, else inline v8); otherwise the original text pointer is used.
- V: result = GUITextNode_SetString(node, str).
- V: afterwards if capacity >= 16 the heap buffer is freed through allocator vtable slot +24 with size capacity + 1.

## State touched

- Calls: [GUIText_Expand](GUIText_Expand.md), [GUITextNode_SetString](GUITextNode_SetString.md)

## Referenced by

- Appears in flows: [BattleMessageBanner](../flows/BattleMessageBanner.md)
- Called by: [ErrorBanner_Show](ErrorBanner_Show.md), [GUITextNode_SetTextById](GUITextNode_SetTextById.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md), [UIMessageBanner_Show](UIMessageBanner_Show.md), [sub_1401560D0](sub_1401560D0.md)

## Notes

This is where in-text macros (names, numbers) are resolved before the string reaches the layout. Chip text goes through this when set by id.

## Open questions

? exactly which macros GUIText_Expand resolves and what its return value means (non-zero = expanded, I).
