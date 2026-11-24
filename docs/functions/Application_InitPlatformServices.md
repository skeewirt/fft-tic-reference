# Application_InitPlatformServices

- **Address:** `0x14002DEFC`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 Application_InitPlatformServices(void *app, const uint8_t *startup)`
- **Callers:** Application_Initialize (0x140029795)
- **Callees:** GetCurrentProcess, GetPriorityClass, SetPriorityClass, GetModuleFileNameA, GetFileVersionInfoSizeA, GetFileVersionInfoA, VerQueryValueA, Mem_Alloc, VerSetConditionMask, VerifyVersionInfoW, VerifyVersionInfoA, CoInitializeEx, CoInitialize, Startup_InstallExceptionHandling, CoCreateInstance, sub_1400B1D50, sub_14002E51C, sub_14002FDA8, sub_14002F060

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gathers process and machine facts into the application object, starts COM and the exception handling, and applies the low-memory and file-cache switches.

## Behavior

- V: stores the process priority class at +416 and +420 and sets it again; reads the program's file version resource and stores the ProductVersion text as an integer (value x 100) at +412.
- V: tests for Windows 10 or later; when true the dword +408 is 1 if the build number is at least 22000 and 0 otherwise, and when false it is 2.
- V: sets the flush-to-zero bit in the SSE control register, then CoInitializeEx (apartment threaded) and CoInitialize; a failure reports an error and returns.
- V: calls Startup_InstallExceptionHandling; fails if the global dwRefData is already set; creates a 5432-byte helper object stored in dwRefData, and builds it from two COM objects (CoCreateInstance).
- V: sets +944 to 1, stores one value from sub_1400B1D50 in both +392 and +396, builds a 304-byte object at +328 and fills +368, +376, +384 and +396..+404 with a processor mask and three population counts.
- V: calls sub_14002F060 with the startup bytes +262 and +263 and fails with an error code when it returns the code -1778122728; also returns an error when the startup byte +262 is 0 and the byte at +24 is 0.
- V: +428 (the file-cache byte) is set to 1 when the startup byte +232 (/disable_file_cache) is non-zero.
- V: low-memory mode: when qword_142E80448 is below 0x440000000 and the dword +392 is below 12, or when the startup byte +215 (/enable_memory_save) is set, the byte at qword_140C69718+617 becomes 1 and +428 becomes 1.
- I: qword_142E80448 is the machine's physical memory and +392 a processor count (rest on the 12 and 0x440000000 thresholds and the popcounts of masks).

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md), [Startup_InstallExceptionHandling](Startup_InstallExceptionHandling.md)

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)
- Called by: [Application_Initialize](Application_Initialize.md)

## Notes

The low-memory mode that /enable_memory_save forces is also entered automatically on a small-memory, few-core machine.

## Open questions

? what sub_14002F060 decides with the two startup bytes; ? the use of the byte qword_140C69718+617.
