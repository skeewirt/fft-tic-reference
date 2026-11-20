# PoachResultFromJob

- **Kind:** observed behaviour
- **Scope:** engine (Poach action)
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [Poach_GiveResult](../functions/Poach_GiveResult.md), [Job_HasMonsterPair](../functions/Job_HasMonsterPair.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A successful Poach gives the PoachItem named by the target unit's job: usually the job's poach_item, about one time in eight its poach_item_rare.

## Behavior

- V: Poach_GiveResult reads the acting unit's job byte (+3), the Job row (table 46) and Rng_Percent(256, 31) (true when 256 * rand15 / 0x8000 >= 31, 225 of 256 draws): true -> Job +0x24 (poach_item), false -> Job +0x28 (poach_item_rare).
- V: the value is a PoachItem row id (table 236); when it is above 96 or its held count (g_PoachCount) is below 99 the item is added, otherwise the gil given is the PoachItem row's dword +0x28 halved.
- V: Job_HasMonsterPair is true when either column is non-zero: the job can be poached. The two columns are not a monster sprite or portrait pair.
- M: stock poach_item values are odd ids 1..95 on the poachable jobs and 0 on the others; poach_item_rare is always poach_item + 1.

## Open questions

None recorded.
