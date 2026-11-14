# g_JobAbilityPairList

- **Kind:** global
- **Address:** `0x142E93E40`
- **Type:** `job data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

146 entries of 8 bytes (word 0 = job, word 1 = skillset or ability id, words 2..3 unused by the producers); a list ends at the entry whose word 1 is 0xFFFF. sub_14000E114 initialises all 146 (0, 0xFFFF). Written by JobScreen_BuildTabList (secondary skillset pairs, or sub_14028A8B0's ability rows); read by sub_14033564C, sub_1403358FC, sub_1403369F8 and sub_140367D24.

## Referenced by

- Described by tables: [JobAbilityPairList](../tables/JobAbilityPairList.md)
- Observed behaviours: [SecondarySkillsetListsTakeEveryUnlockedJob](../behaviors/SecondarySkillsetListsTakeEveryUnlockedJob.md)

## Open questions

None recorded.
