# MenuCtl_ListCursorStep

- **Address:** `0x140378B88`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t MenuCtl_ListCursorStep(int *record)`
- **Callers:** Errand_StatusMenuInput, Errand_ProgressListInput, Errand_UnitListInput
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves the cursor of a vertical list screen by one row on an up or down press.

## Behavior

- V: with more than one row (dword 12) it moves the cursor row (dword 7) with wrap and the cursor's y word by 16 pixels, and plays cue 3.

## Referenced by

- Called by: [Errand_ProgressListInput](Errand_ProgressListInput.md), [Errand_StatusMenuInput](Errand_StatusMenuInput.md), [Errand_UnitListInput](Errand_UnitListInput.md)

## Open questions

None recorded.
