# AbilityLearnedByBeingHit

- **Kind:** observed behaviour
- **Scope:** engine (ability aux flags3 bit 0x20)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [sub_14030CD08](../functions/sub_14030CD08.md), [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An ability whose AbilityAux flags3 has bit 0x20 can be learned by a unit it hits, when the unit's job skillset lists it.

## Behavior

- V: after an action whose ability has the bit, sub_14030CD08 names the first unit (other than the user) that was hit, has no status of group 4, whose job's skillset lists the ability and who has not learned it, with chance AbilityAux +2 percent per candidate slot.
- V: flags3 bit 0x80 is the opposite switch for JP learning: the ability is left out of the Learn list (JobAbilityList_Build) and a learned one gets token flag 0x6000 instead of 0x4000.

## Open questions

? how the caller applies the result.
