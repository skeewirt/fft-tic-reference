# EaseCurvesSetG

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14071EFB0`
- **Rows:** 6 rows of 8 bytes
- **Keyed by:** pair index, from / to
- **Row layout:** [EaseEndpoints](../structs/EaseEndpoints.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Six start and end factors (0 to 1.0, 1.0 to 0, ...) used as ramp endpoints. Verdict: engine-data.

## Behavior

- V: 0x30 bytes up to the next table; two reads of dword [index * 2] and [index * 2 + 1]
- V: sub_14035C330: reads the pair at [index * 8] and [index * 8 + 4] and scales a distance by it

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

None recorded.
