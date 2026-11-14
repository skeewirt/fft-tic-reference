# BattleRangeMarks

- **Kind:** table
- **Storage:** Executable (filled at run time)
- **Rows:** 2560 entries of 1 byte
- **Held in:** [g_BattleRangeMarks](../globals/g_BattleRangeMarks.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Range-mark array: 512 records of 5 bytes, index x + y * width + 256 * layer (layer 1 at +0x500). Byte 0 = in reach (a spread value or 1), byte 1 = spread frontier; written by the BattleRange_* builders, read by BattleRange_FlagTargetTiles.

## Open questions

None recorded.
