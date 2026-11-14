# GUIWidget_Show

- **Address:** `0x1403F930C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIWidget_Show(GUIWidget *w, char flags)`
- **Callers:** sub_1400EB0A4, sub_1400EB228, sub_14013EB34, sub_140181980, sub_1401881A8, sub_140196E0C, sub_1401D1E30, sub_140207AA0 (UI addon open paths)
- **Callees:** GUIWidget_FindFirstKind1Component2, GUINode_StopState, GUINode_PlayStateAtFrame, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks a widget shown and plays the Show state of its root component (Hide state stopped); posts owner event 5.

## Behavior

- V: flags bit0 = instant (skip to the last frame), bit1 = force. When byte w+74 is 0 or bit1 is set: word w+74 = 1 (w+74 = 1, w+75 = 0); root = GUIWidget_FindFirstKind1Component2(w); when it exists GUINode_StopState(root, Hide key +4616) and sub_140409824(root, Show key +4600, frame) with frame = (bit0 == 0) - 1, i.e. 0 for an animated show, -1 (last frame) for an instant one; then event {5} is posted with GUIOwners_PostEvent(w+288, w, ev).
- V: when w+74 is already 1 and bit1 is clear and bit0 is set: only the Show state of the root is snapped to its last frame (sub_140409824(root, Show, -1)); no event, no flag change.
- V: when w+74 is already 1 and bit0 is clear nothing happens.

## State touched

- Calls: [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The name is ours (IDB: sub_1403F930C). The Show / Hide states are authored in the UIB on the root component. 'a1' is a widget, not a component: it reads the root through the widget's component vector (w+104..+112, kind 1 = Root).

## Open questions

? the exact contract of w+75 and who reads w+74 (hit testing / draw?). ? the meaning of the flag combination values the callers use.
