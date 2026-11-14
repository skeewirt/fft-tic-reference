# GUITextBoard_FindTextNode

- **Address:** `0x14040AAC0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINode *GUITextBoard_FindTextNode(GUIComponent *comp)`
- **Callers:** GUITextBoardComponent_Update, UIAddonFFTOBattleMain4_vfunc_4 and about 18 addon functions
- **Callees:** GUINode_FindPartByName

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the text node (kind 3) of a text-board component: the part found by name key qword_143CDA2A0+5000 under comp+272, or null.

## Behavior

- V (live read 2026-10-28): the name key at qword_143CDA2A0+5000 is the C string "Title" (the text node every text board component names), so this returns the component's node called Title when its kind is 3.
- V: node = GUINode_FindPartByName(comp+272, qword_143CDA2A0 + 5000); returns node only when node != 0 and node+52 = 3, else 0.

## State touched

- Calls: [GUINode_FindPartByName](GUINode_FindPartByName.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUITextBoard_CacheAuthoredBox](GUITextBoard_CacheAuthoredBox.md)

## Notes

The name is ours (IDB: sub_14040AAC0). 5632 hits per 4 s.

## Open questions

? The name string at qword_143CDA2A0+5000 (set at runtime; not read).
