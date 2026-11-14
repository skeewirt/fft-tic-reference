# GUIComponent_Disable

- **Address:** `0x140408FF8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponent_Disable(GUIComponent *comp, char recurse)`
- **Callers:** about 24 UI addon methods (UIAddonFFTOTitlePlaymode_vfunc_14, sub_1400EA5B8, sub_140116914, sub_1401B7884, sub_1402B0984, ...)
- **Callees:** GUIWidget_FindComponentCached, GUINode_StopState, GUINode_FindState, GUINode_PlayState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Mirror of GUIComponent_Enable: clears +554, plays the Disable state (Enable stopped) and posts event 11.

## Behavior

- V: same recursion over the widget's reference nodes with GUIComponent_Disable(child, 1).
- V: when comp+554 != 0: comp+554 = 0; StopState(comp, 'Enable' +4632); FindState(comp, 'Disable' +4648) +104 = 1, PlayState; event {11}.

## State touched

- Calls: [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [JobChangeAddon_SetState](JobChangeAddon_SetState.md)

## Notes

The name is ours (IDB: sub_140408FF8). With +554 = 0 the press / click virtuals are not called (GUICore_UpdateFrame calls the disabled-click virtual +80 instead).

## Open questions

None recorded.
