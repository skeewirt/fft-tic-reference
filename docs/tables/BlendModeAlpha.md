# BlendModeAlpha

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x1407143E8`
- **Rows:** 4 rows of 1 bytes
- **Keyed by:** semi-transparency mode 0..3
- **Read by:** [Palette_ConvertToRgba](../functions/Palette_ConvertToRgba.md)
- **Row layout:** [BlendModeAlphaEntry](../structs/BlendModeAlphaEntry.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Alpha for each of the four semi-transparency modes (half, add, subtract, quarter). Verdict: engine-data.

## Behavior

- V: index masked with 3
- V: sub_14025D99C, sub_14025DB10, sub_14025DB94, sub_14025E274, sub_14025E2E4, sub_14025E358, sub_14025E3CC, sub_14025E440, sub_14025EB10: alpha = table[mode & 3] when semi-transparency is on

## Notes

Our names. Tags: V layout, I mode names.

## Open questions

- ?: mode 1 vs 2 (add vs subtract) is inferred from the values
