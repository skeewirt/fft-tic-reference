# PopupBounceStep

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the PopupBounceCurve table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dy"></a>`0x0` | dy | `int16` | V | signed offset for this frame (0, -72 ... -144 ... -72, 0: an arc) |

## Referenced by

- Described by tables: [PopupBounceCurve](../tables/PopupBounceCurve.md)

## Open questions

None recorded.
