# JobTreePanel_SetTextKey

- **Address:** `0x14029BC00`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JobTreePanel_SetTextKey(__int64 ctx, __int64 binding, const char *key, __int64 textNode, __int64 args)`
- **Callers:** JobTreePanel_SetJobIcon
- **Callees:** sub_1403F0F8C, sub_1403FBE3C, UIName_Key, sub_1403D87F4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Points a name-board text binding at a text key and clears the text node's fixed text id so the keyed text is used.

## Behavior

- V: when a text node is given, its text id (+248) is cleared (dirty byte +316 set) and sub_1403F0F8C(node, args) applies the arguments.
- V: when a binding is given, the key string stored at binding+232 is compared with `key`; if it differs and the context's owner resolves the key (sub_1403FBE3C), the binding is re-keyed with UIName_Key + sub_1403D87F4.

## State touched

- Calls: [UIName_Key](UIName_Key.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [ItemCell_BindIconAndName](ItemCell_BindIconAndName.md), [JobTreePanel_SetJobIcon](JobTreePanel_SetJobIcon.md)

## Notes

JobTreePanel_SetJobIcon overrides the cleared id with 1010 afterwards for a locked job.

## Open questions

What sub_1403FBE3C resolves (?).
