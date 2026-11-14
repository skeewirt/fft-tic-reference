# NxdHandle_GetHeap

- **Address:** `0x1403D3014`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `Heap *NxdHandle_GetHeap(NexResourceHandle *h)`
- **Callers:** ResourceHandle_ReadData (vtable +112)
- **Callees:** sub_14001A29C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 14 of the nxd handle vtables: the heap the handle's file buffer is allocated from.

## Behavior

- V: byte +160 = 0 (every nxd and root.nxl handle): sub_14001A29C(qword_140C696D0).
- V: else the heap at qword_140C696D8 + 8, or qword_140C69708 when that is null.
- V: ResourceHandle_ReadData passes it to the reader that fills +56.

## Referenced by

- Called by: [ResourceHandle_ReadData](ResourceHandle_ReadData.md)

## Open questions

None recorded.
