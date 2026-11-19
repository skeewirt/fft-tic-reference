# EventId_TestByte27

- **Address:** `0x140254ABC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int EventId_TestByte27(void)`
- **Callers:** sub_14024C068
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns 0 when event variable 39's EventId row byte +0x27 is non-zero, else 0x10002.

## Behavior

- V: reads the EventId row of event variable 39; byte +0x27 non-zero -> 0, else 0x10002.
- V: the only caller, sub_14024C068, stores the result in dword_142FF9CA4 and goes on to EventCmd_UiDispatch.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Open questions

? what the two result values select (the meaning of EventId +0x27 is not decoded).
