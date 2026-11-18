# EaseCurvesSetH

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14071EFE0`
- **Rows:** 5 rows of 12 bytes
- **Keyed by:** curve 0..4, 3 samples
- **Row layout:** [EaseSample3](../structs/EaseSample3.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Short 3-sample curves; the 0x80-byte object ends with a list of byte pairs (cell step offsets) that this reader does not use. Verdict: engine-data.

## Behavior

- V: address computed as table + index * 12 in sub_14035D5F0
- V: sub_14035D5F0 and sub_14035DDAC: row stride 12 (index * 3 dwords)

## Notes

Our names. Tags: V layout, ? tail.

## Open questions

- ?: the byte pairs at the end of the object
