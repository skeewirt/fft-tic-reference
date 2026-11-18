# EventOperandLengthRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Operand length of one opcode.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="length"></a>`0x0` | length | `uint8` | V | Operand byte count of the opcode; opcode 0xE6 and some cases of 0x10, 0x51 and 0xEB are code exceptions. |

## Referenced by

- Described by tables: [EventOperandLengths](../tables/EventOperandLengths.md)

## Open questions

None recorded.
