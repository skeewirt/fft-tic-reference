# TriggerConditionArgCount

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the TriggerConditionArgCounts table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="arg_words"></a>`0x0` | arg_words | `uint8` | V | number of u16 argument words that follow the condition opcode word in a battle-event trigger condition list (record length = 1 + this) |

## Referenced by

- Described by tables: [TriggerConditionArgCounts](../tables/TriggerConditionArgCounts.md)

## Open questions

None recorded.
