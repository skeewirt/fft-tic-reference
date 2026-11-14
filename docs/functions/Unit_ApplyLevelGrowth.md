# Unit_ApplyLevelGrowth

- **Address:** `0x140278B24`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `uint8_t Unit_ApplyLevelGrowth(uint8_t *save, int levels)`
- **Callers:** sub_140289900 (hatching a monster from an egg, I)
- **Callees:** none (all arithmetic is inline)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Raises a save record's level by a number of levels, growing the five 24-bit stat accumulators at each step from the job row's growth C values.

## Behavior

- V: `save` is the UnitSaveData record (A): job id at +2, level at +29 (0x1D), accumulators at +32, +35, +38, +41, +44 (HP, MP, SP, PA, MA).
- V: the new level is min(level + levels, 99); one growth step runs per level actually gained.
- V: one step: for each stat, accumulator += accumulator / (level + C), then the 24-bit value is clamped; the level byte is incremented after all five stats. C is the even byte of the stat's pair at job row +14+2i, and a C of 0 counts as 1.
- V: the row is chosen by the job id at +2, with one substitution: job 161 uses row 164 when the low nibble at +126 (the level of job index 21) is 8 or more.
- V: returns the final level (the capped target when no level was gained).
- I: the row-164 substitution is a second growth profile for the hidden job 161 once it reaches level 8.

## Notes

Only the M byte of each pair is ignored here; it is used later by Unit_ComputeStats. The step matches the per-level loop that Unit_ComputeStats replays for generated units.

## Open questions

What row 164 holds in the stock build and whether any other caller reaches this routine.
