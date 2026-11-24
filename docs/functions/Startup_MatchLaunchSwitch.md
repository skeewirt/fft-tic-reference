# Startup_MatchLaunchSwitch

- **Address:** `0x14002C634`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char Startup_MatchLaunchSwitch(int *args, const char *name, int *index)`
- **Callers:** Startup_ParseLaunchSwitches (23 calls), Startup_ParseDisplaySwitches (10 calls)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks for an argument that is exactly the given switch name and reports whether it is present and at which index.

## Behavior

- V: walks the argument vector from index 0 (the program path is compared too) and stops at the first entry equal to `name` byte for byte; the comparison is exact and case-sensitive.
- V: when `index` is not null it receives the position of the match; the value switches use it to find their values at index + 1 (and + 2).
- V: returns 1 on a match and 0 when no argument matches or the count is 0.
- V: only the first occurrence counts; a repeated switch is not seen a second time.

## Referenced by

- Called by: [Startup_ParseDisplaySwitches](Startup_ParseDisplaySwitches.md), [Startup_ParseLaunchSwitches](Startup_ParseLaunchSwitches.md)
- Resolves registries: [LaunchSwitches](../registries/LaunchSwitches.md)

## Notes

The argument block is the one the startup block carries: count at +0, vector at +8. Startup_ParseDisplaySwitches passes the copy at g_Application+1200.

## Open questions

None recorded.
