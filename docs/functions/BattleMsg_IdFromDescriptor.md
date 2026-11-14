# BattleMsg_IdFromDescriptor

- **Address:** `0x1400FCC04`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `unsigned int BattleMsg_IdFromDescriptor(BattleMsgDescriptor *desc)`
- **Callers:** BattleMsg_BuildArgs, BattleMsg_TextFromDescriptor, sub_1400FCCFC, BattleMsg_ResolveEntry (five sites in four functions)
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns a message descriptor into the row id used by NXD table 172 (C_Mes_Id_Sample-en).

## Behavior

- V: the function returns -1 unless the descriptor's class dword is 0 and its subtype dword is 2.
- V: for class 0 and subtype 2 it returns 1000 * kind + (word & 0x7FF), where kind is the dword at desc+8 and word is the signed 16-bit value at desc+12.
- V: the kinds with a row are 2, 3, 6, 7, 8, 9, 10, 11, 14, 16, 17, 18, 22 and 23; their bases are 2000, 3000, 6000, 7000, 8000, 9000, 10000, 11000, 14000, 16000, 17000, 18000, 22000 and 23000.
- V: any other class, subtype or kind returns 0xFFFFFFFF.
- V: kind 10 with word 98 gives 10098.
- V: the function makes no calls and has no side effects.
- I: the kind numbers are the battle message kinds, but they do not match the battle message record kinds one for one.
- ?: the meaning of kinds 14, 16 to 18 and 22 to 23 in game terms.

## Referenced by

- Called by: [BattleMsg_BuildArgs](BattleMsg_BuildArgs.md), [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md), [BattleMsg_TextFromDescriptor](BattleMsg_TextFromDescriptor.md)

## Notes

The name is ours (IDB: sub_1400FCC04). 0xFFFFFFFF is the no-row value. The function is 0xF6 bytes (246) and read in full; five direct call sites across four functions.

## Open questions

What the kinds outside the list are (they have no row in this table); whether callers test 0xFFFFFFFF before the lookup; which producer emits each accepted kind.
