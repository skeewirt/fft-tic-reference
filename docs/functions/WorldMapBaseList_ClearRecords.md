# WorldMapBaseList_ClearRecords

- **Address:** `0x1401603D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t WorldMapBaseList_ClearRecords(int64_t self, int newState)`
- **Callers:** WorldMapAgent_SetState (vtable slot 25 of each addon)
- **Callees:** UIListGadget_SetCount

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vtable slot 25 of the Locations list addon (struct WorldMapBaseList) (the agent's state-change notice): empties the three record vectors unless the new state is 3.

## Behavior

- V: for a new state other than 3 it sets each vector's end to its begin and the list count to 0.

## State touched

- Calls: [UIListGadget_SetCount](UIListGadget_SetCount.md)

## Open questions

None recorded.
