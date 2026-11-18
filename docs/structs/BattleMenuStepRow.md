# BattleMenuStepRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the command menu step tables (same shape as the stock menu step table).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="node"></a>`0x0` | node | `int16` | I | menu node number the step works on |
| <a id="code"></a>`0x2` | code | `uint16` | I | screen / message code written to the node (0x8004, 0x500x ...) |
| <a id="arg_a"></a>`0x4` | arg_a | `int16` | I | second node or value |
| <a id="arg_b"></a>`0x6` | arg_b | `int16` | I | third value (0xFFFF = none) |
| <a id="flag"></a>`0x8` | flag | `uint32` | I | 1 in most rows |
| <a id="task"></a>`0x10` | task | `pointer` | V | entry function of the task the step starts (here the command menu task) |
| <a id="arg"></a>`0x18` | arg | `uint32` | I | small argument (0, 2, 3, 8, 0x28 seen) |

## Referenced by

- Described by tables: [CommandMenuSteps](../tables/CommandMenuSteps.md)

## Open questions

None recorded.
