# MenuCursorDefault

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the MenuCursorDefaults table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="menu"></a>`0x0` | menu | `uint16` | V | menu node number |
| <a id="pad"></a>`0x2` | pad | `uint16` | I | zero |
| <a id="pad2"></a>`0x4` | pad2 | `uint32` | I | zero |
| <a id="record"></a>`0x8` | record | `pointer` | V | pointer to a small record in the data segment (0x14078DD88..0x14078DDEC) for this menu |

## Referenced by

- Described by tables: [MenuCursorDefaults](../tables/MenuCursorDefaults.md)

## Open questions

None recorded.
