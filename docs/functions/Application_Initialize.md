# Application_Initialize

- **Address:** `0x1400296BC`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void Application_Initialize(void *app, const uint8_t *startup)`
- **Callers:** sub_14002C820 (call at 0x14002C82D) is the only direct caller; sub_14002BF70 reaches it through the application object's virtual table (slot +8 of the table at 0x1406FB098 is sub_14002C820); also a data reference at 0x1406FB1D0
- **Callees:** sub_14002A8D0, Mem_Alloc, sub_140032208, Application_InitPlatformServices, Splash_CreateWindow, sub_14002AA60, GetCurrentThreadId, sub_14002AF64, sub_14002B98C, sub_14002BB60, sub_14002B364, sub_14002B89C, sub_14002BA44, sub_14002B29C, sub_14002ABEC, sub_1400A0BD8, sub_14002AC90, sub_14002BC1C, OpenThread, SetThreadAffinityMask, SetThreadPriority, CloseHandle

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

First virtual step of the application object: copies the startup block into the object, brings up the platform services and decides whether the splash window is shown.

## Behavior

- V: copies the startup block into g_Application+1200 (two passes of 128 bytes plus the last 24, 280 bytes in all, the size of the block; the copy every later reader of a switch uses), and copies the byte at +1404 to +1521.
- V: runs sub_14002A8D0, then creates a 40-byte object stored at +1160 and clears +1184, then calls Application_InitPlatformServices and stops on a failure.
- V: the splash window is created through Splash_CreateWindow only when the startup byte +270 (/return) is 0 and the byte 0x142C81C79 is 0.
- V: then runs sub_14002AA60 and, only when the error-dialog object qword_143CD9B40 is still null (everything below runs only inside that condition), builds that 144-byte object (vtable of the error dialog class, the wide title text 'FINAL FANTASY TACTICS - The Ivalice Chronicles' at +16) and the current thread id into qword_140C6AD58.
- V: a chain of init calls must all succeed (inside the same condition, after UnDecorator::getFunctionIndirectType and the thread-affinity setup): sub_14002AF64, sub_14002B98C, sub_14002BB60, sub_14002B364, sub_14002B89C, sub_14002BA44 (which hands g_Application+1200 to the DirectStorage setup), sub_14002B29C, sub_14002ABEC, sub_1400A0BD8, sub_14002AC90, sub_14002BC1C (with UnDecorator::getArrayType between sub_14002B29C and sub_14002ABEC); then the window object at +1152 gets its virtual call at +8.
- V: afterwards it applies the thread affinity mask (dwThreadAffinityMask, when non-zero) and normal priority to the current thread, sets +1504 to 15, stores 20000 in the qword at +16 of the object at +1160, sets +941 to 1 and clears the byte at qword_140C69680+28.
- V: stores one 64-bit constant at g_RenderDevice+48 (one 64-bit store: 0x176A in the low dword, 100 in the high dword).
- ?: what that pair of numbers means was not traced.

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md), [Application_InitPlatformServices](Application_InitPlatformServices.md), [Splash_CreateWindow](Splash_CreateWindow.md), [sub_14002BA44](sub_14002BA44.md)

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)

## Notes

Only the parts that read the startup block are described in detail; the init calls in the chain were not read here.

## Open questions

? what the chain's init calls set up beyond DirectStorage (sub_14002BA44).
