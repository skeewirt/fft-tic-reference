# UIGuide_Set

- **Address:** `0x1400EB65C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIGuide_Set(void *a1, int key, int rows)`
- **Callers:** ConfigMenu_UpdateFooter
- **Callees:** GuideBar_SetPage

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the guide bar's key and sub-row mask.

## Behavior

- V: uses the guide agent (agents array entry 14, +112) when it is active (its vtable +16), its add-on +64; calls GuideBar_SetPage(addon, key, rows).

## State touched

- Calls: [GuideBar_SetPage](GuideBar_SetPage.md)

## Referenced by

- Called by: [Battle_TimelineFocusCamera](Battle_TimelineFocusCamera.md), [ConfigMenu_UpdateFooter](ConfigMenu_UpdateFooter.md), [JournalScreen_OnAction](JournalScreen_OnAction.md), [WorldMapAgent_SetState](WorldMapAgent_SetState.md)
- Observed behaviours: [GuideBarLayout](../behaviors/GuideBarLayout.md)

## Open questions

None recorded.
