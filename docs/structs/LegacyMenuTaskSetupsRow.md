# LegacyMenuTaskSetupsRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the LegacyMenuTaskSetups table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="handlers"></a>`0x0` | handlers | `bytes[24]` | I | three (function pointer, flag) pairs |
| <a id="pane_ids"></a>`0x18` | pane_ids | `uint32[3]` | V | task ids 9, 10, 11 |
| <a id="owner_ids"></a>`0x24` | owner_ids | `uint32[3]` | V | owner ids 0x20, 0x21, 0x22 or -1 |

## Referenced by

- Described by tables: [LegacyMenuTaskSetups](../tables/LegacyMenuTaskSetups.md)

## Open questions

None recorded.
