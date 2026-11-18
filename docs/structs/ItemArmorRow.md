# ItemArmorRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Armor sub-record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="hp_bonus"></a>`0x0` | hp_bonus | `uint8` | V | Added to unit work +50 (max HP, capped 999) when slot flags & 0x30. |
| <a id="mp_bonus"></a>`0x1` | mp_bonus | `uint8` | V | Added to unit work +54 (max MP, capped 999). |

## Referenced by

- Described by tables: [ItemArmorRecords](../tables/ItemArmorRecords.md), [ItemArmorRecordsHigh](../tables/ItemArmorRecordsHigh.md)

## Open questions

None recorded.
