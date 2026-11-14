# GlobalWork

- **Kind:** structure
- **Area:** [Application and startup](../areas/app-startup.md)
- **Size:** 136 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

ffto::Game::GlobalWork (vtable 0x140713EA8), the singleton at g_GlobalWork. Only the fast-forward fields are listed.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="ff_level"></a>`0x58` | ff_level | `uint32` | V | Fast-forward level: 0 off, 1 (3 game steps per frame), 2 (5 steps). Written every frame by BattleControl_FrameUpdate (mode 1), EventControl_RunningTick (mode 2) and WorldMap_UpdateFastForward (mode 3); cleared when a pause overlay opens, when the battle leaves a fast-forward state and by several world UI routines. | [BattleControl_FrameUpdate](../functions/BattleControl_FrameUpdate.md), [EventControl_ApplyCarry](../functions/EventControl_ApplyCarry.md), [EventControl_RunningTick](../functions/EventControl_RunningTick.md), [WorldMap_UpdateFastForward](../functions/WorldMap_UpdateFastForward.md) | [EventControl_CarryToNextEvent](../functions/EventControl_CarryToNextEvent.md), [EventControl_IsAutoAdvancing](../functions/EventControl_IsAutoAdvancing.md), [EventControl_UpdateGuide](../functions/EventControl_UpdateGuide.md), [GlobalWork_GetSpeedMultiplier](../functions/GlobalWork_GetSpeedMultiplier.md) |
| <a id="frame_step"></a>`0x5C` | frame_step | `uint32` | V | Index of the game step being run inside the current displayed frame (0 .. multiplier - 1), 0 outside GameTasks_RunFrameSteps. EventControl_Update runs only on step 0. | [GameTasks_RunFrameSteps](../functions/GameTasks_RunFrameSteps.md) |  |
| <a id="ff_mode"></a>`0x60` | ff_mode | `uint32` | V | Which fast-forward handler is live: 0 none, 1 battle, 2 event script, 3 world map. Rewritten every battle frame by the battle frame routine sub_140210AF0; 3 is set by the world map set-up sub_14033EC0C. |  | [GlobalWork_GetFastForwardMode](../functions/GlobalWork_GetFastForwardMode.md) |
| <a id="flag_64"></a>`0x64` | flag_64 | `uint8` | ? | Tested by the message tasks and the opening tasks next to the fast-forward fields; meaning not read. |  |  |

## Behavior

- V: the constructor sub_1401E88D4 zeroes the qwords +88 and +96 (level, step, mode and the dword after it).
- V: no reader uses ff_level without GlobalWork_GetFastForwardMode: a stale level under mode 0 has no effect.

## Referenced by

- Global instances: [g_GlobalWork](../globals/g_GlobalWork.md)
- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? The other fields (a float 1.0 at +8, two containers, the dwords +116 .. +128).
