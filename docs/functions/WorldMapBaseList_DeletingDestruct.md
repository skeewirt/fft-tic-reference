# WorldMapBaseList_DeletingDestruct

- **Address:** `0x14015F5FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t WorldMapBaseList_DeletingDestruct(int64_t self, char flags)`
- **Callers:** vtable 0x14070F5C8 slot 0; sub_1401CF310 (the second base's thunk)
- **Callees:** WorldMapBaseList_Destruct, sub_14041FB00

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vtable slot 0 of the Locations list addon (struct WorldMapBaseList): destructs and, with flag bit 1, frees the 1,856 bytes.

## Behavior

- V: WorldMapBaseList_Destruct, then sub_14041FB00(self, 1856) when flags & 1.

## State touched

- Calls: [WorldMapBaseList_Destruct](WorldMapBaseList_Destruct.md)

## Open questions

None recorded.
