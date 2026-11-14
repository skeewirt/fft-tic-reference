# TopLevelExceptionFilter

- **Address:** `0x14002EAE0`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `LONG __stdcall TopLevelExceptionFilter(struct _EXCEPTION_POINTERS *info)`
- **Callers:** None (installed by Startup_InstallExceptionHandling via SetUnhandledExceptionFilter)
- **Callees:** sub_14007EB7C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The unhandled-exception filter installed by Startup_InstallExceptionHandling. It shows the localized 'an error has occurred, the application will close' dialog and returns 1, so the process terminates.

## Behavior

- V: increments `dword_142C8B964` and enters the critical section at `stru_141D8BCB0`.
- V: builds a six-entry message table with English, French and German variants, then selects an entry from `g_LanguageInfo+8` (language code 0..5; fallback 1).
- V: when `qword_143CD9B40` is non-null, calls `sub_14007EB7C` with the selected message.
- V: leaves the critical section, decrements the counter and returns 1 (EXCEPTION_EXECUTE_HANDLER), which ends the process.
- V: no direct caller; it is installed as a callback with SetUnhandledExceptionFilter.

## State touched

- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)
- Writes: [g_ExceptionFilterDepth](../globals/g_ExceptionFilterDepth.md)

## Notes

This is the dialog seen when an unhandled breakpoint or access violation reaches the game's filter. It runs only for exceptions that no earlier handler consumed.

## Open questions

The meaning of the counter at dword_142C8B964 (re-entry guard vs. telemetry) and the six-entry language table's exact ordering.
