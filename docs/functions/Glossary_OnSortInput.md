# Glossary_OnSortInput

- **Address:** `0x140173AC4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Glossary_OnSortInput(void *screen)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Handles the glossary's sort command.

## Behavior

- V: sets the current tab's mode (+3488 + 4 * tab) to 2 when the chosen row (a1 + 968) is row 0, else 3; the screen's setup sets all three tabs to 1.

## Referenced by

- Observed behaviours: [GlossaryPagesAreMetRowsOfOneEntry](../behaviors/GlossaryPagesAreMetRowsOfOneEntry.md)

## Open questions

None recorded.
