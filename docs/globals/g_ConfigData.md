# g_ConfigData

- **Kind:** global
- **Address:** `0x140C69690`
- **Area:** [Save data](../areas/save-data.md)
- **Type:** `void *`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The loaded config object; the settings record of ConfigSettings_Serialize starts 16 bytes in: byte +55 forwardEnabledType (0 enable, 1 disable, 2 disable in story scenes), byte +59 enableEventKeepAuto.

## Referenced by

- Observed behaviours: [SettingsCloseSavesSystemFile](../behaviors/SettingsCloseSavesSystemFile.md)
- Read by: [EventControl_RunningTick](../functions/EventControl_RunningTick.md), [GlobalWork_GetFastForwardMode](../functions/GlobalWork_GetFastForwardMode.md), [Guide_IsUnlocked](../functions/Guide_IsUnlocked.md)
- Written by: [Guide_MarkShown](../functions/Guide_MarkShown.md), [UIAddonFFTOConfig_OnClose](../functions/UIAddonFFTOConfig_OnClose.md)

## Open questions

None recorded.
