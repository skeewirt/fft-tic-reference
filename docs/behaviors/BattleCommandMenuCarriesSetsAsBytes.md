# BattleCommandMenuCarriesSetsAsBytes

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [sub_14030E010](../functions/sub_14030E010.md), [sub_140217630](../functions/sub_140217630.md), [sub_140316B04](../functions/sub_140316B04.md), [sub_140316D24](../functions/sub_140316D24.md), [Mem_CopyChecked](../functions/Mem_CopyChecked.md), [g_BattleCommandBytes](../globals/g_BattleCommandBytes.md), [g_BattleCommandBytesB](../globals/g_BattleCommandBytesB.md), [g_BattleCommandKinds](../globals/g_BattleCommandKinds.md), [g_AiCommandTable](../globals/g_AiCommandTable.md), [g_CommandKind](../globals/g_CommandKind.md), [UnitWorkRecord.action_command](../structs/UnitWorkRecord.md#action_command)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle command menu works with skillset ids as single bytes at every step: the unit's two set bytes, the byte lists the menu builders write, the kind array, the AI's command table and the command byte of the 20-byte action block. 0xFF ends every list, 0x18 is never listed, and set bytes are copied by Mem_CopyChecked.

## Behavior

- V: sub_14030E010 builds the list for a unit: byte 0 = 1, then +0x12 (skipped when 0 or 0x18), +0x13 (skipped when 0), 2 and 3 from the passive bits at +0x9B (not for a Toad), then 0xFF; a unit with +0x65 bit 0x04 (or +0x1B4 bit 0x40 with dword_14185670C zero) gets 0xFF alone; a monster set (0xB0..0xDF in either byte) gives the primary set alone. It then fills g_BattleCommandKinds with g_CommandKind[byte] & 0xF for up to 6 entries.
- V: sub_140217630 builds the same list (1, +0x12, +0x13, 0xFF; no 2 and 3) on a scratch unit in a stack array and asks sub_14030DD8C for each command with kind 0, 1, 2, 3, 4, 7 or 10.
- V: sub_140316B04 / sub_140316D24 write the AI's table: the command byte (the unit's set) goes to byte +2 of each entry, 0xFF ends the row.
- V: the 20-byte action block at unit +0x1A0 (+1 command byte, +2 ability id u16) is written by only four direct stores (BattleAction_BuildUnitRequest 0x1402832AD, sub_1402831D8 0x140283235, Formula_37_RendEquipment 0x140307EB9 and its restore 0x140307EED); every other copy of it goes through Mem_CopyChecked with size 0x14.

## Notes

Source: IDA reads of 2026-11-12.

## Open questions

None recorded.
