# Unit_TryLearnAbility

- **Address:** `0x1402780B0`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `char Unit_TryLearnAbility(uint8_t *work, int jobIndex, int slot, uint16_t abilityId, char force, char payJp)`
- **Callers:** sub_1402781A8 (queues a job's abilities for learning, I)
- **Callees:** Rng_Percent, Ability_GetJpCost, sub_1403D325C, sub_1403D3AE8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Attempts to mark one ability of a job as learned in a work record, optionally charging JP and rolling the ability's learn chance. Returns 1 when the learned bit was set.

## Behavior

- V: nothing happens (returns 0) when the ability id is 0, or when `force` is 0 and the learn roll fails.
- V: the roll is Rng_Percent(100, learn_percent) == 0, where learn_percent is byte +2 of the ability's 8-byte aux record at 0x140787F80 + 8 * id.
- V: with `payJp` 0 the bit is set at once and no JP is touched.
- V: with `payJp` set, the cost is Ability_GetJpCost(id); if the unit's current JP for that job (u16 at work+240+2*jobIndex) covers it, the JP is deducted and the bit is set.
- V: when JP is short and `force` is set, the Ability table row is looked up (table id 39, result unused here) and the bit is set anyway without charging JP; with `force` 0 it returns 0.
- V: the learned bit is slot bit 7 - (slot mod 8) of byte slot / 8 in the job's 3-byte group at work+162+3*jobIndex.
- ?: the purpose of the row lookup in the forced-short-JP path (its result is never used in this function).

## State touched

- Calls: [Rng_Percent](Rng_Percent.md), [Ability_GetJpCost](Ability_GetJpCost.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [Unit_QueueJobAbilitiesToLearn](Unit_QueueJobAbilitiesToLearn.md)

## Notes

Its aux operand (lea at 0x1402780DD) reads learn_percent.

The work record is layout C: learned bits +162, current JP array +240. The party record B keeps the same data at +123 and +202.

## Open questions

Whether the forced path is used by battle learning with a short-JP unit, and what the row lookup is for.
