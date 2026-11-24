# Startup_ParseLaunchSwitches

- **Address:** `0x14002C2EC`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 Startup_ParseLaunchSwitches(char *startup)`
- **Callers:** Game_Main (0x14002BDC0)
- **Callees:** Startup_MatchLaunchSwitch, sub_1405DA6BC, unknown_libname_292

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the process arguments for the startup switches and sets the matching bytes, words and dwords of the 0x118-byte startup block that `Game_Main` built just before.

## Behavior

- V: the block holds the argument count (dword +0) and the argument vector (qword +8); each switch is looked up with Startup_MatchLaunchSwitch and nothing is read from the environment, a file or the registry.
- V: flag switches set one byte to 1: /exceptionoff +191, /console +192, /cmd +193, /enable_memory_save +215, /disable_tty +222, /disable_gpu_decompression +226, /disable_gpu_decompression_metacommand +227, /enable_builtin_cpu_decompression +228, /disable_direct_destination +230, /disable_file_buffering +231, /disable_file_cache +232, /razor_gpu_friendly +236, /razor_cpu_friendly +237, /disable_directstorage +254, /disable_nxd_allocator +266, /ignore_config +55, /windowtopmost +205, /return +270, /ouncenx_upgrade +271.
- V: /disable_direct_device stores the 16-bit value 257 at +229, which sets both byte +229 and byte +230 to 1 (so it also implies /disable_direct_destination).
- V: value switches take the next argument(s) and only when the needed index is below the argument count: /memory_limit and /buildin_cpu_decompression_threads need one value, /windowpos needs two.
- V: /memory_limit converts its value with a decimal-float routine, multiplies by 1024.0 and shifts the integer left by 20, so the qword at +160 is the value in GiB expressed in bytes (a limit of 8 gives 8 x 2^30).
- V: /buildin_cpu_decompression_threads converts its value with a decimal-integer routine into the dword at +36.
- V: /windowpos X Y stores X in the dword at +32 and Y in the dword at +28 (note the order).
- I: the decimal conversions are the C runtime's string-to-number routines (rests on the call shape: a string in, a number out).
- V: the function returns 0 whatever it found; an unknown switch is ignored without a message.
- V: only the switches that have a reader in this executable do anything; see the LaunchSwitches registry for which byte is read where and which switches have no reader (I).

## State touched

- Calls: [Startup_MatchLaunchSwitch](Startup_MatchLaunchSwitch.md)

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)
- Resolves registries: [LaunchSwitches](../registries/LaunchSwitches.md)

## Notes

Defaults come from sub_14002C1FC, called just before: the window size and position dwords at +20, +24, +28 and +32 start at 0x8000 (the 'not given' value that the window code tests), +160 starts at 0 and every flag starts at 0.

## Open questions

? what the six switches without a reader were meant to do (see the LaunchSwitches registry).
