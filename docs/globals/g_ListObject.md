# g_ListObject

- **Kind:** global
- **Address:** `0x1418716A0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Type:** `uint8[1024]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The static list object: u16 cell words at +0 (stride 2), a property word array at +0xA4, the bare-id array at +0x148 and five byte arrays after it. Rebuilt in place, never allocated.

## Behavior

- V: the cell value is 0x3800|id, 0x7000|id or 8; no 32-bit per-cell field exists.

## Referenced by

- Read by: [sub_140237CD0](../functions/sub_140237CD0.md), [sub_140237FA4](../functions/sub_140237FA4.md)

## Open questions

None recorded.
