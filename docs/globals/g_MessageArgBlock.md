# g_MessageArgBlock

- **Kind:** global
- **Address:** `0x140783210`
- **Area:** [Data access](../areas/data.md)
- **Type:** `uint32[16]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The current-message argument vector: 0x40 bytes, sixteen dwords. Slots +0, +4 and +8 are separate arguments (a tagged text id, a bare item id and an ability argument in the battle path).

## Behavior

- V: 36 dword stores, four 16-byte copies, no word or byte access.

## Referenced by

- Read by: [sub_140220EA0](../functions/sub_140220EA0.md), [sub_140243A60](../functions/sub_140243A60.md)
- Written by: [sub_140233588](../functions/sub_140233588.md), [sub_140243A60](../functions/sub_140243A60.md)

## Open questions

None recorded.
