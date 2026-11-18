# g_AiCommandTable

- **Kind:** global
- **Address:** `0x141872598`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `AiCommandEntry[16][34]`
- **Points to / is a:** [AiCommandEntry](../structs/AiCommandEntry.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The AI's candidate action table: 16 rows (one per AI unit) of 34 four-byte entries; each entry is an ability word and the command (skillset) byte it came from.

## Behavior

- V: sub_140316B04 and sub_140316D24 write it (the byte +2 at 0x14187259A, the word at 0x141872598; the stores at 0x140316DE0, 0x140316E35, 0x140316E78, 0x140316E9F, 0x140316FFF are variable stores of the command byte); sub_14038BC00, sub_14038C8F8, sub_14038D65C and Ai_SurveyTargets read it.
- V: the row is byte_141873038[unit slot]; the row stride is 34 x 4 = 136 bytes (68 words) and the table ends at 0x141872E18, before the row headers at byte_141872E20.
- V: the command byte +2 is the skillset id, so a set past 255 does not fit; 0xFF at +2 ends a row, so set 255 is reserved.

## Referenced by

- Observed behaviours: [BattleCommandMenuCarriesSetsAsBytes](../behaviors/BattleCommandMenuCarriesSetsAsBytes.md)
- Written by: [sub_140316B04](../functions/sub_140316B04.md), [sub_140316D24](../functions/sub_140316D24.md)

## Notes

Source: IDA reads of 2026-11-12. The IDA item is the first word (word_141872598).

## Open questions

? the readers' use of the entries (selection of the AI action).
