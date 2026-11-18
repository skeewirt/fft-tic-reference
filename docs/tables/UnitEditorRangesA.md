# UnitEditorRangesA

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F8D90`
- **Rows:** 22 rows of 8 bytes
- **Keyed by:** editor field 0..21
- **Row layout:** [UnitEditorRange](../structs/UnitEditorRange.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Value ranges of the 22 editable fields of the unit editor screen, mode A (level 1..99, brave / faith 0..100, three ability id ranges 144..171, 172..207, 208..239, ...). Verdict: designer-data.

## Behavior

- V: sub_14033BE88: copied into the live range table when the mode word is 0
- V: 22 pairs of two dwords (0xB0 bytes); the copy to the live table moves 0xA8 bytes (21 pairs)

## Notes

Our names. Tags: V layout, I field meaning.

## Open questions

- ?: which field each row is (the editor looks like a developer screen)
