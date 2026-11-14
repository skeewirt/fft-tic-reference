# g_SaveAutoSlot

- **Kind:** global
- **Address:** `0x142E75DF8`
- **Area:** [Save data](../areas/save-data.md)
- **Type:** `uint8[40164]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The auto-slot record, one 0x9CE4-byte slot. The resume header import copies its summary fields into it, and the classic list exposes it as list slot 0.

## Behavior

- V: the classic slot mapping moves 0x9CE4 bytes between this record and the cache.

## Referenced by

- Read by: [sub_14021A030](../functions/sub_14021A030.md), [sub_140245B7C](../functions/sub_140245B7C.md)
- Written by: [sub_14021849C](../functions/sub_14021849C.md), [sub_14021A030](../functions/sub_14021A030.md), [sub_140245B7C](../functions/sub_140245B7C.md)

## Open questions

None recorded.
