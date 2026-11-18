# SaveErrorMessage

- **Kind:** structure
- **Area:** [Save data](../areas/save-data.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the SaveErrorMessages table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="error_code"></a>`0x0` | error_code | `uint32` | V | result code of the save-data layer (0x80110000 + n) |
| <a id="message"></a>`0x4` | message | `uint32` | V | message number shown for that result (1..20); a result not in the list shows 21 |

## Referenced by

- Described by tables: [SaveErrorMessages](../tables/SaveErrorMessages.md)

## Open questions

None recorded.
