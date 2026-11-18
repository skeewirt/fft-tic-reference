# InflictRecordRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 6 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One added-effect record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="flags"></a>`0x0` | flags | `uint8` | V | How the statuses apply: 0x80 ORs them into the unit first status group (work +9..), 0x10 into the group at +14..; 0x20, 0x40, 0xA0 and 0xE0 are tested by the action setup (meaning of the groups: I, always / immune). |
| <a id="statuses"></a>`0x1` | statuses | `uint8[5]` | V | Status bit field (40 statuses) copied into the action or the unit; which bit is which status follows the status ids. |

## Referenced by

- Described by tables: [InflictRecords](../tables/InflictRecords.md)

## Open questions

None recorded.
