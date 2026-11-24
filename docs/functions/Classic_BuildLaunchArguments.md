# Classic_BuildLaunchArguments

- **Address:** `0x1401E6354`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 Classic_BuildLaunchArguments(char *out)`
- **Callers:** App_LaunchClassic (0x1401DDB9F)
- **Callees:** Str_Format, GetWindowRect

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the current display, sound and camera settings as a switch string of the second kind (the one Startup_ParseDisplaySwitches reads) into a 256-byte buffer and returns its length.

## Behavior

- V: the order is /output ID A B (only when the render device object and its output record exist), /resolution W H, /screenmode N, /deactiveplay N, /cursorclip N, /enablevsync N, /brightness N, /language CODE, /sound a b c d e, /camera H V, /windowpos X Y.
- V: the values come from g_ConfigData: resolution dwords at +248 and +252, screen mode byte +17, deactiveplay byte +50, cursorclip byte +52, vsync byte +57, brightness byte +19, sound dwords +24, +28, +32, +36, +40, camera bytes +48 and +49.
- V: the output id comes from the render device's output record (dword +288 of the record at g_RenderDevice+88); A and B are two dwords of a sub-record at +320 of it when the byte at +280 is 2, else 0.
- V: the language code is picked from the list ja, en, fr, de, cs, ct, ko by the two bits 5 and 6 of the config byte at +21, so only ja, en, fr and de can ever be written (an index 4..6 is unreachable).
- V: /windowpos is the top-left corner of the first window of the window list at g_Application+864 (GetWindowRect; a null window handle when the list count at +936 is not above 0).
- V: a trailing space is cut off; the string never contains /return.

## State touched

- Calls: [Str_Format](Str_Format.md)

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)

## Notes

App_LaunchClassic appends this string to the Classic program's command line.

## Open questions

? the game's own use of /return (nothing in this executable writes it).
