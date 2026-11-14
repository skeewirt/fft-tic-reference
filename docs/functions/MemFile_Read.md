# MemFile_Read

- **Address:** `0x1403D2358`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `__int64 MemFile_Read(MemFile *f, void *dst, unsigned int offset, unsigned int len)`
- **Callers:** EventScript_LoadFile, GameData_ReadSectors, EventSprite_LoadTask, EventMapTitle_LoadTexture, sub_1403D2450 and about 20 more
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies len bytes at offset from an in-memory file buffer (clamped to its size); returns 0 on success, 1 when the file has no buffer.

## Behavior

- V: obj = *(qword *)(f + 24); 0 returns 1. buf = *(obj + 56), size = *(obj + 64). When offset + len > size then len = size - offset. memmove(dst, buf + offset, len); returns 0.
- V: no check that offset <= size (a larger offset makes len wrap; I: callers are trusted).

## Referenced by

- Called by: [GameDataPack_Open](GameDataPack_Open.md), [Resource_GetSlotObject](Resource_GetSlotObject.md), [sub_1403D2450](sub_1403D2450.md)

## Notes

The name is ours (IDB: sub_1403D2358). Medium confidence on the 'file' reading; the +24 object may be a streaming buffer object.

## Open questions

? the class of the +24 object.
