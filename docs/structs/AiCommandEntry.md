# AiCommandEntry

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One candidate action of the AI's command table: the ability word (id | unit slot << 10), the command (skillset) byte it comes from and a flag byte. A row of 34 entries per AI unit lives in g_AiCommandTable; the byte +2 = 0xFF of the entry after the last one ends the row.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="word"></a>`0x0` | word | `uint16` | V | The ability id in the low bits, the unit's slot << 10 above it (sub_140316D24 writes id \| slot << 10, or slot << 10 alone for an entry with no ability, such as the Arithmeticks and Jump entries). |
| <a id="command"></a>`0x2` | command | `uint8` | V | The command (skillset) byte the entry came from: 1 for the plain action of sub_140316B04's first entry, the unit's set for sub_140316D24's entries; 0xFF ends the row. |
| <a id="flags"></a>`0x3` | flags | `uint8` | V | Entry flags: the last entry holds 0x84 here (the word 0x84A9 stored at +2); sub_140316D24 sets bit 0x08 for the fourth list ability of a monster set (0xB0..0xDF) and clears it for the others. The other bits were not read. |

## Behavior

- V: the table is word_141872598 (g_AiCommandTable): 16 rows x 34 entries x 4 bytes, the row chosen by byte_141873038[unit slot]; an 8-byte header per row sits at byte_141872E20 (the item id word at header +4 is read by sub_140316D24 for the command kind 10 test).
- V: sub_140316B04 writes entry 0 (command 1, word = slot << 10), then calls sub_140316D24 for the primary and (outside the monster range 0xB0..0xDF) the secondary set, then writes the last entry (word = (slot << 10) + 367, bytes +2 / +3 = 0xA9 / 0x84) and the 0xFF terminator when fewer than 34 entries are used.
- V: readers of the command byte: 0x140320569, sub_14031FD40 (0x14031FED7), sub_14038D65C (0x14038D835); sub_140275EF4 (0x140276076) copies byte +2 to a unit's +0x13.

## Referenced by

- Global instances: [g_AiCommandTable](../globals/g_AiCommandTable.md)

## Notes

Source: IDA reads of 2026-11-12. The row-header bytes other than the item word were not read.

## Open questions

? what a row header's bytes mean beyond the item word at +4; the readers of the table (sub_14038BC00, sub_14038C8F8, sub_14038D65C) were not read for this record.
