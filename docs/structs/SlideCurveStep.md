# SlideCurveStep

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the PanelSlideCurve table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="value"></a>`0x0` | value | `int16` | V | curve value; the 12 values rise 4, 13, 31, 67, 139, 144 and fall back symmetrically |

## Referenced by

- Described by tables: [PanelSlideCurve](../tables/PanelSlideCurve.md)

## Open questions

None recorded.
