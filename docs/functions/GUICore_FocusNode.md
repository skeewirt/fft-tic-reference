# GUICore_FocusNode

- **Address:** `0x1401D2240`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUICore_FocusNode(GUINode *node)`
- **Callers:** JobTree_HandleInput, JobTree_OnFocusChange
- **Callees:** GUICore_SetFocusComponent, GUICore_IsFocusTarget, GUICore_IsCursorTarget, GUICore_SetCursorTarget, GUICore_GetFocus

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves the GUI focus (and with it the finger cursor) onto a node, or clears the focus when the node is null. The job tree calls it with a panel node for every cursor move.

## Behavior

- V: with a node: the owning widget is node+496; when sub_1403D6E8C(core, widget, node) reports the node is already the focus it returns that result, otherwise it clears the focus (sub_1403D6A64(core, 0, 0)) when sub_1403D6BFC(core, widget, node) is 0, calls GUICore_SetFocusComponent(core, widget, node) and finishes with sub_1403D6A64(core, widget, node).
- V: with a null node: clears the focus (sub_1403D6A64(core, 0, 0)), then, when a focus exists (sub_1403D6E28), empties the three key strings at core+1968 / +1984 / +2000, calls the old focus node's virtual +104 (focus lost) and sets core byte +2128 = 1.

## State touched

- Calls: [GUICore_SetFocusComponent](GUICore_SetFocusComponent.md), [GUICore_IsFocusTarget](GUICore_IsFocusTarget.md), [GUICore_IsCursorTarget](GUICore_IsCursorTarget.md), [GUICore_SetCursorTarget](GUICore_SetCursorTarget.md), [GUICore_GetFocus](GUICore_GetFocus.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Referenced by

- Called by: [GUIList_SetCount](GUIList_SetCount.md), [JobChangeAddon_SetState](JobChangeAddon_SetState.md), [JobTree_HandleInput](JobTree_HandleInput.md), [JobTree_OnEvent](JobTree_OnEvent.md), [JobTree_OnFocusChange](JobTree_OnFocusChange.md), [Launcher_DrawStartPage](Launcher_DrawStartPage.md), [ListScroll_Step](ListScroll_Step.md), [TabBar_Select](TabBar_Select.md), [TitleMenu_FocusCurrent](TitleMenu_FocusCurrent.md), [TitleMenu_MoveCursor](TitleMenu_MoveCursor.md), [UISaveLoad_StateEnter](UISaveLoad_StateEnter.md), [UISaveLoad_StateSourcePick](UISaveLoad_StateSourcePick.md), [WorldMapBaseList_SelectTab](WorldMapBaseList_SelectTab.md), [sub_1400F5674](sub_1400F5674.md), [sub_1400F5B0C](sub_1400F5B0C.md), [sub_1400F5BCC](sub_1400F5BCC.md), [sub_140131068](sub_140131068.md), [sub_1401365AC](sub_1401365AC.md), [sub_1401839E4](sub_1401839E4.md), [sub_140197BCC](sub_140197BCC.md), [sub_1403358FC](sub_1403358FC.md), [sub_1403456D4](sub_1403456D4.md)
- Observed behaviours: [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md)

## Notes

The finger cursor widget follows the focused node; its placement is a widget transform, not a node position (live read: the Hand layer position did not change while the cursor moved). The code that converts the focus node into that transform was not located.

## Open questions

None recorded.
