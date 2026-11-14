# GenericUnitSpriteNumberFromJob

- **Kind:** observed behaviour
- **Scope:** engine (unit sprite selection)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md), [Unit_ResolvePreviewShape](../functions/Unit_ResolvePreviewShape.md), [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [Job_IdToIndex](../functions/Job_IdToIndex.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A generic unit has no stored sprite number: the game derives it from the job and the sex, with the same sum in at least ten places, and every other job id falls back to a default.

## Behavior

- I (address list checked to exist in our database): the sprite number of a male generic unit is twice the job id minus 0x34 and a female unit's is one more (Mime, 0x5D, one lower); the sum is computed at 0x1402C082F (Unit_GetSpriteSetId), 0x1402B573F (PartyUnit_BuildJobRecord), 0x1402DB44D, 0x1403009BD, 0x140300F95 and 0x14032ABEA, each reading the job byte twice, and Unit_ResolvePreviewShape computes (job + 0x26) * 2 + the sprite set.
- V (decompiled, 2026-11-08): Job_IdToIndex returns job - 74 for jobs 74 to 93, job - 140 for 160 and 161, and 0 for every other id, so an unknown job id selects the first job's slot (the Squire's), not an error.
- I: the sprite byte of a battle actor sits at actor +0xA and is copied from the per-unit graphics record array (sprite id at +1 of each 0x32D6-byte record); a roster record's first byte is the sprite set: below 0x80 a story sprite number, 0x80 a male generic unit, 0x81 a female one, 0x82 a monster.
- I: for a sprite pair (S, S + 1), S even, the job value (S + 0x34) / 2 makes the game's own sum give S for men and S + 1 for women; the values for the spare pairs 88/89, 90/91, 92/93, 94/95, 156/157 and 164 to 169 are 70 to 73, 104 and 108 to 110, none of which the functions special-case.

## Open questions

? the six sprite readers in the battle code (0x2DB09C, 0x300768, 0x300D74, 0x32AB3C) were not each decompiled by us.
