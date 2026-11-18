# NxdDataEventIdRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 44 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.event_id table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 485, 62 distinct values. |
| <a id="comment"></a>`0x8` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="comment2"></a>`0xC` | comment2 | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="sortie_confirm_union_id"></a>`0x10` | sortie_confirm_union_id | `union {int32 kind; int32 id}` | I | Typed reference: a table kind and a row id in that table. Observed in the stock rows: 146 distinct values. |
| <a id="sead_state_parameter_id"></a>`0x18` | sead_state_parameter_id | `int32` | I | Row id of SeadStateParameter (a reference by column name). Observed in the stock rows: 0 to 11, 12 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="flag_20"></a>`0x20` | flag_20 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_21"></a>`0x21` | flag_21 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_22"></a>`0x22` | flag_22 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_23"></a>`0x23` | flag_23 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_24"></a>`0x24` | flag_24 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_25"></a>`0x25` | flag_25 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_26"></a>`0x26` | flag_26 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="flag_27"></a>`0x27` | flag_27 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_28"></a>`0x28` | flag_28 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="flag_29"></a>`0x29` | flag_29 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_2a"></a>`0x2A` | flag_2a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_2b"></a>`0x2B` | unk_2b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataEventId](../tables/NxdDataEventId.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

14 of 19 columns not decoded.
