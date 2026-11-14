# GUIWidget_Hide

- **Address:** `0x1403F93F8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIWidget_Hide(GUIWidget *w, char flags)`
- **Callers:** 16 UI addon methods (sub_1400E43B4, sub_1400EB0A4, sub_1400EB228, sub_14011245C, sub_140134EC8, sub_14013EB34, sub_14013EB98, sub_14013F40C, sub_14018834C, sub_140196F1C, sub_1401D1148, sub_1401D1A3C, sub_1401D1BA0, sub_1401D1EAC, sub_140207AA0)
- **Callees:** GUIWidget_FindFirstKind1Component2, GUINode_StopState, GUINode_PlayStateAtFrame, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Mirror of GUIWidget_Show: marks a widget hidden, plays the Hide state of its root component (Show stopped) and posts event 6.

## Behavior

- V: flags as GUIWidget_Show. When w+74 != 0 or bit1 is set: w+74 = 0; w+75 = (bit0 == 0) (set when the hide is animated, clear when instant); root = first kind-1 component; StopState(root, Show +4600), sub_140409824(root, Hide +4616, (bit0 == 0) - 1); event {6} is posted to w+288.
- V: when w+74 is already 0 and bit1 clear and bit0 set: only the Hide state of the root is snapped to its last frame.

## State touched

- Calls: [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The name is ours (IDB: sub_1403F93F8). sub_140134EC8 sits in the job tree address range (next to JobTree_OnCursorLeave at 0x1401346D4) and sub_1401D1BA0 / sub_1401D1EAC next to the JobTree_HandleInput helpers (I that they are tree code).

## Open questions

? w+75 consumer.
