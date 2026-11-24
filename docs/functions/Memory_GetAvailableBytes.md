# Memory_GetAvailableBytes

- **Address:** `0x140018A2C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `unsigned __int64 Memory_GetAvailableBytes(void)`
- **Callers:** sub_140014CF4, App_RunFrame, sub_14006B948, sub_140092D84, ModelResourceHandle_vfunc_25
- **Callees:** GlobalMemoryStatusEx

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reports how much memory the game may still use: the operating system's available physical memory, or the /memory_limit figure minus what the allocators hold.

## Behavior

- V: asks the OS for the memory status and returns 0 when that fails.
- V: when qword_142E93E38 (the limit) is non-zero and qword_142E80448 is at least the limit, the result is the limit minus qword_142F0D960, floored at 0.
- V: otherwise the result is the OS's available physical memory.
- I: qword_142E80448 is the machine's physical memory and qword_142F0D960 the bytes the allocators hold (rest on how they are compared and on the memory threshold test in Application_InitPlatformServices).

## Notes

So a limit larger than the machine's memory is ignored.

## Open questions

? what the five callers do with the figure (not read).
