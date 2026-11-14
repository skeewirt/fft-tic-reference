# SpawnRecordPassiveWords

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Unit_BuildRsmAbilityList](../functions/Unit_BuildRsmAbilityList.md), [Unit_InitAbilitiesFromJob](../functions/Unit_InitAbilitiesFromJob.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle spawn record's reaction / support / movement word below 0x1FE names an ability and 0x1FE or above asks for a random one of the unit's skillset slots 16..21.

## Behavior

- V (code): Unit_BuildRsmAbilityList returns a word below 0x1FE as is; otherwise it gathers the unit's slot ids 16..21 per job and keeps them by stock ranges (R 422..453, S 454..485, M >= 486).
- V (code): Unit_InitAbilitiesFromJob puts the record's three words into the unit's learn queue only when below 0x1FE (three compares sharing dx = 0x1FE), then calls Unit_BuildRsmAbilityList for each (masks 2, 4, 8) and stores the answers at work +0x14 / +0x16 / +0x18.
- V (code): sub_1401EA638 copies an OverrideEntryData row's reaction / support / movement (row +0x20 / +0x24 / +0x28) to the spawn entry's +0x0C / +0x0E / +0x10 as u16.

## Open questions

None recorded.
