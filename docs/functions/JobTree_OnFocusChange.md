# JobTree_OnFocusChange

- **Address:** `0x140133F30`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_OnFocusChange(JobTreeAddon *addon, int newFocus, int oldFocus)`
- **Callers:** UI system (vtable)
- **Callees:** GUICore_FocusNode, sub_1401D1E30, sub_1401D1EAC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Focus change handler (vtable slot 27): when the tree gains the input focus (id 1409) it puts the cursor back on the remembered panel; when it loses it, it tells its parent.

## Behavior

- V: second argument == 1409: sub_1401D1E30(addon, 0), then GUICore_FocusNode on the node of panel addon+12236 when that panel is within the cap (stock <= 0x13, the plan raises it).
- V: third argument == 1409: sub_1401D1EAC(addon, 0) and message 127 to the parent (addon+16, its vtable +48).
- I: the second argument is the focus gained and the third the focus lost (the first branch restores the cursor, the second reports to the parent).
- V: 1409 is the tree's input focus: sub_140115EA8 sends focus 1409 to JobTree_HandleInput and every other focus to the job list addon.

## State touched

- Calls: [GUICore_FocusNode](GUICore_FocusNode.md), [sub_1401D1E30](sub_1401D1E30.md), [sub_1401D1EAC](sub_1401D1EAC.md)

## Referenced by

- Observed behaviours: [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md)

## Notes

addon+12236 is written by JobTree_SetPanelRecord: the panel of the unit's current job, so a reopened tree starts on it.

## Open questions

None recorded.
