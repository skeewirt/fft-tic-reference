# ErrandBlobLayout

- **Kind:** structure
- **Area:** [Errands](../areas/errands.md)
- **Size:** 2768 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Layout of the errand data block: a header of sub-table offsets followed by the errand records and the scoring and reward tables.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="header_offsets"></a>`0x0` | header_offsets | `uint32[15]` | ? | Offsets of the sub-tables (meaning of each not established). |
| <a id="records"></a>`0x3C` | records | `uint8[2208]` | V | 96 errand records of 23 bytes (ErrandRecordRow). |
| <a id="money_table"></a>`0x8DC` | money_table | `uint16[10]` | V | Gil amounts the two fee indices stand for (0 up to 10000). |
| <a id="reaction_matrix"></a>`0x8F0` | reaction_matrix | `uint8[9]` | V | Offset added to the base animation id of the featured unit in the result scene, plus 3 for a female unit. |
| <a id="pad_a"></a>`0x8F9` | pad_a | `uint8[3]` | ? | Padding. |
| <a id="job_fit_category"></a>`0x8FC` | job_fit_category | `uint8[176]` | V | 8 rows of 22 job columns: score a unit of the job adds in an errand of the category (see ErrandJobFitCategory). |
| <a id="job_fit_type"></a>`0x9AC` | job_fit_type | `uint8[66]` | V | 3 rows of 22 job columns: second job score by errand type. |
| <a id="pad_b"></a>`0x9EE` | pad_b | `uint8[2]` | ? | Padding. |
| <a id="brave_score"></a>`0x9F0` | brave_score | `uint8[15]` | V | Score from the unit Brave, 3 rows of 5: type 1 rises with Brave (5 up to 20), type 2 falls, type 3 is flat. |
| <a id="pad_c"></a>`0x9FF` | pad_c | `uint8` | ? | Padding. |
| <a id="faith_score"></a>`0xA00` | faith_score | `uint8[15]` | V | Score from the unit Faith, 3 rows of 5: type 1 falls with Faith (20 down to 5), type 2 rises, type 3 is flat. |
| <a id="pad_d"></a>`0xA0F` | pad_d | `uint8` | ? | Padding. |
| <a id="level_score_unused"></a>`0xA10` | level_score_unused | `uint8[30]` | V | A 3 x 10 table rising with level that no code reads (no cross-reference); probably the table the level lookup should use. |
| <a id="pad_e"></a>`0xA2E` | pad_e | `uint8[2]` | ? | Padding. |
| <a id="treasure_pairs"></a>`0xA30` | treasure_pairs | `uint8[16]` | V | 8 pairs by category: gil tier (becomes the bonus gil of the result) and JP tier (added to every unit JP) when a treasure is picked. |
| <a id="roll_pairs"></a>`0xA40` | roll_pairs | `uint8[48]` | V | 8 triples of (gil tier, JP tier) pairs by category for the random bonus; (0, 0) gives nothing. |
| <a id="jp_tiers"></a>`0xA70` | jp_tiers | `uint16[8]` | V | JP per unit by tier (10 up to 120) before the grade, score and day factors; added to the unit current JP and total JP of its current job (cap 9999). |
| <a id="gil_tiers"></a>`0xA80` | gil_tiers | `uint16[8]` | V | Gil per unit by tier (150 up to 5500) before the factors; the sum plus the bonus gil is added to event variable 44. |
| <a id="jp_day_pct"></a>`0xA90` | jp_day_pct | `uint16[10]` | V | Percent multiplier of each unit JP reward by days over the base (100 up to 120). |
| <a id="gil_day_pct"></a>`0xAA4` | gil_day_pct | `uint16[10]` | V | Percent multiplier of each unit gil reward by days over the base (100 up to 150). |
| <a id="tail_unused"></a>`0xAB8` | tail_unused | `uint8[24]` | ? | A permutation-like list with no reader; purpose unknown. |

## Referenced by

- Described by tables: [ErrandBlob](../tables/ErrandBlob.md)

## Open questions

None recorded.
