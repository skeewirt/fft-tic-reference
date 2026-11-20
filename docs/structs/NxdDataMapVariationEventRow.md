# NxdDataMapVariationEventRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.map_variation_event table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="event"></a>`0x8` | event | `int32` | V | Read in the code: Story event number; the variation element that points to this row applies when the current event number (scene variable 39) equals it. Observed in the stock rows: 0 to 482, 14 distinct values. |
| <a id="more_events"></a>`0xC` | more_events | `int32[] {int32 offset; uint32 count}` | V | Read in the code: Array (offset from the row start, count at +0x10) of further event numbers, any of which also accepts the element. Observed in the stock rows: 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataMapVariationEvent](../tables/NxdDataMapVariationEvent.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
