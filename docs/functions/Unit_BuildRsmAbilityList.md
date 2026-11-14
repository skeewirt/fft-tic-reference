# Unit_BuildRsmAbilityList

- **Address:** `0x140278358`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `uint16 Unit_BuildRsmAbilityList(UnitWork *c, uint16 request, char kinds, void *spawn)`
- **Callers:** Unit_InitAbilitiesFromJob (3)
- **Callees:** Skillset_GetAbility

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers a reaction / support / movement request of a spawn record: a fixed id is returned as is, a 'random' request (>= 0x1FE) picks one of the learned RSM abilities of the unit.

## Behavior

- V: request < 0x1FE: returned unchanged. Units flagged 0x20 at +6 get 0.
- V: walks the jobs 74..93 (list index 0..19; index 0 = the spawn job or the unit's marker job): the 3rd learned byte of each job (C +164 + 3 x index) selects slots 16..21 of the job's skillset; abilities 422..453 (reaction), 454..485 (support), >= 486 (movement) are collected by the kind bits.
- V: then picks one with the battle random generator.
- V: the compare of the request word with the bound 0x1FE and its jump are at 0x140278392; the first range test is at 0x1402784DB (the request mask is r9b, reloaded every slot).

## State touched

- Calls: [Skillset_GetAbility](Skillset_GetAbility.md)

## Referenced by

- Observed behaviours: [SpawnRecordPassiveWords](../behaviors/SpawnRecordPassiveWords.md)

## Notes

Only generic jobs are walked; this concerns generated units only (a player's unit equips through the job menus).

## Open questions

None recorded.
