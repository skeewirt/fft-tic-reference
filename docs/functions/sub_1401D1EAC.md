# sub_1401D1EAC

- **Address:** `0x1401D1EAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void sub_1401D1EAC(UIAddon *a, char flags)`
- **Callers:** JobTree_OnFocusChange, EventUnitObject_ApplyId and about 120 others
- **Callees:** sub_1403F93F8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Deactivates the addon's root widget (a+24) through sub_1403F93F8.

## Behavior

- V: w = *(a+24); if w+74 != 0 sets word a+42 = 0x100. sub_1403F93F8(w, flags): if w+74 != 0 or flags & 2: w+74 = 0, w+75 = (flags & 1) == 0, stops state +4600, plays +4616 (frame -1 when flags & 1, else 0), posts event 0x1407232B0; else if flags & 1 jumps +4616 to its end. Sets g_GUICore + 2126 = 1 when w+78 != 0.

## State touched

- Reads: [g_GUICore](../globals/g_GUICore.md)

## Referenced by

- Appears in flows: [ScreenAddonCreation](../flows/ScreenAddonCreation.md)
- Called by: [EventSubquestPanel_Run](EventSubquestPanel_Run.md), [EventUnitObject_ApplyId](EventUnitObject_ApplyId.md), [JobTree_OnFocusChange](JobTree_OnFocusChange.md), [UITitle_ShowPlayMode](UITitle_ShowPlayMode.md), [sub_140134B54](sub_140134B54.md), [sub_1402D67C8](sub_1402D67C8.md), [sub_14036AC74](sub_14036AC74.md)

## Notes

Proposed name UIAddon_Deactivate. JobTree_OnFocusChange calls it with 0 when the Job Tree loses focus (the id focus moves to is 1409) and then posts owner command 127.

## Open questions

? as sub_1401D1E30.
