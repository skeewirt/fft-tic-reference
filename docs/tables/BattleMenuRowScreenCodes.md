# BattleMenuRowScreenCodes

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x140672170`
- **Rows:** 24 rows of 1 bytes
- **Keyed by:** battle command menu row id (the row-content byte of the battle menu row buffer at 0x14184A9A8)
- **Read by:** [BattleMenu_ConfirmRow](../functions/BattleMenu_ConfirmRow.md)
- **Row layout:** [BattleMenuRowScreenCode](../structs/BattleMenuRowScreenCode.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per battle-menu row id, the screen or message code its confirm opens. Verdict: engine-data.

## Behavior

- V: single reader; 24 bytes up to the next symbol; row ids come from the battle menu row buffer (seen live in earlier research)
- V: sub_140237B18 (battle menu row confirm): code = 0x1000 + table[row id] unless the unit is in a special state (codes 0x1003 / 0x1007 / 0x100C), stored at scene block +0xC24 and run by the scene task sub_14023286C

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which row id is which command (Move, Act, Wait, Status, Auto-battle)
- ?: what screen each 0x10xx code opens
- ?: true count: index range of the row-id byte
