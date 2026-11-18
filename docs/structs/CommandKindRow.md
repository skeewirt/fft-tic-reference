# CommandKindRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One byte per skillset id.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="kind"></a>`0x0` | kind | `uint8` | V | What the skillset runs as when it is a unit command: 0 plain action list, 2 Throw, 3 Arithmeticks, 6 monster list, 7 Iaido, 9 Jump, 10 Charge; the Item command has kind 1. |

## Referenced by

- Described by tables: [CommandKind](../tables/CommandKind.md)

## Open questions

None recorded.
