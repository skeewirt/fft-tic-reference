# Memory_InitAllocators

- **Address:** `0x1400112F4`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 Memory_InitAllocators(const uint8_t *startup)`
- **Callers:** sub_14002BF70 (0x14002BF85)
- **Callees:** sub_140018914, sub_140013430, InitializeCriticalSection, sub_140013698, sub_1400150CC, sub_1400186A4, sub_1400146E0, sub_140014820, sub_140013778, sub_1400147BC, sub_14001866C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Brings the allocators up (reference counted) and records the memory limit given by /memory_limit.

## Behavior

- V: when the init count dword_142FCE7C0 is already non-zero it only increments it and returns 0.
- V: otherwise initialises the OS allocator and the system allocator (the latter with the size 0x20000000 and the startup byte +199), requires the qword_142F0D970 to be at least 0x1000000000, and builds the pool object at unk_142FCE540.
- V: on success it increments the count and stores the startup qword +160 (the /memory_limit value in bytes, 0 when the switch is absent) in qword_142E93E38; any failure unwinds and returns -1.
- V: the limit is read by Memory_GetAvailableBytes and by nothing else.

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)

## Notes

No switch sets the startup byte +199.

## Open questions

? the allocator internals (not read).
