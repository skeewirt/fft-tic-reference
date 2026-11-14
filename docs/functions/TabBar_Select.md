# TabBar_Select

- **Address:** `0x1402A9944`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char TabBar_Select(TabBar *t, int index)`
- **Callers:** TabBar_SetTable (tail), sub_140117330, sub_14012B870, sub_14012FC6C, sub_140131068, sub_1402A9B08
- **Callees:** sub_1400F5828, sub_1400F5BCC, GUICore_FocusNode, UIName_Key, GUINode_StopState, GUINode_FindState, GUINode_PlayState, sub_1403D8D1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Selects a tab: puts the cursor / focus on tab 'index' of the bar's nodes and plays Active on it and Deactive on all the others.

## Behavior

- V: runs only when sub_1400F5828(t+24, count = (char)t[424], 0, 0) reports that the first `count` tab node pointers are all non-null.
- V: builds an option block {0, 0, 0, 1} and calls sub_1400F5BCC to move the focus: when byte t+425 == 0 it is called with a null focus root and followed by GUICore_FocusNode(0) (focus cleared); otherwise with root = *(t+16)+496 (the bar's widget) so the selected tab node takes the focus. sub_1400F5BCC(root, nodes, count, index, opts) focuses nodes[index] (sub_1400F5674: GUICore_FocusNode with node+557 cleared under a g_CharaRenderMgr condition) and applies sub_1400F5C78(node, opts, i == index) to every node (the CursorOver / CursorOut / Check / Uncheck state logic of a component).
- V: then for every tab i < count: i == index plays 'Active' and stops 'Deactive'; others stop 'Active' and play 'Deactive' (state +104 = 1 + GUINode_PlayState).
- V: t+420 = index.

## State touched

- Calls: [sub_1400F5BCC](sub_1400F5BCC.md), [GUICore_FocusNode](GUICore_FocusNode.md), [UIName_Key](UIName_Key.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [JobChangeAddon_SetState](JobChangeAddon_SetState.md)

## Notes

Name proposed (IDB: sub_1402A9944). Shows how a cursor move between tabs works: focus moves AND the Active / Deactive state pair flips on the same call, not through the usual CursorOver event alone.

## Open questions

? what byte t+425 means (from table 139 row +16: 'tabs take focus' vs 'bar is display only').
