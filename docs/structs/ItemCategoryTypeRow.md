# ItemCategoryTypeRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Record kind of one category.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="kind"></a>`0x0` | kind | `uint32` | V | Record kind 0..9: selects the sub-record accessor; 8-byte records for kinds 0 and 5, 2-byte for 1, 2, 3, 6, 7, 8, 3-byte for 4 and 9. |

## Referenced by

- Described by tables: [ItemCategoryTypes](../tables/ItemCategoryTypes.md)

## Open questions

None recorded.
