# g_BattleMsgQueueCount

- **Kind:** global
- **Address:** `0x142FCF864`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `int`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The number of entries in the deferred battle message queue, at most sixteen.

## Behavior

- V: the producer stops at 0x10 and the consumer decrements it.

## Referenced by

- Read by: [sub_14020558C](../functions/sub_14020558C.md)
- Written by: [sub_14020558C](../functions/sub_14020558C.md), [sub_1402055FC](../functions/sub_1402055FC.md)

## Open questions

None recorded.
