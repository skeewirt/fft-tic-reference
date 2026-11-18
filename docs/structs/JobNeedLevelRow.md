# JobNeedLevelRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The required job levels for one job index: 24 nibbles.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="required_levels"></a>`0x0` | required_levels | `uint8[12]` | V | Nibble j (high nibble first) is the level needed in job index j; only the first 20 nibbles are compared. |

## Referenced by

- Described by tables: [JobNeedLevelRows](../tables/JobNeedLevelRows.md)

## Open questions

None recorded.
