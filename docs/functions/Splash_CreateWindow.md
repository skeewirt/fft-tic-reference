# Splash_CreateWindow

- **Address:** `0x14002EDC8`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 Splash_CreateWindow(void *splash, HINSTANCE instance, int showCmd, unsigned __int16 resourceId)`
- **Callers:** Application_Initialize (0x1400297D2), only when the startup byte +270 (/return) is 0 and the byte 0x142C81C79 is 0
- **Callees:** LoadImageA, GetObjectA, RegisterClassExA, AdjustWindowRectEx, GetSystemMetrics, CreateWindowExA, ShowWindow, UpdateWindow, SetForegroundWindow, GetLastError, sub_140026CF0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the splash window: loads a bitmap resource, registers a window class and shows a centred window of the bitmap's size.

## Behavior

- V: loads the bitmap resource named by `resourceId`, stores the handle at +16 and its description at +24 (width at +28, height at +32).
- V: registers the class 'SplashClass' (window procedure sub_14002ED50), sizes the window to the bitmap with AdjustWindowRectEx and centres it on the primary screen.
- V: creates the window titled 'FINAL FANTASY TACTICS - The Ivalice Chronicles Splash', stores it at +8, shows it with `showCmd`, updates it and brings it to the foreground; returns 0.
- V: a failure before the window exists reports the last error through sub_140026CF0 and returns its result; a failed UpdateWindow is reported the same way but the function carries on and returns 0.

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)
- Called by: [Application_Initialize](Application_Initialize.md)

## Notes

Application_Initialize passes the splash part of the window object (qword_140C69D28 + 8) as `splash`.

## Open questions

? where the splash window is closed.
