# ItemAccessoryRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Accessory sub-record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="phys_evade"></a>`0x0` | phys_evade | `uint8` | V | Physical evade, copied to unit work +72. |
| <a id="magic_evade"></a>`0x1` | magic_evade | `uint8` | V | Magic evade, copied to unit work +76. |

## Referenced by

- Described by tables: [ItemAccessoryRecords](../tables/ItemAccessoryRecords.md), [ItemAccessoryRecordsHigh](../tables/ItemAccessoryRecordsHigh.md)

## Open questions

None recorded.
