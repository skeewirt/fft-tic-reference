# Startup_SetDataDirectory

- **Address:** `0x14002EA04`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `int __fastcall Startup_SetDataDirectory(void)`
- **Callers:** Game_Main (0x14002BD98)
- **Callees:** sub_140027FEC, sub_14006E460, sub_14001B798, sub_140079A8C, SetCurrentDirectoryW

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ensures the process working directory is the executable's `data` directory, so relative `data/` paths resolve when the game is launched from another directory.

## Behavior

- V: probes `data` with `sub_140027FEC`; if it exists and has the directory attribute 0x10, returns immediately.
- V: obtains the executable directory with `sub_14006E460`, formats `%s/data` with `sub_14001B798`, and probes the result with `sub_140027FEC`.
- V: when that directory exists, resolves its full path with `sub_140079A8C` and calls `SetCurrentDirectoryW`.
- V: returns the probe/call result; a missing `data` directory leaves the working directory unchanged.

## Referenced by

- Called by: [Game_Main](Game_Main.md)

## Notes

This is the first thing Game_Main does after the startup debugger check.

## Open questions

What the attribute bits returned by sub_140027FEC mean beyond the directory bit 0x10.
