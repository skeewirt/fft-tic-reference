# EaseCurvesSetA

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14071EA40`
- **Rows:** 56 rows of 4 bytes
- **Keyed by:** curve * samples + step
- **Row layout:** [EaseSample](../structs/EaseSample.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Easing curve set for legacy screen animations: 6 curves of 9 samples (linear up, linear down, ease up, ease down, bump, constant 1.0) plus a short tail. Verdict: engine-data.

## Behavior

- V: dword samples in 0..0x1000; the curves repeat a few shapes (ramp up, ramp down, ease-in-out up and down, bump, constant 1.0); readers multiply a distance by the sample and shift right by 12
- V: sub_140348924, sub_14034B9F0, sub_140358CCC, sub_1403554C4 and sub_140350DE4: index (curve * 9 + step) to interpolate positions and scales

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which animation uses which curve row
