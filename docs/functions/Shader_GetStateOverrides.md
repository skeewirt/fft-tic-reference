# Shader_GetStateOverrides

- **Address:** `0x1403CFA94`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 Shader_GetStateOverrides(void *library, int shaderId, uint8_t *out)`
- **Callers:** stored in the shader library's virtual table (slot 5); no direct caller
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Adjusts a small state record for a shader id (flags that differ from the default for some of the built-in shaders).

## Behavior

- V: for the ids 1008, 1009, 1011, 1012, 1013, 1014, 1017, 1027, 1028, 1030, 1032 and 1033 the dword at out+0 is set to 1.
- V: for the ids 1000 and 1020 the byte at out+4 is cleared.
- V: for the ids 1026 .. 1035 the byte at out+5 is cleared.
- V: other ids leave the record as it was; the returned number is not meaningful.
- I: out+4 may be a depth-test flag (the post-effect and blur shaders do not clear it, the fill and debug-line shaders do), but the use of the record was not traced.

## Referenced by

- Observed behaviours: [DebugShadersAreRegisteredButNeverRequested](../behaviors/DebugShadersAreRegisteredButNeverRequested.md)

## Notes

Id 1020 is SHADER_ID_DEBUG_LINE.

## Open questions

? what reads the record and what the three fields mean.
