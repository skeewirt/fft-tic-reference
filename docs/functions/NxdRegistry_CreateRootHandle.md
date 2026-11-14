# NxdRegistry_CreateRootHandle

- **Address:** `0x1403D32DC`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxlResourceHandle *NxdRegistry_CreateRootHandle(NxdRegistry *reg, ...)`
- **Callers:** sub_1400B2738
- **Callees:** Mem_Alloc, ResourceHandle_Init

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The resource-handle factory for root.nxl: a 168-byte NxlResourceHandle (vtable 0x140721580) whose load callback is NxdRegistry_LoadRootNxl.

## Behavior

- V: allocates 168 bytes from the registry's heap (+8), ResourceHandle_Init, flags 0x2000, byte +160 = 0, vtable NxlResourceHandle.
- V: callback pairs: +112 NxdRegistry_LoadRootNxl, +144 sub_1403D3858, both with the registry as context.

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md), [ResourceHandle_Init](ResourceHandle_Init.md)

## Notes

Its vtable shares NxdHandle_OnLoaded (slot 8) with the nxd tables' handles.

## Open questions

? what sub_1403D3858 does after the root list loaded.
