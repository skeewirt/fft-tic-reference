# Video_RefreshState

- **Address:** `0x140255DEC`
- **Area:** [Display](../areas/display.md)
- **Prototype:** `__int64 Video_RefreshState(void)`
- **Callers:** sub_1401E79A0
- **Callees:** sub_1403CA57C, sub_1403CA668, sub_1402572BC, sub_1403D189C, sub_1403D1D90, sub_1401E774C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Re-applies the video state (mode flags, viewport, aspect factor) after a mode change.

## Behavior

- V: sets the update flags of the main window object, recomputes g_UnitImageAspectX with the same rule as Video_OnResize, refreshes the viewport (sub_1403CA668) and resets several frame-state globals.

## State touched

- Reads: [g_Application](../globals/g_Application.md), [g_UnitImageAspectOn](../globals/g_UnitImageAspectOn.md)
- Writes: [g_UnitImageAspectX](../globals/g_UnitImageAspectX.md)

## Referenced by

- Called by: [Boot_SetState](Boot_SetState.md)

## Notes

Only the head of this function was read (?).

## Open questions

None recorded.
