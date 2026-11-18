# Job_ReadLearnedBitsForBattle

- **Address:** `0x14020D190`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Job_ReadLearnedBitsForBattle(UnitWork *c, ...)`
- **Callers:** the battle ability menu builders
- **Callees:** Job_IdToIndex, Skillset_GetAbility

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Walks the skillset of a work record's current job and tests each slot's learned bit (3 bytes at C +162 + 3*index).

## Behavior

- V: index from Job_IdToIndex(c +3); copies the 3 learned bytes to the stack, then for each slot tests bit (0x80 >> slot%8) of byte slot/8 and asks Skillset_GetAbility(c +18 skillset, slot).

## State touched

- Calls: [Job_IdToIndex](Job_IdToIndex.md), [Skillset_GetAbility](Skillset_GetAbility.md)

## Referenced by

- Observed behaviours: [JobArrayAccessesPutTheRecordPointerInTheIndexRegister](../behaviors/JobArrayAccessesPutTheRecordPointerInTheIndexRegister.md), [JobArraysInThePartyRecordHoldStockIndicesOnly](../behaviors/JobArraysInThePartyRecordHoldStockIndicesOnly.md)

## Notes

None.

## Open questions

I: name from the reads; the output list is not traced.
