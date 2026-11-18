# LegacyMenuRowResultRecord

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the LegacyMenuRowResults table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="menu_id"></a>`0x0` | menu_id | `uint32` | V | menu node id (0, 14, 19, 20, 32 ... 106) |
| <a id="pad"></a>`0x4` | pad | `uint32` | V | zero |
| <a id="results"></a>`0x8` | results | `pointer` | V | pointer to a byte list: +0 count, then the result code of each row |

## Referenced by

- Described by tables: [LegacyMenuRowResults](../tables/LegacyMenuRowResults.md)

## Open questions

None recorded.
