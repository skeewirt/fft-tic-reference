# Video_OnResize

- **Address:** `0x1401E7BA4`
- **Area:** [Display](../areas/display.md)
- **Prototype:** `__int64 Video_OnResize(__int64 window, int width, int height)`
- **Callers:** sub_1400B532C
- **Callees:** sub_1403CA57C, sub_1403CA668

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores the new backbuffer size for the main window and refreshes the unit-image width factor.

## Behavior

- V: only for the main window (qword_140C696A8 + 88); dword_140D3AD24 = width, dword_140D3AD4C = height; g_UnitImageAspectX = 1.1408199 when g_UnitImageAspectOn is non-zero, else 1.0; then sub_1403CA668 (viewport update).

## State touched

- Reads: [g_RenderDevice](../globals/g_RenderDevice.md), [g_UnitImageAspectOn](../globals/g_UnitImageAspectOn.md)
- Writes: [g_UnitImageAspectX](../globals/g_UnitImageAspectX.md)

## Open questions

None recorded.
