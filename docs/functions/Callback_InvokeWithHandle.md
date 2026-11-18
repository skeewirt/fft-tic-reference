# Callback_InvokeWithHandle

- **Address:** `0x1400674E8`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int Callback_InvokeWithHandle(void *context, void **callback, void **handle)`
- **Callers:** NxdHandle_OnLoaded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The invoker every nxd resource handle gets: calls the callback with the context and the handle.

## Behavior

- V: `return (*a2)(a1, *a3)`; NxdTable_CreateHandle stores it at handle +96 and +128, so the load callback runs as NxdTable_BindRows(table, handle).

## Referenced by

- Observed behaviours: [NxdTableRebinding](../behaviors/NxdTableRebinding.md)

## Open questions

None recorded.
