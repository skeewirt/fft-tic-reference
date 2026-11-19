# NxdDataScenarioIdRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.scenario_id table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="event_ids"></a>`0x4` | event_ids | `int32[] {int32 offset; uint32 count}` | M | Measured over every stock row: Every value is a key of nxd.EventId. Observed in the stock rows: 350 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2164, 349 distinct values. |

## Referenced by

- Described by tables: [NxdDataScenarioId](../tables/NxdDataScenarioId.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 3 columns not decoded.
