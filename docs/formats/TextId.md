# TextId

- **Kind:** file format
- **Area:** [Data access](../areas/data.md)
- **Read by:** [sub_140226208](../functions/sub_140226208.md), [EventText_FindMessage](../functions/EventText_FindMessage.md), [sub_140153CA0](../functions/sub_140153CA0.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A 16-bit text id in two fields: the top 5 bits select one of 32 string pools, the low 11 bits index the strings inside that pool. The single decoder sub_140226208 returns the string pointer; kinds 14 and 22 are redirected before the pool is used. Item names and item help are two different pools: 0x3800 is item text (kind 7), 0x6800 is item help (kind 13).

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="kind"></a>bits 15..11 | kind | `5 bits (0..31)` | V | Selects the pool through the 32-entry table qword_140D40990. 0x3800 is kind 7 (item text), 0x6800 kind 13 (item help), 0x7000 kind 14 (ability name). |
| <a id="index"></a>bits 10..0 | index | `11 bits (0..0x7FF)` | V | String index inside the pool; an index of 0 returns the pool base. The decoder masks the word with 0x7FF and walks that many record separators. |
| <a id="pool_table"></a>pool table | pool_table | `char *[32]` | V | qword_140D40990: one base per kind. Slot 0 is the event-script text block, written at load by EventScript_LoadIntoBuffer; slots 1..31 are filled by one loop from the text pack at qword_14375F8F0 (base = pack + 0x80 + dword[pack + 4 x kind]). The table is zero in the image. |
| <a id="strings"></a>pool | strings | `char[]` | V | Terminated records separated by byte 0xFE (0xFF counts as a separator too). The walk keeps no end pointer and no length. |
| <a id="overrides"></a>kind 14 and kind 22 | overrides | `two kinds` | V | Kind 14 is answered by the ability name source sub_140332B48 with argument 2; kind 22 (0xB000) is redirected through sub_1402BACCC(9) to the pool at qword_14375F938 instead of its table entry. |

## Behavior

- V (sub_140226208, 21 direct call sites in 11 functions): kind = (word >> 11) & 0x1F; index = word & 0x7FF; the base comes from qword_140D40990[kind].
- V: index 0 returns the pool base; a non-zero index counts bytes of 0xFE and above and returns the start of the index-th record. Neither an end pointer nor a length is kept, so an index past the pool runs into the next one.
- V (load): slot 0 is written by EventScript_LoadIntoBuffer and slots 1..31 by one loop in sub_140301ED8 from the pack at qword_14375F8F0, so every kind has a base at run time.
- I: the pools are per-category string lists; their content was not read (the table is zero in the image).
- V: the 16-bit packing is the wall. 0x3800 + N with N >= 0x800 changes the kind (N = 0x800 gives kind 8, base 0x4000), and 0x6800 + N with N >= 0x800 becomes 0x7000, the ability kind. A wider id needs a different carrier, not a different mask.
- V (scene text formatter): the tag helper sub_140220E10 maps a format selector byte to a tag: 0xE9 adds 0x3800, 0xEA adds 0x7000, 0xEB leaves the id bare, 0xE5 adds 0x9000.
- V: three other id spaces are easy to confuse with it: the battle message id (1000 x kind + (word & 0x7FF), table 172), the scene message word (5-bit group + 11-bit index) and the battle message entry kind (a dword per entry).

## Referenced by

- Appears in flows: [ItemNameToScreen](../flows/ItemNameToScreen.md)
- Indexed by registries: [TextIdKinds](../registries/TextIdKinds.md)

## Notes

V: the 32 kinds are in registry TextIdKinds, with the base and the observed producers of each. V: the item name has a second, pool-free route: ItemTable_GetName reads the Item-en row (nxd table 45) by a full 32-bit key, and the equipment detail panel's help is that row's description field, not a 0x6800 token.

## Open questions

? which string each of the 32 pools holds at run time; ? whether a stock index can run past its pool (the walk has no end pointer).
