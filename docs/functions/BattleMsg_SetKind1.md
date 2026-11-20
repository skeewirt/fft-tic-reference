# BattleMsg_SetKind1

- **Address:** `0x1401FA5C4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleMsg_SetKind1(int slot, int id)`
- **Callers:** BattleMsg_Dispatch (five sites) and the callers of BattleMsg_Dispatch that build a kind-1 entry
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets one battle message entry to kind 1 and stores its id.

## Behavior

- V: returns when the message object pointer is null or the slot is above 0x27 (the forty-entry bound).
- V: the entry is the object plus 0x20C times the slot; the kind constant 1 and the id are written into its header dwords.
- V: the body is 42 bytes, the same size as its three siblings, and it calls nothing.
- I: the four setters differ only in the kind constant they write (kinds 1, 3, 6 and 9).
- ?: whether the id belongs at entry+4 or at the text-id dword +0xC; the sibling sheet reads +4 while the carrier census read +0xC.

## State touched

- Reads: [g_BattleMsgObject](../globals/g_BattleMsgObject.md)
- Writes: [g_BattleMsgObject](../globals/g_BattleMsgObject.md)

## Referenced by

- Called by: [BattleMsg_Dispatch](BattleMsg_Dispatch.md), [DeploymentGrid_CommenceCheck](DeploymentGrid_CommenceCheck.md), [Deployment_SelectTile](Deployment_SelectTile.md), [sub_140323D1C](sub_140323D1C.md)

## Notes

Name taken from the existing BattleMsg_SetKind6 sheet, which already records this address as the kind-1 sibling. Only g_BattleMsgObject is touched.

## Open questions

None recorded.
