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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 31110, 33 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 767, 518 distinct values. |
| <a id="scion_labels"></a>`0xC` | scion_labels | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 353730 to 357346, 571 distinct values. |
| <a id="scion_labels_2"></a>`0x10` | scion_labels_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 0 to 357347, 17 distinct values. |
| <a id="scion_labels_3"></a>`0x14` | scion_labels_3 | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 0 to 357348, 17 distinct values. |
| <a id="scion_labels_4"></a>`0x18` | scion_labels_4 | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 0 to 357349, 17 distinct values. |
| <a id="scion_labels_5"></a>`0x1C` | scion_labels_5 | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 0 to 357350, 17 distinct values. |
| <a id="scion_labels_6"></a>`0x20` | scion_labels_6 | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 0 to 357351, 17 distinct values. |
| <a id="scion_labels_7"></a>`0x24` | scion_labels_7 | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 0 to 357352, 17 distinct values. |
| <a id="scion_labels_8"></a>`0x28` | scion_labels_8 | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 0 to 357353, 17 distinct values. |

## Referenced by

- Described by tables: [NxdDataUnitHelpMessage](../tables/NxdDataUnitHelpMessage.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 3 of 11 columns not decoded.
