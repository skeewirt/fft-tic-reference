# LegacyCellRects

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FF810`
- **Rows:** 5 rows of 20 bytes
- **Keyed by:** rectangle 0..4
- **Row layout:** [LegacyCellRectsRow](../structs/LegacyCellRectsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Five 20-byte rectangle records (size, texture position and flag bytes) of legacy item page cells; the rest of the 0xD0-byte object holds pointers and floats. Verdict: designer-data.

## Behavior

- V: five records of identical shape, then pointer slots to buffers
- V: sub_140394C14 (legacy item page cell setup): selects a group by a byte list and passes the cell records to sub_14039AD30

## Notes

Our names. Tags: V layout, ? flags.

## Open questions

- ?: what each of the five rectangles is
