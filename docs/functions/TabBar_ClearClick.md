# TabBar_ClearClick

- **Address:** `0x1402A9BD8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 TabBar_ClearClick(TabBar *t)`
- **Callers:** sub_14012B870, sub_1401319FC
- **Callees:** sub_14040ABDC, UIName_Key, GUINode_StopState, sub_1403D8D1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Releases the pressed state of the four tab nodes: for each existing node (kind 5) calls sub_14040ABDC(node, 0) and stops its 'Click' state.

## Behavior

- V: loops the four qwords at t+24..t+48; for a non-null node: if node+536 == 5 it calls sub_14040ABDC(node, 0); then UIName_Key('Click') and GUINode_StopState(node, key) with the key released afterwards.
- V (sub_14040ABDC(node, instant): ): only when byte node+648 is set: clears it, stops the state at qword_143CDA2A0 + 4792, plays the state at +4808 (sub_140409824, frame (instant ^ 1) - 1) and posts the event template xmmword_140723390 through GUIOwners_PostEvent(node+584). I.e. kind 5 (button) 'pressed' flag reset plus a release event.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_StopState](GUINode_StopState.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

Name proposed (IDB: sub_1402A9BD8). Kind 5 at node+536 is the button component (the same value the nested-state walk in GUINode_StopState uses).

## Open questions

? the texts of the keys +4792 / +4808 (I: press / release states of a button).
