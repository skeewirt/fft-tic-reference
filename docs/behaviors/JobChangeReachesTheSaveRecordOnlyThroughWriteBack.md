# JobChangeReachesTheSaveRecordOnlyThroughWriteBack

- **Kind:** observed behaviour
- **Scope:** engine (Jobs screen, party and save records)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [PartyUnit_WriteBackToSave](../functions/PartyUnit_WriteBackToSave.md), [PartyUnit_FillFromWork](../functions/PartyUnit_FillFromWork.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Changing a unit's job on the Jobs screen changes the save record's job byte (+2) in exactly one place: PartyUnit_WriteBackToSave copies the low byte of the party record's job word (+0x24) into it.

## Behavior

- V (write watch on save record 0 +2, 80 s, Ramza changed from Ninja to Knight with Change Job on the Jobs screen, 2026-11-04): the byte went 0x59 to 0x4C, and all 4 accesses came from PartyUnit_WriteBackToSave (the store at 0x1402857DB; the instruction after it reports). No other function wrote the byte during the change.
- V (disassembly): the save record is g_UnitSaveData + 0x258 * (signed word at party +0x2C); the stored byte is the low byte of the party word at +0x24 (a byte load from party +0x24, a byte store to save +2), and PartyUnit_FillFromWork stores that word as a 16-bit value (0x140284AF1), so the party record can hold an id wider than the save byte.
- I: the other stores of the byte (work-to-save, spawn, event unit setup) were not exercised by this change.

## Open questions

None recorded.
