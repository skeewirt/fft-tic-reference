# LauncherFocusRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of UiLauncherFocusNeighborsAlt.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="neighbour"></a>`0x0` | neighbour | `uint8[16]` | I | four dwords: the button ids (110..116) reached by the four directions |
| <a id="direction_flags"></a>`0x10` | direction_flags | `uint32` | I | four bytes, one flag per direction |
| <a id="reserved"></a>`0x14` | reserved | `uint32` | I | zero |

## Referenced by

- Described by tables: [UiLauncherFocusNeighborsAlt](../tables/UiLauncherFocusNeighborsAlt.md)

## Open questions

None recorded.
