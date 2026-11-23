# Errand_ScoreParty

- **Address:** `0x1402D2DB0`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void Errand_ScoreParty(void)`
- **Callers:** Errand_ComputeRewards
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scores the 1 to 3 units sent on an errand and sets the party grade (0 best, 2 worst). It works on the active errand's globals and is the 'party matrix' of earlier notes.

## Behavior

- V: if the active record's flag has value 2 it zeroes all per-unit rewards, sets grade 2 and a forced-failure flag, and returns (Errand_RunningConfirmInput, the legacy list of dispatches away, sets that flag when a dispatch is called back).
- V: otherwise each unit's score is the sum of five bytes: job fit by errand category (8 rows of 22 columns), job fit by errand type (3 rows), a Brave score and a Faith score (5 values per type, index (stat - 1) / 20) and a level score.
- V: the job column is job - 74 for jobs 74..93, 21 for jobs 94 and above, and 22 for lower ids. Column 22 lies past a row's 22 columns (0..21), so a job below 74 (Ramza's own jobs) reads column 0 of the next category / type row; after the last type row it reads the two pad bytes (0).
- V: nothing random and no day count enters the grade (the days scale only the gil and JP, Errand_ComputeRewards); more units add their scores to the total.
- V: the level score index is 10 x (type - 1) + (level - 1) / 10 into the same base table as the Brave score, so for type 1 it re-reads the Brave values and for types 2 and 3 it runs into the Faith values.
- V: grade from the party total: below 59 gives 2, below 99 gives 1, otherwise 0. Per-unit scores are kept for Errand_ComputeRewards.
- V: a unit index of 54 or more falls back to a placeholder record.
- I: the level-score read is probably unintended; a separate rising 3 x 10 table exists in the data block but no code reads it.

## Referenced by

- Called by: [Errand_ComputeRewards](Errand_ComputeRewards.md)
- Reads tables: [ErrandBlob](../tables/ErrandBlob.md), [ErrandJobFitCategory](../tables/ErrandJobFitCategory.md), [ErrandJobFitType](../tables/ErrandJobFitType.md)

## Notes

The job-fit matrix is 8 category + 3 type scores per job id, read through header[3] / header[4] of the blob; code locations: both strides (imul imm8 at 0x1402D2F1A, 0x1402D2F24), row biases (disp8 at 0x1402D2FCB, 0x1402D300E) and the two column rules (0x1402D2F9F..0x1402D2FB8, 0x1402D2FDB..0x1402D2FF6).

Eight blob operands (0x1402D2DC1 .. 0x1402D2E2A: four header offsets and four `image base + offset + blob` leas). The column rule (0x1402D2F9F / 0x1402D2FB0 and 0x1402D2FDB / 0x1402D2FE7) and the 22-column stride (0x1402D2F17, 0x1402D2F22) are at those addresses.

Unit data is the 600-byte save record: job at +2, level at +0x1D, Brave +0x1E, Faith +0x1F.

## Open questions

Whether the level-score reading is a porting error.
