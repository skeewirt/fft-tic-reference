# UnitPanelNumberFieldsA

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F4AF0`
- **Rows:** 15 rows of 32 bytes
- **Keyed by:** number field 0..14
- **Row layout:** [UiNumberField](../structs/UiNumberField.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number fields (Move, Jump, Wt, weapon powers, At, Def, Ar, Av and their magic pairs) of the unit status page, first panel. Verdict: designer-data.

## Behavior

- V: sub_14033054C (unit panel page task, task id 12): the table of the first panel; three groups are drawn from rows 0..2, 3..6 and 7..14 with the number drawer
- V: labels are readable in the rows (fifteen developer tags); the code draws rows at +96 and +224; 0x1E0 bytes = 15 rows up to the next table

## Notes

Our names. Tags: V layout, I that all 15 rows are used.

## Open questions

None recorded.
