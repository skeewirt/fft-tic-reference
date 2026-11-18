# JobArrayAccessesPutTheRecordPointerInTheIndexRegister

- **Kind:** observed behaviour
- **Scope:** engine (per-unit job arrays)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobRecord_FromJobId](../functions/JobRecord_FromJobId.md), [Job_ReadLearnedBitsForBattle](../functions/Job_ReadLearnedBitsForBattle.md), [Job_LearnAbilityByMenu](../functions/Job_LearnAbilityByMenu.md), [sub_14030CD08](../functions/sub_14030CD08.md), [sub_1403170CC](../functions/sub_1403170CC.md), [Unit_TryLearnAbility](../functions/Unit_TryLearnAbility.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Nine accesses of the per-unit job arrays are written with the byte offset in the register that stands first in the address and the pointer into the record in the register that stands second, so the record pointer is not the first register of the address.

## Behavior

- V (disassembly): the level read of JobRecord_FromJobId (0x1400FBE09) is a one-byte load whose first register holds the job index halved (Job_IdToIndex, shift right by one at 0x1400FBE06) and whose second register holds the key's pointer to the level array; the even or odd index then selects the high or low nibble.
- V (disassembly): the learned-bit reads and writes have the same shape: Job_ReadLearnedBitsForBattle (0x14020D1E5 word read, 0x14020D22F byte OR), Job_LearnAbilityByMenu (0x14028942B, 0x140289435, and two accesses at displacement 0xBD from 0x1402894BF), sub_14030CD08 (0x14030CDDE), sub_1403170CC (0x140317144) and Unit_TryLearnAbility (0x140278192): the offset is 3 times the job index plus the array start in one register, the record pointer in the other.
- I: the count of nine comes from the stage reading; the disassembly scan of the six functions lists these instructions with two registers in the address and no scale.
- V: none of the nine tests the job index against a limit: the address is array start plus the offset, so an index larger than the array's own length reads and writes whatever follows the array, in the same record or in the next one.

## Notes

The sizes of the arrays are in JobArraysInThePartyRecordHoldStockIndicesOnly.

## Open questions

None recorded.
