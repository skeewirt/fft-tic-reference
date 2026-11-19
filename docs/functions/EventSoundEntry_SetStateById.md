# EventSoundEntry_SetStateById

- **Address:** `0x1401D7CF0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventSoundEntry_SetStateById(int64_t obj, int32_t id)`
- **Callers:** EventScript_Run, at 0x14023DFEF (opcode 0xA7, with the id read from operand bytes 1 to 4). Also sub_1400F4C54 (at 0x1400F4CC2), sub_1401BDB90 (at 0x1401BDBF2), sub_1401BF8C4 (at 0x1401BF8E7), sub_1401C01E4 (at 0x1401C0270), sub_1401C87A4 (at 0x1401C87D7), sub_1401D7F4C (at 0x1401D804D), sub_1401D9784 (at 0x1401D97B5), and data references at 0x143D35BCC.
- **Callees:** `sub_14009B550` (only for matches that hold a handle while the manager exists)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The body of opcode 0xA7: for every entry in the sound object's entry list whose id equals the operand, stops its resource if one is held, and sets the entry's state byte to 4.

## Behavior

- V: walks the circular list whose sentinel is at obj + 280, from the sentinel's next node until it returns to the sentinel, following the qword at each node +0.
- V: the resource of each node is the qword at node +16. It is a match when the dword at resource +32 equals the id; the comparison is a 32-bit compare.
- V: for a match whose resource qword +16 is non-null, when the sound manager qword_143CD9B60 is also non-null, it calls `sub_14009B550(manager, resource + 16)` first and reloads the manager global afterwards.
- V: for every match it sets the byte at resource +36 to 4.
- V: there is no early exit; every entry is visited. Nothing changes when no entry matches.
- V: the return value is whatever the last call left in rax; the caller does not use it.
- I: state 4 is later acted on by `sub_1401D5FA4`, which releases the entry through `sub_1401D5F34` when byte +37 is non-zero (not traced here).

## Referenced by

- Called by: [CreditRoll_StartMusic](CreditRoll_StartMusic.md), [sub_1400F4C54](sub_1400F4C54.md)

## Notes

Opcode 0xA7 and this routine match the record for 0xA7: the state byte is set to 4 for every matching entry.

## Open questions

What `sub_14009B550` returns and does to the handle. Where byte +36 value 4 leads in `sub_1401D5FA4` for entries whose byte +37 is zero.
