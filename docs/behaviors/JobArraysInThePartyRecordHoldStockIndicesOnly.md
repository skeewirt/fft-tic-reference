# JobArraysInThePartyRecordHoldStockIndicesOnly

- **Kind:** observed behaviour
- **Scope:** engine (party record)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [PartyUnit_FillFromWork](../functions/PartyUnit_FillFromWork.md), [JobRecord_FromJobId](../functions/JobRecord_FromJobId.md), [Job_ReadLearnedBitsForBattle](../functions/Job_ReadLearnedBitsForBattle.md), [Unit_TryLearnAbility](../functions/Unit_TryLearnAbility.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

In the 640-byte party record the per-job arrays are sized for the stock job indices, so an access with a larger index leaves its own array and, from a certain index, the record.

## Behavior

- V: record B (640 bytes, 55 of them): unlock mask +120 (3 bytes), learned bits +123 (66 bytes, 3 per job index) ending in a word at +187, job levels +189 (12 bytes, one nibble per index), current job points +202 (46 bytes, one word per index), second points array +248 (46 bytes) (PartyUnit_FillFromWork copies them from the save record).
- V (arithmetic of those offsets): the level of index n sits at +189 + n/2, so from n = 902 the address is outside the record (189 + 451 = 640) and in the record that follows; the learned bits of index n sit at +123 + 3n, so from n = 173 they start past the 640 bytes (123 + 3 x 172 = 639 is the last that starts inside), and below that, from n = 22, they overlap the level, points and later arrays of the same record.
- V: Job_IdToIndex answers 0 for every job id outside 74..93 and 160..161 (see UnlockMaskStreamRunsIntoLearnedBitsPastIndex23), so a stock job never produces a large index; an index above 23 reaches these arrays only from data that names such a job.
- I: the next record after a party record is the next party unit, so a read through an index past the record returns another unit's level or learned bits (zero for a unit with none).

## Notes

Record letters and offsets as in PartyUnit_FillFromWork and the sheets that cite A, B and C.

## Open questions

? the exact learned-bit overlap for indices 24 to 172 (they land on fields the stock code never reads at those offsets).
