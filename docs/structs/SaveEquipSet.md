# SaveEquipSet

- **Kind:** structure
- **Area:** [Save data](../areas/save-data.md)
- **Size:** 88 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One saved equipment set of a unit (three per unit record).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="name"></a>`0x0` | name | `char[65]` | V | Set name, 65 signed bytes. |
| <a id="items"></a>`0x42` | items | `int16[5]` | V | Five item ids. |
| <a id="abilities"></a>`0x4C` | abilities | `int16[5]` | V | Five ability ids. |
| <a id="job"></a>`0x56` | job | `uint8` | V | Job of the set (a signed byte in the schema). |
| <a id="is_double_hand"></a>`0x57` | is_double_hand | `uint8` | V | Double-hand flag. |

## Open questions

None recorded.
