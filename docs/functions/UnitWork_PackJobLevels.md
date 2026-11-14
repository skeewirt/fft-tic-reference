# UnitWork_PackJobLevels

- **Address:** `0x140278DA8`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `void UnitWork_PackJobLevels(const uint16_t *total_jp, uint8_t *out)`
- **Callers:** UnitWork_BuildFromSave, sub_140275EF4
- **Callees:** Job_LevelFromTotalJp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the packed job-level nibbles of a save record from the unit total-JP array, two jobs per byte.

## Behavior

- V: it reads ten 16-bit total-JP values from the first argument, one per job index 0..9.
- V: Job_LevelFromTotalJp converts each value to a level, and the low nibble of the first level becomes the high nibble of the output byte.
- V: the loop writes ten bytes, so 20 job levels are packed; the loop bound is 0x14 (20 values read as ten pairs).
- V: the first argument advances four bytes per output byte, so the JP array is a sequence of 16-bit entries, not a byte array.
- V: the second argument receives the packed bytes and is advanced one byte per iteration.
- I: the packed form matches the save field described as 12 bytes of 24 nibbles; this routine writes the first ten of those bytes.
- ?: how the remaining two bytes (jobs 20..23) are produced; this function stops at ten output bytes.

## State touched

- Calls: [Job_LevelFromTotalJp](Job_LevelFromTotalJp.md)
- Reads: [UnitSaveRecord.total_jp](../structs/UnitSaveRecord.md#total_jp)
- Writes: [UnitSaveRecord.job_levels](../structs/UnitSaveRecord.md#job_levels)

## Notes

Whole function read (98 bytes). Used on load, where the levels are recomputed rather than trusted from the file.

## Open questions

None recorded.
