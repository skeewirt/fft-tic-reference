# WindowColourSetRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of UiLegacyWindowColourSetsLang1.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="flag"></a>`0x0` | flag | `uint32` | I | 1 starts a colour group |
| <a id="colour"></a>`0x4` | colour | `uint32` | I | colours of the form (red, green, blue, 0), mostly shades 0x94 8A 80 / 0x4E 44 30 |

## Referenced by

- Described by tables: [UiLegacyWindowColourSetsLang1](../tables/UiLegacyWindowColourSetsLang1.md), [UiLegacyWindowColourSetsLang2](../tables/UiLegacyWindowColourSetsLang2.md), [UiLegacyWindowColourSetsLang3](../tables/UiLegacyWindowColourSetsLang3.md)

## Open questions

None recorded.
