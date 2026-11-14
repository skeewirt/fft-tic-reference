# Structures

Runtime records: objects and blocks the game keeps in memory, field by field, with who writes and who reads each field.

67 records. Format of a record: [kinds/struct.json](../../kinds/struct.json). Data: [data/structs.jsonl](../../data/structs.jsonl).

| Name | Size (bytes) | Area | Summary |
|---|---|---|---|
| [AbilityListRow](AbilityListRow.md) | 8 | [Job list and unlock](../areas/job-list.md) | One 8-byte row of the job screen's ability page: word 0 job id, word 1 ability id with flag bits; the list ends with {0, 0xFFFF}. |
| [ActionEntryWord](ActionEntryWord.md) | 2 | [Battle](../areas/battle.md) | The 16-bit word of a four-byte action entry (the AI and preview form): the action id in bits 0..9 and the acting unit slot in bits 10..15. |
| [ActionResult](ActionResult.md) | 48 | [Battle](../areas/battle.md) | The result of one action on one target, filled by the formula handler and read by the result applier, the preview and the messages. |
| [AiCommandEntry](AiCommandEntry.md) | 4 | [Battle](../areas/battle.md) | One candidate action of the AI's command table: the ability word (id \| unit slot << 10), the command (skillset) byte it comes from and a flag byte. |
| [AtlasShelf](AtlasShelf.md) | 16 | [Graphics](../areas/graphics.md) | The state of one layer atlas allocator (a shelf / row packer): the cursor in the current row, the start of the row, the height of the row and the page. |
| [BattleMsgDescriptor](BattleMsgDescriptor.md) | 16 | [Battle](../areas/battle.md) | The 4-dword descriptor the banner takes: class, subtype, kind and a message word. |
| [BattleMsgEntry](BattleMsgEntry.md) | 524 | [Battle](../areas/battle.md) | One slot of the battle message store: the kind, the kind-dependent argument, a message id and a 512-byte text buffer. |
| [BattleMsgRecord](BattleMsgRecord.md) |  | [Battle](../areas/battle.md) | The record the message object holds at +8: the values the argument filler reads for a message. |
| [BattlePanelHandWord](BattlePanelHandWord.md) | 2 | [Battle](../areas/battle.md) | One hand word as the flag-aware panels read it: the item id in bits 0..8 and a two-bit value in bits 14..15. |
| [BattleRangeMarkRecord](BattleRangeMarkRecord.md) | 5 | [Battle](../areas/battle.md) | One record of g_BattleRangeMarks, parallel to BattleTileRecord (512 records, layer 1 at +0x500). |
| [BattleSnapshot](BattleSnapshot.md) | 668112 | [Save data](../areas/save-data.md) | The 668,112-byte battle image a kind-1 resume entry carries, as the capture builds it in g_BattleState: a battle context, five blocks (A..E), the 21 x 512-byte unit records and 3,000 more bytes of scene-task state. |
| [BattleTileRecord](BattleTileRecord.md) | 8 | [Battle](../areas/battle.md) | One tile of the battle map in g_BattleTileTable: 256 records per layer, two layers (layer 1 at +0x800), index x + y * width. |
| [ClutBank](ClutBank.md) | 2450 | [Graphics](../areas/graphics.md) | One of the 14 banks of the palette manager (g_ClutManager, from +8): 16 rows of 16 colours with a timer per row, the state of every colour and the bank's base rows. |
| [CrystalRollResult](CrystalRollResult.md) | 1393 | [Battle](../areas/battle.md) | The block Unit_RollAbilityLearning fills at dword_1411A6AB0 (1393 bytes, the next data starts at 0x1411A7024) when a unit stops on a crystal or chest. |
| [EquipPanelBlock](EquipPanelBlock.md) | 64 | [Battle](../areas/battle.md) | A 64-byte copy of a party or battle record's bytes +0x30..+0x6F, kept at 0x141876E90 for the field equip screens and at 0x141D3B880 for the battle panels. |
| [EquipSetBlock](EquipSetBlock.md) | 64 | [Items and shops](../areas/items.md) | The equip screen's computed set at 0x141876C40: stat deltas at +0x00..+0x23, the five candidate equipment words at +0x24..+0x2D, a five-word display array at +0x2E..+0x37, and unclassified words at +0x38..+0x3F. It is... |
| [ErrandActiveSlot](ErrandActiveSlot.md) | 9 | [Errands](../areas/errands.md) | One of the eight active errand slots at g_ErrandActive (9 bytes each, count g_ErrandActiveCount): a dispatch in progress or back, its errand, its days, the town it left from and up to three units. |
| [EventControl](EventControl.md) | 64 | [Event system](../areas/event-system.md) | ffto::Game::Event::EventControl (vtable 0x140713658), the singleton at g_EventControl: the event-script pause overlay and its hold-to-skip. |
| [FormatArgRecord](FormatArgRecord.md) | 264 | [Battle](../areas/battle.md) | One argument of a formatted UI text string: a 256-byte text area and a type dword at +0x100. |
| [FormulaBlock](FormulaBlock.md) | 72 | [Battle](../areas/battle.md) | The state of the one action being resolved: Battle_ResolveAction fills it per target and every formula handler reads and writes it. |
| [GlobalWork](GlobalWork.md) | 136 | [Application and startup](../areas/app-startup.md) | ffto::Game::GlobalWork (vtable 0x140713EA8), the singleton at g_GlobalWork. |
| [GUILayer](GUILayer.md) | 592 | [UI framework](../areas/ui-framework.md) | A UI layer: a component drawn offscreen and composited with its effects (mask, drop shadow, glow). |
| [GUINode](GUINode.md) | 224 |  | Size from the 224-byte free in GUILayerNode's destructor. |
| [GUINodeState](GUINodeState.md) | 208 | [UI framework](../areas/ui-framework.md) | One state (timeline) of a component: its clock, its loop range, its flags and the channel sets and entries it applies. |
| [GUINodeStateEntry](GUINodeStateEntry.md) | 64 | [UI framework](../areas/ui-framework.md) | One entry of a state's entry list (GUINodeState.entries): a jump marker, a trigger, a state link, a state reset or a part trigger, built from the state's special tracks by UIAnim_ApplyTrack and UIAnim_ApplyComponentTr... |
| [HdSheetGroup](HdSheetGroup.md) | 21144 | [Graphics](../areas/graphics.md) | One of the 20 sheet groups of the battle HD layer (g_HdSheetGroups): a sheet entry kept in memory and the textures cut from it, one per piece and palette. |
| [InputActionRow](InputActionRow.md) | 48 | [Input](../areas/input.md) | One action of the input module (g_InputModule + 1360 + 48 * action id, 256 rows; ids are UIKeyAssign keys): three 16-byte bindings, the pad button first, then two keys. |
| [InputStateAxes](InputStateAxes.md) | 1352 | [Input](../areas/input.md) | The analog part of the 0x548-byte input state that the UI listeners receive (copied whole by sub_1400EFB50 and by GUICore_OnInputState): four signed stick bytes, two trigger bytes and the button dwords. |
| [ItemListCells](ItemListCells.md) |  | [Battle](../areas/battle.md) | The static item-list cell store: 82 two-byte cells (kind tag in bits 15..11, id in bits 10..0) and the parallel per-cell arrays beside them. |
| [ItemNewFlagBlock](ItemNewFlagBlock.md) | 1007 | [Items and shops](../areas/items.md) | The block at g_ItemNewFlags: the shop new-item flags first, then the four Poachers' Den (poach) arrays. |
| [ItemOrderLists](ItemOrderLists.md) |  | [Items and shops](../areas/items.md) | The ten saved item order lists: 16-bit words in static storage, no header and no length word. |
| [ItemRecord](ItemRecord.md) | 12 | [Items and shops](../areas/items.md) | The 12-byte record of an item (Item_GetRecord): icon, level, equipment slot bits, equipment category, attribute index, price and the story progress it is sold from. |
| [ItemWeaponRecord](ItemWeaponRecord.md) | 8 | [Items and shops](../areas/items.md) | The 8-byte weapon sub-record of an item whose category kind is 0 or 5 (sub_1402B8C74). |
| [JobChangeListAddon](JobChangeListAddon.md) | 19024 | [Job data](../areas/job-data.md) | The Change Job list screen object (the list addon, reached as [[[root]+0x10]+0x58]+0x78 and as field 15 of the screen object): 19 cell records of 148 bytes, 19 cell gadgets of 256 bytes, and the cursor state; every ar... |
| [JobListWord](JobListWord.md) | 2 | [Job list and unlock](../areas/job-list.md) | One entry of g_RuntimeJobList: the job id in bits 0..9, bit 13 locked (not unlocked by any party member) and bit 14 current job. |
| [JobRecord](JobRecord.md) | 148 |  | Only the listed offsets are verified; the rest of the 148 bytes is copied wholesale. |
| [JobTreeAddon](JobTreeAddon.md) | 13312 |  | STOCK layout (20 panels). |
| [JobTreePanel](JobTreePanel.md) | 456 |  | Stride 456 bytes (stock: 20 panels). |
| [KeyTrack](KeyTrack.md) |  | [UI framework](../areas/ui-framework.md) | A keyframe track of one property of one target: sorted keys, the first four stored inline. |
| [KeyTrackKey](KeyTrackKey.md) | 16 | [UI framework](../areas/ui-framework.md) | One keyframe: its frame, the curve that shapes the interval to the next key, and the value. |
| [LookPoolRecord](LookPoolRecord.md) | 13014 | [Graphics](../areas/graphics.md) | One of the 15 sprite records at 0x140D005A0 (stride 0x32D6) that hold the loaded graphics of a look; records are shared by every unit that has the same sprite number. |
| [LookQueueEntry](LookQueueEntry.md) | 32 | [Graphics](../areas/graphics.md) | One entry of the 16-entry load queue that Battle_BuildRosterTeam, Battle_AddJoinedUnit and the scene preview code fill (LookQueue_Add) and CharaPalette_ReloadForShape consumes; entry n starts at 0x141856728 + 32 * n, ... |
| [MenuListWord](MenuListWord.md) | 2 | [Items and shops](../areas/items.md) | One entry of g_MenuList, the array the shop, equip, item and ability screens reuse: the id in bits 0..9, bit 14 "cannot equip / cannot learn / current", and the list-kind-specific bits 12 and 13. |
| [MoveBlockerRecord](MoveBlockerRecord.md) | 7 | [Battle](../areas/battle.md) | One entry of g_MoveBlockers: another unit on the map as the move-range builder sees it. |
| [MoveRangeScratch](MoveRangeScratch.md) | 128 | [Battle](../areas/battle.md) | The move-range builder's scratch block at g_MoveRangeScratch, filled by Battle_MoveRangeSetup from the unit record. |
| [MovieControl](MovieControl.md) | 32 | [UI framework](../areas/ui-framework.md) | ffto::Game::Movie::MovieControl (vtable 0x1407154B0), at g_MovieControl: pause overlay and hold-to-skip of a playing movie. |
| [MovieController](MovieController.md) |  | [UI framework](../areas/ui-framework.md) | ffto::Game::GameUI::MovieController (vtables 0x140702D20 and 0x140702D30): the movie host at *(qword_143CD9DC8) + 0xC8. |
| [NameSlotTable](NameSlotTable.md) |  | [Graphics](../areas/graphics.md) | A name-to-slot table of the render device (constant buffers, textures, samplers): names hashed into a tree, each with a dense slot id. |
| [NexResourceHandle](NexResourceHandle.md) | 168 | [Resource](../areas/resource.md) | The resource handle an nxd file is loaded through (NxdTable_CreateHandle; root.nxl uses the same layout with the NxlResourceHandle vtable): the common resource handle plus two callback pairs. |
| [NxdTable](NxdTable.md) | 80 | [Data access](../areas/data.md) | One table object of the nxd registry (NxdRegistry_LoadRootNxl allocates one per root.nxl line); NxdTable_BindRows fills its entries from the loaded file and every row lookup reads it. |
| [PartyHandWord](PartyHandWord.md) | 2 | [Items and shops](../areas/items.md) | One equipment slot of a party unit: the item id in bits 0..9 and bit 15 as the Outfitter-session pending flag. |
| [PartyUnitRecord](PartyUnitRecord.md) | 640 | [Unit data](../areas/unit-data.md) | A unit as the party, status and job screens read it (55 records at g_PartyUnitRecords, reached through g_PartyUnits). |
| [PostBattleCalc](PostBattleCalc.md) | 3400 | [Battle](../areas/battle.md) | The per-formula post-processing object of a battle: a virtual function table pointer and 106 rows of 32 bytes, one per formula id, that sub_14030A11C runs after a formula handler. |
| [PostBattleCalcRow](PostBattleCalcRow.md) | 32 | [Battle](../areas/battle.md) | One row of PostBattleCalc: an entry thunk, its argument, and the callback the thunk jumps to. |
| [RenderContext](RenderContext.md) | 6032 | [Graphics](../areas/graphics.md) | The per-thread draw state every pass fills before it packs a command: sort key, clip rectangle, render target, blend and raster words, vertex/index buffers and three binding tables (constant buffers, textures, sampler... |
| [Renderer](Renderer.md) |  | [Graphics](../areas/graphics.md) | The renderer object (global g_Renderer): output size, the render-target table and the per-type target slot tables, and the UI manager. |
| [SaveManager](SaveManager.md) |  | [Save data](../areas/save-data.md) | The two singletons the save path runs on, with the fields it uses: the save-I/O state object that holds the frame step's command and sub-state, and the save manager object that holds the 50-slot image the `fftsave.bin... |
| [SaveRequestRecord](SaveRequestRecord.md) | 328 | [Save data](../areas/save-data.md) | One queued file request of the save container manager: the consumer object, the entry name, the delivery buffer and its status. |
| [SceneUnitSlot](SceneUnitSlot.md) | 1352 | [Graphics](../areas/graphics.md) | One of the 16 scene-unit records at 0x140D30038 (stride 0x548) that sub_14026EB74 builds for a queued unit; the code addresses it by the pointer it returns, the in-use dword sits 8 bytes before that pointer (0x140D300... |
| [ShopEntry](ShopEntry.md) | 40 | [Items and shops](../areas/items.md) | One entry of a shop item list (buy, sell or equip), built per list index by ShopEntry_Fill from word_141811470 and drawn by ShopItemList_DrawRow. |
| [ShopRowCallbackTable](ShopRowCallbackTable.md) | 56 | [Items and shops](../areas/items.md) | The seven qword row handlers at 0x141876AD0..0x141876B00 that the list gadget calls per visible row; the shop, equip and item screens install different functions in the same slots. |
| [UIAddonFingerCursor](UIAddonFingerCursor.md) |  | [UI framework](../areas/ui-framework.md) | The finger cursor addon: the loaded cursor widget (ffto_finger_cursor.uib), the parts it moves, and the glide state of GUICursorHand_StepToward. |
| [UIAgentCursor](UIAgentCursor.md) |  | [UI framework](../areas/ui-framework.md) | The cursor agent: element 1 of the addon manager's agent vector (global qword_143CD9DA8, vector at +16). |
| [UIManager](UIManager.md) |  | [UI framework](../areas/ui-framework.md) | The UI manager object at Renderer.ui_manager: the shader selectors of the UI technique and the shared layer quad buffers. |
| [UIRender](UIRender.md) |  | [UI framework](../areas/ui-framework.md) | The UI render object (the command ring): the slot ids it resolved by name when it was created, used by every UI draw. |
| [UnitSaveRecord](UnitSaveRecord.md) | 600 | [Unit data](../areas/unit-data.md) | A unit as the save keeps it (54 records at g_UnitSaveData; copied whole into the save slot at +1304 + 600 n). |
| [UnitWorkRecord](UnitWorkRecord.md) | 512 | [Unit data](../areas/unit-data.md) | The working copy of a unit: the 21 battle units (g_BattleUnits) and temporary copies for previews and the job screens. |
