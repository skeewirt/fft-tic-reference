# EffectKindRecordsRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EffectKindRecords table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="sequence_kind"></a>`0x0` | sequence_kind | `uint8` | V | handler kind of the sequence entry (0..22) |
| <a id="pad"></a>`0x1` | pad | `uint8` | I | zero in every row |
| <a id="param"></a>`0x2` | param | `uint16` | I | per kind parameter (flash profile row or flag bits) |

## Referenced by

- Described by tables: [EffectKindRecords](../tables/EffectKindRecords.md)

## Open questions

None recorded.
