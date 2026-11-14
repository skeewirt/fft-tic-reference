# ResourceHandle_Init

- **Address:** `0x140095DA0`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `ResourceHandle *ResourceHandle_Init(ResourceHandle *h)`
- **Callers:** NxdTable_CreateHandle, NxdRegistry_CreateRootHandle, UIResourceHandle_New, CustomResourceHandle_Ctor and about 12 others
- **Callees:** GetCurrentThreadId

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructs the common part of a resource handle: reference count 1, empty path, reader, buffer and status fields.

## Behavior

- V: vtable ResourceHandle (0x1406FF618), +12 reference count 1, +8 = 1; +16..+88 cleared (+24 requested path, +40 resolved path object, +48 reader, +56 buffer, +64 size, +72 path hash, +80 status, +84 state).
- V: +92 flag bits 6..7: 0x80 when called off the main thread (qword_140C6AD58).

## Referenced by

- Called by: [NxdRegistry_CreateRootHandle](NxdRegistry_CreateRootHandle.md), [NxdTable_CreateHandle](NxdTable_CreateHandle.md)

## Open questions

None recorded.
