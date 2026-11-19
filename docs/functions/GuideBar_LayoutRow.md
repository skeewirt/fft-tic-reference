# GuideBar_LayoutRow

- **Address:** `0x14013D844`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GuideBar_LayoutRow(ButtonGuide *g, int *x, int slot, unsigned int row, char rightPass)`
- **Callers:** GuideBar_Layout
- **Callees:** GUINode_ApplyStateAtFrame, GUINode_SetPosition, GUINode_SetSize, GUINode_UpdateColourAndMatrix, GUINode_UpdateSubtree, GUITextNode_SetString, GUIWidget_FindComponentCached, UIName_Key, sub_14013DD70, sub_14028BE4C, sub_1403DBDF4, sub_1403F1234, sub_1403D8D1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Configures one guide slot for table 33 row `row`: sets the text, the up to four button icons (keyboard / pad variants), places the slot at x and starts its on-animation.

## Behavior

- V: row = sub_1403DBDF4(33, g+2224, row); skipped (returns 0) when the row's bit is clear in g+2228, the row's text id (+12) is 0 or its placement byte (+37) != rightPass.
- V: text: from the override map g+2288 (std::map keyed by row, string at node+32) when present else the row's text id into the text node at slot+240 (GUITextNode_SetString / dirty byte +316); the node is resized (GUINode_SetSize with text width, 432 - 424) and the slot width v47 is computed.
- V: icons: row dwords +4 / +16 (pad) or +28 / +32 (when UI config byte 13696 == 1) pick the primary / secondary button ids; when the pad icon ids are 19 / 20 it sets four ids {0x24, 0x22, 0x23, 0x21} (the four direction buttons: a 4-button group); each is passed to sub_14028BE4C (set the icon of the button part).
- V: 'Hide2ndButton / Show2ndButton', '3rdButton', '4thButton' states are applied (GUINode_ApplyStateAtFrame, frame -1) on the slot's widget according to the button count v39 = dword slot+164.
- V: sets the slot node's x with GUINode_SetPosition (x -= width on the right pass, += width on the left pass; extra buttons add g+2244 each), +144 = 1 visible, updates matrix / subtree, stores slot+264 = row, calls sub_14013DD70(g, row, placement) to fade it in. Returns 1.

## State touched

- Calls: [GUINode_ApplyStateAtFrame](GUINode_ApplyStateAtFrame.md), [GUINode_SetPosition](GUINode_SetPosition.md), [GUINode_SetSize](GUINode_SetSize.md), [GUINode_UpdateColourAndMatrix](GUINode_UpdateColourAndMatrix.md), [GUINode_UpdateSubtree](GUINode_UpdateSubtree.md), [GUITextNode_SetString](GUITextNode_SetString.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [UIName_Key](UIName_Key.md), [sub_14013DD70](sub_14013DD70.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GuideBar_Layout](GuideBar_Layout.md)
- Observed behaviours: [GuideBarLayout](../behaviors/GuideBarLayout.md)

## Notes

The 'four direction buttons' reading of the 19 / 20 group is I (ids 0x21..0x24 are the actions the direction helpers test). Column names of table 33 (UIButtonGuide, 2026-11-19): +4 guide_icon, +0xC title_text, +0x10 guide_icon_2, +0x1C key_texture, +0x20 key_texture_2, +0x25 right_aligned (the placement byte); +8 / +0x14 are the actions ui_key_assign / ui_key_assign_2.

## Open questions

Answered 2026-11-19: the dwords +28 / +32 are key_texture / key_texture_2 (V: in keyboard mode with +28 non-zero the slot icons are (+28, +32) flagged as keyboard keys, drawn from the key texture path 'ui/platform/win/textureparts/key_%03d_uitx' by sub_14028BE4C); the placement byte (+37) is right_aligned: GuideBar_Layout lays rows out twice, rightPass 0 from the left margin (g+2232) and rightPass 1 from 1920 minus the margin. ? the bar's role is still I (button hints), the Show / Hide Nth button states being the only strings read.
