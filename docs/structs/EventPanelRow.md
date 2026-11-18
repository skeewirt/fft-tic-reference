# EventPanelRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 56 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EventPanelRows tables.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="arg_a"></a>`0x0` | arg_a | `uint32` | I | small selector (0, 1, 2, 3 seen) |
| <a id="arg_b"></a>`0x4` | arg_b | `uint32` | I | second selector (0 or 0xFFFFFFFF seen) |
| <a id="data_ptr"></a>`0x8` | data_ptr | `pointer` | V | pointer to the row's data record |
| <a id="code"></a>`0x10` | code | `uint32` | I | message or panel code (0x15..0x1F seen) |
| <a id="flags"></a>`0x14` | flags | `uint32` | I | flag word (0x2000, 0x10000, 0x20000 seen) |
| <a id="ptr_a"></a>`0x18` | ptr_a | `pointer` | I | pointer to a layout record |
| <a id="ptr_b"></a>`0x20` | ptr_b | `pointer` | I | pointer to a layout record |
| <a id="ptr_c"></a>`0x28` | ptr_c | `pointer` | I | pointer to a layout record |
| <a id="ptr_d"></a>`0x30` | ptr_d | `pointer` | I | pointer to a layout record |

## Referenced by

- Described by tables: [EventPanelRowsDefault](../tables/EventPanelRowsDefault.md), [EventPanelRowsLanguage0](../tables/EventPanelRowsLanguage0.md)

## Open questions

None recorded.
