# NxdHandle_OnLoaded

- **Address:** `0x1403D3048`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `__int64 NxdHandle_OnLoaded(NexResourceHandle *h)`
- **Callers:** ResourceHandle_LoadNow and the resource system's asynchronous load path (vtable slot 8)
- **Callees:** sub_1400674E8 (callback invoker), NxdTable_BindRows, NxdRegistry_LoadRootNxl

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 8 of the NexResourceHandle and NxlResourceHandle vtables: when the file has been read, calls the handle's load callback with its context and the handle.

## Behavior

- V: returns 0 when the context at +104 is null; else calls the invoker at +96 with (context +104, &callback +112, &h), which calls callback(context, h).
- V: for an nxd table the callback is NxdTable_BindRows(table, h); for root.nxl it is NxdRegistry_LoadRootNxl(registry, h).
- V: ResourceHandle_LoadNow calls it (vtable +64) once the read has reached state 3.
- V: returns 0 when the context (+104) is null, else makes an indirect call to the invoker at handle +96 with (context, &callback at +112, &handle); the invoker is Callback_InvokeWithHandle.

## State touched

- Calls: [NxdTable_BindRows](NxdTable_BindRows.md), [NxdRegistry_LoadRootNxl](NxdRegistry_LoadRootNxl.md)
- Reads: [NexResourceHandle.loaded_context](../structs/NexResourceHandle.md#loaded_context), [NexResourceHandle.loaded_callback](../structs/NexResourceHandle.md#loaded_callback)

## Referenced by

- Appears in flows: [NxdTableLoad](../flows/NxdTableLoad.md)
- Called by: [ResourceHandle_LoadNow](ResourceHandle_LoadNow.md)
- Observed behaviours: [NxdTableRebinding](../behaviors/NxdTableRebinding.md)

## Open questions

? the thread the asynchronous path calls it on (I: a resource loader thread).
