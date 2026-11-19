# NxdDataGuideRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.guide table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="window_type"></a>`0x8` | window_type | `int32` | V | Read in the code: How the guide is shown and where its 'seen' bit lives: 1 -> large guide window (UI row 181, pauses the game), 2 -> guide window (UI row 182, pauses), 3 -> GuideTip (UI row 184); kinds 1 and 2 keep their seen bit in the config bits (g_ConfigData +204), kinds 4..6 their read bit in the job flag block (+146); 0 = not shown. Observed in the stock rows: 0 to 4, 4 distinct values. |
| <a id="category"></a>`0xC` | category | `int32` | V | Read in the code: List (tab) the guide belongs to: 1..3 are the three tutorial lists (category - 1 = tab), 7..12 the six Lessons lists (category - 7 = tab); 0 and other values are in no list. Observed in the stock rows: 0 to 12, 10 distinct values. |
| <a id="guide_page"></a>`0x10` | guide_page | `int32` | M | Measured over every stock row: Every value is a key of nxd.GuidePage-en. Observed in the stock rows: 0 to 3277, 226 distinct values. |
| <a id="job_type"></a>`0x14` | job_type | `int32` | V | Read in the code: JobType (table JobType) key: a lesson with a non-zero value is unlocked and listed only while that job type's disable flag (g_UnitJobFlags +21 + value, 125 flags) is 0. Observed in the stock rows: 0 to 59, 19 distinct values. |
| <a id="user_situation"></a>`0x18` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 60016, 13 distinct values. |
| <a id="user_situation_2"></a>`0x1C` | user_situation_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 12700, 8 distinct values. |
| <a id="delay"></a>`0x20` | delay | `float32` | V | Read in the code: Seconds of input pause before an auto-shown guide opens (0 = none); the value is also queued with the guide id. Observed in the stock rows: 0 to 2.8, 14 distinct values. |
| <a id="title"></a>`0x24` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 166 distinct values, 77 empty. |
| <a id="sort_order"></a>`0x28` | sort_order | `int16` | V | Read in the code: The guide lists are sorted by this value, ascending: the comparator used by the list builders compares the u16 at row +0x28 of the two guide rows. Observed in the stock rows: 0 to 3600, 115 distinct values. |
| <a id="seen_bit"></a>`0x2A` | seen_bit | `int16` | V | Read in the code: 1-based number of the guide's bit: for window types 1/2 in the config bits g_ConfigData +204 (seen; values below 80), for lessons in two bit sets of the job flag block (+169 unlocked, +146 read; values below 184); 0 = no bit (always shown again). Observed in the stock rows: 0 to 165, 166 distinct values. |
| <a id="unlocked_by_story"></a>`0x2C` | unlocked_by_story | `uint8` | V | Read in the code: A guide with this set counts as unlocked (listed) once UserSituation 10200 is met, even if it was never shown. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataGuide](../tables/NxdDataGuide.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 13 columns not decoded.
