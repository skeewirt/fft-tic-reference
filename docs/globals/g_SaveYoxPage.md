# g_SaveYoxPage

- **Kind:** global
- **Address:** `0x142FF9F90`
- **Area:** [Save data](../areas/save-data.md)
- **Type:** `uint8[1048576]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 1 MB 16-bit image page carried after a battle snapshot. It is compressed into the payload on write and inflated back here on load.

## Behavior

- V: the page is written with a 0x800-byte row stride and inflated on load.

## Referenced by

- Read by: [sub_140217EF8](../functions/sub_140217EF8.md), [sub_14025FC38](../functions/sub_14025FC38.md)
- Written by: [sub_1402181EC](../functions/sub_1402181EC.md), [sub_14025FC38](../functions/sub_14025FC38.md)

## Open questions

None recorded.
