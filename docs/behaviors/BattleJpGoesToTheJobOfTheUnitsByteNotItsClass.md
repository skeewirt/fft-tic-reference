# BattleJpGoesToTheJobOfTheUnitsByteNotItsClass

- **Kind:** observed behaviour
- **Scope:** engine (battle JP award and learning)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [Battle_AwardActorJp](../functions/Battle_AwardActorJp.md), [Job_IdToIndex](../functions/Job_IdToIndex.md), [Unit_AwardJobJp](../functions/Unit_AwardJobJp.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle JP award reads the acting unit's job byte, runs it through Job_IdToIndex and adds the JP to that job's slot: a job id wider than the byte cannot be held in it.

## Behavior

- V (live, gamecall): with the acting unit pointer set to Ramza's battle record (job byte 76) and the award amount 10, Battle_AwardActorJp raised Knight's JP by 10 and nothing else; Job_IdToIndex(76) is Knight's index.
- V (disassembly): the award path loads the unit's job byte (byte +3 of the unit record) just before each Job_IdToIndex call: Battle_AwardActorJp (0x14030C7E8), Battle_AwardUnitJp (0x140283546), Battle_ActorResultLevels (0x14030C78C), sub_14030CD08 (0x14030CDCB, unit at rbx-0x1BB), sub_1403170CC (0x1403170FD), Job_ReadLearnedBitsForBattle (0x14020D1D3).

## Open questions

None recorded.
