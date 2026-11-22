# Save data

The schema layer for save and config records: the generic descriptor walker, the schemas for the save file and its sections, and the config file.

Functions: 139, Structures: 13, Globals: 8, File formats: 4, Flows: 3, Observed behaviours: 6, Tables: 10.

## Functions (139)

| Name | Address | Purpose |
|---|---|---|
| [Battle_RestoreCapture](../functions/Battle_RestoreCapture.md) | `0x1402CE7A8` | Restores the five memory blocks and the live state of a saved battle payload into the running scene, excluding the scene-task block that the game never restored. |
| [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md) | `0x1402CE5C8` | Puts a saved battle's scene state back from the battle snapshot region: seven scene variables, the live stores, the battle unit table, the look queue and the look pool. |
| [Battle_SaveCapture](../functions/Battle_SaveCapture.md) | `0x1402CDBC4` | Captures the battle state into the autosave battle payload: the scene variables, the five memory blocks A..E, the live item and unit state and the item order record. |
| [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md) | `0x140279BF4` | Captures or restores the live save state the battle image carries: the item stores and the unit save records, copied between the live globals and a save work block in the direction the second argument selects. |
| [BattleCapture_CopyFaceValues](../functions/BattleCapture_CopyFaceValues.md) | `0x140304BEC` | Copies the 10 battle face values of the look pool and the globals after them to (mode 0) or from (mode 1) the battle capture. |
| [CardSlot_IsValid](../functions/CardSlot_IsValid.md) | `0x140245C34` | Tests that a slot of the cache starts with the `SC` magic: returns 0 when valid, -1 otherwise. |
| [ConfigFile_Serialize](../functions/ConfigFile_Serialize.md) | `0x1400C5868` | Describes the config file body: the settings and guide records, the output id, window position, resolution, refresh rate and the cleared, classic-started and enhanced-started flags. |
| [ConfigGuideFlag_Serialize](../functions/ConfigGuideFlag_Serialize.md) | `0x1400C4BD4` | Describes the guide flag. |
| [ConfigRoot_Serialize](../functions/ConfigRoot_Serialize.md) | `0x1400C5E8C` | Describes the root of the config file: a single `m_system` record that holds the config body. |
| [ConfigSettings_Serialize](../functions/ConfigSettings_Serialize.md) | `0x1400C4C78` | Describes the game's option settings: resolution, screen mode and brightness, depth of field, speaker and subtitle visibility, text and voice language, sound, camera reversal, cursor behaviour, auto equip, button and ... |
| [ConfigVolume_Serialize](../functions/ConfigVolume_Serialize.md) | `0x1400C48FC` | Describes the volume settings: overall, music, sound effects, voice and movie volume, and the visual-effect switch. |
| [FieldSchema_LoadFromNode](../functions/FieldSchema_LoadFromNode.md) | `0x1400B059C` | The load half of the field-schema walker: for each descriptor of a schema it looks a node up by name and decodes it into the record. |
| [FieldSchema_Run](../functions/FieldSchema_Run.md) | `0x1400B024C` | The generic walker behind the game's save and config records: it takes a table of field descriptors and turns one in-memory record into a tree of named value nodes (or, for the other direction, fills a record from suc... |
| [Save_BootClear](../functions/Save_BootClear.md) | `0x1402D3FA0` | The boot-time save clear: it fills the save cache and the auto slot with the empty pattern, resets the save manager and the auto-slot header, and starts the reload state machine. |
| [Save_ResumeCheckpoint](../functions/Save_ResumeCheckpoint.md) | `0x1402D03D8` | After a slot load, decides whether the auto-slot checkpoint is a plain world-map one: only then it copies the checkpoint into the save work block and unpacks it to the live records. |
| [SaveAnimUnit_Serialize](../functions/SaveAnimUnit_Serialize.md) | `0x1400B7970` | Describes one animated unit's state: animation work id, unit id, colour and colour offset, flags and animation sequence. |
| [SaveBattleCamera_Serialize](../functions/SaveBattleCamera_Serialize.md) | `0x1400C24CC` | Describes the battle camera reserve record. |
| [SaveBlockHeader_Serialize](../functions/SaveBlockHeader_Serialize.md) | `0x140032318` | Describes the header of a stored data block: its size, checksum and version. |
| [SaveCameraSettings_Serialize](../functions/SaveCameraSettings_Serialize.md) | `0x1400C23B8` | Describes two camera settings (`m_zoom` and `m_fukan`). |
| [SaveCard_Serialize](../functions/SaveCard_Serialize.md) | `0x1400B75A8` | Describes the memory-card style block header: magic, type, block entry, title, timestamp and icon. |
| [SaveDarlavon_Serialize](../functions/SaveDarlavon_Serialize.md) | `0x1400BFC68` | Describes the Darlavon opened flag and an arrival flag. |
| [SaveData_InflateEntry](../functions/SaveData_InflateEntry.md) | `0x14003425C` | Decodes one container entry: unscrambles it and inflates it with zlib using a 32768-byte preset dictionary. |
| [SaveData_Scramble](../functions/SaveData_Scramble.md) | `0x1400341BC` | XOR-scrambles (and unscrambles: it is its own inverse) a buffer with the container's fixed key. |
| [SaveDifficulty_Serialize](../functions/SaveDifficulty_Serialize.md) | `0x1400C1A78` | Describes the difficulty level. |
| [SaveEquipSet_Serialize](../functions/SaveEquipSet_Serialize.md) | `0x1400B9744` | Describes one saved equipment set: name, item, ability, job and a double-hand flag. |
| [SaveEquipSort_Serialize](../functions/SaveEquipSort_Serialize.md) | `0x1400BCB4C` | Describes the sort orders of the equipment lists for hands, head, armor and accessories, and the order items were obtained in. |
| [SaveFftPsp_Serialize](../functions/SaveFftPsp_Serialize.md) | `0x1400C2D5C` | Describes the `m_fftpsp` record, which wraps the save work. |
| [SaveFile_QueueEntry](../functions/SaveFile_QueueEntry.md) | `0x140033B9C` | Queues one named entry (name, version, data buffer) into the save file object for writing into the PNG container. |
| [SaveFile_Serialize](../functions/SaveFile_Serialize.md) | `0x1400C2598` | Describes the top level of a save file: the list of sections and which schema fills each. |
| [SaveGameFlow_Serialize](../functions/SaveGameFlow_Serialize.md) | `0x1400BFD78` | Describes the game-flow record: progress with its flag, and the bonus items. |
| [SaveGameProgress_Serialize](../functions/SaveGameProgress_Serialize.md) | `0x1400BF970` | Describes story progress and the game flag. |
| [SaveHeader_FillBattleFields](../functions/SaveHeader_FillBattleFields.md) | `0x1402D0108` | Fills the battle-specific fields of the autosave payload header: the kind, the place bytes and the unit preview records the resume screen reads. |
| [SaveIdPair_Serialize](../functions/SaveIdPair_Serialize.md) | `0x1400B8584` | Describes a small record with a second id (`id2`). |
| [SaveInfo_Serialize](../functions/SaveInfo_Serialize.md) | `0x1400B83D8` | Describes the `info` section: a header, a checksum, the play time, and the slot summary. |
| [SaveIsNew_Serialize](../functions/SaveIsNew_Serialize.md) | `0x1400B734C` | Describes a one-flag record: an `is_new` marker. |
| [SaveItemOpened_Serialize](../functions/SaveItemOpened_Serialize.md) | `0x1400BFB98` | Describes an item entry that wraps an exists/opened flag pair. |
| [SaveJobNew_Serialize](../functions/SaveJobNew_Serialize.md) | `0x1400C138C` | Describes the saved job-new record: which jobs the player has not yet looked at, and a disable flag. |
| [SaveKeyNew_Serialize](../functions/SaveKeyNew_Serialize.md) | `0x1400C1CBC` | Describes a keyed entry with new and arrival flags. |
| [SaveLatestKey_Serialize](../functions/SaveLatestKey_Serialize.md) | `0x1400C1F7C` | Describes the latest-key marker. |
| [SaveLibrary_Serialize](../functions/SaveLibrary_Serialize.md) | `0x1400C2020` | Describes the library menu state: zodiac stones, books, journal, glossary, world situation and the unlock flag. |
| [SaveLoadList_BuildEntries](../functions/SaveLoadList_BuildEntries.md) | `0x140185D1C` | Builds the ENHANCED save/load list: one 240-byte entry per cache slot whose magic is `SC`, then sorts the entry vector. |
| [SaveLoadList_FillItem](../functions/SaveLoadList_FillItem.md) | `0x1401864A4` | Fills one save/load list item from an entry: slot number, level, location, next event, date, play time, clear / auto marks, and registers the four preview sprites. |
| [SaveMarkerTown_Serialize](../functions/SaveMarkerTown_Serialize.md) | `0x1400C0698` | Describes the marker town record. |
| [SaveMenuNewA_Serialize](../functions/SaveMenuNewA_Serialize.md) | `0x1400BFEC8` | Describes one menu's new-entry marker (`menu_new`). |
| [SaveMenuNewB_Serialize](../functions/SaveMenuNewB_Serialize.md) | `0x1400C00D0` | Describes another menu's new-entry flags (`menu_new`). |
| [SaveMenuNewC_Serialize](../functions/SaveMenuNewC_Serialize.md) | `0x1400C01A0` | Describes a third menu's new-entry flags (`menu_new`). |
| [SaveMenuNewLast_Serialize](../functions/SaveMenuNewLast_Serialize.md) | `0x1400BFF98` | Describes a menu's new-entry flags and the last selected menu index. |
| [SaveMoukeState_Serialize](../functions/SaveMoukeState_Serialize.md) | `0x1400B8EDC` | Describes a day-counted record: flag, number, current and maximum day, town and unit count and number. |
| [SaveNewArrival_Serialize](../functions/SaveNewArrival_Serialize.md) | `0x1400B7504` | Describes a one-flag record: an `is_newarrival` marker. |
| [SaveNewArrivalListA_Serialize](../functions/SaveNewArrivalListA_Serialize.md) | `0x1400C1B1C` | Describes a new-arrival list entry. |
| [SaveNewArrivalListB_Serialize](../functions/SaveNewArrivalListB_Serialize.md) | `0x1400C1BEC` | Describes a second new-arrival list entry. |
| [SaveNewArrivalSub_Serialize](../functions/SaveNewArrivalSub_Serialize.md) | `0x1400C1E40` | Describes a new-arrival entry with a sub-key. |
| [SaveNewFlags_Serialize](../functions/SaveNewFlags_Serialize.md) | `0x1400B73F0` | Describes a two-flag record: `is_new` and `is_newarrival`. |
| [SaveOpenedFlag_Serialize](../functions/SaveOpenedFlag_Serialize.md) | `0x1400BFA84` | Describes an exists/opened flag pair. |
| [SavePageState_Serialize](../functions/SavePageState_Serialize.md) | `0x1400B8698` | Describes the state of a scripted page or scene: its data table, address, flags, page and step, work value, book number and page, picture and position, music number, effect mode and ambient sound. |
| [SaveShopPoach_Serialize](../functions/SaveShopPoach_Serialize.md) | `0x1400BCDBC` | Describes shop and poach item bookkeeping: the shop new flag, the poach item count, obtain order, sort order and new flags. |
| [SaveSlot_BuildClassicTitle](../functions/SaveSlot_BuildClassicTitle.md) | `0x14021C07C` | Builds the CLASSIC-mode slot title text: hero name, job name, level, date and location, in the classic text encoding. |
| [SaveSlot_LoadToLive](../functions/SaveSlot_LoadToLive.md) | `0x1400C45A0` | Loads one save slot: copies it from the RAM cache into the work copy and unpacks it into the live arrays. |
| [SaveSlot_WriteFromLive](../functions/SaveSlot_WriteFromLive.md) | `0x1400C4420` | Writes one save slot: packs the live state into the work copy and copies it into the 50-slot RAM cache. |
| [SaveSlots_LoadFromFile](../functions/SaveSlots_LoadFromFile.md) | `0x1400C3B24` | Loads the `fftsave.bin` entry from the save container into the manager's image (the slot cache is filled from it by sub_1402185A4). |
| [SaveSlots_StoreToFile](../functions/SaveSlots_StoreToFile.md) | `0x1400C39A0` | Copies the slot cache (0x1EA488 bytes = 50 x 40164) into the manager's image and queues it as the `fftsave.bin` entry of the save container. |
| [SaveSortie_Serialize](../functions/SaveSortie_Serialize.md) | `0x1400C03C0` | Describes sortie routing: the town and route to avoid, the last route, the restart goal town, and the reserved last town and route. |
| [SaveSummary_Serialize](../functions/SaveSummary_Serialize.md) | `0x1400B7C4C` | Describes the save-slot summary the load menu shows: hero name, job, level, date, play progress, difficulty and new-game-plus state. |
| [SaveUnit_Serialize](../functions/SaveUnit_Serialize.md) | `0x1400B99BC` | Describes one saved unit (character) record: it builds a table of 108 field descriptors and runs FieldSchema_Run over it. |
| [SaveUnitJobInfo_Serialize](../functions/SaveUnitJobInfo_Serialize.md) | `0x1400C14CC` | Describes the unit job and guide record: the unit job, the info-guide flags and the skin colour offset. |
| [SaveUnlockProgress_Serialize](../functions/SaveUnlockProgress_Serialize.md) | `0x1400C169C` | Describes unlock progress: unlocked and progress values, poach item type, summon, geomancy, song and iaido types and the dance turn count. |
| [SaveUwasaMouke_Serialize](../functions/SaveUwasaMouke_Serialize.md) | `0x1400C0270` | Describes the rumor and Mouke menu records (`uwasa` and `mouke`). |
| [SaveWalkRoute_Serialize](../functions/SaveWalkRoute_Serialize.md) | `0x1400C073C` | Describes the world-map walking route: flags, route number, step counters and maxima, costs, start and end towns, rotation, a stack buffer and two points. |
| [SaveWork_CopyErrandState](../functions/SaveWork_CopyErrandState.md) | `0x14027966C` | Copies the party-wide status masks, the errand arrays and the active errand slot records between a save work block and the live globals, in the direction the second argument selects. |
| [SaveWork_ImportLegacyHeader](../functions/SaveWork_ImportLegacyHeader.md) | `0x14038E330` | (I) Imports a legacy PSP save header into the work copy: writes the summary bytes +274..+286. |
| [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md) | `0x140218F78` | Fills the save work copy (`g_SaveWorkCurrent`, 40164 bytes) from the live game state: slot summary, four preview sprite records, the 54 live 600-byte unit records and the other tables. |
| [SaveWork_PackFromParty](../functions/SaveWork_PackFromParty.md) | `0x14021B070` | Chooses the leader for the slot summary and packs the live state: the first party unit whose kind byte (+114) is 1..3, falling back to unit 0. |
| [SaveWork_Serialize](../functions/SaveWork_Serialize.md) | `0x1400C2C40` | Describes the `saveWork` record. |
| [SaveWork_UnpackToLive](../functions/SaveWork_UnpackToLive.md) | `0x14021B0E8` | Reverse of SaveWork_PackFromLive: copies the save work copy into the live arrays: 54 unit records of 600 bytes into `g_UnitSaveData`, then the item and flag tables. |
| [SaveWork_UnpackToLive_Repair](../functions/SaveWork_UnpackToLive_Repair.md) | `0x14021DE98` | (I) A second unpack variant that copies the work copy to the live arrays and re-derives the ability flags from the JobTable and the skillset table. |
| [SaveWorld_Serialize](../functions/SaveWorld_Serialize.md) | `0x1400BD078` | Describes the world part of a save: the 54 unit slots and the party item, shop, found-item, event and sort lists. |
| [SaveWorldEvents_Serialize](../functions/SaveWorldEvents_Serialize.md) | `0x1400B9228` | Describes world-map event counters and dates: treasure and unregistered find days, delay and finish days, page and static flags, the year of a person, and the event list. |
| [SaveWorldMap_Serialize](../functions/SaveWorldMap_Serialize.md) | `0x1400C0FDC` | Describes the world-map state: map menu, deep dungeon, bar, sortie, map and walk info. |
| [sub_140025D74](../functions/sub_140025D74.md) | `0x140025D74` | Computes the CRC-32 checksum the save format stores in every entry header: the manual-slot payload, the resume entries and the settings block are all sealed with it. |
| [sub_14002BA44](../functions/sub_14002BA44.md) | `0x14002BA44` | Builds and probes the console save thumbnail path, `system/savedata/ICON0.PNG`, and mounts or opens the save folder that would hold it. |
| [sub_140033CBC](../functions/sub_140033CBC.md) | `0x140033CBC` | Asks the save-file object for one named container entry: it builds a request that carries both the requesting object and the entry name, and queues it so the delivery path can fill the requester's buffer and size later. |
| [sub_140033DA4](../functions/sub_140033DA4.md) | `0x140033DA4` | The attach check: compares the CRC word the entry header carries with the checksum of the payload that was just inflated, and refuses the entry when they differ. |
| [sub_140033DF0](../functions/sub_140033DF0.md) | `0x140033DF0` | The generic entry dispatcher: takes one inflated container entry, copies its 16-byte header into the file object, and hands the payload, size and version to the object's own handler. |
| [sub_1400348F8](../functions/sub_1400348F8.md) | `0x1400348F8` | The boot "has any save" probe: asks whether the manual, the autosave and the system containers exist and remembers the answers on the manager so the title knows whether to offer a load or a continue. |
| [sub_140034C64](../functions/sub_140034C64.md) | `0x140034C64` | Kicks the container write state machine for one area name: it hands the file object the area whose queued entries should be packed and written. |
| [sub_140034CF0](../functions/sub_140034CF0.md) | `0x140034CF0` | Kicks the container read state machine for one area name, which makes the pending entry requests for that area get looked up, inflated and delivered. |
| [sub_140034D7C](../functions/sub_140034D7C.md) | `0x140034D7C` | The container writer: a multi-state machine that re-reads the existing PNG, adopts every entry it did not queue itself, rebuilds the `UMIF` header and entry table, deflates each entry and writes the picture back. |
| [sub_140035A28](../functions/sub_140035A28.md) | `0x140035A28` | Walks the `UMIF` entry table of a freshly read container: validates the header, descrambles the entry names and keeps one record per entry for the lookup that follows. |
| [sub_140036064](../functions/sub_140036064.md) | `0x140036064` | Finds one entry in the container's entry list by name, inflates it and returns its record; it is the name lookup the loader uses for `fftsave.bin`, `settings.sav` and every resume entry. |
| [sub_1400366B0](../functions/sub_1400366B0.md) | `0x1400366B0` | Answers whether the container file for one area name exists, formatting the path against the save root selected by its second argument. |
| [sub_140036724](../functions/sub_140036724.md) | `0x140036724` | The legacy per-slot probe: scans numbered container names `0001.png` through `0050.png` in one save root and reports whether any of them exists. |
| [sub_1400367F4](../functions/sub_1400367F4.md) | `0x1400367F4` | The mount machine: a six-state routine that creates the save folder, then probes, opens and if necessary deletes the containers the game knows about (`AUTOENHANCED`, the numbered set `0001` to `0005`, and `SYSTEM`). |
| [sub_140036AE0](../functions/sub_140036AE0.md) | `0x140036AE0` | Opens one area container for reading: it checks the parent-folder candidate exists, then prefers the Steam-id subfolder copy and falls back to the parent folder when only that one exists. |
| [sub_140036BD4](../functions/sub_140036BD4.md) | `0x140036BD4` | Deletes the container file of one area: it formats the `%s%s.png` name and removes it through the file layer. |
| [sub_140036D8C](../functions/sub_140036D8C.md) | `0x140036D8C` | Writes the finished container into a PNG: it creates the picture, adds the private chunk that holds the container body, and saves it under the formatted `%s.png` name. |
| [sub_14006B144](../functions/sub_14006B144.md) | `0x14006B144` | Builds the save folder path once at startup: Documents, the game folder, the profile part and the Steam account id, then creates it. |
| [sub_14006BA2C](../functions/sub_14006BA2C.md) | `0x14006BA2C` | Returns one of the two save-root strings held on the manager, selected by index: the primary root or the fallback root without the Steam id. |
| [sub_14006E5DC](../functions/sub_14006E5DC.md) | `0x14006E5DC` | Resolves the user's Documents folder through the shell and returns it as the base for the save path. |
| [sub_1400B5E24](../functions/sub_1400B5E24.md) | `0x1400B5E24` | Applies a changed option block and asks for the settings container to be written. |
| [sub_1400C2ED8](../functions/sub_1400C2ED8.md) | `0x1400C2ED8` | The manual-slot handler: for a version-14 `fftsave.bin` entry it verifies the CRC and the exact payload size, then copies the whole 50-slot image into the save object. |
| [sub_1400C30BC](../functions/sub_1400C30BC.md) | `0x1400C30BC` | Stores a freshly built payload into one resume group: it frees the group's previous buffer, allocates the new size, copies the bytes and marks the group ready. |
| [sub_1400C3140](../functions/sub_1400C3140.md) | `0x1400C3140` | Turns one ready buffer into a named container entry: it seals the buffer with a CRC, queues it under the given name with version 17 and marks the object clean. |
| [sub_1400C3B84](../functions/sub_1400C3B84.md) | `0x1400C3B84` | The per-frame resume flush: it turns every dirty resume group into named entries, rotates the three-point ring and kicks the autosave container write. |
| [sub_1400C3DBC](../functions/sub_1400C3DBC.md) | `0x1400C3DBC` | Walks the resume name-to-record map and queues every dirty record as a container entry, erasing each record as it goes. |
| [sub_1400C3ED8](../functions/sub_1400C3ED8.md) | `0x1400C3ED8` | Packs one resume record under a given name: it ensures a map record exists for the name, copies the group's buffer into it, clears the group's ready byte and queues the entry. |
| [sub_1400C4198](../functions/sub_1400C4198.md) | `0x1400C4198` | Prepares and queues one named resume entry: formats the entry name from a part and a point, then hands the group to the packer. |
| [sub_1400C4214](../functions/sub_1400C4214.md) | `0x1400C4214` | Requests one resume point from the autosave container: the main part always, and optionally the world, attack and fturn parts, then kicks the read. |
| [sub_1400C42E0](../functions/sub_1400C42E0.md) | `0x1400C42E0` | Requests one named resume entry from the autosave container: it formats the name for a part and a point and queues the request on the group object. |
| [sub_1400C4360](../functions/sub_1400C4360.md) | `0x1400C4360` | Builds a resume entry name from a part index and a point index: `resume_enNN_<part>.sav`, `resume_enwm_main.sav` or `resume_enbtl_<part>.sav`. |
| [sub_1400C43D8](../functions/sub_1400C43D8.md) | `0x1400C43D8` | Returns the payload buffer and length of one part of the current resume point, so the Continue path can read the header without a copy. |
| [sub_1400C4690](../functions/sub_1400C4690.md) | `0x1400C4690` | The resume-order state machine: it walks the three-point ring at boot, requests each point's parts and keeps the newest three points in order. |
| [sub_1400C480C](../functions/sub_1400C480C.md) | `0x1400C480C` | The world-map save step: it flushes any ready resume record and, only when something was queued, kicks the autosave container write. |
| [sub_1400C6008](../functions/sub_1400C6008.md) | `0x1400C6008` | Fills a 50-slot save image with the empty-slot pattern, so a missing or rejected file reads as 50 empty slots instead of stale bytes. |
| [sub_140183658](../functions/sub_140183658.md) | `0x140183658` | The world-map screen's update callback, in two modes: build and show the map panel, or trigger the world-map save. |
| [sub_14018373C](../functions/sub_14018373C.md) | `0x14018373C` | The load screen's resume-header table: it builds the small object that holds one summary per resume point and fills one entry from each delivered resume payload. |
| [sub_1401839E4](../functions/sub_1401839E4.md) | `0x1401839E4` | The load-confirmation handler: it takes the selected slot, asks for its resume parts, loads the slot into the live state and, when the slot was saved in a battle, starts the resume path instead of a plain load. |
| [sub_140183C38](../functions/sub_140183C38.md) | `0x140183C38` | The save-confirmation handler: it writes the chosen slot from live state, then updates the screen and plays the confirmation cue. |
| [sub_140183DD4](../functions/sub_140183DD4.md) | `0x140183DD4` | Deletes one manual save slot: it fills the slot's 40,164-byte work copy with the empty pattern, copies it into the cache and marks the cache dirty. |
| [sub_14018403C](../functions/sub_14018403C.md) | `0x14018403C` | The load-screen setup callback: in mode 0 it reads the whole manual-save container, and in mode 1 it advances the screen when there is something to show. |
| [sub_1401E7EF8](../functions/sub_1401E7EF8.md) | `0x1401E7EF8` | Probes the SYSTEM save area for `settings.sav` while the title and continue paths set themselves up, and applies what it reads. |
| [sub_140217EF8](../functions/sub_140217EF8.md) | `0x140217EF8` | Builds one resume payload in scratch memory: header, work copy or battle snapshot, and the YOX image page. |
| [sub_1402181EC](../functions/sub_1402181EC.md) | `0x1402181EC` | Materialises a resume payload: it copies the body back into the live buffers, restores the control words and inflates the image page. |
| [sub_14021849C](../functions/sub_14021849C.md) | `0x14021849C` | Validates a resume payload's header and copies its summary fields into the auto slot. |
| [sub_1402185A4](../functions/sub_1402185A4.md) | `0x1402185A4` | The save frame step: it runs one of store, load or image-to-cache per frame, according to the manager's command. |
| [sub_140218728](../functions/sub_140218728.md) | `0x140218728` | Loads all fifty slots into the caller's buffer, through the PNG path or the legacy per-slot files. |
| [sub_140218C04](../functions/sub_140218C04.md) | `0x140218C04` | Copies a freshly loaded flat image into the slot cache. |
| [sub_14021A030](../functions/sub_14021A030.md) | `0x14021A030` | The classic save/load menu: it lists the slots, maps slot 0 to the auto slot, and runs the save or load step. |
| [sub_14021AEC0](../functions/sub_14021AEC0.md) | `0x14021AEC0` | The classic-mode save step: it packs the live party into the work copy and writes the chosen slot. |
| [sub_14021BD04](../functions/sub_14021BD04.md) | `0x14021BD04` | Builds the classic save menu's slot list, one title card per valid slot. |
| [sub_14021C620](../functions/sub_14021C620.md) | `0x14021C620` | The classic load menu: it reads the chosen card, imports the header and materialises the run. |
| [sub_140245B7C](../functions/sub_140245B7C.md) | `0x140245B7C` | Maps classic list slot 0 to the auto slot record and moves the 0x9CE4 bytes between them. |
| [sub_140245C84](../functions/sub_140245C84.md) | `0x140245C84` | Clears every stored slot to the empty-slot pattern. |
| [sub_140246014](../functions/sub_140246014.md) | `0x140246014` | Moves the 0x9CE4-byte slot record between the work copy and the checkpoint copy: a non-zero second argument copies the checkpoint back into the work copy; zero builds the work copy from the party and stores it in the ... |
| [sub_140257074](../functions/sub_140257074.md) | `0x140257074` | Builds the capture handler object and installs the autosave writer stub in it. |
| [sub_140257354](../functions/sub_140257354.md) | `0x140257354` | The single resume entry point: it reads the part selector, imports the header and hands over to the materialiser. |
| [sub_14025FC38](../functions/sub_14025FC38.md) | `0x14025FC38` | Copies rows into the 16-bit image page stored in the battle payload. |
| [sub_1402CEEE8](../functions/sub_1402CEEE8.md) | `0x1402CEEE8` | The checkpoint writer: it builds a fresh work copy of the party, stores it in the checkpoint copy, and then overwrites the checkpoint copy's unit area and many other fields with the live state, so the checkpoint holds... |
| [sub_1402CF768](../functions/sub_1402CF768.md) | `0x1402CF768` | The reverse of the slot-record builder: it takes the work copy and writes its sections back into live state, including the ten item order lists. |
| [sub_140327004](../functions/sub_140327004.md) | `0x140327004` | Moves the ten item order lists between a work record and the live arrays, in either direction. |

## Structures (13)

| Name | Size (bytes) | Summary |
|---|---|---|
| [BattleSnapshot](../structs/BattleSnapshot.md) | 668112 | The 668,112-byte battle image a kind-1 resume entry carries, as the capture builds it in g_BattleState: a battle context, five blocks (A..E), the 21 x 512-byte unit records and 3,000 more bytes of scene-task state. |
| [ClassicLoadWindowDefaultRecord](../structs/ClassicLoadWindowDefaultRecord.md) |  | One row of the ClassicLoadWindowDefault table. |
| [ClassicSaveListLanguage0Record](../structs/ClassicSaveListLanguage0Record.md) | 176 | One row of the ClassicSaveListLanguage0 table. |
| [ClassicSaveWindowALanguage0Record](../structs/ClassicSaveWindowALanguage0Record.md) |  | One row of the ClassicSaveWindowALanguage0 table. |
| [ClassicSaveWindowAOtherLanguagesRecord](../structs/ClassicSaveWindowAOtherLanguagesRecord.md) |  | One row of the ClassicSaveWindowAOtherLanguages table. |
| [ClassicSaveWindowBLanguage0Record](../structs/ClassicSaveWindowBLanguage0Record.md) |  | One row of the ClassicSaveWindowBLanguage0 table. |
| [ClassicSaveWindowBOtherLanguagesRecord](../structs/ClassicSaveWindowBOtherLanguagesRecord.md) |  | One row of the ClassicSaveWindowBOtherLanguages table. |
| [SaveBlockUiMarks](../structs/SaveBlockUiMarks.md) | 7780 | The parts of the save block behind qword_143CD9DC8 that hold the 'new' marks and the current position of the Zodiac Stone, Chronicle, Events and glossary screens. |
| [SaveEquipSet](../structs/SaveEquipSet.md) | 88 | One saved equipment set of a unit (three per unit record). |
| [SaveErrorMessage](../structs/SaveErrorMessage.md) | 8 | One row of the SaveErrorMessages table. |
| [SaveFieldDescriptor](../structs/SaveFieldDescriptor.md) | 88 | One field of a saved record, as the save walker reads it (built on the stack by each schema function). |
| [SaveManager](../structs/SaveManager.md) |  | The two singletons the save path runs on, with the fields it uses: the save-I/O state object that holds the frame step's command and sub-state, and the save manager object that holds the 50-slot image the `fftsave.bin... |
| [SaveRequestRecord](../structs/SaveRequestRecord.md) | 328 | One queued file request of the save container manager: the consumer object, the entry name, the delivery buffer and its status. |

## Globals (8)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_ConfigData](../globals/g_ConfigData.md) | `0x140C69690` | `void *` | The loaded config object; the settings record of ConfigSettings_Serialize starts 16 bytes in: byte +55 forwardEnabledType (0 enable, 1 disable, 2 disable in story scenes), byte +59 enableEventKeepAuto. |
| [g_SaveAutoSlot](../globals/g_SaveAutoSlot.md) | `0x142E75DF8` | `uint8[40164]` | The auto-slot record, one 0x9CE4-byte slot. |
| [g_SaveBattleSnapshot](../globals/g_SaveBattleSnapshot.md) | `0x1408167A0` | `uint8[668112]` | The battle snapshot buffer: 668,112 bytes of sparse live battle state (unit table, tile table, scene-task records, action state) captured for a kind-1 resume payload. |
| [g_SaveCheckpointCopy](../globals/g_SaveCheckpointCopy.md) | `0x142E80450` | `uint8[72564]` | The checkpoint copy: 40,164 bytes of slot record whose unit area (offset 0x518) is overwritten with the live unit save data by the checkpoint writer sub_1402CEEE8, followed by further live fields. |
| [g_SaveRequestManager](../globals/g_SaveRequestManager.md) | `0x140C69698` | `void *` | The save-data request object the slot, settings and PNG code queues work on. |
| [g_SaveSlotCache](../globals/g_SaveSlotCache.md) | `0x142C8B970` | `uint8[2008200]` | The fifty-slot image in memory: 50 records of 0x9CE4 bytes, the same bytes the PNG container carries. |
| [g_SaveWorkCurrent](../globals/g_SaveWorkCurrent.md) | `0x142C81C80` | `uint8[40164]` | The live work copy of the running game, one 0x9CE4-byte slot record. |
| [g_SaveYoxPage](../globals/g_SaveYoxPage.md) | `0x142FF9F90` | `uint8[1048576]` | The 1 MB 16-bit image page carried after a battle snapshot. |

## File formats (4)

| Name | Extension | Summary |
|---|---|---|
| [BattleResumeImage](../formats/BattleResumeImage.md) | `.sav` | The payload of a resume entry of `autoenhanced.png`. |
| [ManualSaveEntry](../formats/ManualSaveEntry.md) | `.bin` | The `fftsave.bin` entry of `enhanced.png` (and of `classic.png`): one flat image of the 50-slot save cache, 50 x 40,164 bytes behind a 16-byte header. |
| [ResumeEntry](../formats/ResumeEntry.md) | `.sav` | One entry of `autoenhanced.png`: a 16-byte entry header, a 340-byte payload header, then a body that is either the 40,164-byte save work copy (kind 0, the world and main form) or a 668,112-byte battle snapshot followe... |
| [SavePngContainer](../formats/SavePngContainer.md) | `.png` | A game save file: an ordinary PNG whose private `ffTo` chunk carries a `UMIF` container. |

## Flows (3)

| Name | Summary |
|---|---|
| [AutoSaveRead](../flows/AutoSaveRead.md) | How a resume entry reaches the game: the reader queues one request per entry name, a single read kick mounts the container, and the delivery function hands each entry to its object, where the header is validated and t... |
| [AutoSaveWrite](../flows/AutoSaveWrite.md) | Where a resume entry comes from and when it is written: the per-frame flush turns dirty group buffers into named entries, stamps each with a CRC, and one write kick sends the whole container. |
| [SaveFrameStep](../flows/SaveFrameStep.md) | How a manual save or load reaches the file: the save screen changes a command, and one frame step does the work once per frame, blocking that frame while the container is read or written. |

## Observed behaviours (6)

| Name | Scope | Summary |
|---|---|---|
| [AnUnservedIdFromASaveFreezesTheGame](../behaviors/AnUnservedIdFromASaveFreezesTheGame.md) | loading a save whose item ids have no row | The game trusts every id in a save: an equipped item with no item row reaches the unit stat builder, which reads the armor record it does not get and faults inside a game task, freezing the game. |
| [BattleLoadWritesThePartyBackToTheSaveRecords](../behaviors/BattleLoadWritesThePartyBackToTheSaveRecords.md) | loading a story battle from the world map | While a battle loads, the game writes every party work record back into its save record (PartyUnit_WriteBackToSave once per party slot, 0 to 6 with a party of seven). |
| [BattleRetriesRestoreTheirOwnCapture](../behaviors/BattleRetriesRestoreTheirOwnCapture.md) | the battle System Menu's Retry choices | Both Retry choices rebuild the battle from a battle capture, not from the battle as it stands: 'Change Formation and Retry' restores a capture taken after the battle's own units were built and before any party unit jo... |
| [CheckpointCopyHoldsTheLiveUnitRecords](../behaviors/CheckpointCopyHoldsTheLiveUnitRecords.md) | the checkpoint copy of the slot record (g_SaveCheckpointCopy) | The checkpoint writer packs the party into the work copy, copies the work copy to the checkpoint copy, and then overwrites the checkpoint copy's unit area with the live unit records. |
| [ResumedBattleRestoresUnitRecordsWithoutUnpack](../behaviors/ResumedBattleRestoresUnitRecordsWithoutUnpack.md) | resuming a battle from an autosave: where the live unit records come from | A battle resumed from an autosave gets its live unit records (g_UnitSaveData) from the battle snapshot region through Battle_RestoreSceneVars, and SaveWork_UnpackToLive does not run for it: the resume entry unpacks on... |
| [SaveCardJobIsTheLeadersPartyJobWordLowByte](../behaviors/SaveCardJobIsTheLeadersPartyJobWordLowByte.md) | a manual save's slot card | The slot card's job byte (slot image +274) is the low byte of the leader's 16-bit party job word: SaveWork_PackFromParty picks the first party unit whose marker (+114) is 1..3 and passes its word +36 to SaveWork_PackF... |

## Tables (10)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [ClassicLoadWindowDefault](../tables/ClassicLoadWindowDefault.md) | Executable (initialised data, written at run time) |  | ? | Window template and live fields of the classic load menu, one of three language variants. |
| [ClassicSaveListLanguage0](../tables/ClassicSaveListLanguage0.md) | Executable (initialised data, written at run time) |  | 1 rows of 176 bytes | Template and cursor of the classic save list, language 0 variant. |
| [ClassicSaveWindowALanguage0](../tables/ClassicSaveWindowALanguage0.md) | Executable (initialised data) |  | 1 bytes | Classic save / load menu window template A, language 0. |
| [ClassicSaveWindowAOtherLanguages](../tables/ClassicSaveWindowAOtherLanguages.md) | Executable (initialised data) |  | 1 bytes | Classic save / load menu window template A, other languages. |
| [ClassicSaveWindowBLanguage0](../tables/ClassicSaveWindowBLanguage0.md) | Executable (initialised data) |  | 1 bytes | Classic save / load menu window template B, language 0. |
| [ClassicSaveWindowBOtherLanguages](../tables/ClassicSaveWindowBOtherLanguages.md) | Executable (initialised data) |  | 1 bytes | Classic save / load menu window template B, other languages. |
| [ResumeKindNames](../tables/ResumeKindNames.md) | Executable |  | 4 rows of 8 bytes (the run continues with two more string pointers) | Short names of the four kinds of a resume (suspend) save entry: main, world, attack, fturn. |
| [SaveErrorMessages](../tables/SaveErrorMessages.md) | Executable |  | 48 rows of 8 bytes | Result code of the save-data layer to message number for the save and load screens. |
| [SaveFieldDescriptorLists](../tables/SaveFieldDescriptorLists.md) | Executable (built on the stack by code) |  | 11 / 108 / 76 / 2 descriptors of 88 bytes | The save schema: every saved record type has a function that builds an array of 88-byte field descriptors on the stack and hands it to FieldSchema_Run. |
| [UnitSaveSlots](../tables/UnitSaveSlots.md) | Executable (filled at run time) |  | 54 records of 600 bytes | The live unit save table: the units as the save keeps them. |
