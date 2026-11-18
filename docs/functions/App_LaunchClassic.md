# App_LaunchClassic

- **Address:** `0x1401DDB5C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void App_LaunchClassic(void)`
- **Callers:** Boot_Update
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the Classic executable and ends this one.

## Behavior

- V: `CreateProcessA` of `<game dir>/FFT_classic.exe <args>` (the arguments from 0x1401E6354, the game directory from `qword_143CD9B90`+48), closes the handles, then sets the quit request (`g_Application`+1520 = 1).

## Referenced by

- Observed behaviours: [QuitRequest](../behaviors/QuitRequest.md)

## Notes

Behavior: QuitRequest. Separately, the game imports `SteamAPI_RestartAppIfNecessary`, called from another function (0x14002F060), not from this one.

## Open questions

None recorded.
