# GUIWidget_Tick

- **Address:** `0x1403FC14C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIWidget_Tick(GUIWidget *w, float dt)`
- **Callers:** GUICore_UpdateWidgets path (sub_1403D7670 and related)
- **Callees:** sub_1403FC5A0, sub_1403F9DA0, sub_1403F9D6C, GUINode_FindState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame update of one widget: rebuilds the node lists when flagged, delivers the pending-ready event, ticks the main component, and posts the update event 4 to the widget's owners.

## Behavior

- V: w+81 != 0 -> sub_1403FC5A0(w) (rebuilds the widget's lookup vectors; clears +81 itself).
- V: w+75 != 0 (pending): comp = sub_1403F9DA0(w) (main component); when it is missing, or its state with the key at qword_143CDA2A0+4616 is missing or not running (state+105 == 0), event {7} is posted (GUIOwners_PostEvent(w+288, w, ev)); when the owner left ev+12 == 0, w+75 = 0.
- V: main component comp = sub_1403F9D6C(w): when present, its virtual +32 is called (comp, dt, 0). I: dt is the incoming float argument, passed straight on (xmm6 in the disassembly).
- V: w+72 (byte countdown) is decremented when non-zero; event {4} is posted to w+288; w+68 = g_GUICore+2096 (the frame counter).

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_GUICore](../globals/g_GUICore.md), [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Called by: [GUICore_TickWidget](GUICore_TickWidget.md)

## Notes

The name is ours (IDB: sub_1403FC14C). Event 4 reaches JobTree_OnEvent (the 'held flag copy' in the addon's event handler). The key +4616 is one of the interned state names of qword_143CDA2A0 (next to +4664 CursorOver and +4680 CursorOut); its text was not read here.

## Open questions

? Text of the state key +4616 and the meaning of event 7 (I: 'widget ready / opened'; owners may veto it by setting ev+12).
