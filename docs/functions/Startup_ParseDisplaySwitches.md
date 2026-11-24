# Startup_ParseDisplaySwitches

- **Address:** `0x1401E6650`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 Startup_ParseDisplaySwitches(void)`
- **Callers:** sub_1400B532C (0x1400B53E3; that function is itself reached through a pointer table)
- **Callees:** Startup_MatchLaunchSwitch, unknown_libname_292

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads a second set of switches (resolution, screen mode, output, focus and cursor options, vsync, brightness, language, sound volumes, camera options) from the argument copy held by the application and fills a 48-byte settings block in the data section.

## Behavior

- V: sets the block's defaults first (resolution pair and output id all ones, screen mode all ones, brightness 5, language 0, the five sound values 70 then 100 four times, every other flag 0), then looks for each switch with Startup_MatchLaunchSwitch on the argument copy at g_Application+1200.
- V: /resolution W H (needs index+2 below the count): both values above 0 are stored as the two dwords at 0x1407DC3C0 and 0x1407DC3C4.
- V: /screenmode N: a value of 0..2 goes to the byte at 0x1407DC3D8, any other value leaves it alone.
- V: /output ID A B (needs index+3 below the count): a non-zero ID is stored as the qword at 0x1407DC3C8; A and B, when both are non-zero, go to the dwords at 0x1407DC3D0 and 0x1407DC3D4.
- V: /deactiveplay, /cursorclip and /enablevsync take 0 or 1 (any non-zero value counts as 1) into the bytes at 0x1407DC3D9, 0x1407DC3DA and 0x1407DC3DB.
- V: /brightness N: a value of 0..10 goes to the dword at 0x1407DC3DC.
- V: /language CODE: the argument is compared with the seven strings ja, en, fr, de, cs, ct, ko and the index of the match (0..6) goes to the dword at 0x1407DC3E0; no match leaves it alone.
- V: /sound A B C D E (needs index+5 below the count): each value of 0..100 goes to its own byte at 0x1407DC3E4 .. 0x1407DC3E8; a value above 100 leaves that byte alone.
- V: /camera H V (needs index+2 below the count): bytes 0x1407DC3E9 and 0x1407DC3EA become 1 when the value is non-zero, else 0.
- V: the only references to the block 0x1407DC3C0 .. 0x1407DC3EA are in this function (every field is written here and read nowhere else).
- I: the block therefore has no effect in this executable; the switches and the field order are the same set that Classic_BuildLaunchArguments writes into the relaunch string (rests on the identical names and order).
- V: /windowpos is not read here; it belongs to the startup parser.

## State touched

- Calls: [Startup_MatchLaunchSwitch](Startup_MatchLaunchSwitch.md)

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)
- Resolves registries: [LaunchSwitches](../registries/LaunchSwitches.md)

## Notes

The block is two globals, xmmword_1407DC3C0 (resolution pair, output id) and ymmword_1407DC3D0 (everything else). The switch syntax is listed in the LaunchSwitches registry.

## Open questions

? whether a reader reaches the block through a computed address (no direct reference exists).
