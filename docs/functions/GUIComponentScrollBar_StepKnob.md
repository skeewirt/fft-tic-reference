# GUIComponentScrollBar_StepKnob

- **Address:** `0x14040BBF0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `_UNKNOWN **GUIComponentScrollBar_StepKnob(GUIComponentScrollBar *bar)`
- **Callers:** GUIComponentScrollBar_Update
- **Callees:** GUINode_FindState, sub_140400344 (track group by name), UIAnim_SampleFloatTrack, GUINode_FindPartByName, GUINode_IsAncestorDirty, GUINode_ResolvePinsDispatch, GUINode_SetPosition, GUINode_SetSize, GUIWidget_FindComponentCached, GUIComponent_SetAllocatedSize, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

While the bar has a pending move (+681), eases the shown position toward the target using the ScrollUp / ScrollDown state tracks, then sizes and places the Knob part inside the Base part and posts event 27.

## Behavior

- V: runs only when bar+681 != 0. ease = 1.0 and settled = 1. For the state 'ScrollUp' (+4968) and then 'ScrollDown' (+4984): when the state exists and its running byte (+105) is set, the float track at index 4 of the state's '#ScrollBar' (+5176) channel group (found by name with sub_140400344) is sampled at the state's current frame (+80) into ease and settled = 0.
- V: shown = (float)(target bar+648 - start bar+676) * ease + start (bar+676). So with no running scroll state the knob jumps to the target at once; with one it follows the authored ease track.
- V: parts 'Base' (+5096) and 'Knob' (+5112) are looked up with GUINode_FindPartByName(bar+272, ...). With both present: when bar+664 and +668 are both 0 the knob's authored size qword (knob+64) is stored there; the Base's pins are resolved when dirty (GUINode_IsAncestorDirty / GUINode_ResolvePinsDispatch).
- V: range = max(upper bar+656 - lower bar+652 - viewport bar+660, 0); frac = range > 0 ? clamp((shown - lower) / range, 0, 1) : 0. Vertical (bar+680 == 0): knob length L = base.h when range <= 0, else max(authored knob height (+668), base.h * viewport / max(upper - lower, viewport)) with C integer division; knob size = (knob.w, L), knob position = (knob.x, base.y + roundf((base.h - L) * frac)). Horizontal (bar+680 != 0): the same on the x axis with base.w and the authored width (+664) as the minimum length, size = (L, knob.h), position = (base.x + roundf((base.w - L) * frac), knob.y). The knob is set with GUINode_SetPosition and GUINode_SetSize; a reference-node knob (kind 12) also gets GUIComponent_SetAllocatedSize.
- V: when settled and bar+681 still set, bar+681 = 0. bar+672 = shown. Event {27} is posted to the owners.

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [UIAnim_SampleFloatTrack](UIAnim_SampleFloatTrack.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUINode_IsAncestorDirty](GUINode_IsAncestorDirty.md), [GUINode_ResolvePinsDispatch](GUINode_ResolvePinsDispatch.md), [GUINode_SetPosition](GUINode_SetPosition.md), [GUINode_SetSize](GUINode_SetSize.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [GUIComponent_SetAllocatedSize](GUIComponent_SetAllocatedSize.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUIComponentScrollBar_Update](GUIComponentScrollBar_Update.md)

## Notes

The name is ours (IDB: sub_14040BBF0). Companion to ScrollBar_SetPosition (position +648, lower +652, upper +656, viewport +660, smooth +672 / +676). The ease value comes from game data: a float track inside the ScrollUp / ScrollDown state, so the scroll speed of every list is authored, not coded. The orientation byte at +680 and the exact use of +676 as the start of the move are read from this function only.

## Open questions

? who sets +676 (the start value of an eased move) and +680 (orientation). ? the track's authoring (curve / length).
