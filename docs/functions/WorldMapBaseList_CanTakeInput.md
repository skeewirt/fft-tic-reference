# WorldMapBaseList_CanTakeInput

- **Address:** `0x1401603C4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool WorldMapBaseList_CanTakeInput(int64_t self)`
- **Callers:** vtable 0x14070F5C8 slot 3 (WorldMapAgent_LocationsListBlocked calls it through the vtable)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vtable slot 3 of the Locations list addon (struct WorldMapBaseList): true when neither busy byte +42 nor +43 is set.

## Behavior

- V: returns +42 == 0 and +43 == 0.

## Open questions

None recorded.
