# BattleMsg_BuildArgs

- **Address:** `0x1400F79D0`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `int BattleMsg_BuildArgs(FormatArgVec *outVec, BattleMsgRecord *rec, BattleMsgDescriptor *desc)`
- **Callers:** BattleMsg_FillArgs (one direct site)
- **Callees:** BattleMsg_IdFromDescriptor, ItemTable_GetName, FormatArgs_Push, sub_1400F48E0, sub_1401E8B7C, sub_1402B89F8, sub_14002620C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the format-argument vector for a message descriptor: selects the message id, then pushes the values that replace the template's <string=lstrN> and <num=...> placeholders.

## Behavior

- V: dispatches on the message id: for class 0 subtype 2 it uses BattleMsg_IdFromDescriptor(desc); for class 1 subtype 27, message ids 3981 and 3905 have their own cases.
- V: the arguments come from the battle message record rec (the object's +8): rec[0] kind, rec[1] actor index into g_BattleUnitTable (512-byte stride, index at most 0x14), rec+12 a name string, rec[4193] (byte offset 0x4184), rec[133] (0x214), rec[134..] (0x218, a 256-byte string area) and rec[263] (0x41C).
- V: for message id 10098 the string argument is ItemTable_GetName(id), with id = rec[1] & 0x7FF when rec[0] == 4 and id = rec[1] (unmasked) when rec[0] == 9; when neither holds, nothing is pushed and the function returns 0.
- V: the item name is copied into a 256-byte stack buffer with a 255-byte cap before it is pushed.
- V: arguments are pushed through FormatArgs_Push; the pushed record carries a type dword at offset 256 (4 for a string argument, 1 for an integer argument).
- V: message ids 10141 and 10145 and above push the actor name and a status or ability value read through sub_1402B89F8.
- V: message 3062 (C_Mes_Id_Sample "<string=lstr0>'s <lowerall=<jobname(lnum1, lnum2)>> job level increased!", the job level-up banner): pushes the unit's name (rec+12), then the unit's job byte (+3 of the g_BattleUnitTable record named by rec[1]; loaded at 0x1400F7C6B) as lnum1, then lnum2 from the flags +6: 0 when the byte is negative (its top bit set), else 1 when bit 0x40 is set, else 2.
- V (seen live 2026-11-17): the banner read "Ramza's knight job level increased!" for a unit whose job byte was 76 (Knight).
- ?: the other message-id cases and what they push were not read.
- I: a 0 return means no argument was pushed, which makes BattleMsg_FillArgs use its stored argument set instead.
- I: the 11-bit mask on the kind-4 id is the item text-id field, not the item store; kind 9 carries the item id without that mask.

## State touched

- Calls: [BattleMsg_IdFromDescriptor](BattleMsg_IdFromDescriptor.md), [ItemTable_GetName](ItemTable_GetName.md), [FormatArgs_Push](FormatArgs_Push.md), [sub_1402B89F8](sub_1402B89F8.md), [sub_14002620C](sub_14002620C.md)

## Referenced by

- Called by: [BattleMsg_FillArgs](BattleMsg_FillArgs.md)

## Notes

The name is ours (IDB: sub_1400F79D0). The record layout is known only at the offsets named above. The function is 0x7F9 bytes (about 2 KB) and has one direct caller, BattleMsg_FillArgs (0x1401EC074).

## Open questions

What the cases other than 3062, 10098, 10141 and 10145+ push; what rec[4193], rec[133], rec[263] and the rec[134..] range hold; whether every case uses the same 0/1 return convention; whether kind 9 is reserved for the item-use record and kind 4 for another item message.
