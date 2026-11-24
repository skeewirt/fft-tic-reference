# DrawMode_BuildShaderTable

- **Address:** `0x1403CECFC`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `bool DrawMode_BuildShaderTable(char *table)`
- **Callers:** sub_1403CC5D4 (a jump at 0x1403CC7BB); also stored in a pointer table
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills a 34-entry table that maps a draw mode number to a shader id, a variant number and a flag byte.

## Behavior

- V: for each mode 0..33 it writes three values at table+24+12*mode: the shader id (dword), a variant number (dword at +4) and a flag byte (+8, 1 when a variant applies).
- V: the default id is 1002; mode 1 gets 1005, mode 2 gets 1007, modes 5 and 6 get 1008, modes 7 and 8 get 1010, mode 9 gets 1011, mode 10 gets 1012, modes 11 to 16 get 1014, modes 17, 19, 30 and 32 get 1015, mode 18 gets 1016, modes 20 to 25 get 1017, modes 26, 27 and 29 get 1019 and mode 33 gets 1018.
- V: no mode is given 1020 or 1021.
- I: the variant numbers 1..13 select a sub-variant of the shader (rest on their grouping by mode only; not traced to a reader).

## Referenced by

- Observed behaviours: [DebugShadersAreRegisteredButNeverRequested](../behaviors/DebugShadersAreRegisteredButNeverRequested.md)

## Notes

Modes 0, 3, 4, 28 and 31 keep the default 1002.

## Open questions

? the meaning of the variant numbers and of the draw modes.
