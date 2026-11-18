# UnitEditorWidget

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the UnitEditorWidgets tables.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="pos_ptr"></a>`0x0` | pos_ptr | `pointer` | V | pointer to a position record (x, y, w, h and more words) in the executable |
| <a id="desc"></a>`0x8` | desc | `bytes[8]` | ? | descriptor bytes: two small selectors, an offset byte and a size word |
| <a id="tail"></a>`0x10` | tail | `bytes[8]` | ? | tail words (a small count and flags) |

## Referenced by

- Described by tables: [UnitEditorWidgetsDefault](../tables/UnitEditorWidgetsDefault.md), [UnitEditorWidgetsLanguage0](../tables/UnitEditorWidgetsLanguage0.md)

## Open questions

None recorded.
