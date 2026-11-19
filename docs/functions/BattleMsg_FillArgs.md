# BattleMsg_FillArgs

- **Address:** `0x1401EC074`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `void BattleMsg_FillArgs(BattleMsgObject *obj, FormatArgVec *outVec, BattleMsgDescriptor *desc)`
- **Callers:** UIMessageBanner_Show (with qword_143CDA388, the banner's argument vector at a1+152 and the descriptor)
- **Callees:** BattleMsg_BuildArgs, FormatArgs_Push

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the format-argument vector for the banner: first asks the message-id-specific builder, and when that pushes nothing, copies the object's up to 40 stored argument entries.

## Behavior

- V: resets outVec (end = begin).
- V: calls BattleMsg_BuildArgs(outVec, obj+8, desc).
- V: when desc is null or that call returns 0, it copies up to 40 stored argument entries instead, 524 bytes apart from obj+12, each with a type dword (1 = int, otherwise a 255-character string), pushed through FormatArgs_Push.
- V: the stored entries are the fallback for messages whose id-specific case pushes nothing.
- I: the 40-entry store is the message manager's saved argument set; the record at obj+8 is the battle message record BattleMsg_BuildArgs reads.

## State touched

- Calls: [BattleMsg_BuildArgs](BattleMsg_BuildArgs.md), [FormatArgs_Push](FormatArgs_Push.md)

## Referenced by

- Called by: [ErrorBanner_Show](ErrorBanner_Show.md), [UIMessageBanner_Show](UIMessageBanner_Show.md)

## Notes

The name is ours (IDB: sub_1401EC074). 40 entries of 524 bytes are read from obj+12; one entry becomes one 264-byte FormatArgs_Push record.

## Open questions

How the 40 stored entries are written; the exact relation between the record at obj+8 and the entry store at obj+12 (the recorded base addresses overlap; only the copy was read); whether the type dword has values other than 0 and 1.
