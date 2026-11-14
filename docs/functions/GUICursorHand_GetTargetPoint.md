# GUICursorHand_GetTargetPoint

- **Address:** `0x1401D2FF8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUICursorHand_GetTargetPoint(GUICursorHand *hand, int out[2])`
- **Callers:** GUICursorHand_Update users
- **Callees:** GUIWidget_GetNodeScreenRect

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The hand's rest position for the focused component (left edge + hand+80, vertical centre + hand+84), or the screen centre (960, 540) when nothing is focused.

## Behavior

- V: the same rule as GUICursorHand_Update's second branch.

## State touched

- Calls: [GUIWidget_GetNodeScreenRect](GUIWidget_GetNodeScreenRect.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Open questions

None recorded.
