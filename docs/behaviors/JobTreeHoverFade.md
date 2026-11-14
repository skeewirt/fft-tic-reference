# JobTreeHoverFade

- **Kind:** observed behaviour
- **Scope:** the focused Job Tree panel while its UnitJob CursorOver state plays
- **Area:** [Job tree](../areas/job-tree.md)
- **Affects:** [GUINode_PlayCursorOverState](../functions/GUINode_PlayCursorOverState.md), [GUINode_SetCursorOverState](../functions/GUINode_SetCursorOverState.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Focusing a panel plays the UnitJob component's CursorOver state at 60 Hz: the ring (UnitSelect) opacity 0 -> 1, the sprite (Unit) scale 1.125 -> 1.2 and the name tag fade in over frames 0 - 6 with the curves of the UIB timeline; drawn with the same layer and blend rules as the settled frame.

## Behavior

- V (live 2026-10-31, stock tree, Ramza as Squire, Squire focused): the panel's CursorOver state (component +616 vector, rate +0x48, time +0x4C, frame +0x50) was held at rate 0 before the cursor arrived, then set to frames 0 to 6 and each frame captured.
- V: writing the frame of a state that has finished changes nothing on screen; the state must be playing (here: started with rate 0).
- V (live 2026-10-31, a generic male unit with Squire and Chemist only, every job known to the party): the shaded (LockReleased) Arithmetician panel with its four red chips, frames 0 to 6: the whole frame outside the glove 97.9 % exact, the panel box mean 0.011 - 0.013, max 5, at every frame.

## Notes

Timeline keys and curves: the UIB CursorOver state.

## Open questions

None recorded.
