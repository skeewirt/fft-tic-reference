# HdSheetGroups_ClearUsedMarks

- **Address:** `0x14041E3D8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void HdSheetGroups_ClearUsedMarks(void)`
- **Callers:** HdLayer_BuildTextures
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Called at the end of every HD texture pass: in each of the 20 sheet groups, frees the pieces and palette entries nothing used this frame and clears the used marks for the next one.

## Behavior

- V: for each group (count 20 at 0x14041E3DF): for the 128 piece entries (20 bytes from +4), an entry whose used dword (+20) is 0 gets its rectangle's first dword cleared, then the used dword is set to 0; for the 16 palette entries (+2564), an entry whose used flag is 0 gets the word -1, then the flag is set to 0.

## Referenced by

- Observed behaviours: [WordSeventeensArithmeticReachesNewSheetGroups](../behaviors/WordSeventeensArithmeticReachesNewSheetGroups.md)

## Open questions

None recorded.
