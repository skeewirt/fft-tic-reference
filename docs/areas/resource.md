# Resource

Pack entry lookup, file reading and inflation.

Functions: 27, Structures: 1.

## Functions (27)

| Name | Address | Purpose |
|---|---|---|
| [GameDataPack_Open](../functions/GameDataPack_Open.md) | `0x1402F3A3C` | Opens system/ffto/fftpack.bin once and loads its two tables of 4-byte entries (offsets and sizes) that GameData_ReadSectors indexes by file number. |
| [Mem_Alloc](../functions/Mem_Alloc.md) | `0x140011750` | The engine's allocation entry: asks the heap object for `size` bytes with at least 8-byte alignment. |
| [Mem_Free](../functions/Mem_Free.md) | `0x140011804` | The engine's free entry: finds the heap that owns a pointer (or uses the one given) and returns the block to it. |
| [MemFile_Read](../functions/MemFile_Read.md) | `0x1403D2358` | Copies len bytes at offset from an in-memory file buffer (clamped to its size); returns 0 on success, 1 when the file has no buffer. |
| [Pack_MountList](../functions/Pack_MountList.md) | `0x140092928` | Mounts the game's twelve stock data packs, by leaf name, through the one-pack mount call. |
| [Pack_MountOne](../functions/Pack_MountOne.md) | `0x140092A04` | Finds or creates the registry entry for one pack leaf name and opens the pack behind it. |
| [PackEntry_Inflate](../functions/PackEntry_Inflate.md) | `0x1403D1ED8` | Reads one pack entry: a 16-byte header, then either stored bytes or a zlib stream. |
| [PackFile_EntryPtr](../functions/PackFile_EntryPtr.md) | `0x1403D2668` | Returns the in-memory address of a loaded pack entry: from one of the 8 cached entry slots when index is cached, else base + (offset[index] - offset[first loaded]). |
| [PackFile_ReadEntry](../functions/PackFile_ReadEntry.md) | `0x1403D25D8` | Copies (and, when needed, inflates) one entry of an index-addressed pack into a caller buffer. |
| [Resource_AcquireHandle](../functions/Resource_AcquireHandle.md) | `0x1400912B4` | Finds or creates the registry entry of one resource name (a pack or a file) under its bucket's lock and, when asked, loads it before returning. |
| [Resource_FindOrOpen](../functions/Resource_FindOrOpen.md) | `0x140091124` | Opens a game resource by path through the mounted packs, after normalising the path, and returns a handle or null. |
| [Resource_GetSlotObject](../functions/Resource_GetSlotObject.md) | `0x1402BACCC` | Returns the shared twenty-byte wrapper object for a resource slot, creating and constructing it on first use. |
| [ResourceHandle_FinishLoad](../functions/ResourceHandle_FinishLoad.md) | `0x1400965C4` | Ends a load: releases the reader, sets the final state, tags a localised file, and frees the resolved path string. |
| [ResourceHandle_FreeData](../functions/ResourceHandle_FreeData.md) | `0x140095EB0` | Frees a handle's file buffer (+56) with Mem_Free unless flag 0x100 (+92) says the buffer is not the handle's. |
| [ResourceHandle_Init](../functions/ResourceHandle_Init.md) | `0x140095DA0` | Constructs the common part of a resource handle: reference count 1, empty path, reader, buffer and status fields. |
| [ResourceHandle_LoadNow](../functions/ResourceHandle_LoadNow.md) | `0x14009627C` | Drives one handle's load to the end: steps the read until state 3, calls the loaded callback (slot 8), records the status, calls the ready callback (slot 13) and finishes. |
| [ResourceHandle_ReadData](../functions/ResourceHandle_ReadData.md) | `0x1400961D4` | Reads the handle's file into its buffer (+56) through its reader object (+48), allocating from the heap the handle's slot 14 returns. |
| [ResourceHandle_ResolvedPath](../functions/ResourceHandle_ResolvedPath.md) | `0x1400962FC` | The path the reader resolved (+40, a string object whose text is at +8, heap pointer when its capacity +32 is 16 or more), else the requested path (+24), else an empty string. |
| [Sound_PlayNovelSe](../functions/Sound_PlayNovelSe.md) | `0x1402BA7C4` | Plays one of the common novel sound effects by id: it finds a free channel, loads the sound from the shared novel sound bank and starts it. |
| [sub_14006BAA8](../functions/sub_14006BAA8.md) | `0x14006BAA8` | Reads a file through the engine's virtual file system: it resolves the path, opens the stream, copies the bytes into the caller's buffer and closes it. |
| [sub_14006C6F4](../functions/sub_14006C6F4.md) | `0x14006C6F4` | A typed read wrapper over the virtual file system: opens a named file, optionally seeks to an offset, reads a fixed block and closes it. |
| [sub_140073918](../functions/sub_140073918.md) | `0x140073918` | Creates a directory: the engine's mkdir, used for the save folder, the pack cache and the log folder. |
| [sub_140093108](../functions/sub_140093108.md) | `0x140093108` | Looks a file name up in the mounted-pack registry's hash tree, inserting a new node when the name is not there yet. |
| [sub_1400FE810](../functions/sub_1400FE810.md) | `0x1400FE810` | Appends one 16-byte element to a segmented container whose control block sits at a fixed global plus 0xF8. |
| [sub_1403D2450](../functions/sub_1403D2450.md) | `0x1403D2450` | Loads the byte range of chunks [first, last) of a chunked file into one of 8 cached buffers (or a single scratch buffer) and returns 0 on success. |
| [sub_1403D25A4](../functions/sub_1403D25A4.md) | `0x1403D25A4` | Frees the scratch buffer of a chunked-file reader and resets its cached chunk index to -1. |
| [sub_140405DF4](../functions/sub_140405DF4.md) | `0x140405DF4` | Appends one 16-byte element to a segmented container whose control block sits at a fixed global plus 0x2D8. |

## Structures (1)

| Name | Size (bytes) | Summary |
|---|---|---|
| [NexResourceHandle](../structs/NexResourceHandle.md) | 168 | The resource handle an nxd file is loaded through (NxdTable_CreateHandle; root.nxl uses the same layout with the NxlResourceHandle vtable): the common resource handle plus two callback pairs. |
