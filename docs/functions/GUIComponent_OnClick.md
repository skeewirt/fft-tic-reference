# GUIComponent_OnClick

- **Address:** `0x14040A444`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponent_OnClick(GUIComponent *comp)`
- **Callers:** vtable slot +72 (GUICore_UpdateFrame calls it as virtual +72)
- **Callees:** GUINode_FindState, GUINode_PlayState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Component virtual +72: a completed click; plays the Click state and posts event 16.

## Behavior

- V: state = GUINode_FindState(comp, key +4760 = 'Click'); when it exists +104 = 1 and PlayState; event {16} to the owners.
- V (caller): GUICore_UpdateFrame calls it when comp+554 (enabled) is set, no re-target happened this frame and the release edge byte (a1+1902 or a1+1904, chosen by the press mode a1+2064) is set.
- V: JobTree_OnEvent case 0x10 (= 16) sets addon+12242, so a click on a panel marks it held; the addon base handler plays the click sound (a1+612) on event 16.

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The name is ours (IDB: sub_14040A444); 11 of the component vtables hold this entry (16 hold the Down / Up / cursor-leave entries), the rest override it.

## Open questions

None recorded.
