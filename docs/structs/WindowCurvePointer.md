# WindowCurvePointer

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the WindowCurvePointers table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="curve"></a>`0x0` | curve | `pointer` | V | pointer to a list of u16 animation steps ending with 4096 (the window grows or shrinks along it) |

## Referenced by

- Described by tables: [WindowCurvePointers](../tables/WindowCurvePointers.md)

## Open questions

None recorded.
