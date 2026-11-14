# UIRender_GetThreadContext

- **Address:** `0x1403B8288`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall UIRender_GetThreadContext(__int64 renderer)`
- **Callers:** UIRender_AppendCommand, UIRender_QueueImageDraw, sub_1403B830C, sub_1403B8384, sub_1403B8474 (V)
- **Callees:** _dyn_tls_on_demand_init

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the UIContext slot (80 bytes) belonging to the calling thread, chosen by the thread state's position in the thread-state array.

## Behavior

- V: ts = *(TLS-state + 56) (the thread's render thread state, lazily initialised by _dyn_tls_on_demand_init).
- V: index = (ts - *(qword_140C696A8 + 4984)) / 6032 (array of 6032-byte thread states).
- V: returns *(*(renderer + 8408) + 200) + 80 * index. The UIContext array (80 bytes each, 32 of them) is the one built by UIRender_CreateBuffers at r+200.
- I: the +8408 object is the UIRender Renderer, +200 its UIContext array: a per-thread command list so UI draws can be recorded from up to 32 threads without locking.

## State touched

- Reads: [g_RenderDevice](../globals/g_RenderDevice.md)

## Referenced by

- Called by: [UIRender_AppendCommand](UIRender_AppendCommand.md), [UIRender_QueueImageDraw](UIRender_QueueImageDraw.md)

## Open questions

None recorded.
