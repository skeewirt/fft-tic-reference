# UnitEditorRangesB

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F8E40`
- **Rows:** 22 rows of 8 bytes
- **Keyed by:** editor field 0..21
- **Row layout:** [UnitEditorRange](../structs/UnitEditorRange.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Value ranges of the unit editor, mode B: rows 0..13 equal mode A, rows 14..18 each allow 1..356 where mode A allows 1..187 twice and then three ranges 428..453, 454..485, 486..509, rows 19..21 equal mode A. Verdict: designer-data.

## Behavior

- V: sub_14033BE88: copied into the live range table when the mode word is non-zero; the 0x420 bytes after it hold two widget tables (see notes)
- V: 0xB0 bytes of ranges (mode B differs from mode A only in rows 14..18), then two tables of 22 widget records (0x1408F8EF0 and 0x1408F9100, 24 bytes each) selected by the text language

## Notes

Our names. Tags: V ranges, I widgets.

## Open questions

- ?: widget record fields
