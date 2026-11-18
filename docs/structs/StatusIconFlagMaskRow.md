# StatusIconFlagMaskRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of BattleStatusIconFlagMasks.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="scene_flag_mask"></a>`0x0` | scene_flag_mask | `uint32` | V | bit mask OR-ed into or cleared from the scene object's status effect flag words when the status starts or ends |

## Referenced by

- Described by tables: [BattleStatusIconFlagMasks](../tables/BattleStatusIconFlagMasks.md)

## Open questions

None recorded.
