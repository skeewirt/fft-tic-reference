# LegacyListRowSlot

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140692EF0`
- **Rows:** 48 rows of 1 byte
- **Keyed by:** row code
- **Row layout:** [LegacyListRowSlotRow](../structs/LegacyListRowSlotRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sparse byte map from a list row code to a slot number; nearly all entries are 0. Verdict: engine-data.

## Behavior

- V: 0x30 bytes up to the next object; two readers test it for zero; only five entries are non-zero
- V: sub_140371F68 (legacy list screen task): tests table[row code] and skips the entry when it is 0 (two sites)

## Notes

Our names. Tags: V layout, ? meaning.

## Open questions

- ?: which screen's rows these are
- ?: what slots 1..5 are
