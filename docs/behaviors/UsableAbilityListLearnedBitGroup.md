# UsableAbilityListLearnedBitGroup

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [sub_14030E368](../functions/sub_14030E368.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The usable-ability list reads a unit's learned bits per job group. For a skillset outside 5..0x17 it takes group 0 when the set is the unit's primary (+0x12) or its special character's own set (+0x192), which is right for the special characters' own sets; any other such set, the secondary (+0x13) among them, counts every slot as learned.

## Behavior

- V (code): sub_14030E368 picks the group as skillset - 5 for 5..0x17, the hidden Dark Knight job's for 0xE0, 0 for a set equal to the unit's +0x12 or +0x192, and all 24 bits for any other set and for a monster (+0x06 & 0x20). The three group paths meet at 0x14030E55A (the reads of +0xA2..+0xA4 of the group); the all-bits path (0x14030E466, which sets the mask to all 24 bits) does not reach it.
- V (code): +0x192 is not the secondary skillset: it holds the set of the special character the unit's marker byte names (0 for a generic unit), so a secondary skillset outside 5..0x17 always lists every slot as learned.
- V (live 2026-11-10): an Archer whose primary skillset was a set outside 5..0x17 listed its slots 1 and 2 as learned from group 0 (the unit's Squire bits 0x60) and not the ability learned in its Archer group.

## Open questions

None recorded.
