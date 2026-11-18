# WindowGroupStartRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of UiLegacyWindowGroupStartsLang0.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="start"></a>`0x0` | start | `uint8[12]` | V | cumulative first cell index of each of the 12 groups (0, 6, 0x16, 0x20, 0x27 ...); 4 padding bytes follow |

## Referenced by

- Described by tables: [UiLegacyWindowGroupStartsLang0](../tables/UiLegacyWindowGroupStartsLang0.md), [UiLegacyWindowGroupStartsLang1](../tables/UiLegacyWindowGroupStartsLang1.md), [UiLegacyWindowGroupStartsLang2](../tables/UiLegacyWindowGroupStartsLang2.md), [UiLegacyWindowGroupStartsLang3](../tables/UiLegacyWindowGroupStartsLang3.md)

## Open questions

None recorded.
