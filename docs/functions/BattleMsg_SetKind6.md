# BattleMsg_SetKind6

- **Address:** `0x1401FA61C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleMsg_SetKind6(int slot, int id)`
- **Callers:** BattleMsg_Dispatch (5 sites), BattleMsg_UnitTurnScene, sub_1402EB408
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets one battle message record entry to kind 6 and stores its id.

## Behavior

- V: returns when g_BattleMsgObject is null or slot > 0x27.
- V: entry = g_BattleMsgObject + 0x20C * slot; the dword at entry+0 becomes 6 and the dword at entry+4 becomes id.
- V: three siblings have the same body with another kind constant: BattleMsg_SetKind1 (0x1401FA5C4, kind 1), BattleMsg_SetKind3 (0x1401FA5F0, kind 3) and BattleMsg_SetKind9 (0x1401FA648, kind 9).
- V: BattleMsg_Dispatch calls it for case 7 (the action name) and case 11; BattleMsg_UnitTurnScene calls it for the acting unit's ability; the scene twin sub_1402EB408 calls it too.

## Referenced by

- Called by: [BattleMsg_Dispatch](BattleMsg_Dispatch.md), [BattleMsg_UnitTurnScene](BattleMsg_UnitTurnScene.md)

## Notes

The name is ours (IDB: sub_1401FA61C). The function is 0x2A bytes; the three siblings are the same size.

## Open questions

None read: the function has one visible effect.
