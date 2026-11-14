# GameDataPack_Open

- **Address:** `0x1402F3A3C`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int GameDataPack_Open(int fileNumber)`
- **Callers:** GameData_ReadSectors
- **Callees:** MemFile_Read, sub_140010F50, sub_14002620C, sub_140026288, sub_1403D2004, sub_1403D21C8, sub_1403D21F0, sub_14041FB00

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens system/ffto/fftpack.bin once and loads its two tables of 4-byte entries (offsets and sizes) that GameData_ReadSectors indexes by file number.

## Behavior

- V: builds the path from the game directory plus the text system/ffto/fftpack.bin, opens it as the memory file qword_143793118 and reads a 16-byte header; the first dword (dword_143793168) is the file count.
- V: returns 1 (failure, the object is freed) when the open fails or the requested file number is at or above the count; otherwise it allocates and fills two arrays of count dwords: qword_143793178 (offsets, read at +16) and qword_143793180 (read at +16 + 4 * count), and returns 0.
- V (data, English pack): the header is the count (3931 in this pack), three more dwords, then the offset array, then the size array; effect files sit at indices 900 to 1300.

## State touched

- Calls: [MemFile_Read](MemFile_Read.md), [sub_14002620C](sub_14002620C.md)

## Notes

Name is ours. GameData_ReadSectors adds sector * 2048 to the offset of the file number when it reads.

## Open questions

? the three header dwords after the count.
