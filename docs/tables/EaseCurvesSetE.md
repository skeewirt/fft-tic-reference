# EaseCurvesSetE

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14071ECB0`
- **Rows:** 72 rows of 4 bytes
- **Keyed by:** curve * samples + step
- **Row layout:** [EaseSample](../structs/EaseSample.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Easing curve set e: 72 samples (8 curves of 9), the shapes of set a plus a decay curve. Verdict: engine-data.

## Behavior

- V: dword samples in 0..0x1000; the curves repeat a few shapes (ramp up, ramp down, ease-in-out up and down, bump, constant 1.0); readers multiply a distance by the sample and shift right by 12
- V: sub_140350250, sub_1403585D4 and sub_140350DE4: curve * 9 + step

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which animation uses which curve row
