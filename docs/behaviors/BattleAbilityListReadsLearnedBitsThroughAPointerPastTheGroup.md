# BattleAbilityListReadsLearnedBitsThroughAPointerPastTheGroup

- **Kind:** observed behaviour
- **Scope:** engine (battle ability list)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [sub_14030E368](../functions/sub_14030E368.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle's usable-ability list builder reads the three learned bytes of a job group from a battle record with the group number in one address register and the record pointer plus twice the group in the other, so for a large group neither register points into the record that is read.

## Behavior

- V (disassembly): at 0x14030E55A the group is widened, then three one-byte loads at 0x14030E561, 0x14030E56D and 0x14030E57A read the record's learned array at +0xA2, +0xA3 and +0xA4 for that group (3 bytes a group) and join them into one 24-bit mask, high byte first.
- V (disassembly): the address is the group plus a register holding the record address plus twice the group; the record address itself stays in the register that holds the unit's record through the function.
- I: with a group of 24 or more the pointer register lies past the 512-byte record's stock array, and from a group of about 104 past the record, inside the next battle record of the unit table.
- V (seen live 2026-11-17, Siedge Weald): with the group of a unit's own job read from outside the stock array, the job's command opened its list only when these three reads returned that job's learned bits; reading other bytes gave the red 'Unable to use' banner.

## Notes

The same split of offset and pointer as JobArrayAccessesPutTheRecordPointerInTheIndexRegister, with the pointer register advanced by twice the group.

## Open questions

None recorded.
