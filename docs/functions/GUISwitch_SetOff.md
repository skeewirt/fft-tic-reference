# GUISwitch_SetOff

- **Address:** `0x14040ABDC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUISwitch_SetOff(GUINode *node, int instant)`
- **Callers:** ConfigMenu_DrawRowValue
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets a switch node off: plays its state and posts event 22 (constant at 0x140723390).

## Behavior

- V: mirror of GUISwitch_SetOn.

## Referenced by

- Called by: [ConfigMenu_DrawRowValue](ConfigMenu_DrawRowValue.md)

## Open questions

None recorded.
