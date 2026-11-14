# BattleMsgKindBase

- **Kind:** registry
- **Area:** [Battle](../areas/battle.md)
- **Values stored in:** [BattleMsgDescriptor.kind](../structs/BattleMsgDescriptor.md#kind), [BattleMsgDescriptor.word](../structs/BattleMsgDescriptor.md#word)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The message-id base per descriptor kind for class 0 subtype 2: id = 1000 x kind + (word & 0x7FF). Only the kinds listed give an id; every other descriptor returns 0xFFFFFFFF (no message).

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="kind_2"></a>2 | `kind_2` | `2000` | V | Base 2000: the reachable ids are 2000..4047, the word's low 11 bits being the offset. |
| <a id="kind_3"></a>3 | `kind_3` | `3000` | V | Base 3000: the reachable ids are 3000..5047, the word's low 11 bits being the offset. |
| <a id="kind_6"></a>6 | `kind_6` | `6000` | V | Base 6000: the reachable ids are 6000..8047, the word's low 11 bits being the offset. |
| <a id="kind_7"></a>7 | `kind_7` | `7000` | V | Base 7000: the reachable ids are 7000..9047, the word's low 11 bits being the offset. |
| <a id="kind_8"></a>8 | `kind_8` | `8000` | V | Base 8000: the reachable ids are 8000..10047, the word's low 11 bits being the offset. |
| <a id="kind_9"></a>9 | `kind_9` | `9000` | V | Base 9000: the reachable ids are 9000..11047, the word's low 11 bits being the offset. |
| <a id="kind_10"></a>10 | `kind_10` | `10000` | V | Base 10000: the reachable ids are 10000..12047, the word's low 11 bits being the offset. |
| <a id="kind_11"></a>11 | `kind_11` | `11000` | V | Base 11000: the reachable ids are 11000..13047, the word's low 11 bits being the offset. |
| <a id="kind_14"></a>14 | `kind_14` | `14000` | V | Base 14000: the reachable ids are 14000..16047, the word's low 11 bits being the offset. |
| <a id="kind_16"></a>16 | `kind_16` | `16000` | V | Base 16000: the reachable ids are 16000..18047, the word's low 11 bits being the offset. |
| <a id="kind_17"></a>17 | `kind_17` | `17000` | V | Base 17000: the reachable ids are 17000..19047, the word's low 11 bits being the offset. |
| <a id="kind_18"></a>18 | `kind_18` | `18000` | V | Base 18000: the reachable ids are 18000..20047, the word's low 11 bits being the offset. |
| <a id="kind_22"></a>22 | `kind_22` | `22000` | V | Base 22000: the reachable ids are 22000..24047, the word's low 11 bits being the offset. |
| <a id="kind_23"></a>23 | `kind_23` | `23000` | V | Base 23000: the reachable ids are 23000..25047, the word's low 11 bits being the offset. |

## Behavior

- V: id = 1000 x kind + (word & 0x7FF) for class 0 subtype 2 and the listed kinds; any other descriptor returns 0xFFFFFFFF (decompile).
- V: the keys of table 172 run 2000..23025 (1734 rows), so the base of every listed kind has a row; key 10098 (kind 10, word 98) holds <string=lstr0> (extracted table data).
- ?: the meaning of each kind; the code path only multiplies it.

## Notes

The base is a decimal offset, not a table row id: the row id is the sum above. Not every key in a kind's reach has a table row: for example 10512 (kind 10, word 512) does not exist.

## Open questions

? the meaning of each kind; ? why some kinds are absent from the list.
