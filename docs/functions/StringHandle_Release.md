# StringHandle_Release

- **Address:** `0x140026D9C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void StringHandle_Release(void *member)`
- **Callers:** sub_140095E5C
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Frees a {allocator, pointer} string-like member.

## Behavior

- I: named from its use in the crash below.
- V (crash dump, 2026-11-13): an access violation reading 0xFFFFFFFFFFFFFFFF at its first load through rcx (rcx = 0x3F80000000000000), reached from sub_140095E5C <- UIResourceHandle_Delete (0x1403D99C0) <- GUICore_UpdateFrame <- GUICore_DispatchEvent <- App_RunFrame; the object's vtable was the ResourceHandle vtable 0x1406FF618 left by its destructor (I: the caller addresses and values come from the dump, not from this body).

## Open questions

None recorded.
