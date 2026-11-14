# ResourceHandle_FreeData

- **Address:** `0x140095EB0`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `void ResourceHandle_FreeData(ResourceHandle *h)`
- **Callers:** sub_140095EE0 (handle release), sub_140095234, sub_1400952DC, sub_1403BA95C
- **Callees:** Mem_Free

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Frees a handle's file buffer (+56) with Mem_Free unless flag 0x100 (+92) says the buffer is not the handle's.

## Behavior

- V: when flag 0x100 is clear and +56 is not null: Mem_Free(+56, 0, null), +56 = 0.

## State touched

- Calls: [Mem_Free](Mem_Free.md)
- Reads: [NexResourceHandle.flags](../structs/NexResourceHandle.md#flags)

## Notes

The engine frees whatever +56 holds with Mem_Free, so a buffer stored there must have been allocated with Mem_Alloc from the handle's own heap.

## Open questions

None recorded.
