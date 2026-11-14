# UsableAbilityListLearnedBitGroup

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [sub_14030E368](../functions/sub_14030E368.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The usable-ability list reads a unit's learned bits per job group. For a skillset outside 5..0x17 that is the unit's primary or secondary skillset it takes group 0, which is right for the special characters' own sets.

## Behavior

- V (code): sub_14030E368 picks the group as skillset - 5 for 5..0x17, the hidden Dark Knight job's for 0xE0, 0 for a set equal to the unit's +0x12 or +0x192, and all 24 bits for any other set; every path meets at 0x14030E55A.
- V (live 2026-11-10): an Archer whose primary skillset was a set outside 5..0x17 listed its slots 1 and 2 as learned from group 0 (the unit's Squire bits 0x60) and not the ability learned in its Archer group.

## Open questions

None recorded.
