# JobScreen_BuildTabList

- **Address:** `0x140367A30`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int64 JobScreen_BuildTabList(void *screen, unsigned tab, int mode, char flag)`
- **Callers:** JobChange_FillUnitEntry, sub_140367D24
- **Callees:** JobScreen_BuildJobTabRows, sub_14028A8B0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the list of one tab of the ability screen of the selected party unit into word_142E93E40: tab 1 = the secondary skillsets as (job, skillset) entries, tabs 2..5 = sub_14028A8B0's lists.

## Behavior

- V: tab 0 returns -1; tab 1 calls JobScreen_BuildJobTabRows(g_SelectedUnitIndex, the unit's job word +0x24, 0, word_142E93E40, 1), which is Unit_CollectJobSkillsetPairs; tabs 2..5 call sub_14028A8B0(screen, tab - 1, word_142E93E40, mode, flag); other tabs return 0.

## State touched

- Calls: [JobScreen_BuildJobTabRows](JobScreen_BuildJobTabRows.md), [sub_14028A8B0](sub_14028A8B0.md)

## Referenced by

- Observed behaviours: [SecondarySkillsetListsTakeEveryUnlockedJob](../behaviors/SecondarySkillsetListsTakeEveryUnlockedJob.md)

## Notes

The list word_142E93E40 holds 146 entries (its initialiser sub_14000E114 writes 146). I: the name, from the dispatch; which screen the tabs belong to is inferred from the callers' names.

## Open questions

? whether the screens that read word_142E93E40 (sub_14033564C, sub_1403358FC, sub_1403369F8, sub_140367D24) show more than a screenful of entries (live check).
