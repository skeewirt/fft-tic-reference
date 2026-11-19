# GUIWidget_FindComponentCached

- **Address:** `0x1403F9938`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponent *GUIWidget_FindComponentCached(GUIWidget *w, element *name, element *name2, GUIComponentCache *cache)`
- **Callers:** GUIComponentRef_Draw (ctx+488, ref+208, ref+224, ref+304), sub_140118438, sub_14013D064, GuideBar_LayoutRow, sub_140149148, sub_14014970C, sub_1401BED40, sub_1401BEF44, sub_1401BF48C, sub_1401BFB04
- **Callees:** sub_140098898, sub_140098A58

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a component by two name keys (+280 and +504) with a caller-owned cache cell: if the cell still holds a component whose two keys match it is returned at once, otherwise the same map and vector search as GUIWidget_FindComponentByName runs and the cell is refilled.

## Behavior

- V: returns 0 when the first name string is empty.
- V: fast path: when cache != 0 and *cache != 0 and the cached component's +504/+512 equals name2 and its +280/+288 equals name, that component is returned.
- V: slow path: the same map walk (ordered by the hash at node+32) and vector scan with cursor w+280 as GUIWidget_FindComponentByName, but a candidate must match name2 against its +504/+512 key as well as name against +280/+288 (hash compare when both nonzero, else string compare); a vector hit is re-inserted into the map (sub_140098898 / sub_140098A58).
- V: when found and cache != 0: *cache = component; cache[1] = component+600; component+600 = cache (the cell is pushed onto an intrusive list headed at component+600).

## Referenced by

- Called by: [ComponentEffects_Collect](ComponentEffects_Collect.md), [CreditRoll_AddPictureLine](CreditRoll_AddPictureLine.md), [GUIComponentList_GetHScroll](GUIComponentList_GetHScroll.md), [GUIComponentList_GetSlotComponent](GUIComponentList_GetSlotComponent.md), [GUIComponentList_GetVScroll](GUIComponentList_GetVScroll.md), [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md), [GUIComponent_ApplyStateAnims](GUIComponent_ApplyStateAnims.md), [GUIComponent_Disable](GUIComponent_Disable.md), [GUIComponent_Enable](GUIComponent_Enable.md), [GUIComponent_UpdateNodeTree](GUIComponent_UpdateNodeTree.md), [GUINode_ClearVisibleSubtree](GUINode_ClearVisibleSubtree.md), [GuideBar_LayoutRow](GuideBar_LayoutRow.md)

## Notes

The name is ours. For a component reference node the arguments are node+208 (first key), node+224 (second key) and node+304 (the cache cell, a {component, next} record).

## Open questions

What the second key (component +504) is (unverified); who walks the list at component+600 (probably invalidation when the component goes away; not read).
