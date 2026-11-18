# ClassicLoadWindowDefaultRecord

- **Kind:** structure
- **Area:** [Save data](../areas/save-data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the ClassicLoadWindowDefault table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="window"></a>`0x0` | window | `bytes[128]` | V | window rectangle and text-cell layout of the classic load menu (passed to the window drawer sub_14031DBE4: +0 x, +2 y, +4 w, +6 h, then texture coordinates) |

## Referenced by

- Described by tables: [ClassicLoadWindowDefault](../tables/ClassicLoadWindowDefault.md)

## Open questions

None recorded.
