# ErrandRecordRow

- **Kind:** structure
- **Area:** [Errands](../areas/errands.md)
- **Size:** 23 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One errand record in the errand data block.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="category"></a>`0x0` | category | `uint8` | V | Category 1..8: the row of the job-fit category matrix and of the treasure and roll pair tables. |
| <a id="type"></a>`0x1` | type | `uint8` | V | Type 1..3: the row of the job-fit type matrix and of the Brave, Faith and level score tables. |
| <a id="number"></a>`0x2` | number | `uint8` | V | Errand number (id + 1): starting an errand stores number - 1 in the active record and marks event variable 863 + number. |
| <a id="col3"></a>`0x3` | col3 | `uint8` | ? | Equal to the number in every stock record; no reader found. |
| <a id="fee_a_index"></a>`0x4` | fee_a_index | `uint8` | V | First fee part: index into the money table. The fee shown and paid is the sum of both parts. |
| <a id="fee_b_index"></a>`0x5` | fee_b_index | `uint8` | V | Second fee part: index into the money table. The list screen picks one of two messages by which part is non-zero. |
| <a id="days_base"></a>`0x6` | days_base | `uint8` | V | Fewest days a dispatch may take; days past it raise the JP and gil (index days - days_base, at most 9). |
| <a id="days_max"></a>`0x7` | days_max | `uint8` | I | Most days a dispatch may take (board day picker range); always at or above days_base. |
| <a id="name_text_id"></a>`0x8` | name_text_id | `uint8` | V | Event-text message of the errand title in the legacy windows: message 0xF7FF + this value. The Enhanced board names an errand from its NXD row. |
| <a id="jp_tier"></a>`0x9` | jp_tier | `uint8` | V | JP reward tier (1-based into the JP tier table). |
| <a id="treasure_pool"></a>`0xA` | treasure_pool | `uint8` | V | On a best result: 1 picks one of 31 treasures not yet owned (event variables 801..831), 2 picks one of 16 (848..863), 0 none; a pick also adds the category treasure pair reward. |
| <a id="bonus_roll"></a>`0xB` | bonus_roll | `uint8` | I | Read only when treasure_pool is 0: 1 rolls a random bonus on a best result (60 percent none, 30 percent entry 1, 10 percent entry 2 of the category triple). |
| <a id="gil_tier"></a>`0xC` | gil_tier | `uint8` | V | Gil reward tier (1-based into the gil tier table). |
| <a id="col13"></a>`0xD` | col13 | `uint8` | ? | Equal to the number in every stock record; no reader found. |
| <a id="col14"></a>`0xE` | col14 | `uint8` | ? | Equal to the number in every stock record; no reader found. |
| <a id="col15"></a>`0xF` | col15 | `uint8` | ? | Values 1..4 spread evenly over the records; no reader found. |
| <a id="town"></a>`0x10` | town | `uint8` | V | Settlement where the errand is offered, number + 1; 0 = every settlement. |
| <a id="cond_flags"></a>`0x11` | cond_flags | `uint8` | V | Availability conditions, all set bits must hold: 0x01 event variable 111 >= cond_story; 0x02 the date (event variables 46 / 47, converted) equals cond_ref; 0x04 errand cond_ref has been completed with success. |
| <a id="col18"></a>`0x12` | col18 | `uint8` | ? | Equal to the number in every stock record; no reader found. |
| <a id="featured_selector"></a>`0x13` | featured_selector | `uint8` | V | Which unit is featured in the result: 1 / 2 highest / lowest Brave, 3 / 4 highest / lowest Faith; any other value picks the first unit. Every stock record holds 4. |
| <a id="col20"></a>`0x14` | col20 | `uint8` | ? | Values 0..19 in the stock records; no reader found. |
| <a id="cond_story"></a>`0x15` | cond_story | `uint8` | V | Story progress (event variable 111) the errand needs with cond_flags 0x01. |
| <a id="cond_ref"></a>`0x16` | cond_ref | `uint8` | V | With 0x04 the errand index that must be completed first; with 0x02 the date value. |

## Referenced by

- Described by tables: [ErrandBlob](../tables/ErrandBlob.md)

## Open questions

None recorded.
