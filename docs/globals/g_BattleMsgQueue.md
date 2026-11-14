# g_BattleMsgQueue

- **Kind:** global
- **Address:** `0x142FCF870`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[256]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The deferred battle message queue: sixteen entries of sixteen bytes (id byte, unit byte, qword value). It is filled by the battle action code and drained one entry at a time.

## Behavior

- V: entry stride 0x10 and count at 0x142FCF864.

## Referenced by

- Read by: [sub_14020558C](../functions/sub_14020558C.md), [sub_140210AF0](../functions/sub_140210AF0.md)
- Written by: [sub_1402055FC](../functions/sub_1402055FC.md)

## Open questions

None recorded.
