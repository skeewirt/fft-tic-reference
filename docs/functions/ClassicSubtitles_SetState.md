# ClassicSubtitles_SetState

- **Address:** `0x140196C80`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ClassicSubtitles_SetState(void *addon, int state, int keepShown)`
- **Callers:** sub_1401969CC, sub_140196E0C
- **Callees:** GUIWidget_FindFirstKind1Component2, UIName_Key, GUINode_FindState, GUINode_PlayState, UIName_ReleaseKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays the state of the classic subtitle window.

## Behavior

- V: plays 'Show' on the two window nodes (addon +48 and +56) for states 1..5.
- V: plays the state named by the string table at off_14070D810 (Hide, Line01 .. Line05) on the first kind-1 component; state 0 plays 'Hide' only when the keep-shown byte is 0.

## State touched

- Calls: [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [UIName_Key](UIName_Key.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [UIName_ReleaseKey](UIName_ReleaseKey.md)

## Notes

Name is ours.

## Open questions

None recorded.
