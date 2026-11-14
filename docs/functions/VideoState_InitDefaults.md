# VideoState_InitDefaults

- **Address:** `0x1402739E0`
- **Area:** [Display](../areas/display.md)
- **Prototype:** `void VideoState_InitDefaults(void)`
- **Callers:** sub_14000DFB8
- **Callees:** memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initialises the video/render state globals to their defaults.

## Behavior

- V: among many resets it sets g_UnitImageAspectOn (dword_142E7FCA0) = 1, so the unit image width factor 1.1408199 is active in normal play.

## State touched

- Writes: [g_UnitImageAspectOn](../globals/g_UnitImageAspectOn.md)

## Notes

The only store to g_UnitImageAspectOn found by cross-references is this one (value 1).

## Open questions

None recorded.
