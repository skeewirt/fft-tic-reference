# g_BattleLineAbility

- **Kind:** global
- **Address:** `0x142FD3590`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The ability, cut to 9 bits, that the battle-line task turns into a text id (0xA800 OR the ability) when a unit speaks a line for an action.

## Behavior

- V: BattleMsg_Dispatch writes it at 0x140238BE4 (the ability word of the action copy and 0x1FF) and reads it at 0x140238BFD; sub_140238444 writes it at 0x1402386D4; sub_140243A60 writes (0x140244DC6) and reads (0x1402457C7) it.
- I: because of the 9-bit cut an ability above 511 has no line; the text table was not checked.

## Notes

The line task is 0x140233588 (started with SceneTask_Start in BattleMsg_Dispatch).

## Open questions

? whether the text table has any 0xA800-form row above 511.
