# SceneUnit_SyncSpriteFromPool

- **Address:** `0x14026A1DC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void SceneUnit_SyncSpriteFromPool(SceneUnitSlot *unit, int arg)`
- **Callers:** sub_1401FAF54
- **Callees:** SceneUnit_RunPlacement, sub_140268E80, sub_140268EB0, sub_14026947C, sub_140269BBC, sub_14026AE1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Keeps a scene unit's sprite byte in step with its look pool record, and switches to the four effect sprites 155 to 158 when the unit's effect flags ask for them.

## Behavior

- V: when none of the low four bits of the unit's flag dword (+352) is set, reads the byte at +1 of the pool record named by unit +9 and, when it differs from unit +0xA, copies it there and rebuilds the unit's frame data (sub_14026947C, sub_140269BBC, sub_14026AE1C).
- V: when one of the flags is set it picks 155 (bit 0), 156 (bit 1), 157 (bit 2) or 158 (bit 3) as the sprite and, when it differs from the current byte, replaces the unit's frame sources and runs SceneUnit_RunPlacement.
- V: called from sub_1401FAF54 (SceneUnit_ApplyStatusVisuals); sets the scene unit's sprite byte back to its pool record's +1 when no effect sprite (155..158) is shown, taking the saved frame tables (+0x230 / +0x238; +0x238 is reached through the pair copy).

## State touched

- Calls: [SceneUnit_RunPlacement](SceneUnit_RunPlacement.md), [sub_140269BBC](sub_140269BBC.md)

## Referenced by

- Called by: [SceneUnit_ApplyStatusVisuals](SceneUnit_ApplyStatusVisuals.md)
- Observed behaviours: [LookSlotsAlreadyInTheGame](../behaviors/LookSlotsAlreadyInTheGame.md), [StatusVisualMasks](../behaviors/StatusVisualMasks.md)

## Notes

Structure: SceneUnitSlot. The name is ours (IDB: sub_14026A1DC). The four effect sprites are the ones CharaRender_BuildAtlasTexture answers with HD entry 160.

## Open questions

? what the flag bits mean in play.
