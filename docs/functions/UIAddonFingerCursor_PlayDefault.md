# UIAddonFingerCursor_PlayDefault

- **Address:** `0x1401D34B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFingerCursor_PlayDefault(UIAddonFingerCursor *addon)`
- **Callers:** vtable of UIAddonFingerCursor (slot 6, data)
- **Callees:** GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays the Default pose state on the Hand component (vtable slot 6 of the addon).

## Behavior

- V: with addon+48 present: state Default of addon+48: +104 = 1, GUINode_PlayState. g_GUICore+1908 = 1 in every case.

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Notes

The name is ours (IDB: sub_1401D34B4). Default is a one-frame state of the Hand: IconHand position and rotation 0 (V, UIB data). I: the bob state writes only the position, so the unrotated glove comes from this state having played once.

## Open questions

? Who calls slot 6 and when.
