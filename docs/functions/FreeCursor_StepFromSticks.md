# FreeCursor_StepFromSticks

- **Address:** `0x14016D440`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `double FreeCursor_StepFromSticks(PointerAddon *a1, InputState *in)`
- **Callers:** sub_14016CF24 (the addon's input handler; it sends cancel to the owner on action 27)
- **Callees:** Input_IsActionHeld, GUICore_SetCursorTarget, sub_1403D6F70, UIAgentCursor_Show, sub_1401D2F80

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves a screen-space pointer (the finger cursor) from the left stick or from four direction actions and hit-tests what is under it.

## Behavior

- V: returns at once when a1+736 is not -1. dt = g_GUICore+2100 (the UI frame time). dx = truncate(in[+1224] * dt * 1000 * 0.01), dy = truncate(in[+1225] * dt * 1000 * -0.01): the left stick moves the pointer by axis * dt * 10 pixels (signed bytes -100 .. 100).
- V: with no stick input, actions 0x21 .. 0x24 (33 .. 36, tested with Input_IsActionHeld) give a fixed step of the same size in the four directions.
- V: the new point is clamped to 0 .. 1920 by 0 .. 1080 and held within 440 px of a second point (a1+624 / +628); the finger cursor widget is moved to it (sub_1401D2F80), the point is stored at a1+632, and the addon's virtual +80 hit-tests it: no hit clears the cursor target and the hover.
- V: sets a1+53 = 1 while the pointer moves; UIAgentCursor_Show is called afterwards.

## State touched

- Calls: [Input_IsActionHeld](Input_IsActionHeld.md), [GUICore_SetCursorTarget](GUICore_SetCursorTarget.md), [UIAgentCursor_Show](UIAgentCursor_Show.md)

## Referenced by

- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

The name is ours (IDB: sub_14016D440). Shows how this build reads the left stick as an analog pointer: a per-frame step proportional to the axis and the UI frame time. Which screen owns it was not identified.

## Open questions

? which addon owns it (a pointer-driven screen); ? whether g_GUICore+2100 is in seconds (I: yes, the UI frame time).
