# GUINode_ApplyStateAtFrame

- **Address:** `0x140409A98`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_ApplyStateAtFrame(GUINode *comp, NameKey *stateKey, int frame)`
- **Callers:** UIAddon code (Launcher / Title / Job tree screens: 11+ call sites), GUIAddon_OnStateEvent-style link handlers
- **Callees:** GUINode_FindState, GUINode_FindPartByName, GUINode_FindDescendant, sub_1404007FC, sub_1404015C0, sub_140400840

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Evaluates all property tracks of a named state at one frame and writes the results into the nodes, recursing into the nested state links.

## Behavior

- V: state = GUINode_FindState(comp, key); none -> nothing. frame < 0 -> frame = state+88 (the last frame); f = (float)frame.
- V: for each track group of the state (pointer vector state+144..+152): when sub_1404007FC(group) says the group is named with the component's own key (qword_143CDA2A0+5144, compared by interned id or string), sub_1404015C0(group, f, comp, state+111) applies the component-level properties; otherwise node = GUINode_FindPartByName(comp+272, group name) and sub_140400840(group, f, node, state+111) applies the node properties.
- V: for every entry of the state's list (state+176.., 64 bytes) with type 5 (nested state link): child = GUINode_FindDescendant(comp, entry+16), childState = GUINode_FindState(child, entry+32) and the function recurses with frame' = (int)fmaxf(((f - (float)entry+8) * (float)childState+88) / (float)(entry+12 - entry+8), 0.0) in single precision. The child frame is NOT clamped to its length here (GUIAddon_OnStateEvent clamps).

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUINode_FindDescendant](GUINode_FindDescendant.md)

## Referenced by

- Called by: [EquipDetail_SetHelpText](EquipDetail_SetHelpText.md), [sub_14013D844](sub_14013D844.md)

## Notes

The name is ours (IDB: sub_140409A98). sub_140400840 (3.4 KB) maps the track slots of a group onto node fields (V, read in part): slot 6 position -> GUINode_SetPosition(node+56/+60), 7 size (+64/+68), 8 scale (KeyTrackVec2_Eval -> node+80/+84), 9 rotation (float, +88, radians), 10 order (int +92), 11 colour (+100), 12 colour percent bytes (+104..+106), 13 opacity (+108), 14 visibility (KeyTrackBool_Eval -> +144), then kind specific ones (kind 2 image: +248 / +252 ints, kind 3 text colour +280). With state+111 (a4) == 0 the value is combined with the node's CURRENT field (position, size, rotation, order: added; scale, opacity: multiplied; colours: per channel x / 255), with a4 != 0 it replaces it. A pixel-exact simulator must apply the tracks in this order.

## Open questions

? Whether a4 == 0 (relative) accumulates when evaluated every tick: the node field is overwritten, so relative tracks need a base reset; not traced. ? Slots above 14 and kinds 4..10 in sub_140400840.
