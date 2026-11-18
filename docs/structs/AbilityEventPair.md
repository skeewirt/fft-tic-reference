# AbilityEventPair

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the AbilityEventPairs table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="key"></a>`0x0` | key | `int16` | I | id compared in the job screen (ability or job id) |
| <a id="event_var"></a>`0x2` | event_var | `int16` | V | event variable id written with the value 12 when the pair matches (0x3CE .. 0x3F5) |

## Referenced by

- Described by tables: [AbilityEventPairs](../tables/AbilityEventPairs.md)

## Open questions

None recorded.
