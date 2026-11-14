# GUIComponent_CursorLeave

- **Address:** `0x14040A298`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponent_CursorLeave(GUIComponent *comp)`
- **Callers:** vtable slot +48 of 16 component classes (GUICore_SetCursorTarget and sub_1403D6F70 call virtual +48 on the old cursor target)
- **Callees:** GUICore_GetFocus, GUINode_PlayCursorOutState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Component virtual +48: the GUI cursor target moved away; plays CursorOut unless the component keeps its cursor look while focused, and posts event 13.

## Behavior

- V: (focusWidget, focusNode) = GUICore_GetFocus(g_GUICore). When there is no focus, or the focused node is not this component, or byte comp+569 is 0: GUINode_PlayCursorOutState(comp). So a focused component with +569 set keeps its CursorOver look.
- V: always posts event {13} to the owners (comp+584, source comp).

## State touched

- Calls: [GUICore_GetFocus](GUICore_GetFocus.md), [GUINode_PlayCursorOutState](GUINode_PlayCursorOutState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Notes

The name is ours (IDB: sub_14040A298). Counterpart of GUIComponentCustom_CursorEnter (event 12). Meaning of comp+569 ('stay lit while focused') is I.

## Open questions

? what +569 is called in the component class.
