# GUINode_SetCursorOverState

- **Address:** `0x1400F5C78`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_SetCursorOverState(GUINode *node, _BYTE *opts, char isCursor)`
- **Callers:** sub_1400F58A4, sub_1400F5B0C, sub_1400F5BCC
- **Callees:** GUINode_FindState, GUINode_PlayState, GUINode_StopState, UIName_Key, sub_140409898, sub_1403D8D1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays the node's cursor animation states: on the cursor node CursorOver, on every other node CursorOut, honouring the Check / Uncheck pair of toggle nodes.

## Behavior

- V (guard): returns when node == 0 or (opts[3] == 0 and node+554 == 0) (node+554 is the 'enabled for pointer / cursor' flag).
- V (isCursor): reads state 'CursorOver' (GUINode_FindState by UIName_Key); v = state byte +105 (already playing / finished flag, same field tested elsewhere as 'is playing'). If v == 0: when opts[1] == 0 stops 'Check' and 'Uncheck'; stops 'CursorOut'; then sub_140409898(node, 'CursorOver', 0, flags) where flags = 4 if opts[0] != 0 else 8. Nothing is done when CursorOver is already active.
- V (not cursor): reads 'CursorOver' state byte +105. If it is NOT set: checks 'Check' state (+105) and opts[1] == 0: if the node is checked and opts[1] == 0 it stops Check, CursorOver, CursorOut and plays 'Uncheck' (state +104 = 1, GUINode_PlayState) and exits; otherwise if 'CursorOut' is already set it returns; otherwise if 'Uncheck' is set and opts[1] == 0 it returns. Then (reached also when CursorOver was set) when opts[1] == 0 stops 'Check' and 'Uncheck'; stops 'CursorOver'; plays 'CursorOut' (state +104 = 1, GUINode_PlayState).
- V: every UIName_Key result is released with sub_1403D8D1C(qword_143CDA2A0, key) when its refcount word is non-zero.
- V: sub_140409898(node, key, frames, flags) = find state, set +104 = 1, GUINode_PlayState, then set state+88-based start frame (a3 < 0 uses the state's own length at +88), +76 = frame / 60.0, +106 = 1, and from flags: &1 -> +107, &2 -> +110, &4 -> +108 = 1, &8 -> +108 = 0, &0x10 -> +109 = 1, &0x20 -> +109 = 0. So flag 4 / 8 sets a 'cursor sound-on / off' byte at state+108 (V byte, I meaning).

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_StopState](GUINode_StopState.md), [UIName_Key](UIName_Key.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Observed behaviours: [JobTreeHoverFade](../behaviors/JobTreeHoverFade.md)

## Notes

This is the generic hover / cursor highlight used by every list: GUI animation states named CursorOver, CursorOut, Check, Uncheck are authored in the node's state list; a node without them is silently ignored (FindState returns null). opts[0] chooses the +108 byte value 1 / 0 at CursorOver start.

## Open questions

? meaning of state bytes +105 / +107 / +108 / +109 / +110 (names guessed only from use: +104 start request, +105 playing, +106 started). ? what opts[3] is (it is the 'force' byte; no caller reads showed it set besides the Active / Deactive switcher).
