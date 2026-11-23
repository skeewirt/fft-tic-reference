# StatusGlossary_Open

- **Address:** `0x14036E1D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t StatusGlossary_Open(void)`
- **Callers:** Errand_UnitStatusInput
- **Callees:** WorldMenu_AllocOverlayRecord, ClassicCursorRows_Select

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the help page of a list of cursor rows and pushes kind 56.

## Behavior

- V: saves the previous value of 0x140D49ABC in the new record, creates a window (WorldMenu_AllocOverlayRecord), selects the cursor rows (ClassicCursorRows_Select) and pushes kind 56.

## State touched

- Calls: [WorldMenu_AllocOverlayRecord](WorldMenu_AllocOverlayRecord.md), [ClassicCursorRows_Select](ClassicCursorRows_Select.md)

## Referenced by

- Called by: [Errand_UnitStatusInput](Errand_UnitStatusInput.md)

## Notes

I: the name comes from the unit status page that opens it.

## Open questions

None recorded.
