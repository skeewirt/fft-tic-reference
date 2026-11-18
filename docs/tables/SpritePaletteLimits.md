# SpritePaletteLimits

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** Executable
- **Address:** `0x140680970`
- **Rows:** 208 rows of 1 bytes
- **Keyed by:** sprite sheet id
- **Row layout:** [SpritePaletteLimit](../structs/SpritePaletteLimit.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per sprite sheet, the highest palette number its units may use. Verdict: engine-data.

## Behavior

- V: 0xD0 bytes to the next symbol
- V: sub_140221798 (event actor look resolve): palette = min(unit +4 + 8, table[sprite id])

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: exact count (sheet ids above 0xCF?)
