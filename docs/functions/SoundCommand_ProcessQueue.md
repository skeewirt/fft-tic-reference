# SoundCommand_ProcessQueue

- **Address:** `0x140501F50`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 SoundCommand_ProcessQueue(void)`
- **Callers:** sub_1404FBC90 (0x1404FBCCE); also stored in pointer tables
- **Callees:** EnterCriticalSection, LeaveCriticalSection, sub_14052D910, sub_14052D1D0, sub_14052D350, sub_14052CCD0, sub_14051F8C0, sub_14051FE60, sub_140520780, sub_14052D160

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sound driver step that pops queued commands and runs them; one command selects a config category layer by name.

## Behavior

- V: returns -1 when the driver object xmmword_140C16328 is null; otherwise pops entries from the object's list under its critical section (list head +96, section +152) and switches on the first dword of each entry.
- V: command 3: with a name pointer at entry+24 it looks the name up in the sound config file's category layer list and uses the layer byte of the match; with no name it uses the dword at entry+20.
- V: when the name is not in the file, the text 'SDebug' selects the layer -2 and the text 'SUserConfig' selects the layer -3; any other name leaves -1.
- V: it then calls sub_14052D160 on the object looked up by the id at entry+8 with that layer.
- V: commands 0, 1 and 2 look up the object by the id at +8 and call sub_14052D1D0, sub_14052D350 and sub_14052CCD0.
- ?: the remaining commands were not read (head only).

## Referenced by

- Observed behaviours: [SoundConfigDebugLayerNames](../behaviors/SoundConfigDebugLayerNames.md)

## Notes

Every callee listed is a direct call inside this very large function (V: found by walking all its blocks). Only the head of the function was read. The name 'SUserConfig' is also the category passed by the settings apply routine sub_1400B6CF8 when it sets the volumes, and three times by sub_1401D6E48; 'SDebug' is used nowhere else in the executable.

## Open questions

? the other commands; ? whether any config file in the game data defines an 'SDebug' layer.
