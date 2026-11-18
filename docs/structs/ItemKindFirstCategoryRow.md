# ItemKindFirstCategoryRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

First category of one kind.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="first_category"></a>`0x0` | first_category | `uint32` | V | Index into ItemCategoryFirstIds of the first category of the kind; the kind first item id is that entry, and the sub-record index is id minus it. |

## Referenced by

- Described by tables: [ItemKindFirstCategories](../tables/ItemKindFirstCategories.md)

## Open questions

None recorded.
