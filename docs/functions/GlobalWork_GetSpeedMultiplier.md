# GlobalWork_GetSpeedMultiplier

- **Address:** `0x1401E8AC4`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `int GlobalWork_GetSpeedMultiplier(GlobalWork *gw)`
- **Callers:** GameTasks_RunFrameSteps, UI_FrameUpdate, sub_1400FD49C, sub_14010C624, sub_14013B7C4, sub_14015CE18, sub_14020C30C, sub_140216EB4, sub_14022280C, sub_14022284C, sub_14022347C, sub_1402DA018, sub_1402DAC54
- **Callees:** GlobalWork_GetFastForwardMode

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The number of game steps per displayed frame: 1 normally, 3 at fast-forward level 1, 5 at level 2.

## Behavior

- V: when GlobalWork_GetFastForwardMode is not 0 and the dword at gw +88 is 1 or 2, returns g_FastForwardMultipliers[level]; otherwise 1.
- V (data): the table holds 1, 3, 5 (index 0 is never used: level 0 returns 1 before the table).

## State touched

- Calls: [GlobalWork_GetFastForwardMode](GlobalWork_GetFastForwardMode.md)
- Reads: [GlobalWork.ff_level](../structs/GlobalWork.md#ff_level), [g_FastForwardMultipliers](../globals/g_FastForwardMultipliers.md)

## Referenced by

- Called by: [GameTasks_RunFrameSteps](GameTasks_RunFrameSteps.md)
- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)

## Open questions

? What the fourth dword after the table (28) belongs to.
