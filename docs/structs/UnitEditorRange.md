# UnitEditorRange

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the UnitEditorRanges tables.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="low"></a>`0x0` | low | `int32` | V | smallest value the field accepts |
| <a id="high"></a>`0x4` | high | `int32` | V | largest value the field accepts |

## Referenced by

- Described by tables: [UnitEditorRangesA](../tables/UnitEditorRangesA.md), [UnitEditorRangesB](../tables/UnitEditorRangesB.md)

## Open questions

None recorded.
