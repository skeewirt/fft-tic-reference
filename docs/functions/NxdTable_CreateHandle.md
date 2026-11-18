# NxdTable_CreateHandle

- **Address:** `0x1403D3E64`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NexResourceHandle *NxdTable_CreateHandle(NxdTable *table, ...)`
- **Callers:** NxdRegistry_LoadRootNxl (as the factory of the file-open call)
- **Callees:** Mem_Alloc, ResourceHandle_Init

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The resource-handle factory NxdRegistry_LoadRootNxl passes for every nxd file: creates the 168-byte NexResourceHandle whose callbacks bind the loaded file to the table object.

## Behavior

- V: allocates 168 bytes with Mem_Alloc from the registry's heap (table +0), runs ResourceHandle_Init, sets flags 0x2008 in +92 and byte +160 = 0, and sets the vtable 0x140721600 (NexResourceHandle).
- V: stores two callback pairs, each (invoker sub_1400674E8, context = the table object) followed by (function, 0): +96/+104 with NxdTable_BindRows at +112, and +128/+136 with NxdTable_OnReady at +144.
- V: returns null when the allocation fails.

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md), [ResourceHandle_Init](ResourceHandle_Init.md)
- Writes: [NexResourceHandle.loaded_callback](../structs/NexResourceHandle.md#loaded_callback), [NexResourceHandle.ready_callback](../structs/NexResourceHandle.md#ready_callback)

## Referenced by

- Appears in flows: [NxdTableLoad](../flows/NxdTableLoad.md)
- Observed behaviours: [NxdTableRebinding](../behaviors/NxdTableRebinding.md)

## Notes

Slot 8 of this handle's vtable is NxdHandle_OnLoaded; +112 holds NxdTable_BindRows.

## Open questions

None recorded.
