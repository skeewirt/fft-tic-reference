# NxdDataGossipRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.gossip table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="counter"></a>`0x4` | counter | `int32` | V | Read in the code: Id of a UserSituation counter that reading the rumour raises to the value at +8 (and that, while below it, keeps the rumour marked and shows its picture). Observed in the stock rows: 0 to 2, 2 distinct values. |
| <a id="counter_value"></a>`0x8` | counter_value | `int32` | V | Read in the code: Value the counter at +4 is raised to when the rumour is read (only if it is lower). Observed in the stock rows: 0 to 90, 3 distinct values. |
| <a id="title"></a>`0xC` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 23 distinct values, 0 empty. |
| <a id="text"></a>`0x10` | text | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 23 distinct values, 0 empty. |
| <a id="event_vars"></a>`0x14` | event_vars | `int32[] {int32 offset; uint32 count}` | V | Read in the code: List of event variable numbers written when the rumour first raises its counter; 102 is not a variable but a prefix: its value times 10 is added to the next variable number. Observed in the stock rows: 3 distinct values. |
| <a id="event_var_values"></a>`0x1C` | event_var_values | `int32[] {int32 offset; uint32 count}` | V | Read in the code: The values written to the event variables of +0x14, pair by pair (for the 102 prefix: the multiplier). Observed in the stock rows: 3 distinct values. |
| <a id="user_situation"></a>`0x24` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 3510, 4 distinct values. |
| <a id="picture"></a>`0x28` | picture | `int32` | V | Read in the code: Number of the picture shown beside the rumour text: it fills the path pattern of Icon row 21 ('base/textureparts/base_%02d_uitx') and is drawn when the row's +4 and +8 are both non-zero (state 'ShowImage', else 'Default'). Observed in the stock rows: 0 to 26, 3 distinct values. |
| <a id="always_listed"></a>`0x2C` | always_listed | `uint8` | V | Read in the code: When set the rumour is listed in every tavern without the per-town mask (g_RumourTownMasks) and without its unlock event variable (721 + id); only the user_situation (+0x24) test still applies. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataGossip](../tables/NxdDataGossip.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 10 columns not decoded.
