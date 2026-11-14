# g_BattleUnitTable

- **Kind:** global
- **Address:** `0x141853CE0`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[10752]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The live battle unit table: 21 records of 512 bytes. HP, MP, tile, facing, CT and the action words are all read and written here during a battle.

## Behavior

- V: the table is live during battle (C4, C8); the battle action code reads the item id at +0x1C2 and the ability word at +0x17A.

## Referenced by

- Described by tables: [BattleUnits](../tables/BattleUnits.md)
- Read by: [BattleMsg_Dispatch](../functions/BattleMsg_Dispatch.md), [BattleRange_MarkAttack](../functions/BattleRange_MarkAttack.md), [Battle_MoveRange_Build](../functions/Battle_MoveRange_Build.md), [Battle_MoveRange_Commit](../functions/Battle_MoveRange_Commit.md), [sub_1402055FC](../functions/sub_1402055FC.md), [sub_140206F90](../functions/sub_140206F90.md), [sub_14020A7F0](../functions/sub_14020A7F0.md), [sub_14020AD64](../functions/sub_14020AD64.md), [sub_14020C704](../functions/sub_14020C704.md), [sub_140210AF0](../functions/sub_140210AF0.md), [sub_140221798](../functions/sub_140221798.md), [sub_1402371F8](../functions/sub_1402371F8.md), [sub_140237CD0](../functions/sub_140237CD0.md), [sub_140238444](../functions/sub_140238444.md), [sub_14024138C](../functions/sub_14024138C.md)

## Open questions

None recorded.
