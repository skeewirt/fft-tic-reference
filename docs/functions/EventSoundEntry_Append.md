# EventSoundEntry_Append

- **Address:** `0x1401D7AF8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventSoundEntry_Append(int64_t obj, uint32_t id)`
- **Callers:** EventScript_Run, at 0x14023E014 (opcode 0xA6, with the id read from operand bytes 1 to 4). Also sub_1401D964C (at 0x1401D975F, the cache branch of EventMusic_LoadTrack), sub_1400F4BCC (at 0x1400F4C3E), sub_1401BF8C4 (at 0x1401BF8F5), sub_1401C811C (at 0x1401C822C), and one data reference at 0x143D35BC0.
- **Callees:** `sub_1403D325C`, `sub_1403D3AE8`, `sub_1403D2FD8`, `sub_140011750`, `sub_1401D5EB0` (which calls `sub_140037CA4`, `sub_140091124` and `sub_1401D5FA4`)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The body of opcode 0xA6: looks the id up in data table 280 and then, through a value in that row, in data table 279; when both rows are valid it creates a 56-byte sound resource that carries the id and appends it to the entry list of the sound object.

## Behavior

- V: the table 280 handle is kept in qword_143CDA578. When that is null it is looked up once with sub_1403D325C(qword_143CD9CD0, 280). When neither can be obtained the routine does nothing.
- V: row280 = sub_1403D3AE8(table 280, id). The routine goes on only when row280 is present and either its first qword is negative (then the static block unk_1406F5ED0 is used as its data) or its data pointer, from `sub_1403D2FD8`, is not null.
- V: key279 = the dword at the data pointer of row280 plus 8. The table 279 handle is kept in qword_143CDA580 and is looked up the same way with id 279. row279 = sub_1403D3AE8(table 279, key279), with the same validity test.
- V: the path pointer is the data pointer of row279 plus the dword at that data pointer plus 8. The second start value is the dword at the data pointer of row280 plus 12.
- V: allocates 56 bytes with `sub_140011750` (heap at qword_140C696D0 + 32, alignment 8) and sets: the qword at +8 to 0, the qword at +16 to 0, the dword at +24 to 0, the dword at +28 to 0, the vtable to GameSoundResource_140713440, the dword at +32 to the id, the dwords at +44 and +48 to -1.0, and the word at +37 to 1.
- V: calls `sub_1401D5EB0(resource, path pointer, 0, second start value)`. That helper sets the dword at +24 to 0 and the dword at +28 to the second start value, sets the byte at +36 to 0, and sets the handle at +8 through `sub_140091124` on the service qword_143CD9B88.
- V: if the entry list's count is at its maximum it raises the length error 'list too long'. Otherwise it allocates a 24-byte node through the vtable of the allocator at obj + 272, sets node +16 to the resource, increments the count at obj + 288, and links the node at the tail of the list whose sentinel is obj + 280.
- V: when either row is missing, nothing is allocated and the list is not changed.
- V: the return value is whatever the last call left in rax; the caller does not use it.
- I: the resource is the sound entry that later moves through states 0 to 4 in `sub_1401D5FA4` (not traced beyond its first branches).

## Referenced by

- Called by: [BgmMode_PlaySelected](BgmMode_PlaySelected.md), [CreditRoll_StartMusic](CreditRoll_StartMusic.md), [sub_1400F4BCC](sub_1400F4BCC.md)
- Reads tables: [NxdDataSoundEnhanced](../tables/NxdDataSoundEnhanced.md), [NxdDataSoundEnhancedResource](../tables/NxdDataSoundEnhancedResource.md)

## Notes

The list appended to here is the same list that `EventSoundEntry_SetStateById` (opcode 0xA7) scans and that EventMusic_LoadTrack also appends to.

## Open questions

What `sub_140091124` and `sub_1401D5FA4` do in full. What the row fields mean: the key at table 280 +8, the second start value at +12, and the path offset at table 279 +8. What the static block unk_1406F5ED0 holds.
