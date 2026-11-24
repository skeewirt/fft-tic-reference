# Startup_InstallExceptionHandling

- **Address:** `0x14002EC0C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall Startup_InstallExceptionHandling(void)`
- **Callers:** sub_14002DEFC (application init; called from faith::Framework::Application_vfunc_1)
- **Callees:** SetUnhandledExceptionFilter, GetCurrentProcessId, DebugActiveProcess, GetUserNameW, sub_14006E530, sub_140031F44, GetLocalTime, set_invalid_parameter_handler, sub_1405DA7FC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Installs the top-level unhandled-exception filter and the startup diagnostic state: the self-debug call, the user name, the DebugDump path, the lock-file name and the invalid-parameter handler.

## Behavior

- V: calls `SetUnhandledExceptionFilter(TopLevelExceptionFilter)`.
- V: calls `DebugActiveProcess(GetCurrentProcessId())` at `0x14002EC47`; the result is not checked. A process cannot normally debug itself, so the call's practical effect is I, not established.
- V: reads the user name with `GetUserNameW` into `word_142FCF080` (zeroed on failure).
- V: builds the executable base path with `sub_14006E530`, formats `%lsDebugDump` into `word_142FCF290`, reads the local time, and formats `%ls/lock_YYYYMMDD-HHMMSS.txt` into `word_142FCF4A0`.
- V: installs `Handler` with `set_invalid_parameter_handler` and calls `sub_1405DA7FC(0, 1)`.
- V: returns 0. The caller is `sub_14002DEFC` (application initialization), reached from `faith::Framework::Application_vfunc_1`.

## Referenced by

- Called by: [Application_InitPlatformServices](Application_InitPlatformServices.md)

## Notes

The filter it installs is TopLevelExceptionFilter, the function that shows the localized 'the application will close' dialog. The self-debug call is part of the startup anti-debug/diagnostic setup; it is not needed for the game to run.

## Open questions

Why the game calls DebugActiveProcess on its own pid, and whether the return value is used anywhere later.
