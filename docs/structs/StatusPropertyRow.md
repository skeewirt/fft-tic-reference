# StatusPropertyRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Properties of one status.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="byte0"></a>`0x0` | byte0 | `uint8` | V | Read by no function of the game (every reference to the table reads +2 or later). |
| <a id="byte1"></a>`0x1` | byte1 | `uint8` | V | Read by no function of the game (every reference to the table reads +2 or later). |
| <a id="priority"></a>`0x2` | priority | `uint8` | V | Display priority: Status_ComparePriority sorts the status lists by it (larger first). |
| <a id="duration"></a>`0x3` | duration | `uint8` | V | Countdown start (Unit_SetStatusCountdown): statuses 24..38 count down once per CT round and are removed at 0; 39 (Doom) counts at the unit turn start; the values of rows below 24 are never read. |
| <a id="flags_a"></a>`0x4` | flags_a | `uint8` | V | Group flags (Status_BuildFlagMasks): 0x01 group 0, 0x02 group 1, 0x04 group 2, 0x80 group 3. |
| <a id="flags_b"></a>`0x5` | flags_b | `uint8` | V | Group flags: 0x80 group 4, 0x01 group 5, 0x02 group 6, 0x04 group 7, 0x08 group 8, 0x10 group 9. Group 6 is dropped from an add to a unit with 0x04 set in its +5 flags. |
| <a id="cancels"></a>`0x6` | cancels | `uint8[5]` | V | Status bit set this status removes when applied (and clears from the same add). |
| <a id="blocked_by"></a>`0xB` | blocked_by | `uint8[5]` | V | Status bit set that keeps this status from being applied. |

## Referenced by

- Described by tables: [StatusProperties](../tables/StatusProperties.md)
- Observed behaviours: [RecordBytesTheGameNeverReads](../behaviors/RecordBytesTheGameNeverReads.md)

## Open questions

None recorded.
