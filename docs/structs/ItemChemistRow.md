# ItemChemistRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 3 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Chemist item sub-record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="formula"></a>`0x0` | formula | `uint8` | I | Formula id used when the item is used (stock rows use a few consecutive ids). |
| <a id="amount"></a>`0x1` | amount | `uint8` | I | Amount: 10 * value is written into the action result. |
| <a id="inflict"></a>`0x2` | inflict | `uint8` | V | Index of an inflict record (6 bytes each). |

## Referenced by

- Described by tables: [ItemChemistRecords](../tables/ItemChemistRecords.md)

## Open questions

None recorded.
