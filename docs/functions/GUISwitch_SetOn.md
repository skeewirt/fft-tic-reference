# GUISwitch_SetOn

- **Address:** `0x14040AB40`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUISwitch_SetOn(GUINode *node, int instant)`
- **Callers:** ConfigMenu_DrawRowValue
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets a switch node on: plays its state and posts event 21.

## Behavior

- V: a switch node has kind 4 at +536 and its on flag at +648; the event goes to the add-on ids in its listener slots +584 (4 slots); the event constants are at 0x140723380.

## Referenced by

- Called by: [ConfigMenu_DrawRowValue](ConfigMenu_DrawRowValue.md)

## Open questions

None recorded.
