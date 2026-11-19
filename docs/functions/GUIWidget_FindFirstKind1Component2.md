# GUIWidget_FindFirstKind1Component2

- **Address:** `0x1403F9DA0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponent *GUIWidget_FindFirstKind1Component2(GUIWidget *w)`
- **Callers:** GUIWidget_Tick, JobTree_RefreshAddon, WorldMapScreen_BindNodes, many UIAddonFFTO*_vfunc_4 (181 callers)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same search as GUIWidget_FindFirstKind1Component, pointer-iterator form; used by most addon update methods.

## Behavior

- V: iterates the component vector w+104..+112; returns the first comp with dword +536 = 1, else 0.

## Referenced by

- Called by: [BarTop_Setup](BarTop_Setup.md), [Battle_MenuShowPage](Battle_MenuShowPage.md), [ClassicSubtitles_SetState](ClassicSubtitles_SetState.md), [GUIWidget_Hide](GUIWidget_Hide.md), [GUIWidget_Show](GUIWidget_Show.md), [StatusScreen_DrawLists](StatusScreen_DrawLists.md), [UIAddonFingerCursor_Bind](UIAddonFingerCursor_Bind.md), [UIAddonFingerCursor_FreezePose](UIAddonFingerCursor_FreezePose.md), [UIAddonFingerCursor_PlayLoop](UIAddonFingerCursor_PlayLoop.md), [UIAgentCursor_Hide](UIAgentCursor_Hide.md), [sub_1401D1E70](sub_1401D1E70.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)

## Notes

The name is ours (IDB: sub_1403F9DA0). 28 hits per 4 s.

## Open questions

None recorded.
