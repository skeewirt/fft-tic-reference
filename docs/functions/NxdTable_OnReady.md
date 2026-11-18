# NxdTable_OnReady

- **Address:** `0x1403D417C`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `int NxdTable_OnReady(NxdTable *table, NexResourceHandle *h)`
- **Callers:** NxdHandle_OnReady
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks a table usable after its file loaded: state +12 = 2 when the load status (+80 of the handle) is 1, else 3.

## Behavior

- V: writes table +12 = (status != 1) + 2 and returns 0.

## State touched

- Reads: [NexResourceHandle.status](../structs/NexResourceHandle.md#status)
- Writes: [NxdTable.state](../structs/NxdTable.md#state)

## Referenced by

- Appears in flows: [NxdTableLoad](../flows/NxdTableLoad.md)
- Called by: [NxdHandle_OnReady](NxdHandle_OnReady.md)
- Observed behaviours: [NxdTableRebinding](../behaviors/NxdTableRebinding.md)

## Notes

NxdRegistry_LoadRootNxl leaves every table at state 1 (not loaded); readers accept 2 or 3.

## Open questions

? what status values other than 1 mean for a usable table (state 3).
