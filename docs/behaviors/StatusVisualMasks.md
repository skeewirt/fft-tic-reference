# StatusVisualMasks

- **Kind:** observed behaviour
- **Scope:** scene unit status visuals
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [SceneUnit_ApplyStatusVisuals](../functions/SceneUnit_ApplyStatusVisuals.md), [SceneUnit_SyncSpriteFromPool](../functions/SceneUnit_SyncSpriteFromPool.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A scene unit carries set and clear masks for status visuals; SceneUnit_ApplyStatusVisuals applies them and redraws the pose, and a scene unit build zeroes the words.

## Behavior

- V: scene unit +0x15C..+0x170 are the status visual words: +0x15C = +0x164 | +0x15C & ~+0x16C and +0x160 = +0x168 | +0x160 & ~+0x170 (set masks +0x164 / +0x168, clear masks +0x16C / +0x170); the masks are cleared afterwards.
- V: +0x15C bits 0x1FFFC2C4 make the apply step set +0x370 (a pose flag); +0x160 bits 0..3 select the effect sprites 155..158 and bits 7 / 8 a pending transform (0x100 = sprite 146, the chicken / frog sprite).
- V: SceneUnit_SyncSpriteFromPool (from the apply step) sets the scene unit's sprite byte back to its pool record's +1 when no effect sprite (155..158) is shown, taking the saved frame tables (+0x230 / +0x238).

## Open questions

None recorded.
