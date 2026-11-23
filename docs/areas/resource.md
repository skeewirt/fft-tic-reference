# Resource

Pack entry lookup, file reading and inflation.

Functions: 37, Structures: 7, Observed behaviours: 1, Tables: 15.

## Functions (37)

| Name | Address | Purpose |
|---|---|---|
| [AudioBus_FindByName](../functions/AudioBus_FindByName.md) | `0x14044DFD4` | Returns the mixer bus number for a bus name, or 0xFFFF when there is none. |
| [AudioBus_FindMasterOut](../functions/AudioBus_FindMasterOut.md) | `0x14044E07C` | Returns the bus number of the master output. |
| [AudioDsp_InitCoefficientSets](../functions/AudioDsp_InitCoefficientSets.md) | `0x1404A203C` | Initialises the work area of an audio DSP unit and fills its per-channel coefficient pointer slots. |
| [Callback_InvokeWithHandle](../functions/Callback_InvokeWithHandle.md) | `0x1400674E8` | The invoker every nxd resource handle gets: calls the callback with the context and the handle. |
| [GameDataPack_Open](../functions/GameDataPack_Open.md) | `0x1402F3A3C` | Opens system/ffto/fftpack.bin once and loads its two tables of 4-byte entries (offsets and sizes) that GameData_ReadSectors indexes by file number. |
| [MapResource_Read](../functions/MapResource_Read.md) | `0x140251640` | Reads one resource file of the current battle map, using the per-map file list when the request carries the marker id. |
| [Mem_Alloc](../functions/Mem_Alloc.md) | `0x140011750` | The engine's allocation entry: asks the heap object for `size` bytes with at least 8-byte alignment. |
| [Mem_Free](../functions/Mem_Free.md) | `0x140011804` | The engine's free entry: finds the heap that owns a pointer (or uses the one given) and returns the block to it. |
| [MemFile_Read](../functions/MemFile_Read.md) | `0x1403D2358` | Copies len bytes at offset from an in-memory file buffer (clamped to its size); returns 0 on success, 1 when the file has no buffer. |
| [Pack_MountList](../functions/Pack_MountList.md) | `0x140092928` | Mounts the game's twelve stock data packs, by leaf name, through the one-pack mount call. |
| [Pack_MountOne](../functions/Pack_MountOne.md) | `0x140092A04` | Finds or creates the registry entry for one pack leaf name and opens the pack behind it. |
| [PackedBlock766_Load](../functions/PackedBlock766_Load.md) | `0x1403436C0` | Starts loading one block of packed data file 766 into the shared block buffer. |
| [PackedBlock767_Load](../functions/PackedBlock767_Load.md) | `0x14034370C` | Starts loading one block of packed data file 767 into its block buffer. |
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
| [ResourceManager_ReloadLocalized](../functions/ResourceManager_ReloadLocalized.md) | `0x1400919A8` | Sets a text language and reloads every localized resource handle (flag 8). |
| [ResourcePool_AllocBlocks](../functions/ResourcePool_AllocBlocks.md) | `0x1402F3888` | Allocates a run of 2048-byte blocks from a fixed pool of 128 blocks and returns its address, or null. |
| [Sound_PlayNovelSe](../functions/Sound_PlayNovelSe.md) | `0x1402BA7C4` | Plays one of the common novel sound effects by id: it finds a free channel, loads the sound from the shared novel sound bank and starts it. |
| [sub_14006BAA8](../functions/sub_14006BAA8.md) | `0x14006BAA8` | Reads a file through the engine's virtual file system: it resolves the path, opens the stream, copies the bytes into the caller's buffer and closes it. |
| [sub_14006C6F4](../functions/sub_14006C6F4.md) | `0x14006C6F4` | A typed read wrapper over the virtual file system: opens a named file, optionally seeks to an offset, reads a fixed block and closes it. |
| [sub_140073918](../functions/sub_140073918.md) | `0x140073918` | Creates a directory: the engine's mkdir, used for the save folder, the pack cache and the log folder. |
| [sub_140093108](../functions/sub_140093108.md) | `0x140093108` | Looks a file name up in the mounted-pack registry's hash tree, inserting a new node when the name is not there yet. |
| [sub_1400FE810](../functions/sub_1400FE810.md) | `0x1400FE810` | Appends one 16-byte element to a segmented container whose control block sits at a fixed global plus 0xF8. |
| [sub_1403D2450](../functions/sub_1403D2450.md) | `0x1403D2450` | Loads the byte range of chunks [first, last) of a chunked file into one of 8 cached buffers (or a single scratch buffer) and returns 0 on success. |
| [sub_1403D25A4](../functions/sub_1403D25A4.md) | `0x1403D25A4` | Frees the scratch buffer of a chunked-file reader and resets its cached chunk index to -1. |
| [sub_140405DF4](../functions/sub_140405DF4.md) | `0x140405DF4` | Appends one 16-byte element to a segmented container whose control block sits at a fixed global plus 0x2D8. |
| [TimImage_Parse](../functions/TimImage_Parse.md) | `0x140340AE0` | Reads the header of a legacy-container image (pixel mode, optional palette block, pixel block) into a small descriptor. |

## Structures (7)

| Name | Size (bytes) | Summary |
|---|---|---|
| [BlockSectorStart](../structs/BlockSectorStart.md) | 4 | One row of the sector start tables of the packed UI and event blocks. |
| [DataBlockPointerRow](../structs/DataBlockPointerRow.md) | 8 | One row of AudioDspCoefficientBlockPointers. |
| [MapResourceFileListPointer](../structs/MapResourceFileListPointer.md) | 8 | One row of the MapResourceFilesLanguage0 table. |
| [NexResourceHandle](../structs/NexResourceHandle.md) | 168 | The resource handle an nxd file is loaded through (NxdTable_CreateHandle; root.nxl uses the same layout with the NxlResourceHandle vtable): the common resource handle plus two callback pairs. |
| [SectorOnly](../structs/SectorOnly.md) | 4 | One row of the MapBlockSectorsLanguage0 table and the tables that share its shape. |
| [TextPackPathsRow](../structs/TextPackPathsRow.md) | 8 | One row of the TextPackPaths table. |
| [TextPointerRow](../structs/TextPointerRow.md) | 8 | One row of a table of text pointers (audio loader errors, mixer names, XML status names, value type names). |

## Observed behaviours (1)

| Name | Scope | Summary |
|---|---|---|
| [NxdTableRebinding](../behaviors/NxdTableRebinding.md) | loaded nxd tables and the localized reload | An nxd table can take a new file while the game runs: its load callback NxdTable_BindRows may run again on a bound table, and the game's own language switch reloads every localized handle through it. |

## Tables (15)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [AudioBusAndEffectNames](../tables/AudioBusAndEffectNames.md) | Executable |  | 36 text pointers then 5 function pointers | Names of the audio mixer: eight bus names, the master output name, a second bus list, one shared string, nineteen effect names (reverb, echo, biquad, band pass, compressor, delay, pitch shifter, equalisers, chorus, fl... |
| [AudioCueLoadErrorNames](../tables/AudioCueLoadErrorNames.md) | Executable |  | 7 rows of 8 bytes | Names of the error codes of the audio cue sheet loader: no error, failed to register file, failed to open, failed to load wave bank, invalid wave bank path, failed to calculate work size, failed to allocate memory. |
| [AudioDspCoefficientBlockPointers](../tables/AudioDspCoefficientBlockPointers.md) | Executable |  | 80 rows of 8 bytes (82 in the sweep run) | Pointer lists to the 1024-byte float coefficient blocks of the audio library DSP; 32 distinct blocks, the pointer pattern is a, b, b, a repeated per channel pair. |
| [AudioTableValueTypeNames](../tables/AudioTableValueTypeNames.md) | Executable |  | 13 rows of 8 bytes | Names of the value types of the audio library data tables: signed and unsigned 8 / 16 / 32 / 64 bit integers, 32 and 64 bit floats, string, variable length data and chunk data. |
| [AudioTableValueTypeNamesAlt](../tables/AudioTableValueTypeNamesAlt.md) | Executable |  | 13 rows of 8 bytes | The same value types as AudioTableValueTypeNames in the audio library own spelling; slot 12 is a GUID. Verdict: text. |
| [EmbeddedTimImageA](../tables/EmbeddedTimImageA.md) | Executable (initialised data) |  | 1 block of 2368 bytes | A 4-bit image with its 16-colour palette in the legacy container format (magic 0x10, flags, palette block, image block), read by the world map code. |
| [MapBlockSectorsLanguage0](../tables/MapBlockSectorsLanguage0.md) | Executable (initialised data) |  | 128 rows of 4 bytes | Per battle map, where its 4096-byte map block is, for text language 0. |
| [MapBlockSectorsOtherLanguages](../tables/MapBlockSectorsOtherLanguages.md) | Executable (initialised data) |  | 128 rows of 4 bytes | Per battle map, where its 4096-byte map block is, for the other text languages. |
| [MapResourceFilesDefault](../tables/MapResourceFilesDefault.md) | Executable |  | 128 rows of 8 bytes | Per battle map, where its resource files are, for text languages other than 0 (the copy of MapResourceFilesLanguage0 that the reader picks when the language record is not 0). |
| [MapResourceFilesLanguage0](../tables/MapResourceFilesLanguage0.md) | Executable |  | 128 rows of 8 bytes | Per battle map, where its resource files are, for text language 0. |
| [RecordBlockSectors](../tables/RecordBlockSectors.md) | Executable |  | 93 rows of 4 bytes | Sector start of each block of a packed data file that event commands load. |
| [RecordBlockSectors767](../tables/RecordBlockSectors767.md) | Executable (initialised data) |  | 115 rows of 4 bytes | Sector starts of 114 blocks of 16 sectors (32 KiB) of a second packed file; block 112 is empty. |
| [SoundPackPathPatterns](../tables/SoundPackPathPatterns.md) | Executable |  | 7 rows of 8 bytes | Seven sound pack path patterns: the common UI sound pack, the novel pack, the common sound pack, the per movie sound effect, voice and music packs (movie number %04d) and the per music pack (music number %05u). |
| [TextPackPaths](../tables/TextPackPaths.md) | Executable |  | 45 rows of 8 bytes | Pointers to the file paths of 45 text resources (event help, spell, sample, world, opening, join text, the system text sets, battle and menu tutorials, scenario pages). |
| [XmlStatusNames](../tables/XmlStatusNames.md) | Executable |  | 27 rows of 8 bytes | Names of the XML parser status codes (success, no attribute, wrong attribute type, file not found, could not be opened, read error, parsing errors per node kind, empty document, mismatched element, cannot convert text... |
