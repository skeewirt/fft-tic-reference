# UnitInfo_FillFromBattleUnit

- **Address:** `0x1402CBCA0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool UnitInfo_FillFromBattleUnit(void *out, void *unit, __int64 a3, __int64 a4)`
- **Callers:** EventPreviewUnit_StageSlot, Battle_InitScene, sub_14013F71C, sub_14013FAB0, sub_1401F3F70, sub_140214404, sub_140214610, sub_140214828, sub_140217630, sub_1402C6514, sub_1402C72B8 (IDA code references; which one draws the deployment card was not traced)
- **Callees:** sub_140360700, sub_140214134, JobRecord_FromJobId, sub_1400FBB40

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the unit information record a battle panel draws (the deployment carousel's unit card, an event's unit preview) from a battle unit record: its job line, face, level, HP / MP / CT, Brave and Faith.

## Behavior

- V: sub_140360700(unit, frame) first copies the unit's display fields into a stack frame (the job is the frame's word 18, the level nibbles and the JP / total JP words are frame copies sized for the stock jobs).
- V: out +196 is set to -1, then out +156 = sub_140214134(unit +444, out +196): the unit's battle face and colour.
- V: the job line is JobRecord_FromJobId(out, key) with a key built on the stack: +0 and +36 the frame's job, +8 / +16 / +24 pointers into the frame's level and JP copies, +32 a flags byte; then sub_1400FBB40(out + 92, frame).
- V: then out +160.. takes the frame's level, EXP, HP, MP, CT (100 at +176), Brave and Faith words, +184 / +185 flag bits of the unit's byte +6, +188 the unit's slot byte (+1), +200 the dword at unit +504, +204 a side value from byte +6 (0 when bit 7 is set, else 2 or 1 by bit 6).
- V (live 2026-11-10, tracepoint on JobRecord_FromJobId with the return address): the deployment carousel's card calls it through this function (return 0x1402CBD42); the key held 0x4A for Ramza (Squire).

## State touched

- Calls: [sub_140214134](sub_140214134.md), [JobRecord_FromJobId](JobRecord_FromJobId.md)

## Referenced by

- Called by: [sub_140217630](sub_140217630.md)

## Notes

The name is ours (IDB: sub_1402CBCA0). The key points at stock-sized frame copies of the level and JP words.

## Open questions

? the meaning of a3 / a4 (passed through to sub_140360700) and of out +200.
