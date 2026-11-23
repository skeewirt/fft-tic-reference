# AudioQueue_WaitIdle

- **Address:** `0x140340088`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 AudioQueue_WaitIdle(void)`
- **Callers:** ClassicMenu_RunScreenStack, sub_1402F109C, sub_140345FE4, sub_1403793DC; data references
- **Callees:** sub_14033FE00, EventThread_Yield

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Blocks the calling event thread until the audio command queue has nothing running and nothing queued.

## Behavior

- V: loops while the current command kind `dword_140D49550` or the queued count (low dword of `qword_140D49558`) is non-zero: service the queue with `sub_14033FE00`, then `EventThread_Yield(1)`.

## State touched

- Calls: [sub_14033FE00](sub_14033FE00.md), [EventThread_Yield](EventThread_Yield.md)

## Notes

Whole body read.

## Open questions

None.
