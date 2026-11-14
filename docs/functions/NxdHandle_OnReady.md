# NxdHandle_OnReady

- **Address:** `0x1403D3090`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `__int64 NxdHandle_OnReady(NexResourceHandle *h)`
- **Callers:** ResourceHandle_LoadNow (vtable +104)
- **Callees:** sub_1400674E8, NxdTable_OnReady

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 13 of the nxd handle vtables: calls the second callback pair (+128 invoker, +136 context, +144 function) after the load finished.

## Behavior

- V: returns 0 when the context at +136 is null; else invoker(+136, &+144, &h).
- V: for an nxd table the function is NxdTable_OnReady.

## State touched

- Calls: [NxdTable_OnReady](NxdTable_OnReady.md)

## Referenced by

- Called by: [ResourceHandle_LoadNow](ResourceHandle_LoadNow.md)

## Open questions

None recorded.
