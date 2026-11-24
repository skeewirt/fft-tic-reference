# GlobalWork_GetFastForwardMode

- **Address:** `0x1401E8A9C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `uint32 GlobalWork_GetFastForwardMode(GlobalWork *gw)`
- **Callers:** 25 call sites: EventControl_RunningTick, EventControl_UpdateGuide, EventControl_IsAutoAdvancing, GlobalWork_GetSpeedMultiplier, BattleControl_FrameUpdate, WorldMap_UpdateFastForward, EventControl_CarryToNextEvent, EventMessage_Task, EventMessage_Scripted, EventVoice_PlayTask, sub_1400F08E8, sub_14013B7C4, sub_14014DC80, sub_140157864, sub_140157C30, sub_14015B7C4, sub_14015CE18, sub_1401D6988, sub_1401EC958, sub_14020C30C, sub_140222688, sub_14022284C, sub_140247A4C, sub_1402CC2E0, sub_1402DA018
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the fast-forward mode of the current frame after the 'Fast-forward' setting is applied: 0 none, 1 battle, 2 event script, 3 world map.

## Behavior

- V: when g_ConfigData is set and its byte +55 is 1, returns 0.
- V: when that byte is 2 and the dword at gw +96 is 2, returns 0.
- V: otherwise returns the dword at gw +96.
- V (data): byte +55 is the setting 'Fast-forward' (ConfigItem row 22, values from ConfigItemForwardEnabledType: 0 'Enable', 1 'Disable', 2 'Disable During Story Scenes'); the config schema ConfigSettings_Serialize names the field forwardEnabledType at +39 of the settings record, 16 bytes into the object g_ConfigData points to.
- I: the offset pair (+39 in the record, +55 in the object) and the three values with the same meaning as the three texts make the identification; the write of the setting into the byte was not traced.

## State touched

- Reads: [g_ConfigData](../globals/g_ConfigData.md), [GlobalWork.ff_mode](../structs/GlobalWork.md#ff_mode)

## Referenced by

- Called by: [BattleControl_FrameUpdate](BattleControl_FrameUpdate.md), [BattleVoice_RollAndPlay](BattleVoice_RollAndPlay.md), [EventControl_CarryToNextEvent](EventControl_CarryToNextEvent.md), [EventControl_IsAutoAdvancing](EventControl_IsAutoAdvancing.md), [EventControl_RunningTick](EventControl_RunningTick.md), [EventControl_UpdateGuide](EventControl_UpdateGuide.md), [GlobalWork_GetSpeedMultiplier](GlobalWork_GetSpeedMultiplier.md), [WorldMapAgent_SetState](WorldMapAgent_SetState.md), [WorldMap_UpdateFastForward](WorldMap_UpdateFastForward.md)
- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)

## Notes

Every reader of the level goes through this test first, so a level left non-zero is ignored when the mode is 0 or the setting turns the mode off.

## Open questions

None recorded.
