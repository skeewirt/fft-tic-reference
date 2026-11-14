# GUIOwners_PostEvent

- **Address:** `0x1403DC22C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUIOwners_PostEvent(unsigned int ownerIds[4], GUINode *node, UIEvent *ev)`
- **Callers:** the GUIComponent virtuals (events 12..44)
- **Callees:** sub_1403DC1A8 (actor table lookup), owner OnEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Delivers a component event to every owner registered on the node: each non-zero id (node +584..+596) is resolved in the actor table and its vtable slot 2, OnEvent(owner, node, ev), is called.

## Behavior

- V: this is the dispatcher that reaches JobTree_OnEvent (vtable slot 2 of the tree addon); the job tree registers itself on every panel node in JobTree_RefreshAddon (writes the addon id into the node's owner array).

## State touched

- Reads: [g_GUIActorTable](../globals/g_GUIActorTable.md)

## Referenced by

- Called by: [GUIComponentCustom_CursorEnter](GUIComponentCustom_CursorEnter.md), [GUIComponentGauge_Step](GUIComponentGauge_Step.md), [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md), [GUIComponent_CursorLeave](GUIComponent_CursorLeave.md), [GUIComponent_Disable](GUIComponent_Disable.md), [GUIComponent_Enable](GUIComponent_Enable.md), [GUIComponent_OnClick](GUIComponent_OnClick.md), [GUIComponent_OnDown](GUIComponent_OnDown.md), [GUIComponent_OnFocusGained](GUIComponent_OnFocusGained.md), [GUIComponent_OnFocusLost](GUIComponent_OnFocusLost.md), [GUIComponent_OnUp](GUIComponent_OnUp.md), [GUIFontSlotGroup_OnPartTableLoaded](GUIFontSlotGroup_OnPartTableLoaded.md), [GUIFontSlotGroup_OnTextureLoaded](GUIFontSlotGroup_OnTextureLoaded.md), [GUINodeState_Advance](GUINodeState_Advance.md), [GUIWidget_AllResourcesLoaded](GUIWidget_AllResourcesLoaded.md), [GUIWidget_Hide](GUIWidget_Hide.md), [GUIWidget_PostReadyEvent](GUIWidget_PostReadyEvent.md), [GUIWidget_Show](GUIWidget_Show.md), [GUIWidget_Tick](GUIWidget_Tick.md)

## Notes

Event ids posted (templates at xmmword_1407232F0..): 12/13 select/deselect, 14..17, 18 (job tree panel tag), 19 component focus gained (CursorOver state), 20 focus lost (CursorOut), 21..27 scroll/drag, 31..36 list items, 38..41, 43/44 widget load/unload.

## Open questions

None recorded.
