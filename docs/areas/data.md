# Data access

NXD table accessors, the table registry and other game-data lookups.

Functions: 54, Structures: 1, Globals: 2, Registries: 1, File formats: 5, Flows: 3, Observed behaviours: 4, Tables: 1.

## Functions (54)

| Name | Address | Purpose |
|---|---|---|
| [BattleMsg_BuildArgs](../functions/BattleMsg_BuildArgs.md) | `0x1400F79D0` | Fills the format-argument vector for a message descriptor: selects the message id, then pushes the values that replace the template's <string=lstrN> and <num=...> placeholders. |
| [BattleMsg_FillArgs](../functions/BattleMsg_FillArgs.md) | `0x1401EC074` | Fills the format-argument vector for the banner: first asks the message-id-specific builder, and when that pushes nothing, copies the object's up to 40 stored argument entries. |
| [BattleMsg_IdFromDescriptor](../functions/BattleMsg_IdFromDescriptor.md) | `0x1400FCC04` | Turns a message descriptor into the row id used by NXD table 172 (C_Mes_Id_Sample-en). |
| [BattleMsg_TextFromDescriptor](../functions/BattleMsg_TextFromDescriptor.md) | `0x1400FCBB4` | Returns the template text for a message descriptor from one of two text sources. |
| [CMesId_GetText](../functions/CMesId_GetText.md) | `0x1400FCB2C` | Returns the text of one row of NXD table 172 (0xAC, the C_Mes_Id_Sample table) and caches the table pointer. |
| [FormatArgs_Push](../functions/FormatArgs_Push.md) | `0x1400FE4E4` | Appends one 264-byte format-argument record to a format-argument vector. |
| [ItemTable_GetRow](../functions/ItemTable_GetRow.md) | `0x1400F8674` | Returns the Item-en row (table 45, cache qword_143CDA2E8). |
| [NxdEntries_Search2](../functions/NxdEntries_Search2.md) | `0x1403D4304` | Binary search of bound 16-byte entries by (key1, key2), packed as key1 \| key2 << 32. |
| [NxdEntries_Search3](../functions/NxdEntries_Search3.md) | `0x1403D43C0` | Binary search of bound 16-byte entries by (key1, key2, key3), recursive on the half that can hold the keys. |
| [NxdEntry_CopyKeys](../functions/NxdEntry_CopyKeys.md) | `0x1403D2F90` | Copies the first n keys of the row an entry points to (the record's leading dwords); false when the entry's kind has fewer than n keys. |
| [NxdEntry_GetRow](../functions/NxdEntry_GetRow.md) | `0x1403D2FD8` | Returns the row data an entry points to: the entry's pointer plus the offset its kind names. |
| [NxdHandle_GetHeap](../functions/NxdHandle_GetHeap.md) | `0x1403D3014` | Slot 14 of the nxd handle vtables: the heap the handle's file buffer is allocated from. |
| [NxdHandle_OnLoaded](../functions/NxdHandle_OnLoaded.md) | `0x1403D3048` | Slot 8 of the NexResourceHandle and NxlResourceHandle vtables: when the file has been read, calls the handle's load callback with its context and the handle. |
| [NxdHandle_OnReady](../functions/NxdHandle_OnReady.md) | `0x1403D3090` | Slot 13 of the nxd handle vtables: calls the second callback pair (+128 invoker, +136 context, +144 function) after the load finished. |
| [NxdRegistry_CreateRootHandle](../functions/NxdRegistry_CreateRootHandle.md) | `0x1403D32DC` | The resource-handle factory for root.nxl: a 168-byte NxlResourceHandle (vtable 0x140721580) whose load callback is NxdRegistry_LoadRootNxl. |
| [NxdRegistry_Find](../functions/NxdRegistry_Find.md) | `0x1403D325C` | Returns the table object registered under a table id, or null when the id is unknown. |
| [NxdRegistry_LoadRootNxl](../functions/NxdRegistry_LoadRootNxl.md) | `0x1403D33F0` | Builds the table registry from the root.nxl list: one table object per listed table, keyed by table id, each pointing at its .nxd file. |
| [NxdSet3_FindChild](../functions/NxdSet3_FindChild.md) | `0x1403D3940` | Finds the child record of a key2 inside one triple-keyed set: binary search over the set's 20-byte children (offset +4 relative to the set record, count +8). |
| [NxdSet3_SearchChild](../functions/NxdSet3_SearchChild.md) | `0x1403D422C` | The halving loop of NxdSet3_FindChild over a set's children. |
| [NxdSets_Find2](../functions/NxdSets_Find2.md) | `0x1403D3878` | Finds the set of a key1 in a double-keyed file: binary search over the 12-byte set records the index header at file +32 points to. |
| [NxdSets_Find3](../functions/NxdSets_Find3.md) | `0x1403D38DC` | Finds the set of a key1 in a triple-keyed file: the same search over 20-byte set records. |
| [NxdSets_Search2](../functions/NxdSets_Search2.md) | `0x1403D419C` | The halving loop of NxdSets_Find2 over [lo, hi) of the 12-byte set records. |
| [NxdSets_Search3](../functions/NxdSets_Search3.md) | `0x1403D41E4` | The halving loop of NxdSets_Find3 over 20-byte set records. |
| [NxdTable_BinarySearchRow](../functions/NxdTable_BinarySearchRow.md) | `0x1403D4278` | Binary search over an array of 16-byte entries sorted by the first dword of the row each entry points to; returns the entry address or 0. |
| [NxdTable_BindRows](../functions/NxdTable_BindRows.md) | `0x1403D3F3C` | Binds a loaded nxd file to its table object: reads the header's layout, row count and the contiguous-keys flag, and builds the 16-byte entry array (kind, row pointer). |
| [NxdTable_CreateHandle](../functions/NxdTable_CreateHandle.md) | `0x1403D3E64` | The resource-handle factory NxdRegistry_LoadRootNxl passes for every nxd file: creates the 168-byte NexResourceHandle whose callbacks bind the loaded file to the table object. |
| [NxdTable_GetEntryByIndex](../functions/NxdTable_GetEntryByIndex.md) | `0x1403D3BE4` | Returns the entry at a row position; null when the position is not below the row count. |
| [NxdTable_GetEntryByKeyIndex](../functions/NxdTable_GetEntryByKeyIndex.md) | `0x1403D3C98` | The index-th row of the set key1 (double keyed), or the first leaf of the index-th child of the set (triple keyed), reached through the file's set index and then the bound entries. |
| [NxdTable_GetEntryByKeys2](../functions/NxdTable_GetEntryByKeys2.md) | `0x1403D3B5C` | The row entry of (key1, key2): for a double-keyed table the binary search over the bound entries; for a triple-keyed table the first leaf of child (key1, key2). |
| [NxdTable_GetEntryByKeys3](../functions/NxdTable_GetEntryByKeys3.md) | `0x1403D3BAC` | The row entry of (key1, key2, key3) in a triple-keyed table: the binary search over the bound entries. |
| [NxdTable_GetEntryByKeysIndex3](../functions/NxdTable_GetEntryByKeysIndex3.md) | `0x1403D3D58` | The index-th leaf of child (key1, key2) of a triple-keyed table, through the set index and then the bound entries. |
| [NxdTable_GetEntryCount](../functions/NxdTable_GetEntryCount.md) | `0x1403D3A34` | For a double / triple keyed table: the record count of the set key1 (double: its rows; triple: its children), or 0. |
| [NxdTable_GetLeafCount3](../functions/NxdTable_GetLeafCount3.md) | `0x1403D3A84` | The number of leaves (key3 rows) of child (key1, key2) of a triple-keyed table, or 0. |
| [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md) | `0x1403D3AE8` | The generic row lookup of a loaded Nxd table by id: used by JobTable_GetRow, AbilityTable_GetRow, ItemTable_GetRow, JobCommandTable_GetRow, Icon_FormatPath and over 250 other readers. |
| [NxdTable_GetSetEntries](../functions/NxdTable_GetSetEntries.md) | `0x1403D3DEC` | The rows of one set of a double-keyed table as a span of bound entries: (entry of the set's first record, record count). |
| [NxdTable_OnReady](../functions/NxdTable_OnReady.md) | `0x1403D417C` | Marks a table usable after its file loaded: state +12 = 2 when the load status (+80 of the handle) is 1, else 3. |
| [sub_1400FC85C](../functions/sub_1400FC85C.md) | `0x1400FC85C` | Identifies which text pack and which text kind a string-pool pointer belongs to. |
| [sub_140220E10](../functions/sub_140220E10.md) | `0x140220E10` | Builds a tagged 16-bit text id from a format byte and a bare id. |
| [sub_140220EA0](../functions/sub_140220EA0.md) | `0x140220EA0` | The message measuring pass: walks a message's byte string (with its argument codes and back-references) without drawing and reports the width of every line, the widest line and the number of lines. |
| [sub_140226208](../functions/sub_140226208.md) | `0x140226208` | Turns a 16-bit text id into a pointer to one string inside one of the game's 32 text pools. |
| [sub_14022627C](../functions/sub_14022627C.md) | `0x14022627C` | Counts the decimal digits of a value, for laying out a printed number. |
| [sub_14022720C](../functions/sub_14022720C.md) | `0x14022720C` | Builds one job/command help text id with the 0x7800 token. |
| [sub_140231C9C](../functions/sub_140231C9C.md) | `0x140231C9C` | Resolves one text id through the shared pool decoder and passes the result to the text helper. |
| [sub_140243330](../functions/sub_140243330.md) | `0x140243330` | Posts a text-id command with a target node to the UI dispatcher. |
| [sub_140243390](../functions/sub_140243390.md) | `0x140243390` | Sets a text node from either a text id or a string and records the current-message descriptor. |
| [sub_140243A60](../functions/sub_140243A60.md) | `0x140243A60` | The scene text formatter: it composes a text node from a format string and the shared argument vector. |
| [sub_1402D2578](../functions/sub_1402D2578.md) | `0x1402D2578` | Builds the 0x8800 text message for an errand or battle result record: it switches on the record kind, composes the text and posts it to the UI. |
| [sub_1402EC9D0](../functions/sub_1402EC9D0.md) | `0x1402EC9D0` | The menu-side text-id command thunk. |
| [sub_140332B48](../functions/sub_140332B48.md) | `0x140332B48` | Returns the string pool that belongs to a text kind; the kind selects a pool, which is prepared and then returned by pointer. |
| [TextKind25_LoadPool](../functions/TextKind25_LoadPool.md) | `0x140284098` | Loads the text pool that serves text kind 25 (base 0xC800): it sizes the buffer from the current pool count, allocates it, and reads one of five sectors into it. |
| [UITable_GetRowByKey](../functions/UITable_GetRowByKey.md) | `0x1403DBC74` | Returns the row of an NXD table by table id and row key, or null when the table or row is missing. |
| [UIText_Get](../functions/UIText_Get.md) | `0x1403DBE88` | Returns the UI text string for an id from UI table 19, or a shared empty string when the row is missing. |
| [UIText_ResolveCategoryRow](../functions/UIText_ResolveCategoryRow.md) | `0x1400F3BB0` | Resolves the category name and key of a <category=key> text tag to a table row and fills a 28-byte result record with three string pointers and four flag bytes. |
| [Utf8_DecodeUnit](../functions/Utf8_DecodeUnit.md) | `0x1403BF9D4` | Decodes one UTF-8 sequence to a 16-bit code unit and returns the number of bytes used. |

## Structures (1)

| Name | Size (bytes) | Summary |
|---|---|---|
| [NxdTable](../structs/NxdTable.md) | 80 | One table object of the nxd registry (NxdRegistry_LoadRootNxl allocates one per root.nxl line); NxdTable_BindRows fills its entries from the loaded file and every row lookup reads it. |

## Globals (2)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_MessageArgBlock](../globals/g_MessageArgBlock.md) | `0x140783210` | `uint32[16]` | The current-message argument vector: 0x40 bytes, sixteen dwords. |
| [g_TextPoolTable](../globals/g_TextPoolTable.md) | `0x140D40990` | `char *[32]` | The thirty-two text-pool pointers the generic decoder indexes by a text id's five kind bits. |

## Registries (1)

| Name | Summary |
|---|---|
| [TextIdKinds](../registries/TextIdKinds.md) | The 32 text-id kinds: the 5 bits of a text id, their base (kind x 0x800) and the pool or source each selects. |

## File formats (5)

| Name | Extension | Summary |
|---|---|---|
| [ItemHelpToken](../formats/ItemHelpToken.md) |  | The 0x6800-tagged text id that asks for an item's help string: kind 13, index = item id. |
| [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md) | `.nxd` | The index of a double or triple keyed nxd file (header byte 8 = 2 or 3): sets by key1, per set an array (double) or children by key2 with their leaves (triple), and one flat entry table of every row sorted by the key ... |
| [NxdSingleKeyHeader](../formats/NxdSingleKeyHeader.md) | `.nxd` | The header bytes of an nxd file that the game's loader (NxdTable_BindRows) reads for a single-key table, and the contiguous-keys flag that decides whether a key is read by position or searched. |
| [NxdSingleKeyRows](../formats/NxdSingleKeyRows.md) | `.nxd` | The row area of a single-key nxd file (header byte 8 = 1, byte 9 = 1 or 2): the entry table, the rows and the string pool, and how a row refers to its strings and arrays. |
| [TextId](../formats/TextId.md) |  | A 16-bit text id in two fields: the top 5 bits select one of 32 string pools, the low 11 bits index the strings inside that pool. |

## Flows (3)

| Name | Summary |
|---|---|
| [ItemNameToScreen](../flows/ItemNameToScreen.md) | How an item id becomes a name on screen, by two independent routes: the 0x3800 text id (a pool id decoded by sub_140226208, carried in a 2-byte list cell or a 32-bit message argument) and the Item-en row lookup (ItemT... |
| [NxdMultiKeyLookup](../flows/NxdMultiKeyLookup.md) | How a reader finds a row of a double or triple keyed table, and which parts of the file each path reads. |
| [NxdTableLoad](../flows/NxdTableLoad.md) | How one nxd table goes from a root.nxl line to rows a reader can look up. |

## Observed behaviours (4)

| Name | Scope | Summary |
|---|---|---|
| [CharShapeRowsANewLookNeeds](../behaviors/CharShapeRowsANewLookNeeds.md) | engine (sprite rows in the NXD data) | The CharShape rows (NXD table 174, keyed by look number) end at key 158 and twelve functions look a look up there. |
| [HdSheetAndClassicPaletteLoading](../behaviors/HdSheetAndClassicPaletteLoading.md) | engine (sprite sheets and palettes) | How a sprite number becomes a sheet and a palette: a g2d entry pair through the HD table and the pack's unchecked index table, and a palette from the classic file named in the classic table. |
| [SkillsetNamesAndHelpAreKeyedBySetId](../behaviors/SkillsetNamesAndHelpAreKeyedBySetId.md) | engine | A skillset's name and help are found by the set id alone: the name token is 0xB000 \| set (text kind 22) and the help token 0x9800 \| set (kind 19), both 11-bit indexes; the name row is the JobCommand-en NXD row keyed b... |
| [SpriteSheetsAndClassicFilesByNumber](../behaviors/SpriteSheetsAndClassicFilesByNumber.md) | engine (asset loading) | HD sprite sheets are read by number and the loader accepts any number; classic sprite files are read by name only. |

## Tables (1)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [TextPools](../tables/TextPools.md) | Executable (filled at load) |  | 32 pointers | The thirty-two text pool pointers the generic text decoder indexes by a text id's kind bits. |
