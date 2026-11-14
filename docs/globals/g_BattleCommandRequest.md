# g_BattleCommandRequest

- **Kind:** global
- **Address:** `0x142FD35A0`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[20]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The twenty-byte battle command request: the command byte at +1, the chosen 16-bit value at +2 and +8 (kept equal), and the ability word at +6.

## Behavior

- V: the confirm writers and the reader at +1 are known; the ability word is read at +6.

## Referenced by

- Read by: [sub_14020A7F0](../functions/sub_14020A7F0.md), [sub_14020C704](../functions/sub_14020C704.md)
- Written by: [sub_14020327C](../functions/sub_14020327C.md), [sub_140203450](../functions/sub_140203450.md), [sub_140237FA4](../functions/sub_140237FA4.md)

## Open questions

None recorded.
