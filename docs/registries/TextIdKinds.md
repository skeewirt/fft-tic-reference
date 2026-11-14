# TextIdKinds

- **Kind:** registry
- **Area:** [Data access](../areas/data.md)
- **Resolved by:** [sub_140226208](../functions/sub_140226208.md), [EventText_FindMessage](../functions/EventText_FindMessage.md)
- **Values stored in:** [TextId](../formats/TextId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 32 text-id kinds: the 5 bits of a text id, their base (kind x 0x800) and the pool or source each selects. Every kind gets a pool base at load; a kind's base plus an index is the text id. Several kinds have observed producers; for the rest only the base is known.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="event_script"></a>0 | `event_script` | `0x0000` | V | Event-script text block; slot 0 is written at load by EventScript_LoadIntoBuffer. |
| <a id="kind_1"></a>1 | `kind_1` | `0x0800` | ? | Pool base 0x0800; no producer identified. |
| <a id="kind_2"></a>2 | `kind_2` | `0x1000` | ? | Pool base 0x1000; no producer identified. |
| <a id="kind_3"></a>3 | `kind_3` | `0x1800` | ? | Pool base 0x1800; no producer identified. |
| <a id="kind_4"></a>4 | `kind_4` | `0x2000` | ? | Pool base 0x2000; no producer identified. |
| <a id="kind_5"></a>5 | `kind_5` | `0x2800` | ? | Pool base 0x2800; no producer identified. |
| <a id="kind_6"></a>6 | `kind_6` | `0x3000` | ? | Pool base 0x3000; no producer identified. |
| <a id="item_text"></a>7 | `item_text` | `0x3800` | V | Item text: 0x3800 + item id, built at 20 text sites in 17 functions (12 builders, 8 consumers); pool 7. |
| <a id="kind_8"></a>8 | `kind_8` | `0x4000` | ? | Pool base 0x4000; the scene formatter's tag helper maps selectors 0xE0 and 0xE1 to this base; role not established. |
| <a id="kind_9"></a>9 | `kind_9` | `0x4800` | ? | Pool base 0x4800; no producer identified. |
| <a id="kind_10"></a>10 | `kind_10` | `0x5000` | ? | Pool base 0x5000; no producer identified. |
| <a id="kind_11"></a>11 | `kind_11` | `0x5800` | ? | Pool base 0x5800; observed in text builders (sub_1402F8684, sub_140301ED8, sub_14033F8C0); role not established. |
| <a id="kind_12"></a>12 | `kind_12` | `0x6000` | ? | Pool base 0x6000; no producer identified. |
| <a id="item_help"></a>13 | `item_help` | `0x6800` | V | Item help: 0x6800 + item id, built at 6 sites in 5 functions; a seventh site only bounds a script operand at 0x105; pool 13. |
| <a id="ability_name"></a>14 | `ability_name` | `0x7000` | V | Ability name; the decoder answers it from the ability name source sub_140332B48(2), not from the pool table. |
| <a id="job_help"></a>15 | `job_help` | `0x7800` | I | Job and command help (I: from the functions that add 0x7800 to a stored index); pool 15. |
| <a id="kind_16"></a>16 | `kind_16` | `0x8000` | ? | Pool base 0x8000; no producer identified. |
| <a id="kind_17"></a>17 | `kind_17` | `0x8800` | ? | Pool base 0x8800; add sites exist in sub_1402D2578, Errand_ShowResultUnit, sub_140373BB0 and sub_140373DE8 (not classified); role not established. |
| <a id="kind_18"></a>18 | `kind_18` | `0x9000` | ? | Pool base 0x9000; add sites exist in sub_14036A294 and sub_140371550 (not classified); role not established. |
| <a id="help_alt"></a>19 | `help_alt` | `0x9800` | V | Skillset help: 0x9800 + set id, built at sub_140301ED8 (0x1403020F1), sub_140366ABC (0x140366D1F) and sub_140366FE0 (0x1403671A3; it also adds 0x7800 for the job help); pool 19, 227 stock strings, the index masked with 0x7FF by sub_140226208. |
| <a id="kind_20"></a>20 | `kind_20` | `0xA000` | ? | Pool base 0xA000; no producer identified. |
| <a id="kind_21"></a>21 | `kind_21` | `0xA800` | ? | Pool base 0xA800; no producer identified. |
| <a id="skillset_name"></a>22 | `skillset_name` | `0xB000` | V | Skillset (command) name: 0xB000 + set id, built at nine producers (BattleMsg_UnitTurnScene 0x14023750F, sub_1402EB408 0x1402EB489, sub_140227CF8 and six more); the decoder overrides this kind's table entry with the pool at qword_14375F938 after Resource_GetSlotObject(9); the title widget sub_1401560D0 reads the token as the set id and the JobCommand-en row keyed by it. |
| <a id="kind_23"></a>23 | `kind_23` | `0xB800` | ? | Pool base 0xB800; text builders in sub_1403456D4 and sub_14037E1E8 add it; role not established. |
| <a id="kind_24"></a>24 | `kind_24` | `0xC000` | ? | Pool base 0xC000; no producer identified. |
| <a id="kind_25"></a>25 | `kind_25` | `0xC800` | ? | Pool base 0xC800; sub_140284098 and sub_14037D4BC add it; role not established. |
| <a id="kind_26"></a>26 | `kind_26` | `0xD000` | ? | Pool base 0xD000; sub_1403015A4 writes a 16-byte value over slots 26 and 27; role not established. |
| <a id="kind_27"></a>27 | `kind_27` | `0xD800` | ? | Pool base 0xD800; sub_14033E038 adds it; role not established. |
| <a id="kind_28"></a>28 | `kind_28` | `0xE000` | ? | Pool base 0xE000; no producer identified. The base overlaps the renderer's in-string control codes at 0xE0xx. |
| <a id="kind_29"></a>29 | `kind_29` | `0xE800` | ? | Pool base 0xE800; no producer identified. |
| <a id="kind_30"></a>30 | `kind_30` | `0xF000` | ? | Pool base 0xF000; no producer identified. The base overlaps the renderer's in-string control codes at 0xF0xx. |
| <a id="kind_31"></a>31 | `kind_31` | `0xF800` | ? | Pool base 0xF800; no producer identified. |

## Behavior

- V: every kind receives a pool base at load: slot 0 from EventScript_LoadIntoBuffer and slots 1..31 from one loop in sub_140301ED8 reading the pack at qword_14375F8F0; no kind is unassigned.
- V: base(kind) = kind x 0x800, and a text id is base + index with the index in 0..0x7FF.
- V: the item name and item help roles are kinds 7 and 13 only. The battle message entry carries a plain item id in its own kind field, not a text id.
- I: the roles marked I follow the constant that the surrounding functions add (0x7800, 0x9800); the pool content itself was not read.
- ?: the roles of the kinds marked ?; only the base and, for some, an observed builder are known.

## Referenced by

- Observed behaviours: [SkillsetNamesAndHelpAreKeyedBySetId](../behaviors/SkillsetNamesAndHelpAreKeyedBySetId.md)

## Notes

V: qword_140D40990 is zero in the executable image; the bases above are what the load loop computes at run time. V: a second pool table at 0x14184A8A0 serves the duplicate decoder EventText_FindMessage, with the same kind layout (I).

## Open questions

? what each pool contains; ? why kinds 2..6, 9, 10, 12, 16, 20, 21 and 24 have no observed producer; ? whether kinds 28..30 are ever used as text ids, their bases overlapping the in-string control codes.
