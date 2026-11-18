# LegacyCursorPalette

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FFC60`
- **Rows:** 24 rows of 2 bytes
- **Keyed by:** colour index 0..23
- **Row layout:** [Rgb555Colour](../structs/Rgb555Colour.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Palette words of the legacy cursor highlight (a pale ramp). Verdict: engine-data.

## Behavior

- V: 0x30 bytes of 15-bit colours, then zeros
- V: sub_1403980AC (0x1403980AC): word colours loaded for the page cursor highlight

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which palette slot it fills
