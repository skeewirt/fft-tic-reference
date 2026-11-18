# GridHelpRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the GridHelpRows tables.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="list"></a>`0x0` | list | `pointer` | V | filled at run time with the pointer to the row's message id list; zero in the file |
| <a id="code"></a>`0x8` | code | `uint16` | V | message code selector: 0x6000, 0x6800, 0x7800 and 0x9800 pick special message ranges; any other value is the message number itself |
| <a id="fields"></a>`0xA` | fields | `bytes[14]` | ? | row geometry and neighbour numbers of the cursor grid; not decoded |

## Referenced by

- Described by tables: [GridHelpRowsDefault](../tables/GridHelpRowsDefault.md), [GridHelpRowsLanguage0](../tables/GridHelpRowsLanguage0.md)

## Open questions

None recorded.
