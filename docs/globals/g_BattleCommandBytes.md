# g_BattleCommandBytes

- **Kind:** global
- **Address:** `0x140D40838`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[8]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle command menu's byte list for the unit whose menu is open: the command (skillset) byte of each row, 0xFF-terminated.

## Behavior

- V: written only by sub_14030E010 (called from sub_1402371F8, which first stores 0 here): byte 0 is 1, then the unit's primary set (+0x12, unless 0 or 0x18), the secondary set (+0x13, unless 0) and the commands 2 and 3 when the unit's passive bits +0x9B 0x40 / 0x20 are set; a unit with a monster set (0xB0..0xDF) in either byte lists its primary set alone.
- V: read by sub_14022CBE4, sub_1402371F8, sub_140237FA4 and sub_140243A60; two readers compare an element with 0x14 (I: the Throw command, g_CommandKind row 20 is kind 2).

## Referenced by

- Observed behaviours: [BattleCommandMenuCarriesSetsAsBytes](../behaviors/BattleCommandMenuCarriesSetsAsBytes.md)
- Written by: [sub_14030E010](../functions/sub_14030E010.md)

## Notes

Source: IDA reads of 2026-11-12. The IDA item is one qword; the list is at most 6 bytes (1, two sets, 2, 3, 0xFF). The twin list for the second menu is g_BattleCommandBytesB.

## Open questions

? the third consumer of command bytes 2 and 3 (their command names).
