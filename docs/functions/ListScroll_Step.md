# ListScroll_Step

- **Address:** `0x14028E720`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ListScroll_Step(ListScrollHelper *h, float rows)`
- **Callers:** ListScroll_HandleStick
- **Callees:** GUIComponentList_SetScrollY, GUIComponentList_IsItemVisible, sub_14040C29C, sub_14028D8F4, GUICore_FocusNode

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scrolls a component list vertically by rows x row height, then re-homes the focus when the focused item left the view.

## Behavior

- V: scroll y = list+680 - list+692 (row height) x (rows * -1), through GUIComponentList_SetScrollY(list, y, snap 1, clamp 1).
- V: when the cursor widget is active: if the focused item (h+96, when not negative) is not visible, the first visible usable item (scrolling down: scanned from the first shown item) or the last visible usable one (scrolling up) is focused with sub_14028D8F4(h, item, item, 0); when none is usable the focus is cleared (GUICore_FocusNode(0)). g_GUICore+2112 is set to 3 at the end.
- I: so a stick scroll never moves the focus while the focused item stays visible, and pulls it to the nearest visible item when it does not.

## State touched

- Calls: [GUIComponentList_SetScrollY](GUIComponentList_SetScrollY.md), [GUIComponentList_IsItemVisible](GUIComponentList_IsItemVisible.md), [GUICore_FocusNode](GUICore_FocusNode.md)

## Referenced by

- Called by: [ListScroll_HandleStick](ListScroll_HandleStick.md)
- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

The name is ours (IDB: sub_14028E720). The float argument is the step in rows (sign = direction), passed in xmm1. This is the game's own pattern for stick scrolling with a focused item.

## Open questions

? where the float comes from (value and scale).
