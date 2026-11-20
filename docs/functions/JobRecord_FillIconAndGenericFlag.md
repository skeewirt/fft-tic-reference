# JobRecord_FillIconAndGenericFlag

- **Address:** `0x1400FBEB8`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `bool JobRecord_FillIconAndGenericFlag(JobIcon *out, JobKey *key, char useId)`
- **Callers:** JobTree_FillJobRecords, sub_1402C185C, sub_14033751C
- **Callees:** sub_1400F8574, sub_1403DBC74

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks up the Job row, then the JobType table (id 0xC8) row, and stores an icon id (male/female) at out[0]; out[4] = 'not a generic job' flag.

## Behavior

- V: flag = (id - 74) > 0x13 when useId, else key[1] != 74.
- V: the icon is read from the JobType row (table 200) named by the Job row's job_type column (+0x18): the dword at +0x0C (column female_card_icon) when the byte key+8 is not negative (bit 7 clear), the dword at +0x08 (column male_card_icon) when bit 7 is set; no JobType row stores 0.
- V: this is the only reader of the JobType table in the executable; its columns +0, +4 are read by nothing.
- V: the icon id is the male JobType visual (row +8) when the sex byte at key+8 is negative, otherwise the female one (row +12); no row stores 0.

## Referenced by

- Called by: [JobChange_FillUnitEntry](JobChange_FillUnitEntry.md), [sub_1402C185C](sub_1402C185C.md)
- Observed behaviours: [JobCardComesFromTheJobTypeRow](../behaviors/JobCardComesFromTheJobTypeRow.md), [UnitFaceFromSpriteNumber](../behaviors/UnitFaceFromSpriteNumber.md), [UnreadColumnsOfJobAbilityStatusTables](../behaviors/UnreadColumnsOfJobAbilityStatusTables.md)

## Notes

I: bit 7 of the key byte is the male bit, because the code takes the male_card_icon column when it is set; which sex the bit means was not read from a sex test.

Shapes and records for a job come from the same key: see JobRecord_FromJobId.

## Open questions

None recorded.
