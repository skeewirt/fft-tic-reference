# WindowCurvePointers

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x1406818C8`
- **Rows:** 5 rows of 8 bytes
- **Keyed by:** curve number 0..4
- **Read by:** [WindowRect_AnimateCurve](../functions/WindowRect_AnimateCurve.md)
- **Row layout:** [WindowCurvePointer](../structs/WindowCurvePointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointers to the five window open / close animation step lists. Verdict: pointer-table.

## Behavior

- V: WindowRect_AnimateCurve takes the list for its curve argument and steps through it until the value 4096
- V: the five lists start at 0x14078D8D8, 0x14078D828, 0x14078D858, 0x14078DA80 and 0x14078D808 (values grow towards 4096)

## Notes

Our names. Found beside the table at 0x140681890; tags V.

## Open questions

None recorded.
