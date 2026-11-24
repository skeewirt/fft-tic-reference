# GameWindow_FillCreateParams

- **Address:** `0x140010750`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `int GameWindow_FillCreateParams(void *listener, uint8_t *params)`
- **Callers:** called through the listener's virtual table (no direct caller)
- **Callees:** sub_1400366B0, sub_140033994, sub_140033CBC, sub_140034CF0, sub_140032A20, SleepEx, sub_140033A18, GetModuleHandleA, LoadIconA

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Listener step that fills the window creation record: class and title text, icon, position, size and style, from the saved settings and the startup switches.

## Behavior

- V: unless the startup byte g_Application+1255 (/ignore_config) is set and when sub_1400366B0 allows it, loads the system save file settings.sav (request type 7, 'SYSTEM') into a local copy and waits until the save request count at g_SaveRequestManager+392 is 0.
- V: sets the class name 'FFTTIC', the window title 'FINAL FANTASY TACTICS - The Ivalice Chronicles', the icon resource 0x6B, a callback pointer sub_140010F48 and clears the byte +96.
- V: position: when the dword at g_Application+1232 (the /windowpos X) is not 0x8000, it and +1228 (Y) go to the dwords +152 and +156, but a value at or below -32000 instead sets bit 29 of the dword at +144 (the constant 0x20000000; the code uses a bit-set form, so the number is not an immediate).
- V: size: when the dword at g_Application+1220 is 0x8000 the size pair is 1920 x 1080 (stored into the record only on the saved-settings path below), else the qword at +1220 (width, height) is stored at +88.
- V: when settings.sav was loaded, its saved fields override: +96, +56, +152, the size pair (+88 / +92 and +64 / +68, only when both parts are non-zero, else the defaults above) and the pair at +72 (defaulting to the pair 5994 and 100).
- V: /windowtopmost (g_Application+1405) ORs the flag 8 into the dword at +148.
- V: the dword at +144 is then XORed with 0x50000, and with bit 28 (0x10000000, a bit-toggle form) as well only when /return (g_Application+1470) is absent.
- I: +144 and +148 are the window style and extended style, the 8 being the topmost style (rests on the flag's use in the window record).

## State touched

- Calls: [sub_1400366B0](sub_1400366B0.md), [sub_140033CBC](sub_140033CBC.md), [sub_140034CF0](sub_140034CF0.md)

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)

## Notes

This is where /ignore_config, /windowpos, /windowtopmost and /return take effect on the window; the splash window is decided elsewhere (Application_Initialize).

## Open questions

? the meaning of the saved fields and of the pair 5994 / 100.
