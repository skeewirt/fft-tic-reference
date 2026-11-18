# UITitle_ShowPlayMode

- **Address:** `0x1401C3CE0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UITitle_ShowPlayMode(UIAgentFFTOTitle *agent)`
- **Callers:** not recorded
- **Callees:** sub_1401D1EAC, sub_1401D1E30

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Hides the title menu add-on and shows the play mode add-on.

## Behavior

- I: hides with `sub_1401D1EAC(addon, 1)` and shows with `sub_1401D1E30(addon, 0)` (the add-on hide and show calls).

## State touched

- Calls: [sub_1401D1EAC](sub_1401D1EAC.md), [sub_1401D1E30](sub_1401D1E30.md)

## Referenced by

- Observed behaviours: [ScreenMusicComesFromBGMTransitionRows](../behaviors/ScreenMusicComesFromBGMTransitionRows.md)

## Open questions

None recorded.
