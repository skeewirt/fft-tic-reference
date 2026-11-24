# WorldMapBaseList_Destruct

- **Address:** `0x14015F630`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t WorldMapBaseList_Destruct(_QWORD *self)`
- **Callers:** WorldMapBaseList_DeletingDestruct
- **Callees:** sub_1402AD648, sub_14028BC24, sub_14028C558, sub_14028F528

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Destructor of the Locations list addon (struct WorldMapBaseList).

## Behavior

- V: puts the two vtables back, frees each of the three record vectors through its allocator (vtable +24) and clears it, destroys the radio menu, the two button guide parts, the list gadget and the three parts at +400, puts the base vtables back and runs the base destructor.

## Referenced by

- Called by: [WorldMapBaseList_DeletingDestruct](WorldMapBaseList_DeletingDestruct.md)

## Open questions

None recorded.
