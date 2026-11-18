# NxdDataUnitHelpMessageRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 44 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.unit_help_message table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 31110, 33 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 767, 518 distinct values. |
| <a id="panzer_entry_id1"></a>`0xC` | panzer_entry_id1 | `int32` | I | Packed archive entry id of a voice line. Observed in the stock rows: 353730 to 357346, 571 distinct values. |
| <a id="panzer_entry_id2"></a>`0x10` | panzer_entry_id2 | `int32` | I | Packed archive entry id of a voice line. Observed in the stock rows: 0 to 357347, 17 distinct values. |
| <a id="panzer_entry_id3"></a>`0x14` | panzer_entry_id3 | `int32` | I | Packed archive entry id of a voice line. Observed in the stock rows: 0 to 357348, 17 distinct values. |
| <a id="panzer_entry_id4"></a>`0x18` | panzer_entry_id4 | `int32` | I | Packed archive entry id of a voice line. Observed in the stock rows: 0 to 357349, 17 distinct values. |
| <a id="panzer_entry_id5"></a>`0x1C` | panzer_entry_id5 | `int32` | I | Packed archive entry id of a voice line. Observed in the stock rows: 0 to 357350, 17 distinct values. |
| <a id="panzer_entry_id6"></a>`0x20` | panzer_entry_id6 | `int32` | I | Packed archive entry id of a voice line. Observed in the stock rows: 0 to 357351, 17 distinct values. |
| <a id="panzer_entry_id7"></a>`0x24` | panzer_entry_id7 | `int32` | I | Packed archive entry id of a voice line. Observed in the stock rows: 0 to 357352, 17 distinct values. |
| <a id="panzer_entry_id8"></a>`0x28` | panzer_entry_id8 | `int32` | I | Packed archive entry id of a voice line. Observed in the stock rows: 0 to 357353, 17 distinct values. |

## Referenced by

- Described by tables: [NxdDataUnitHelpMessage](../tables/NxdDataUnitHelpMessage.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

2 of 11 columns not decoded.
