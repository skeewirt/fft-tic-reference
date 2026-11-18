# CommandKindParam

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the CommandKindParams table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="value"></a>`0x0` | value | `int16` | I | signed number (3 or -3 seen): a step / offset of the command kind |
| <a id="flag"></a>`0x2` | flag | `uint16` | V | 1 makes the menu builder treat the kind specially (kind 2 with a command byte of 20 shows another message) |

## Referenced by

- Described by tables: [CommandKindParams](../tables/CommandKindParams.md)

## Open questions

None recorded.
