# ResourceHandle_ReadData

- **Address:** `0x1400961D4`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int ResourceHandle_ReadData(ResourceHandle *h)`
- **Callers:** ResourceHandle_LoadNow (through vtable slot 7, sub_140095F84), sub_1400952DC
- **Callees:** sub_140095FE4, NxdHandle_GetHeap (vtable +112), the reader's read slot

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the handle's file into its buffer (+56) through its reader object (+48), allocating from the heap the handle's slot 14 returns.

## Behavior

- V: with flag 0x800 it first opens the file (sub_140095FE4: the reader resolves the path into the string object at +40 and the size into +64).
- V: then reader->vtable[10](reader, &h->buffer (+56), resolved path, heap = h->vtable[14](h), size +64, size +64, 0).
- V: returns 0x96080017 when there is no reader.

## State touched

- Calls: [NxdHandle_GetHeap](NxdHandle_GetHeap.md)
- Writes: [NexResourceHandle.data](../structs/NexResourceHandle.md#data)

## Referenced by

- Appears in flows: [NxdTableLoad](../flows/NxdTableLoad.md)
- Called by: [ResourceHandle_LoadNow](ResourceHandle_LoadNow.md)

## Open questions

? the reader's allocation alignment (the heap call is in the reader).
