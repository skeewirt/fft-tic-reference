# SceneUnit_ApplyStatusVisuals

- **Address:** `0x1401FAF54`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void SceneUnit_ApplyStatusVisuals(SceneUnit *scene)`
- **Callers:** SceneUnit_BuildFromQueueEntry
- **Callees:** SceneUnit_SyncSpriteFromPool

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies a scene unit's status visual set / clear masks and redraws the pose.

## Behavior

- V: (mask 0x100 is tested as bit 8) +0x15C = +0x164 | +0x15C & ~+0x16C and +0x160 = +0x168 | +0x160 & ~+0x170; clears the masks; redraws the pose (sub_14026947C, sub_14026A048 for the chicken / frog sprite 146, SceneUnit_SyncSpriteFromPool for the effect sprites 155..158).
- V: +0x15C bits 0x1FFFC2C4 make it set +0x370 (a pose flag); +0x160 bits 0..3 select the effect sprites 155..158 and bits 7 / 8 a pending transform (0x100 = sprite 146).
- V: SceneUnit_BuildFromQueueEntry zeroes the status visual words +0x15C..+0x170 (0x14026EEF9..0x14026EF1C, addresses in the caller) and ends with this function.

## State touched

- Calls: [SceneUnit_SyncSpriteFromPool](SceneUnit_SyncSpriteFromPool.md)

## Referenced by

- Observed behaviours: [StatusVisualMasks](../behaviors/StatusVisualMasks.md)

## Open questions

None recorded.
