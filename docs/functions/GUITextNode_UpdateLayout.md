# GUITextNode_UpdateLayout

- **Address:** `0x1403F1234`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUITextNode_UpdateLayout(GUITextNode *node)`
- **Callers:** GUIComponent_UpdateNodeTree, GUITextBoardComponent_Update, sub_1403D64F4 and about 30 screen update functions
- **Callees:** sub_1403DBA94, GUITextLayout_IconsReady, UIText_Get, GUITextNode_SetTextExpandedTemp, GUINode_IsAncestorDirty, GUITextNode_Layout

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame update of a text node: when its font is loaded (and its icons are, for icon nodes) refreshes the string from the text id and re-runs the layout, clearing the dirty byte on success.

## Behavior

- V: first sub_1403DBA94(g_GUIFontSlots, node+300) (font set index -> the font type for the current language -> the font's 'loaded' byte at set row + 16 * type + 145); 0 stops the update.
- V: when the node mode dword +416 is 3 (text with inline icons) GUITextLayout_IconsReady(node+320) must also be true.
- V: if the text id dword node+248 != 0, UIText_Get(id) fetches the string and GUITextNode_SetTextExpandedTemp(node, str) re-expands it (so a language change or a changed text id refreshes the string every update).
- V: if GUINode_IsAncestorDirty(node), node+296 = *(g_GUICore + 2096) (the frame counter used by the draw path); then GUITextNode_Layout(node+320, node); a result of 1 clears byte node+316 (the layout dirty flag).

## State touched

- Calls: [GUITextLayout_IconsReady](GUITextLayout_IconsReady.md), [UIText_Get](UIText_Get.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md), [GUINode_IsAncestorDirty](GUINode_IsAncestorDirty.md), [GUITextNode_Layout](GUITextNode_Layout.md)
- Reads: [g_GUICore](../globals/g_GUICore.md), [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Referenced by

- Called by: [Launcher_FillControls](Launcher_FillControls.md)
- Observed behaviours: [GUITextNodeStringSource](../behaviors/GUITextNodeStringSource.md)

## Notes

The name is ours (IDB: sub_1403F1234). Consequence for the Job Tree: text nodes re-expand and re-lay-out on every update while their font is loaded; hover does not trigger it specially.

## Open questions

? what g_GUICore+2096 is named (value stored to node+296).
