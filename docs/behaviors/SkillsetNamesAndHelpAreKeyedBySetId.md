# SkillsetNamesAndHelpAreKeyedBySetId

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Data access](../areas/data.md)
- **Affects:** [sub_140226208](../functions/sub_140226208.md), [sub_1401560D0](../functions/sub_1401560D0.md), [JobCommandTable_GetRow](../functions/JobCommandTable_GetRow.md), [sub_140301ED8](../functions/sub_140301ED8.md), [BattleMsg_UnitTurnScene](../functions/BattleMsg_UnitTurnScene.md), [TextIdKinds](../registries/TextIdKinds.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A skillset's name and help are found by the set id alone: the name token is 0xB000 | set (text kind 22) and the help token 0x9800 | set (kind 19), both 11-bit indexes; the name row is the JobCommand-en NXD row keyed by the set as a 32-bit value, so a set of 0x800 or more spills into the kind bits.

## Behavior

- V: nine producers add 0xB000 to a set (sub_140227CF8, BattleMsg_UnitTurnScene 0x14023750F, sub_1402EB408 0x1402EB489, sub_14022AFEC, sub_1402E1C64, sub_1402F9F20, sub_14032F410, sub_14032F9F8, sub_14033A37C); the resolver sub_140226208 (and EventText_FindMessage at 0x1402DDBEA) sends a token whose top five bits are 0x16 to the text slot object 9 and masks the index with 0x7FF.
- V: sub_1401560D0 reads the same token as `token - 0xB000` (no mask) and takes the title from JobCommandTable_GetRow(set), the JobCommand-en table (41) row keyed by the set as an unsigned 32-bit value (JobCommandTable_GetRow, 14 call sites); it does not test the row for null.
- V: the help token 0x9800 | set has four producers: sub_140301ED8 (0x1403020F1, adds to the word at word_14186AF1E), sub_140366ABC (0x140366D1F), sub_140366FE0 (0x1403671A3, the flags above the index are removed later) and a shared help slot; the resolver masks the same 0x7FF, and the stock help pool holds 227 strings.

## Notes

Source: IDA reads of 2026-11-12. The pool contents themselves were not read.

## Open questions

? the help text's reader for a set of 0x800 or more outside the three producers listed.
