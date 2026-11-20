# JobTreeNavRecord

- **Kind:** structure
- **Area:** [Job tree](../areas/job-tree.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 32-byte cursor neighbour record inside a Job Tree panel record (panel +0x1A8): for each of the eight pad directions two candidate neighbour panels, each with a flag byte. JobTree_RefreshAddon copies it from the job's GeneralJob row; JobTree_HandleInput reads it.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="up"></a>`0x0` | up | `uint8[4]` | V | Direction 'up' (index 0): byte 0 = panel index of candidate 0 (0..19, 20 = none), byte 1 = its flag (non-zero: skipped when the direction came only from the second input group), byte 2 = panel index of candidate 1, byte 3 = its flag. |
| <a id="up_right"></a>`0x4` | up_right | `uint8[4]` | V | Direction 'up-right' (index 1): byte 0 = panel index of candidate 0 (0..19, 20 = none), byte 1 = its flag (non-zero: skipped when the direction came only from the second input group), byte 2 = panel index of candidate 1, byte 3 = its flag. |
| <a id="right"></a>`0x8` | right | `uint8[4]` | V | Direction 'right' (index 2): byte 0 = panel index of candidate 0 (0..19, 20 = none), byte 1 = its flag (non-zero: skipped when the direction came only from the second input group), byte 2 = panel index of candidate 1, byte 3 = its flag. |
| <a id="down_right"></a>`0xC` | down_right | `uint8[4]` | V | Direction 'down-right' (index 3): byte 0 = panel index of candidate 0 (0..19, 20 = none), byte 1 = its flag (non-zero: skipped when the direction came only from the second input group), byte 2 = panel index of candidate 1, byte 3 = its flag. |
| <a id="down"></a>`0x10` | down | `uint8[4]` | V | Direction 'down' (index 4): byte 0 = panel index of candidate 0 (0..19, 20 = none), byte 1 = its flag (non-zero: skipped when the direction came only from the second input group), byte 2 = panel index of candidate 1, byte 3 = its flag. |
| <a id="down_left"></a>`0x14` | down_left | `uint8[4]` | V | Direction 'down-left' (index 5): byte 0 = panel index of candidate 0 (0..19, 20 = none), byte 1 = its flag (non-zero: skipped when the direction came only from the second input group), byte 2 = panel index of candidate 1, byte 3 = its flag. |
| <a id="left"></a>`0x18` | left | `uint8[4]` | V | Direction 'left' (index 6): byte 0 = panel index of candidate 0 (0..19, 20 = none), byte 1 = its flag (non-zero: skipped when the direction came only from the second input group), byte 2 = panel index of candidate 1, byte 3 = its flag. |
| <a id="up_left"></a>`0x1C` | up_left | `uint8[4]` | V | Direction 'up-left' (index 7): byte 0 = panel index of candidate 0 (0..19, 20 = none), byte 1 = its flag (non-zero: skipped when the direction came only from the second input group), byte 2 = panel index of candidate 1, byte 3 = its flag. |

## Behavior

- V: the candidate 0 panel is the low byte of the GeneralJob dword at row +0x28 + 4 * direction and its flag the byte at row +0x68 + direction; candidate 1 is the low byte of the dword at row +0x48 + 4 * direction and its flag the byte at row +0x70 + direction.

## Referenced by

- Observed behaviours: [JobTreeCursorNeighbourTable](../behaviors/JobTreeCursorNeighbourTable.md)

## Notes

Detail and evidence: behavior JobTreeCursorNeighbourTable and the sheets JobTree_RefreshAddon, JobTree_HandleInput.

## Open questions

None recorded.
