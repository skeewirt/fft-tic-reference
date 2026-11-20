# Data access

NXD table accessors, the table registry and other game-data lookups.

Functions: 60, Structures: 112, Globals: 2, Registries: 3, File formats: 5, Flows: 3, Observed behaviours: 13, Tables: 116.

## Functions (60)

| Name | Address | Purpose |
|---|---|---|
| [BattleMsg_BuildArgs](../functions/BattleMsg_BuildArgs.md) | `0x1400F79D0` | Fills the format-argument vector for a message descriptor: selects the message id, then pushes the values that replace the template's <string=lstrN> and <num=...> placeholders. |
| [BattleMsg_FillArgs](../functions/BattleMsg_FillArgs.md) | `0x1401EC074` | Fills the format-argument vector for the banner: first asks the message-id-specific builder, and when that pushes nothing, copies the object's up to 40 stored argument entries. |
| [BattleMsg_IdFromDescriptor](../functions/BattleMsg_IdFromDescriptor.md) | `0x1400FCC04` | Turns a message descriptor into the row id used by NXD table 172 (C_Mes_Id_Sample-en). |
| [BattleMsg_TextFromDescriptor](../functions/BattleMsg_TextFromDescriptor.md) | `0x1400FCBB4` | Returns the template text for a message descriptor from one of two text sources. |
| [CMesId_GetText](../functions/CMesId_GetText.md) | `0x1400FCB2C` | Returns the text of one row of NXD table 172 (0xAC, the C_Mes_Id_Sample table) and caches the table pointer. |
| [Deflate_Init2](../functions/Deflate_Init2.md) | `0x14040E9B0` | Initialises a deflate compression stream (the embedded zlib-style compressor): validates the arguments, allocates the 5920-byte state and its buffers, then resets the stream. |
| [FormatArgs_Push](../functions/FormatArgs_Push.md) | `0x1400FE4E4` | Appends one 264-byte format-argument record to a format-argument vector. |
| [Glyph_GetAdvance](../functions/Glyph_GetAdvance.md) | `0x140331E60` | Returns the pixel advance of a message glyph. |
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
| [sub_1402EC9D0](../functions/sub_1402EC9D0.md) | `0x1402EC9D0` | The menu-side text-id command thunk. |
| [sub_140332B48](../functions/sub_140332B48.md) | `0x140332B48` | Returns the string pool that belongs to a text kind; the kind selects a pool, which is prepared and then returned by pointer. |
| [TextKind25_LoadPool](../functions/TextKind25_LoadPool.md) | `0x140284098` | Loads the text pool that serves text kind 25 (base 0xC800): it sizes the buffer from the current pool count, allocates it, and reads one of five sectors into it. |
| [TextTag_CountedNounArticle](../functions/TextTag_CountedNounArticle.md) | `0x1400F3F94` | Counted-noun text tag builder that first adds an article or form string from a per-language table. |
| [TextTag_CountedNounForms](../functions/TextTag_CountedNounForms.md) | `0x1400F4200` | Counted-noun text tag builder that adds a form string chosen by two record bytes. |
| [TextTag_CountedNounIndexed](../functions/TextTag_CountedNounIndexed.md) | `0x1400F4558` | Counted-noun text tag builder that indexes a per-language form table with three record bytes. |
| [TextTag_CountedNounPlain](../functions/TextTag_CountedNounPlain.md) | `0x1400F4718` | Counted-noun text tag builder with no article or form string. |
| [TextTag_ExpandKeyIcon](../functions/TextTag_ExpandKeyIcon.md) | `0x1400F2648` | Expands the in-text tags of the UI text engine; the 'keyicon' tag inserts the button glyph of a named input action. |
| [UITable_GetRowByKey](../functions/UITable_GetRowByKey.md) | `0x1403DBC74` | Returns the row of an NXD table by table id and row key, or null when the table or row is missing. |
| [UIText_Get](../functions/UIText_Get.md) | `0x1403DBE88` | Returns the UI text string for an id from UI table 19, or a shared empty string when the row is missing. |
| [UIText_ResolveCategoryRow](../functions/UIText_ResolveCategoryRow.md) | `0x1400F3BB0` | Resolves the category name and key of a <category=key> text tag to a table row and fills a 28-byte result record with three string pointers and four flag bytes. |
| [Utf8_DecodeUnit](../functions/Utf8_DecodeUnit.md) | `0x1403BF9D4` | Decodes one UTF-8 sequence to a 16-bit code unit and returns the number of bytes used. |

## Structures (112)

| Name | Size (bytes) | Summary |
|---|---|---|
| [CalendarDaysPerMonthRow](../structs/CalendarDaysPerMonthRow.md) | 1 | One row of the CalendarDaysPerMonth table. |
| [FunctionPointerRow](../structs/FunctionPointerRow.md) | 8 | One function pointer. |
| [GlyphAdvance](../structs/GlyphAdvance.md) | 1 | One row of the GlyphAdvanceWidths table: the advance width of one glyph. |
| [IdRemapRow](../structs/IdRemapRow.md) | 56 | Seven id pairs. |
| [NxdDataAbilityReactionVoiceTypeRow](../structs/NxdDataAbilityReactionVoiceTypeRow.md) | 48 | One row of the nxd.ability_reaction_voice_type table (data table). |
| [NxdDataAchievementArrayRow](../structs/NxdDataAchievementArrayRow.md) | 28 | One row of the nxd.achievement_groups table (data table). |
| [NxdDataAchievementRow](../structs/NxdDataAchievementRow.md) | 28 | One row of the nxd.achievement table (English text table; the other languages share the layout). |
| [NxdDataBattleVoiceGroupRateRow](../structs/NxdDataBattleVoiceGroupRateRow.md) | 208 | One row of the nxd.battle_voice_group_rate table (data table). |
| [NxdDataBattleVoiceRow](../structs/NxdDataBattleVoiceRow.md) | 44 | One row of the nxd.battle_voice table (data table). |
| [NxdDataBGMModeRow](../structs/NxdDataBGMModeRow.md) | 24 | One row of the nxd.bgm_mode table (English text table; the other languages share the layout). |
| [NxdDataBGMTransitionRow](../structs/NxdDataBGMTransitionRow.md) | 20 | One row of the nxd.bgm_transition table (data table). |
| [NxdDataBraveStoryVoiceRow](../structs/NxdDataBraveStoryVoiceRow.md) | 16 | One row of the nxd.brave_story_voice table (data table). |
| [NxdDataCaptionFreeWordRow](../structs/NxdDataCaptionFreeWordRow.md) | 12 | One row of the nxd.caption_free_word table (English text table; the other languages share the layout). |
| [NxdDataCaptionRow](../structs/NxdDataCaptionRow.md) | 16 | One row of the nxd.caption table (data table). |
| [NxdDataChapterFileRow](../structs/NxdDataChapterFileRow.md) | 8 | One row of the nxd.chapter_file table (data table). |
| [NxdDataChapterRow](../structs/NxdDataChapterRow.md) | 16 | One row of the nxd.chapter table (English text table; the other languages share the layout). |
| [NxdDataCollectionRow](../structs/NxdDataCollectionRow.md) | 44 | One row of the nxd.collection table (English text table; the other languages share the layout). |
| [NxdDataDebugFidG2DRow](../structs/NxdDataDebugFidG2DRow.md) | 12 | One row of the nxd.debug_fid_g2d table (data table). |
| [NxdDataDebugFIdSoundRow](../structs/NxdDataDebugFIdSoundRow.md) | 8 | One row of the nxd.debug_fid_sound table (data table). |
| [NxdDataDebugMapRow](../structs/NxdDataDebugMapRow.md) | 16 | One row of the nxd.debug_map table (data table). |
| [NxdDataDebugSceneSelectCategoryRow](../structs/NxdDataDebugSceneSelectCategoryRow.md) | 12 | One row of the nxd.debug_scene_select_category table (data table). |
| [NxdDataDeepDungeonRow](../structs/NxdDataDeepDungeonRow.md) | 12 | One row of the nxd.deep_dungeon table (English text table; the other languages share the layout). |
| [NxdDataDLCPathListRow](../structs/NxdDataDLCPathListRow.md) | 12 | One row of the nxd.dlc_path_list table (data table). |
| [NxdDataFacilityVoicePatternRow](../structs/NxdDataFacilityVoicePatternRow.md) | 20 | One row of the nxd.facility_voice_pattern table (data table). |
| [NxdDataGameProgressRow](../structs/NxdDataGameProgressRow.md) | 20 | One row of the nxd.game_progress table (data table). |
| [NxdDataGossipRow](../structs/NxdDataGossipRow.md) | 48 | One row of the nxd.gossip table (English text table; the other languages share the layout). |
| [NxdDataGuideCategoryRow](../structs/NxdDataGuideCategoryRow.md) | 16 | One row of the nxd.guide_category table (data table). |
| [NxdDataGuidePageRow](../structs/NxdDataGuidePageRow.md) | 24 | One row of the nxd.guide_page table (English text table; the other languages share the layout). |
| [NxdDataGuideRow](../structs/NxdDataGuideRow.md) | 48 | One row of the nxd.guide table (English text table; the other languages share the layout). |
| [NxdDataJingleRow](../structs/NxdDataJingleRow.md) | 12 | One row of the nxd.jingle table (data table). |
| [NxdDataJournalRow](../structs/NxdDataJournalRow.md) | 40 | One row of the nxd.journal table (English text table; the other languages share the layout). |
| [NxdDataLandRow](../structs/NxdDataLandRow.md) | 20 | One row of the nxd.land table (English text table; the other languages share the layout). |
| [NxdDataLandscapeHeightRow](../structs/NxdDataLandscapeHeightRow.md) | 8 | One row of the nxd.landscape_height table (English text table; the other languages share the layout). |
| [NxdDataLauncherGuideRow](../structs/NxdDataLauncherGuideRow.md) | 16 | One row of the nxd.launcher_guide table (English text table; the other languages share the layout). |
| [NxdDataLoreAffiliationRow](../structs/NxdDataLoreAffiliationRow.md) | 16 | One row of the nxd.lore_affiliation table (English text table; the other languages share the layout). |
| [NxdDataLoreDictionaryCategoryRow](../structs/NxdDataLoreDictionaryCategoryRow.md) | 16 | One row of the nxd.lore_dictionary_category table (English text table; the other languages share the layout). |
| [NxdDataLoreDictionaryRow](../structs/NxdDataLoreDictionaryRow.md) | 84 | One row of the nxd.lore_dictionary table (English text table; the other languages share the layout). |
| [NxdDataLoreNameAliasRow](../structs/NxdDataLoreNameAliasRow.md) | 12 | One row of the nxd.lore_name_alias table (English text table; the other languages share the layout). |
| [NxdDataMapRouteTableRow](../structs/NxdDataMapRouteTableRow.md) | 12 | One row of the nxd.map_route_table table (data table). |
| [NxdDataMovieDataRow](../structs/NxdDataMovieDataRow.md) | 40 | One row of the nxd.movie_data table (data table). |
| [NxdDataNovel00Row](../structs/NxdDataNovel00Row.md) | 8 | One row of the nxd.novel_00 table (English text table; the other languages share the layout). |
| [NxdDataNovel01Row](../structs/NxdDataNovel01Row.md) | 8 | One row of the nxd.novel_01 table (English text table; the other languages share the layout). |
| [NxdDataNovel02Row](../structs/NxdDataNovel02Row.md) | 8 | One row of the nxd.novel_02 table (English text table; the other languages share the layout). |
| [NxdDataNovel03Row](../structs/NxdDataNovel03Row.md) | 8 | One row of the nxd.novel_03 table (English text table; the other languages share the layout). |
| [NxdDataNovel04Row](../structs/NxdDataNovel04Row.md) | 8 | One row of the nxd.novel_04 table (English text table; the other languages share the layout). |
| [NxdDataNovelIconRow](../structs/NxdDataNovelIconRow.md) | 20 | One row of the nxd.novel_icon table (data table). |
| [NxdDataPlaceNameRow](../structs/NxdDataPlaceNameRow.md) | 20 | One row of the nxd.place_name table (English text table; the other languages share the layout). |
| [NxdDataPSPMovieFileRow](../structs/NxdDataPSPMovieFileRow.md) | 12 | One row of the nxd.psp_movie_file table (data table). |
| [NxdDataRouteRow](../structs/NxdDataRouteRow.md) | 28 | One row of the nxd.route table (data table). |
| [NxdDataScionFilesRow](../structs/NxdDataScionFilesRow.md) | 8 | One row of the nxd.scion_files table (data table). |
| [NxdDataScionLabelsRow](../structs/NxdDataScionLabelsRow.md) | 12 | One row of the nxd.scion_labels table (data table). |
| [NxdDataSeadEventRow](../structs/NxdDataSeadEventRow.md) | 16 | One row of the nxd.sead_event table (data table). |
| [NxdDataSeadStateParameterRow](../structs/NxdDataSeadStateParameterRow.md) | 12 | One row of the nxd.sead_state_parameter table (data table). |
| [NxdDataSeDefineRow](../structs/NxdDataSeDefineRow.md) | 16 | One row of the nxd.se_define table (data table). |
| [NxdDataSeSystemRow](../structs/NxdDataSeSystemRow.md) | 8 | One row of the nxd.se_system table (data table). |
| [NxdDataShopVoiceRow](../structs/NxdDataShopVoiceRow.md) | 16 | One row of the nxd.shop_voice table (data table). |
| [NxdDataSoundEnhancedResourceRow](../structs/NxdDataSoundEnhancedResourceRow.md) | 12 | One row of the nxd.sound_enhanced_resource table (data table). |
| [NxdDataSoundEnhancedRow](../structs/NxdDataSoundEnhancedRow.md) | 24 | One row of the nxd.sound_enhanced table (data table). |
| [NxdDataSpeakerRow](../structs/NxdDataSpeakerRow.md) | 8 | One row of the nxd.speaker table (English text table; the other languages share the layout). |
| [NxdDataSpellMessageRow](../structs/NxdDataSpellMessageRow.md) | 12 | One row of the nxd.spell_message table (data table). |
| [NxdDataSubQuestMessageRow](../structs/NxdDataSubQuestMessageRow.md) | 12 | One row of the nxd.sub_quest_message table (data table). |
| [NxdDataSystemBonusEntitlementRow](../structs/NxdDataSystemBonusEntitlementRow.md) | 20 | One row of the nxd.system_bonus_entitlement table (data table). |
| [NxdDataSystemBonusItemContentsRow](../structs/NxdDataSystemBonusItemContentsRow.md) | 12 | One row of the nxd.system_bonus_item_contents table (data table). |
| [NxdDataSystemBonusItemRow](../structs/NxdDataSystemBonusItemRow.md) | 24 | One row of the nxd.system_bonus_item table (English text table; the other languages share the layout). |
| [NxdDataSystemBonusSpecialItemRow](../structs/NxdDataSystemBonusSpecialItemRow.md) | 24 | One row of the nxd.system_bonus_special_item table (English text table; the other languages share the layout). |
| [NxdDataTelemetryAchievementGradeRow](../structs/NxdDataTelemetryAchievementGradeRow.md) | 4 | One row of the nxd.telemetry_achievement_grade table (data table). |
| [NxdDataTelemetryAchievementRow](../structs/NxdDataTelemetryAchievementRow.md) | 64 | One row of the nxd.telemetry_achievement table (English text table; the other languages share the layout). |
| [NxdDataTelemetryEventDefinitionRow](../structs/NxdDataTelemetryEventDefinitionRow.md) | 20 | One row of the nxd.telemetry_event_definition table (data table). |
| [NxdDataTelemetryEventRow](../structs/NxdDataTelemetryEventRow.md) | 20 | One row of the nxd.telemetry_event table (data table). |
| [NxdDataTelemetryObjectRow](../structs/NxdDataTelemetryObjectRow.md) | 20 | One row of the nxd.telemetry_object table (data table). |
| [NxdDataTelemetryPropertyRow](../structs/NxdDataTelemetryPropertyRow.md) | 12 | One row of the nxd.telemetry_property table (data table). |
| [NxdDataTelemetryPropertyValueRow](../structs/NxdDataTelemetryPropertyValueRow.md) | 12 | One row of the nxd.telemetry_property_value table (data table). |
| [NxdDataTelemetryStatExtractionRow](../structs/NxdDataTelemetryStatExtractionRow.md) | 28 | One row of the nxd.telemetry_stat_extraction table (data table). |
| [NxdDataTelemetryStatRow](../structs/NxdDataTelemetryStatRow.md) | 32 | One row of the nxd.telemetry_stat table (data table). |
| [NxdDataTownImageRow](../structs/NxdDataTownImageRow.md) | 4 | One row of the nxd.town_image table (data table). |
| [NxdDataTownRow](../structs/NxdDataTownRow.md) | 52 | One row of the nxd.town table (English text table; the other languages share the layout). |
| [NxdDataUDSActivityRow](../structs/NxdDataUDSActivityRow.md) | 28 | One row of the nxd.uds_activity table (data table). |
| [NxdDataUIAttributiveRow](../structs/NxdDataUIAttributiveRow.md) | 156 | One row of the nxd.ui_attributive table (data table). |
| [NxdDataUIChronicleCharaListRow](../structs/NxdDataUIChronicleCharaListRow.md) | 24 | One row of the nxd.ui_chronicle_chara_list table (data table). |
| [NxdDataUIChroniclePeriodRow](../structs/NxdDataUIChroniclePeriodRow.md) | 40 | One row of the nxd.ui_chronicle_period table (English text table; the other languages share the layout). |
| [NxdDataUIClassicSubtitlesRow](../structs/NxdDataUIClassicSubtitlesRow.md) | 28 | One row of the nxd.ui_classic_subtitles table (English text table; the other languages share the layout). |
| [NxdDataUICreditLineArtRow](../structs/NxdDataUICreditLineArtRow.md) | 8 | One row of the nxd.ui_credit_line_art table (data table). |
| [NxdDataUICreditRowRow](../structs/NxdDataUICreditRowRow.md) | 24 | One row of the nxd.ui_credit_row table (data table). |
| [NxdDataUIElementAttributeRow](../structs/NxdDataUIElementAttributeRow.md) | 12 | One row of the nxd.ui_element_attribute table (English text table; the other languages share the layout). |
| [NxdDataUIEndCreditRow](../structs/NxdDataUIEndCreditRow.md) | 20 | One row of the nxd.ui_end_credit table (data table). |
| [NxdDataUIItemCategoryRow](../structs/NxdDataUIItemCategoryRow.md) | 32 | One row of the nxd.ui_item_category table (English text table; the other languages share the layout). |
| [NxdDataUiJobAbilityHelpRow](../structs/NxdDataUiJobAbilityHelpRow.md) | 12 | One row of the nxd.ui_job_ability_help table (English text table; the other languages share the layout). |
| [NxdDataUIOpCreditRow](../structs/NxdDataUIOpCreditRow.md) | 32 | One row of the nxd.ui_op_credit table (data table). |
| [NxdDataUIRow](../structs/NxdDataUIRow.md) | 8 | One row of the nxd.ui_text table (English text table; the other languages share the layout). |
| [NxdDataUISituationSubtitlesRow](../structs/NxdDataUISituationSubtitlesRow.md) | 8 | One row of the nxd.ui_situation_subtitles table (English text table; the other languages share the layout). |
| [NxdDataUISituationSubtitlesShowtimeRow](../structs/NxdDataUISituationSubtitlesShowtimeRow.md) | 8 | One row of the nxd.ui_situation_subtitles_showtime table (data table). |
| [NxdDataUIStatusEffectCategoryRow](../structs/NxdDataUIStatusEffectCategoryRow.md) | 24 | One row of the nxd.ui_status_effect_category table (English text table; the other languages share the layout). |
| [NxdDataUIStatusEffectRow](../structs/NxdDataUIStatusEffectRow.md) | 36 | One row of the nxd.ui_status_effect table (English text table; the other languages share the layout). |
| [NxdDataUISubtitlesComponentRow](../structs/NxdDataUISubtitlesComponentRow.md) | 16 | One row of the nxd.ui_subtitles_component table (data table). |
| [NxdDataUISubtitlesRow](../structs/NxdDataUISubtitlesRow.md) | 52 | One row of the nxd.ui_subtitles table (English text table; the other languages share the layout). |
| [NxdDataUISubtitlesTimelineRow](../structs/NxdDataUISubtitlesTimelineRow.md) | 24 | One row of the nxd.ui_subtitles_timeline table (data table). |
| [NxdDataUITitleCreditRow](../structs/NxdDataUITitleCreditRow.md) | 20 | One row of the nxd.ui_title_credit table (data table). |
| [NxdDataUnitBarProfitResultMessageRow](../structs/NxdDataUnitBarProfitResultMessageRow.md) | 12 | One row of the nxd.unit_bar_profit_result_message table (data table). |
| [NxdDataUnitCommunMessageRow](../structs/NxdDataUnitCommunMessageRow.md) | 12 | One row of the nxd.unit_commun_message table (data table). |
| [NxdDataUnitHelpMessageRow](../structs/NxdDataUnitHelpMessageRow.md) | 44 | One row of the nxd.unit_help_message table (data table). |
| [NxdDataUnitPartMessageRow](../structs/NxdDataUnitPartMessageRow.md) | 12 | One row of the nxd.unit_part_message table (data table). |
| [NxdDataUnitVoiceRow](../structs/NxdDataUnitVoiceRow.md) | 28 | One row of the nxd.unit_voice table (data table). |
| [NxdDataUnitWarnMessageRow](../structs/NxdDataUnitWarnMessageRow.md) | 12 | One row of the nxd.unit_warn_message table (data table). |
| [NxdDataUserSituationRow](../structs/NxdDataUserSituationRow.md) | 96 | One row of the nxd.user_situation table (data table). |
| [NxdDataVoicePatternRow](../structs/NxdDataVoicePatternRow.md) | 24 | One row of the nxd.voice_pattern table (data table). |
| [NxdDataVoicePatternSituationRow](../structs/NxdDataVoicePatternSituationRow.md) | 16 | One row of the nxd.voice_pattern_situation table (data table). |
| [NxdDataWorldMapProgressInfoRow](../structs/NxdDataWorldMapProgressInfoRow.md) | 44 | One row of the nxd.world_map_progress_info table (English text table; the other languages share the layout). |
| [NxdDataWorldSituationBalloonRow](../structs/NxdDataWorldSituationBalloonRow.md) | 76 | One row of the nxd.world_situation_balloon table (data table). |
| [NxdTable](../structs/NxdTable.md) | 80 | One table object of the nxd registry (NxdRegistry_LoadRootNxl allocates one per root.nxl line); NxdTable_BindRows fills its entries from the loaded file and every row lookup reads it. |
| [PowerOfTen](../structs/PowerOfTen.md) | 4 | One row of the PowersOfTen table. |
| [TextTagNounRecord](../structs/TextTagNounRecord.md) | 28 | The 28-byte result record of UIText_ResolveCategoryRow for a <category=key> text tag: three string pointers and four bytes. |
| [TextTagRecord](../structs/TextTagRecord.md) |  | The record UIText_ResolveCategoryRow gives the counted-noun text tag builders: three strings and four grammar bytes. |

## Globals (2)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_MessageArgBlock](../globals/g_MessageArgBlock.md) | `0x140783210` | `uint32[16]` | The current-message argument vector: 0x40 bytes, sixteen dwords. |
| [g_TextPoolTable](../globals/g_TextPoolTable.md) | `0x140D40990` | `char *[32]` | The thirty-two text-pool pointers the generic decoder indexes by a text id's five kind bits. |

## Registries (3)

| Name | Summary |
|---|---|
| [TextIdKinds](../registries/TextIdKinds.md) | The 32 text-id kinds: the 5 bits of a text id, their base (kind x 0x800) and the pool or source each selects. |
| [TextLanguageCodes](../registries/TextLanguageCodes.md) | The text language codes the game keeps at `g_LanguageInfo`+8, with the language pack and the name suffix each one selects. |
| [TextTagName](../registries/TextTagName.md) | The first 40 records of the UI text engine's tag-name table (16 bytes each: a name pointer and a flag dword). |

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

## Observed behaviours (13)

| Name | Scope | Summary |
|---|---|---|
| [CharShapeRowsANewLookNeeds](../behaviors/CharShapeRowsANewLookNeeds.md) | engine (sprite rows in the NXD data) | The CharShape rows (NXD table 174, keyed by look number) end at key 158 and twelve functions look a look up there. |
| [CountedNounTagRecord](../behaviors/CountedNounTagRecord.md) | engine (UI text tags) | How the four counted-noun tag builders use the four grammar bytes of a text tag record. |
| [FirstDwordOfTableRowsIsNeverRead](../behaviors/FirstDwordOfTableRowsIsNeverRead.md) | engine (nxd table access) | No shared code reads the first dword of a table row; a row is found through the key / offset index record, so the value there decides nothing. |
| [HdSheetAndClassicPaletteLoading](../behaviors/HdSheetAndClassicPaletteLoading.md) | engine (sprite sheets and palettes) | How a sprite number becomes a sheet and a palette: a g2d entry pair through the HD table and the pack's unchecked index table, and a palette from the classic file named in the classic table. |
| [JobNameAndHelpTextTags](../behaviors/JobNameAndHelpTextTags.md) | engine (UI text tags) | The text tags 'jobname' and 'jobhelp' print a Job row's name or help text; each takes a key and a variant, and a variant whose string is empty falls back to the other. |
| [KeyIconTag](../behaviors/KeyIconTag.md) | engine (UI text) | A 'keyicon' text tag names an input action and the text engine inserts that action's current button glyph. |
| [MapTablesBytesAndTablesNothingReads](../behaviors/MapTablesBytesAndTablesNothingReads.md) | engine (Map, MapVariationEvent, MapVariationRandomBattle) | Columns and a whole table of the battle map tables that no code reads, found by listing every fetch of each table and every use of the fetched rows, so the stored values decide nothing. |
| [RecordBytesTheGameNeverReads](../behaviors/RecordBytesTheGameNeverReads.md) | engine (fixed tables in the executable) | Bytes and bits of several fixed tables that no function of the game reads, found by listing every code reference to each table, so the stored values decide nothing. |
| [SkillsetNamesAndHelpAreKeyedBySetId](../behaviors/SkillsetNamesAndHelpAreKeyedBySetId.md) | engine | A skillset's name and help are found by the set id alone: the name token is 0xB000 \| set (text kind 22) and the help token 0x9800 \| set (kind 19), both 11-bit indexes; the name row is the JobCommand-en NXD row keyed b... |
| [SpriteSheetsAndClassicFilesByNumber](../behaviors/SpriteSheetsAndClassicFilesByNumber.md) | engine (asset loading) | HD sprite sheets are read by number and the loader accepts any number; classic sprite files are read by name only. |
| [TextLanguage](../behaviors/TextLanguage.md) | the text language: where it comes from, where it is read, how the text files are chosen | How the game picks and applies its text language. |
| [TextReferenceIsABankAndAnElevenBitIndex](../behaviors/TextReferenceIsABankAndAnElevenBitIndex.md) | engine (event text lookup) | An event message is named by a 16-bit reference: the top five bits select one of 32 text banks (each a resource), the low 11 bits are the message index inside it; the lookup counts message terminators from the start o... |
| [UnreadColumnsOfJobAbilityStatusTables](../behaviors/UnreadColumnsOfJobAbilityStatusTables.md) | engine (nxd tables) | Columns of the GeneralJob, Job, JobCommand, JobType, Ability and UIStatusEffect tables that no code of the game reads; their values change nothing in play. |

## Tables (116)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [CalendarDaysPerMonth](../tables/CalendarDaysPerMonth.md) | Executable |  | 13 rows of 1 byte | Days per month for the new-game birthday picker (February 28); right behind it a table of the 12 zodiac sign start dates (month, day) and a dword table of 7 values (75 to 465, step 65). |
| [DeflateErrorMessages](../tables/DeflateErrorMessages.md) | Executable |  | 10 rows of 8 bytes | Result code messages of the embedded compression library in its usual order: need dictionary, stream end, (empty), file error, stream error, data error, insufficient memory, buffer error, incompatible version, (empty). |
| [GlyphAdvanceExceptions](../tables/GlyphAdvanceExceptions.md) | Executable |  | 32 rows of 1 bytes | Advance widths of the 32 glyphs 2416..2447, an exception list that Glyph_GetAdvance consults before the main table. |
| [GlyphAdvanceWidths](../tables/GlyphAdvanceWidths.md) | Executable |  | 2912 rows of 1 bytes | Advance width of each message glyph (the proportional-font metrics of the legacy text drawer). |
| [IdRemapPairs](../tables/IdRemapPairs.md) | Executable |  | 406 rows of 56 bytes (2842 pairs) | An id alias table: IdRemap_Lookup scans every row for the id; an unknown id maps to itself. |
| [NxdDataAbilityReactionVoiceType](../tables/NxdDataAbilityReactionVoiceType.md) | NXD file | 330 | 4 rows of 48 bytes | Four rows of numeric voice-reaction parameters selected by an ability's reaction voice type; columns not decoded. |
| [NxdDataAchievement](../tables/NxdDataAchievement.md) | NXD file | 195 | 51 rows of 28 bytes, text in 7 languages | Per achievement: link to its telemetry record, a few story-progress numbers and the description text. |
| [NxdDataAchievementArray](../tables/NxdDataAchievementArray.md) | NXD file | 213 | 7 rows of 28 bytes | Seven achievement groupings: arrays of achievement ids per group. |
| [NxdDataBattleVoice](../tables/NxdDataBattleVoice.md) | NXD file | 183 | 53 rows of 44 bytes | Battle voice cue definitions: numeric voice ids, group and probability parameters per cue. |
| [NxdDataBattleVoiceGroupRate](../tables/NxdDataBattleVoiceGroupRate.md) | NXD file | 184 | 6 rows of 208 bytes | Six rows of 50 percentage weights, one per battle voice group, choosing how often each voice group plays. |
| [NxdDataBGMMode](../tables/NxdDataBGMMode.md) | NXD file | 281 | 97 rows of 24 bytes, text in 7 languages | Music player list: per entry a tab index, title text and a reference to the sound resource to play. |
| [NxdDataBGMTransition](../tables/NxdDataBGMTransition.md) | NXD file | 306 | 14 rows of 20 bytes | Music transition parameters: a sound resource reference and two fade-like float values per row. |
| [NxdDataBraveStoryVoice](../tables/NxdDataBraveStoryVoice.md) | NXD file | 233 | 34 rows of 16 bytes | Voice line references for the Brave Story scenes, keyed by scene and line; each row points at a packed audio entry and a timing float. |
| [NxdDataCaption](../tables/NxdDataCaption.md) | NXD file | 87 | 13 rows of 16 bytes | Caption slots whose content is a typed reference (union) to another table's row. |
| [NxdDataCaptionFreeWord](../tables/NxdDataCaptionFreeWord.md) | NXD file | 86 | 8 rows of 12 bytes, text in 7 languages | Free-form caption words used by the caption system. |
| [NxdDataChapter](../tables/NxdDataChapter.md) | NXD file | 206 | 6 rows of 16 bytes, text in 7 languages | The six chapter titles with a story-progress number each. |
| [NxdDataChapterFile](../tables/NxdDataChapterFile.md) | NXD file | 239 | 13 rows of 8 bytes | Maps chapter file slots to chapter numbers. |
| [NxdDataCollection](../tables/NxdDataCollection.md) | NXD file | 121 | 43 rows of 44 bytes, text in 7 languages | Collection entries (43): name, description and numeric parameters. |
| [NxdDataDebugFidG2D](../tables/NxdDataDebugFidG2D.md) | NXD file | 212 | 1285 rows of 12 bytes | Debug 2D resource id list (1285 rows). |
| [NxdDataDebugFIdSound](../tables/NxdDataDebugFIdSound.md) | NXD file | 89 | 691 rows of 8 bytes | Debug sound id list (691 rows). |
| [NxdDataDebugGameFlowSettings](../tables/NxdDataDebugGameFlowSettings.md) | NXD file | 102 | 0 rows of 0 bytes | Debug table with no rows and no layout columns in the retail file. |
| [NxdDataDebugMap](../tables/NxdDataDebugMap.md) | NXD file | 78 | 80 rows of 16 bytes | Debug map list (80 rows) with comment text. |
| [NxdDataDebugNovelPageDefine](../tables/NxdDataDebugNovelPageDefine.md) | NXD file | 300 | 0 rows of 0 bytes | Debug table with no rows and no layout columns. |
| [NxdDataDebugRefinedBgAnim](../tables/NxdDataDebugRefinedBgAnim.md) | NXD file | 79 | 0 rows of 0 bytes | Debug table with no rows and no layout columns. |
| [NxdDataDebugRefinedBgTexture](../tables/NxdDataDebugRefinedBgTexture.md) | NXD file | 80 | 0 rows of 0 bytes | Debug triple-keyed table with no rows and no layout columns. |
| [NxdDataDebugSceneSelect](../tables/NxdDataDebugSceneSelect.md) | NXD file | 58 | 0 rows of 0 bytes | Debug scene picker rows; empty in the retail file. |
| [NxdDataDebugSceneSelectCategory](../tables/NxdDataDebugSceneSelectCategory.md) | NXD file | 110 | 8 rows of 12 bytes | Eight debug scene picker categories with names. |
| [NxdDataDeepDungeon](../tables/NxdDataDeepDungeon.md) | NXD file | 101 | 10 rows of 12 bytes, text in 7 languages | Ten deep-dungeon floors or entries: name and description text. |
| [NxdDataDLCPathList](../tables/NxdDataDLCPathList.md) | NXD file | 335 | 1 rows of 12 bytes | A path list for downloadable content (one row). |
| [NxdDataFacilityVoicePattern](../tables/NxdDataFacilityVoicePattern.md) | NXD file | 203 | 7 rows of 20 bytes | Facility voice sound file paths (seven patterns). |
| [NxdDataGameProgress](../tables/NxdDataGameProgress.md) | NXD file | 92 | 307 rows of 20 bytes | Story progress steps keyed by progress group and value, linked to world-map progress info rows. |
| [NxdDataGossip](../tables/NxdDataGossip.md) | NXD file | 181 | 23 rows of 48 bytes, text in 7 languages | Tavern rumours (23): title, text, story-progress condition and icon. |
| [NxdDataGuide](../tables/NxdDataGuide.md) | NXD file | 187 | 242 rows of 48 bytes, text in 7 languages | Guide entries (242): page reference, conditions, title and sort order. |
| [NxdDataGuideCategory](../tables/NxdDataGuideCategory.md) | NXD file | 301 | 13 rows of 16 bytes | Guide categories. |
| [NxdDataGuidePage](../tables/NxdDataGuidePage.md) | NXD file | 188 | 409 rows of 24 bytes, text in 7 languages | Guide pages keyed by guide id and page index: icon id arrays and text slots. |
| [NxdDataJingle](../tables/NxdDataJingle.md) | NXD file | 319 | 11 rows of 12 bytes | Eleven jingles pointing at sound resources. |
| [NxdDataJournal](../tables/NxdDataJournal.md) | NXD file | 122 | 117 rows of 40 bytes, text in 7 languages | Journal entries (117): story-progress condition, title and text. |
| [NxdDataLand](../tables/NxdDataLand.md) | NXD file | 94 | 64 rows of 20 bytes, text in 7 languages | Terrain feature entries (64): linked ability, name, description and icon. |
| [NxdDataLandscapeHeight](../tables/NxdDataLandscapeHeight.md) | NXD file | 287 | 76 rows of 8 bytes, text in 7 languages | Terrain height description texts (76). |
| [NxdDataLauncherGuide](../tables/NxdDataLauncherGuide.md) | NXD file | 277 | 50 rows of 16 bytes, text in 7 languages | Launcher guide captions keyed by page and line. |
| [NxdDataLoreAffiliation](../tables/NxdDataLoreAffiliation.md) | NXD file | 241 | 23 rows of 16 bytes, text in 7 languages | Lore affiliations (23): icon and caption. |
| [NxdDataLoreDictionary](../tables/NxdDataLoreDictionary.md) | NXD file | 237 | 241 rows of 84 bytes, text in 7 languages | Lore dictionary entries keyed by entry and part: names, descriptions, sort orders, icons and links. |
| [NxdDataLoreDictionaryCategory](../tables/NxdDataLoreDictionaryCategory.md) | NXD file | 246 | 3 rows of 16 bytes, text in 7 languages | Three lore dictionary category names. |
| [NxdDataLoreNameAlias](../tables/NxdDataLoreNameAlias.md) | NXD file | 240 | 52 rows of 12 bytes, text in 7 languages | Lore name aliases (52). |
| [NxdDataMapRouteTable](../tables/NxdDataMapRouteTable.md) | NXD file | 98 | 314 rows of 12 bytes | Route points between map entries keyed by route and step. |
| [NxdDataMovieData](../tables/NxdDataMovieData.md) | NXD file | 65 | 22 rows of 40 bytes | Movie list (22): file path, sound file id and flags. |
| [NxdDataNovel00](../tables/NxdDataNovel00.md) | NXD file | 164 | 256 rows of 8 bytes, text in 7 languages | Story novel text pages, book 0 (256 rows). |
| [NxdDataNovel01](../tables/NxdDataNovel01.md) | NXD file | 165 | 256 rows of 8 bytes, text in 7 languages | Story novel text pages, book 1. |
| [NxdDataNovel02](../tables/NxdDataNovel02.md) | NXD file | 166 | 255 rows of 8 bytes, text in 7 languages | Story novel text pages, book 2. |
| [NxdDataNovel03](../tables/NxdDataNovel03.md) | NXD file | 167 | 255 rows of 8 bytes, text in 7 languages | Story novel text pages, book 3. |
| [NxdDataNovel04](../tables/NxdDataNovel04.md) | NXD file | 168 | 39 rows of 8 bytes, text in 7 languages | Story novel text pages, book 4 (39 rows). |
| [NxdDataNovelIcon](../tables/NxdDataNovelIcon.md) | NXD file | 220 | 131 rows of 20 bytes | Icons of the novel pages (131). |
| [NxdDataPlaceName](../tables/NxdDataPlaceName.md) | NXD file | 85 | 257 rows of 20 bytes, text in 7 languages | Place names (257 ids up to 100050). |
| [NxdDataPSPMovieFile](../tables/NxdDataPSPMovieFile.md) | NXD file | 66 | 22 rows of 12 bytes | Original-version movie file entries (22). |
| [NxdDataRoute](../tables/NxdDataRoute.md) | NXD file | 97 | 51 rows of 28 bytes | Road records (51): parameters of world-map roads. |
| [NxdDataScionFiles](../tables/NxdDataScionFiles.md) | NXD file | 169 | 498 rows of 8 bytes | File names of the voice archives (498). |
| [NxdDataScionLabels](../tables/NxdDataScionLabels.md) | NXD file | 170 | 3323 rows of 12 bytes | Voice line labels (3323): archive file link and packed entry id. |
| [NxdDataSeadEvent](../tables/NxdDataSeadEvent.md) | NXD file | 99 | 15 rows of 16 bytes | Sound event definitions (15). |
| [NxdDataSeadStateParameter](../tables/NxdDataSeadStateParameter.md) | NXD file | 235 | 41 rows of 12 bytes | Sound state parameters (41). |
| [NxdDataSeDefine](../tables/NxdDataSeDefine.md) | NXD file | 69 | 304 rows of 16 bytes | Sound effect definitions (304), each a typed reference. |
| [NxdDataSeSystem](../tables/NxdDataSeSystem.md) | NXD file | 201 | 169 rows of 8 bytes | System sound effects (169). |
| [NxdDataShopVoice](../tables/NxdDataShopVoice.md) | NXD file | 178 | 131 rows of 16 bytes | Shop voice lines keyed by shop and line, each pointing at a packed audio entry. |
| [NxdDataSoundEnhanced](../tables/NxdDataSoundEnhanced.md) | NXD file | 280 | 254 rows of 24 bytes | Enhanced music cue definitions (254) linked to sound resources. |
| [NxdDataSoundEnhancedResource](../tables/NxdDataSoundEnhancedResource.md) | NXD file | 279 | 110 rows of 12 bytes | Sound resource file paths (110). |
| [NxdDataSpeaker](../tables/NxdDataSpeaker.md) | NXD file | 26 | 304 rows of 8 bytes, text in 7 languages | Speaker names (304 ids). |
| [NxdDataSpellMessage](../tables/NxdDataSpellMessage.md) | NXD file | 146 | 1182 rows of 12 bytes | Spell voice lines keyed by spell and line, pointing at packed audio entries. |
| [NxdDataSubQuestMessage](../tables/NxdDataSubQuestMessage.md) | NXD file | 320 | 3 rows of 12 bytes | Three sub-quest message sound links. |
| [NxdDataSystemBonusEntitlement](../tables/NxdDataSystemBonusEntitlement.md) | NXD file | 293 | 31 rows of 20 bytes | Bonus entitlements (31): download path link and parameters. |
| [NxdDataSystemBonusItem](../tables/NxdDataSystemBonusItem.md) | NXD file | 297 | 3 rows of 24 bytes, text in 7 languages | Bonus item list (3): title, description and a typed reference. |
| [NxdDataSystemBonusItemContents](../tables/NxdDataSystemBonusItemContents.md) | NXD file | 296 | 12 rows of 12 bytes | Bonus item contents, keyed by bonus and slot, typed references. |
| [NxdDataSystemBonusSpecialItem](../tables/NxdDataSystemBonusSpecialItem.md) | NXD file | 295 | 6 rows of 24 bytes, text in 7 languages | Special bonus items (6): typed reference, quantity and caption. |
| [NxdDataTelemetryAchievement](../tables/NxdDataTelemetryAchievement.md) | NXD file | 173 | 54 rows of 64 bytes, text in 7 languages | Achievement definitions for the platform (54): id strings, names, descriptions and parameters. |
| [NxdDataTelemetryAchievementGrade](../tables/NxdDataTelemetryAchievementGrade.md) | NXD file | 135 | 5 rows of 4 bytes | Five achievement grades. |
| [NxdDataTelemetryEvent](../tables/NxdDataTelemetryEvent.md) | NXD file | 133 | 8 rows of 20 bytes | Telemetry event list (8). |
| [NxdDataTelemetryEventDefinition](../tables/NxdDataTelemetryEventDefinition.md) | NXD file | 131 | 8 rows of 20 bytes | Telemetry event definitions (8) with names. |
| [NxdDataTelemetryObject](../tables/NxdDataTelemetryObject.md) | NXD file | 314 | 109 rows of 20 bytes | Telemetry object list (109). |
| [NxdDataTelemetryProperty](../tables/NxdDataTelemetryProperty.md) | NXD file | 130 | 28 rows of 12 bytes | Telemetry property names (28). |
| [NxdDataTelemetryPropertyValue](../tables/NxdDataTelemetryPropertyValue.md) | NXD file | 132 | 37 rows of 12 bytes | Telemetry property value lists (37). |
| [NxdDataTelemetryStat](../tables/NxdDataTelemetryStat.md) | NXD file | 134 | 52 rows of 32 bytes | Telemetry statistics (52). |
| [NxdDataTelemetryStatExtraction](../tables/NxdDataTelemetryStatExtraction.md) | NXD file | 318 | 50 rows of 28 bytes | Telemetry statistic extraction rules (50). |
| [NxdDataTown](../tables/NxdDataTown.md) | NXD file | 52 | 48 rows of 52 bytes, text in 7 languages | Per town (48): description, place name link, condition and parameters. |
| [NxdDataTownImage](../tables/NxdDataTownImage.md) | NXD file | 158 | 27 rows of 4 bytes | Town image indices (27). |
| [NxdDataUDSActivity](../tables/NxdDataUDSActivity.md) | NXD file | 313 | 74 rows of 28 bytes | Activity records for the platform's activity feed (74). |
| [NxdDataUI](../tables/NxdDataUI.md) | NXD file | 19 | 4050 rows of 8 bytes, text in 7 languages | The general UI text table: 4050 strings keyed by UI text key. |
| [NxdDataUIAttributive](../tables/NxdDataUIAttributive.md) | NXD file | 229 | 39 rows of 156 bytes | Attributive text variants (39 rows of 3 string groups). |
| [NxdDataUIChronicleCharaList](../tables/NxdDataUIChronicleCharaList.md) | NXD file | 283 | 168 rows of 24 bytes | Chronicle character lists keyed by period and slot. |
| [NxdDataUIChroniclePeriod](../tables/NxdDataUIChroniclePeriod.md) | NXD file | 275 | 31 rows of 40 bytes, text in 7 languages | Chronicle periods (31): condition, type, character list, icon, caption and balloon links. |
| [NxdDataUIClassicSubtitles](../tables/NxdDataUIClassicSubtitles.md) | NXD file | 128 | 93 rows of 28 bytes, text in 7 languages | Classic-mode movie subtitles keyed by movie and line, with start and end seconds. |
| [NxdDataUICreditLineArt](../tables/NxdDataUICreditLineArt.md) | NXD file | 304 | 19 rows of 8 bytes | Credit line art UI names (19). |
| [NxdDataUICreditRow](../tables/NxdDataUICreditRow.md) | NXD file | 309 | 1227 rows of 24 bytes | Credit rows (1227): type, caption array and icon. |
| [NxdDataUIElementAttribute](../tables/NxdDataUIElementAttribute.md) | NXD file | 55 | 8 rows of 12 bytes, text in 7 languages | Element attribute names (8). |
| [NxdDataUIEndCredit](../tables/NxdDataUIEndCredit.md) | NXD file | 307 | 1201 rows of 20 bytes | End credit script rows (1201). |
| [NxdDataUIItemCategory](../tables/NxdDataUIItemCategory.md) | NXD file | 38 | 35 rows of 32 bytes, text in 7 languages | Item category names and parameters (35). |
| [NxdDataUiJobAbilityHelp](../tables/NxdDataUiJobAbilityHelp.md) | NXD file | 303 | 35 rows of 12 bytes, text in 7 languages | Job ability help texts (35). |
| [NxdDataUIOpCredit](../tables/NxdDataUIOpCredit.md) | NXD file | 316 | 130 rows of 32 bytes | Opening credit rows keyed by credit and part. |
| [NxdDataUISituationSubtitles](../tables/NxdDataUISituationSubtitles.md) | NXD file | 224 | 74 rows of 8 bytes, text in 7 languages | Situation subtitle captions keyed by situation and line. |
| [NxdDataUISituationSubtitlesShowtime](../tables/NxdDataUISituationSubtitlesShowtime.md) | NXD file | 226 | 7 rows of 8 bytes | Subtitle display times (7). |
| [NxdDataUIStatusEffect](../tables/NxdDataUIStatusEffect.md) | NXD file | 57 | 45 rows of 36 bytes, text in 7 languages | Status effect names and captions (45) with a type. |
| [NxdDataUIStatusEffectCategory](../tables/NxdDataUIStatusEffectCategory.md) | NXD file | 56 | 13 rows of 24 bytes, text in 7 languages | Status effect category names (13 rows of 3 forms). |
| [NxdDataUISubtitles](../tables/NxdDataUISubtitles.md) | NXD file | 138 | 662 rows of 52 bytes, text in 7 languages | Event subtitles keyed by event and line, linked to voice labels. |
| [NxdDataUISubtitlesComponent](../tables/NxdDataUISubtitlesComponent.md) | NXD file | 162 | 79 rows of 16 bytes | Subtitle window components (79). |
| [NxdDataUISubtitlesTimeline](../tables/NxdDataUISubtitlesTimeline.md) | NXD file | 142 | 94 rows of 24 bytes | Subtitle timelines (94). |
| [NxdDataUITitleCredit](../tables/NxdDataUITitleCredit.md) | NXD file | 308 | 1201 rows of 20 bytes | Title credit script rows (1201). |
| [NxdDataUnitBarProfitResultMessage](../tables/NxdDataUnitBarProfitResultMessage.md) | NXD file | 205 | 240 rows of 12 bytes | Errand result message voice entries keyed by errand and slot. |
| [NxdDataUnitCommunMessage](../tables/NxdDataUnitCommunMessage.md) | NXD file | 192 | 72 rows of 12 bytes | Unit common message voice entries keyed by unit and slot. |
| [NxdDataUnitHelpMessage](../tables/NxdDataUnitHelpMessage.md) | NXD file | 194 | 572 rows of 44 bytes | Unit help message voice entries keyed by unit and line. |
| [NxdDataUnitPartMessage](../tables/NxdDataUnitPartMessage.md) | NXD file | 191 | 59 rows of 12 bytes | Unit part message voice entries. |
| [NxdDataUnitVoice](../tables/NxdDataUnitVoice.md) | NXD file | 204 | 10 rows of 28 bytes | Unit voice type definitions (10). |
| [NxdDataUnitWarnMessage](../tables/NxdDataUnitWarnMessage.md) | NXD file | 190 | 59 rows of 12 bytes | Unit warning message voice entries. |
| [NxdDataUserSituation](../tables/NxdDataUserSituation.md) | NXD file | 90 | 499 rows of 96 bytes | Story situation conditions keyed by situation and slot: up to three check types with indices, values and success flags. |
| [NxdDataVoicePattern](../tables/NxdDataVoicePattern.md) | NXD file | 185 | 110 rows of 24 bytes | Voice patterns (110). |
| [NxdDataVoicePatternSituation](../tables/NxdDataVoicePatternSituation.md) | NXD file | 196 | 18 rows of 16 bytes | Voice pattern situations keyed by pattern and slot, with story-condition links. |
| [NxdDataWorldMapProgressInfo](../tables/NxdDataWorldMapProgressInfo.md) | NXD file | 123 | 91 rows of 44 bytes, text in 7 languages | World-map progress steps keyed by group and step: towns, roads, caption and condition links. |
| [NxdDataWorldSituationBalloon](../tables/NxdDataWorldSituationBalloon.md) | NXD file | 286 | 90 rows of 76 bytes | World situation balloons keyed by period and slot (90). |
| [PowersOfTen](../tables/PowersOfTen.md) | Executable |  | 10 rows of 4 bytes | Powers of ten used to split a number into decimal digits for text. |
| [TextPools](../tables/TextPools.md) | Executable (filled at load) |  | 32 pointers | The thirty-two text pool pointers the generic text decoder indexes by a text id's kind bits. |
