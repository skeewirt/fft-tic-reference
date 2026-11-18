# KeyRepeatPreset

- **Kind:** structure
- **Area:** [Input](../areas/input.md)
- **Size:** 6 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the KeyRepeatPresets table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="repeat_threshold_a"></a>`0x0` | repeat_threshold_a | `uint8` | V | copied to byte_1407829FB, a key-repeat threshold |
| <a id="repeat_threshold_b"></a>`0x1` | repeat_threshold_b | `uint8` | V | copied to byte_1407829FE |
| <a id="repeat_threshold_c"></a>`0x2` | repeat_threshold_c | `uint8` | V | copied to byte_1407829FF |
| <a id="value_d"></a>`0x3` | value_d | `uint8` | V | copied to byte_1407829FC |
| <a id="value_e"></a>`0x4` | value_e | `uint8` | V | copied to byte_1407829FD |
| <a id="value_f"></a>`0x5` | value_f | `uint8` | V | copied to byte_1407829F8 |

## Referenced by

- Described by tables: [KeyRepeatPresets](../tables/KeyRepeatPresets.md)

## Open questions

None recorded.
