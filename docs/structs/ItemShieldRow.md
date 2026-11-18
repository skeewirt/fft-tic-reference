# ItemShieldRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Shield sub-record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="phys_evade"></a>`0x0` | phys_evade | `uint8` | V | Physical evade, copied to unit work +73 and +74 (I: physical evade). |
| <a id="magic_evade"></a>`0x1` | magic_evade | `uint8` | V | Magic evade, copied to unit work +77 and +78 (I: magic evade). |

## Referenced by

- Described by tables: [ItemShieldRecords](../tables/ItemShieldRecords.md)

## Open questions

None recorded.
