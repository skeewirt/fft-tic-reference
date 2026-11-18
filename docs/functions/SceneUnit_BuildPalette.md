# SceneUnit_BuildPalette

- **Address:** `0x14026C858`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneUnit_BuildPalette(void *unit)`
- **Callers:** EventScript_Run, at 0x14023DFC7 (opcode 0xA8, with the unit from `SceneObject_FindBySlot`). Also SceneUnit_RunPlacement (at 0x14026921F), SceneUnit_BuildFromQueueEntry (at 0x14026EFC0), sub_1402735F0 (at 0x140273677), and one data reference at 0x143D39058.
- **Callees:** `sub_1403D325C`, `sub_1403D3AE8`, `sub_1403D2FD8`, `sub_1402F7594` (level 2: `sub_1402F74D8` splits each 15-bit word into five-bit fields and a flag bit in a 7-byte-stride table)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The body of opcode 0xA8: when the unit exists, builds 16 packed 15-bit words from the table 302 row selected by the unit's byte +343 and passes them to `sub_1402F7594` with the index 3.

## Behavior

- V: returns at once when the unit pointer is null.
- V: the key is the unit's byte at +343. Opcode 0xA8 writes that byte before calling this routine (see the record for 0xA8).
- V: the table 302 handle is kept in qword_143CDA868. When it is null it is looked up once with sub_1403D325C(qword_143CD9CD0, 302). When neither can be obtained, nothing is written.
- V: row = sub_1403D3AE8(table 302, key). The routine goes on only when the row is present and either its first qword is negative (then the static block unk_1406F5ED0 is used as its data) or its data pointer is not null.
- V: for 16 steps, i = 2, 5, 8, ... 47: it reads three bytes at the data pointer plus the dword at data +8 plus i - 2, plus i - 1 and plus i. The first byte becomes bits 0 to 4 of the word (from its bits 3 to 7), the second becomes bits 5 to 9 (from its bits 3 to 7) and the third becomes bits 10 to 14 (from its bits 3 to 7).
- V: bit 15 of the first word is clear; bit 15 is set on every later word of the 16.
- V: the 16 words are stored in a 32-byte stack buffer, and then `sub_1402F7594(buffer, 3, 15)` is called. The fourth argument of that call is not set in the visible code.
- V: returns nothing. When the row is missing nothing is written.

## State touched

- Calls: [sub_1402F7594](sub_1402F7594.md), [sub_1402F74D8](sub_1402F74D8.md)

## Referenced by

- Called by: [SceneUnit_BuildFromQueueEntry](SceneUnit_BuildFromQueueEntry.md), [SceneUnit_RunPlacement](SceneUnit_RunPlacement.md)
- Called by event opcodes: [0xA8](../opcodes/README.md)
- Reads tables: [NxdDataCharaZodiacStoneCLUT](../tables/NxdDataCharaZodiacStoneCLUT.md)

## Notes

The record for 0xA8 calls the effect a packed value; the code builds 16 words into a 32-byte buffer.

## Open questions

What the table 302 rows hold beyond the three bytes per step. What the block with index 3 is, what the fourth argument of `sub_1402F7594` is, and what bit 15 means. Why the calls to `sub_1402F7594` take index 3 and 15.
