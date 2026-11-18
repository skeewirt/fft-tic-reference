# EaseCurvesSetC

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14071EBD0`
- **Rows:** 20 rows of 4 bytes
- **Keyed by:** curve * samples + step
- **Row layout:** [EaseSample](../structs/EaseSample.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Easing curve set c: 20 samples of small step curves (0, 0x800, 0x1000 ramps). Verdict: engine-data.

## Behavior

- V: dword samples in 0..0x1000; the curves repeat a few shapes (ramp up, ramp down, ease-in-out up and down, bump, constant 1.0); readers multiply a distance by the sample and shift right by 12
- V: sub_14034DE90: curve * 9 + step

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which animation uses which curve row
