# SceneUnit_SetFlag12C

- **Address:** `0x14026CA00`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneUnit_SetFlag12C(void *unit)`
- **Callers:** EventScript_Run, at 0x14023DF84 (opcode 0xA9, with the unit from `SceneObject_FindBySlot`). Also SceneUnit_RunPlacement (at 0x140269227), SceneUnit_BuildFromQueueEntry (at 0x14026EFC8), sub_1402735F0 (at 0x140273693), and data references at 0x143D39058 and 0x143D39064.
- **Callees:** `sub_1403D325C`, `sub_1403D3AE8`, `sub_1403D2FD8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The body of opcode 0xA9: clears bit 0x40 of the unit's byte +0x12C (300) and sets it again to bit 0 of byte +8 of the table 305 row selected by the unit's byte +345, when that row exists.

## Behavior

- V: returns at once when the unit pointer is null.
- V: clears bit 0x40 of the unit's byte at +300 (0x12C) in every case where the unit exists.
- V: the table 305 handle is kept in qword_143CDA860. When it is null it is looked up once with sub_1403D325C(qword_143CD9CD0, 305). When neither can be obtained, the bit stays clear.
- V: row = sub_1403D3AE8(table 305, the unit's byte +345). The routine goes on only when the row is present and either its first qword is negative (then unk_1406F5ED0 is used as its data) or its data pointer is not null.
- V: bit 0 of the byte at data +8 becomes bit 6 of the unit's byte +300; the other bits of that byte are kept.
- V: when no row is found the bit stays clear. Returns nothing.

## Referenced by

- Called by: [SceneUnit_BuildFromQueueEntry](SceneUnit_BuildFromQueueEntry.md), [SceneUnit_RunPlacement](SceneUnit_RunPlacement.md)
- Reads tables: [NxdDataCharaPartsDrawParam](../tables/NxdDataCharaPartsDrawParam.md)

## Notes

The byte at +345 is written by opcode 0xA9 before this call. The bit is the same byte that the flag at +0x12C holds in the unit record.

## Open questions

What the table 305 rows hold and what the bit 0x40 of the unit byte at +300 controls in the game.
