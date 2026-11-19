# Structures

Runtime records: objects and blocks the game keeps in memory, field by field, with who writes and who reads each field.

515 records. Format of a record: [kinds/struct.json](../../kinds/struct.json). Data: [data/structs.jsonl](../../data/structs.jsonl).

| Name | Size (bytes) | Area | Summary |
|---|---|---|---|
| [AbilityActionRow](AbilityActionRow.md) | 20 | [Ability data](../areas/ability-data.md) | One action record of an ability. |
| [AbilityAnimRow](AbilityAnimRow.md) | 3 | [Ability data](../areas/ability-data.md) | Battle presentation of one ability. |
| [AbilityAuxRow](AbilityAuxRow.md) | 8 | [Ability data](../areas/ability-data.md) | One auxiliary ability record. |
| [AbilityEffectNumberRow](AbilityEffectNumberRow.md) | 2 | [Ability data](../areas/ability-data.md) | Effect word of one ability. |
| [AbilityEventPair](AbilityEventPair.md) | 4 | [Job data](../areas/job-data.md) | One row of the AbilityEventPairs table. |
| [AbilityKind1Row](AbilityKind1Row.md) | 1 | [Ability data](../areas/ability-data.md) | Item id of an Item-command ability. |
| [AbilityKind2Row](AbilityKind2Row.md) | 1 | [Ability data](../areas/ability-data.md) | Item type of a Throw ability. |
| [AbilityKind3Row](AbilityKind3Row.md) | 2 | [Ability data](../areas/ability-data.md) | Jump reach. |
| [AbilityKind4Row](AbilityKind4Row.md) | 2 | [Ability data](../areas/ability-data.md) | Charge values. |
| [AbilityKind5Row](AbilityKind5Row.md) | 1 | [Ability data](../areas/ability-data.md) | Arithmeticks mask. |
| [AbilityKind6Row](AbilityKind6Row.md) | 1 | [Ability data](../areas/ability-data.md) | Passive ability index. |
| [AbilityListRow](AbilityListRow.md) | 8 | [Job list and unlock](../areas/job-list.md) | One 8-byte row of the job screen's ability page: word 0 job id, word 1 ability id with flag bits; the list ends with {0, 0xFFFF}. |
| [ActionEntryWord](ActionEntryWord.md) | 2 | [Battle](../areas/battle.md) | The 16-bit word of a four-byte action entry (the AI and preview form): the action id in bits 0..9 and the acting unit slot in bits 10..15. |
| [ActionResult](ActionResult.md) | 48 | [Battle](../areas/battle.md) | The result of one action on one target, filled by the formula handler and read by the result applier, the preview and the messages. |
| [AiCommandEntry](AiCommandEntry.md) | 4 | [Battle](../areas/battle.md) | One candidate action of the AI's command table: the ability word (id \| unit slot << 10), the command (skillset) byte it comes from and a flag byte. |
| [AtlasShelf](AtlasShelf.md) | 16 | [Graphics](../areas/graphics.md) | The state of one layer atlas allocator (a shelf / row packer): the cursor in the current row, the start of the row, the height of the row and the page. |
| [AvailabilityFlag](AvailabilityFlag.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the GridAvailableTemplate table. |
| [BannerWordRange](BannerWordRange.md) | 4 | [Battle](../areas/battle.md) | One row of the BannerWordRanges table. |
| [BattleMainWindow](BattleMainWindow.md) |  | [Battle](../areas/battle.md) | The battle main window object (UIAddonFFTOBattleMain4): only the fields read so far. |
| [BattleMenuRowScreenCode](BattleMenuRowScreenCode.md) | 1 | [Battle](../areas/battle.md) | One row of the BattleMenuRowScreenCodes table. |
| [BattleMenuStepRow](BattleMenuStepRow.md) | 32 | [Battle](../areas/battle.md) | One row of the command menu step tables (same shape as the stock menu step table). |
| [BattleMsgDescriptor](BattleMsgDescriptor.md) | 16 | [Battle](../areas/battle.md) | The 4-dword descriptor the banner takes: class, subtype, kind and a message word. |
| [BattleMsgEntry](BattleMsgEntry.md) | 524 | [Battle](../areas/battle.md) | One slot of the battle message store: the kind, the kind-dependent argument, a message id and a 512-byte text buffer. |
| [BattleMsgRecord](BattleMsgRecord.md) |  | [Battle](../areas/battle.md) | The record the message object holds at +8: the values the argument filler reads for a message. |
| [BattlePanelHandWord](BattlePanelHandWord.md) | 2 | [Battle](../areas/battle.md) | One hand word as the flag-aware panels read it: the item id in bits 0..8 and a two-bit value in bits 14..15. |
| [BattleRangeMarkRecord](BattleRangeMarkRecord.md) | 5 | [Battle](../areas/battle.md) | One record of g_BattleRangeMarks, parallel to BattleTileRecord (512 records, layer 1 at +0x500). |
| [BattleSnapshot](BattleSnapshot.md) | 668112 | [Save data](../areas/save-data.md) | The 668,112-byte battle image a kind-1 resume entry carries, as the capture builds it in g_BattleState: a battle context, five blocks (A..E), the 21 x 512-byte unit records and 3,000 more bytes of scene-task state. |
| [BattleSpawnEntry](BattleSpawnEntry.md) | 40 | [Unit data](../areas/unit-data.md) | One 40-byte entry of a scripted battle's entry block: the description of one unit to build. |
| [BattleTileRecord](BattleTileRecord.md) | 8 | [Battle](../areas/battle.md) | One tile of the battle map in g_BattleTileTable: 256 records per layer, two layers (layer 1 at +0x800), index x + y * width. |
| [BlendModeAlphaEntry](BlendModeAlphaEntry.md) | 1 | [Graphics](../areas/graphics.md) | One row of the BlendModeAlpha table. |
| [BlockSectorStart](BlockSectorStart.md) | 4 | [Resource](../areas/resource.md) | One row of the sector start tables of the packed UI and event blocks. |
| [BoneLinkPairsRow](BoneLinkPairsRow.md) | 16 | [Graphics](../areas/graphics.md) | One row of the BoneLinkPairs table. |
| [BufferPointer](BufferPointer.md) | 8 | [Event system](../areas/event-system.md) | One row of the EventWorkBufferPointers table. |
| [BytePopcountRow](BytePopcountRow.md) | 1 | [Math](../areas/math.md) | One row of MathBytePopcount. |
| [CalendarDateRow](CalendarDateRow.md) | 2 | [Event system](../areas/event-system.md) | One row of CalendarTrackedDates. |
| [CalendarDaysBeforeMonthRow](CalendarDaysBeforeMonthRow.md) | 2 | [Math](../areas/math.md) | One row of the CalendarDaysBeforeMonth table. |
| [CalendarDaysPerMonthRow](CalendarDaysPerMonthRow.md) | 1 | [Data access](../areas/data.md) | One row of the CalendarDaysPerMonth table. |
| [CategoryIconCell](CategoryIconCell.md) | 2 | [Items and shops](../areas/items.md) | One row of the ItemCategoryIconCells table. |
| [ChannelExpandRow](ChannelExpandRow.md) | 1 | [Graphics](../areas/graphics.md) | One row of GfxBitExpandTables. |
| [CharGridCell](CharGridCell.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the CharGridOrder table. |
| [ClassicLoadWindowDefaultRecord](ClassicLoadWindowDefaultRecord.md) |  | [Save data](../areas/save-data.md) | One row of the ClassicLoadWindowDefault table. |
| [ClassicSaveListLanguage0Record](ClassicSaveListLanguage0Record.md) | 176 | [Save data](../areas/save-data.md) | One row of the ClassicSaveListLanguage0 table. |
| [ClassicSaveWindowALanguage0Record](ClassicSaveWindowALanguage0Record.md) |  | [Save data](../areas/save-data.md) | One row of the ClassicSaveWindowALanguage0 table. |
| [ClassicSaveWindowAOtherLanguagesRecord](ClassicSaveWindowAOtherLanguagesRecord.md) |  | [Save data](../areas/save-data.md) | One row of the ClassicSaveWindowAOtherLanguages table. |
| [ClassicSaveWindowBLanguage0Record](ClassicSaveWindowBLanguage0Record.md) |  | [Save data](../areas/save-data.md) | One row of the ClassicSaveWindowBLanguage0 table. |
| [ClassicSaveWindowBOtherLanguagesRecord](ClassicSaveWindowBOtherLanguagesRecord.md) |  | [Save data](../areas/save-data.md) | One row of the ClassicSaveWindowBOtherLanguages table. |
| [ClutBank](ClutBank.md) | 2450 | [Graphics](../areas/graphics.md) | One of the 14 banks of the palette manager (g_ClutManager, from +8): 16 rows of 16 colours with a timer per row, the state of every colour and the bank's base rows. |
| [CodePointerRow](CodePointerRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of UiLegacyLayoutScriptOps. |
| [ColourPair](ColourPair.md) | 4 | [UI framework](../areas/ui-framework.md) | One row of the EquipPanelColourPairs table. |
| [CommandKindMessageOffset](CommandKindMessageOffset.md) | 1 | [Battle](../areas/battle.md) | One row of the CommandKindMessageOffsets table. |
| [CommandKindParam](CommandKindParam.md) | 4 | [Battle](../areas/battle.md) | One row of the CommandKindParams table. |
| [CommandKindRow](CommandKindRow.md) | 1 | [Job data](../areas/job-data.md) | One byte per skillset id. |
| [CornerColour](CornerColour.md) | 4 | [Battle](../areas/battle.md) | One row of the BannerWordColours table. |
| [CrystalRollResult](CrystalRollResult.md) | 1393 | [Battle](../areas/battle.md) | The block Unit_RollAbilityLearning fills at dword_1411A6AB0 (1393 bytes, the next data starts at 0x1411A7024) when a unit stops on a crystal or chest. |
| [CursorPosition](CursorPosition.md) | 2 | [UI framework](../areas/ui-framework.md) | One row of the LegacyCursorPositions table. |
| [DataBlockPointerRow](DataBlockPointerRow.md) | 8 | [Resource](../areas/resource.md) | One row of AudioDspCoefficientBlockPointers. |
| [DissolveStep](DissolveStep.md) | 64 | [Graphics](../areas/graphics.md) | One row of the DissolveOffsets table. |
| [EaseEndpoints](EaseEndpoints.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the EaseCurvesSetG table. |
| [EaseSample](EaseSample.md) | 4 | [UI framework](../areas/ui-framework.md) | One row of the EaseCurvesSetA table. |
| [EaseSample3](EaseSample3.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the EaseCurvesSetH table. |
| [EffectBlendWeightsRow](EffectBlendWeightsRow.md) | 7 | [Battle](../areas/battle.md) | One row of the EffectBlendWeights table. |
| [EffectFileLocatorRow](EffectFileLocatorRow.md) | 8 | [Battle](../areas/battle.md) | One row of EffectFileLocatorsLangOther. |
| [EffectFlashProfilesRow](EffectFlashProfilesRow.md) | 14 | [Battle](../areas/battle.md) | One row of the EffectFlashProfiles table. |
| [EffectKindRecordsRow](EffectKindRecordsRow.md) | 4 | [Battle](../areas/battle.md) | One row of the EffectKindRecords table. |
| [EffectLabelRectRow](EffectLabelRectRow.md) | 4 | [Battle](../areas/battle.md) | One row of BattleEffectLabelRectsLang0. |
| [EffectNumberPseudoRow](EffectNumberPseudoRow.md) | 2 | [Battle](../areas/battle.md) | One row of the EffectNumberPseudo table. |
| [EffectPaletteSeedsRow](EffectPaletteSeedsRow.md) | 3 | [Battle](../areas/battle.md) | One row of the EffectPaletteSeeds table. |
| [EffectSpriteSpawnRecordsRow](EffectSpriteSpawnRecordsRow.md) | 46 | [Battle](../areas/battle.md) | One row of the EffectSpriteSpawnRecords table. |
| [ElementColoursRow](ElementColoursRow.md) | 3 | [Battle](../areas/battle.md) | One row of the ElementColours table. |
| [ElementMaskOrderRow](ElementMaskOrderRow.md) | 1 | [Battle](../areas/battle.md) | One row of the ElementMaskOrder table. |
| [EquipmentOrderListPointer](EquipmentOrderListPointer.md) | 8 | [Items and shops](../areas/items.md) | One row of the EquipmentOrderLists table. |
| [EquipPanelBlock](EquipPanelBlock.md) | 64 | [Battle](../areas/battle.md) | A 64-byte copy of a party or battle record's bytes +0x30..+0x6F, kept at 0x141876E90 for the field equip screens and at 0x141D3B880 for the battle panels. |
| [EquipSetBlock](EquipSetBlock.md) | 64 | [Items and shops](../areas/items.md) | The equip screen's computed set at 0x141876C40: stat deltas at +0x00..+0x23, the five candidate equipment words at +0x24..+0x2D, a five-word display array at +0x2E..+0x37, and unclassified words at +0x38..+0x3F. It is... |
| [ErrandActiveSlot](ErrandActiveSlot.md) | 9 | [Errands](../areas/errands.md) | One of the eight active errand slots at g_ErrandActive (9 bytes each, count g_ErrandActiveCount): a dispatch in progress or back, its errand, its days, the town it left from and up to three units. |
| [ErrandBlobLayout](ErrandBlobLayout.md) | 2768 | [Errands](../areas/errands.md) | Layout of the errand data block: a header of sub-table offsets followed by the errand records and the scoring and reward tables. |
| [ErrandJobFitRow](ErrandJobFitRow.md) | 22 | [Errands](../areas/errands.md) | Job fit scores of one errand category or type row. |
| [ErrandMilestoneRow](ErrandMilestoneRow.md) | 1 | [Errands](../areas/errands.md) | One treasure milestone. |
| [ErrandRecordRow](ErrandRecordRow.md) | 23 | [Errands](../areas/errands.md) | One errand record in the errand data block. |
| [EventControl](EventControl.md) | 64 | [Event system](../areas/event-system.md) | ffto::Game::Event::EventControl (vtable 0x140713658), the singleton at g_EventControl: the event-script pause overlay and its hold-to-skip. |
| [EventGenericLookSet](EventGenericLookSet.md) | 32 | [Event system](../areas/event-system.md) | One row of the EventGenericLookSets table. |
| [EventOperandLengthRow](EventOperandLengthRow.md) | 1 | [Event system](../areas/event-system.md) | Operand length of one opcode. |
| [EventPanelRow](EventPanelRow.md) | 56 | [Event system](../areas/event-system.md) | One row of the EventPanelRows tables. |
| [EventSideYaw](EventSideYaw.md) | 2 | [Event system](../areas/event-system.md) | One row of the EventSideYawTargets table. |
| [EventSoundGroup](EventSoundGroup.md) | 4 | [Event system](../areas/event-system.md) | One row of the EventSoundGroups table: four sound effect numbers played together. |
| [EventViewerEntry](EventViewerEntry.md) | 2 | [Event system](../areas/event-system.md) | One row of the EventViewerList table. |
| [FaceShapeId](FaceShapeId.md) | 4 | [Event system](../areas/event-system.md) | One row of the FaceSlotShapeIds table. |
| [FixedRampBlockRow](FixedRampBlockRow.md) | 16 | [Graphics](../areas/graphics.md) | One row of EffectPoseBlendKeys. |
| [FormatArgRecord](FormatArgRecord.md) | 264 | [Battle](../areas/battle.md) | One argument of a formatted UI text string: a 256-byte text area and a type dword at +0x100. |
| [FormulaBlock](FormulaBlock.md) | 72 | [Battle](../areas/battle.md) | The state of the one action being resolved: Battle_ResolveAction fills it per target and every formula handler reads and writes it. |
| [FrameSetPointer](FrameSetPointer.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the UiFrameSets tables. |
| [FunctionPointerRow](FunctionPointerRow.md) | 8 | [Data access](../areas/data.md) | One function pointer. |
| [GlobalWork](GlobalWork.md) | 136 | [Application and startup](../areas/app-startup.md) | ffto::Game::GlobalWork (vtable 0x140713EA8), the singleton at g_GlobalWork. |
| [GlyphAdvance](GlyphAdvance.md) | 1 | [Data access](../areas/data.md) | One row of the GlyphAdvanceWidths table: the advance width of one glyph. |
| [GlyphCodeTripleRow](GlyphCodeTripleRow.md) | 3 | [UI framework](../areas/ui-framework.md) | One row of UiGlyphCodeTriples. |
| [GradientWindowVertexPaletteIndex](GradientWindowVertexPaletteIndex.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the GradientWindowVertexPalette table. |
| [GridHelpRow](GridHelpRow.md) | 24 | [UI framework](../areas/ui-framework.md) | One row of the GridHelpRows tables. |
| [GUILayer](GUILayer.md) | 592 | [UI framework](../areas/ui-framework.md) | A UI layer: a component drawn offscreen and composited with its effects (mask, drop shadow, glow). |
| [GUINode](GUINode.md) | 224 |  | Size from the 224-byte free in GUILayerNode's destructor. |
| [GUINodeState](GUINodeState.md) | 208 | [UI framework](../areas/ui-framework.md) | One state (timeline) of a component: its clock, its loop range, its flags and the channel sets and entries it applies. |
| [GUINodeStateEntry](GUINodeStateEntry.md) | 64 | [UI framework](../areas/ui-framework.md) | One entry of a state's entry list (GUINodeState.entries): a jump marker, a trigger, a state link, a state reset or a part trigger, built from the state's special tracks by UIAnim_ApplyTrack and UIAnim_ApplyComponentTr... |
| [HdSheetGroup](HdSheetGroup.md) | 21144 | [Graphics](../areas/graphics.md) | One of the 20 sheet groups of the battle HD layer (g_HdSheetGroups): a sheet entry kept in memory and the textures cut from it, one per piece and palette. |
| [HdTextureId](HdTextureId.md) | 4 | [Unit rendering](../areas/unit-rendering.md) | One row of the EventSpriteHdTextures table and the tables that share its shape. |
| [IdRemapRow](IdRemapRow.md) | 56 | [Data access](../areas/data.md) | Seven id pairs. |
| [ImportSlotRow](ImportSlotRow.md) | 8 | [Application and startup](../areas/app-startup.md) | One row of SteamApiImportSlots. |
| [InflictRecordRow](InflictRecordRow.md) | 6 | [Items and shops](../areas/items.md) | One added-effect record. |
| [InputActionRow](InputActionRow.md) | 48 | [Input](../areas/input.md) | One action of the input module (g_InputModule + 1360 + 48 * action id, 256 rows; ids are UIKeyAssign keys): three 16-byte bindings, the pad button first, then two keys. |
| [InputStateAxes](InputStateAxes.md) | 1352 | [Input](../areas/input.md) | The analog part of the 0x548-byte input state that the UI listeners receive (copied whole by sub_1400EFB50 and by GUICore_OnInputState): four signed stick bytes, two trigger bytes and the button dwords. |
| [ItemAccessoryRow](ItemAccessoryRow.md) | 2 | [Items and shops](../areas/items.md) | Accessory sub-record. |
| [ItemArmorRow](ItemArmorRow.md) | 2 | [Items and shops](../areas/items.md) | Armor sub-record. |
| [ItemAttributeRow](ItemAttributeRow.md) | 26 | [Items and shops](../areas/items.md) | Equipment attribute record. |
| [ItemCategoryFirstIdRow](ItemCategoryFirstIdRow.md) | 2 | [Items and shops](../areas/items.md) | First item id of one category. |
| [ItemCategoryTypeRow](ItemCategoryTypeRow.md) | 4 | [Items and shops](../areas/items.md) | Record kind of one category. |
| [ItemChemistRow](ItemChemistRow.md) | 3 | [Items and shops](../areas/items.md) | Chemist item sub-record. |
| [ItemEquipPaletteRow](ItemEquipPaletteRow.md) | 2 | [Items and shops](../areas/items.md) | Palette selector of one item. |
| [ItemKindFirstCategoryRow](ItemKindFirstCategoryRow.md) | 4 | [Items and shops](../areas/items.md) | First category of one kind. |
| [ItemListCells](ItemListCells.md) |  | [Battle](../areas/battle.md) | The static item-list cell store: 82 two-byte cells (kind tag in bits 15..11, id in bits 10..0) and the parallel per-cell arrays beside them. |
| [ItemNewFlagBlock](ItemNewFlagBlock.md) | 1007 | [Items and shops](../areas/items.md) | The block at g_ItemNewFlags: the shop new-item flags first, then the four Poachers' Den (poach) arrays. |
| [ItemOrderLists](ItemOrderLists.md) |  | [Items and shops](../areas/items.md) | The ten saved item order lists: 16-bit words in static storage, no header and no length word. |
| [ItemRecord](ItemRecord.md) | 12 | [Items and shops](../areas/items.md) | The 12-byte record of an item (Item_GetRecord): icon, level, equipment slot bits, equipment category, attribute index, price and the story progress it is sold from. |
| [ItemScreenPaletteRow](ItemScreenPaletteRow.md) | 2 | [Graphics](../areas/graphics.md) | One row of the ItemScreenPalette table. |
| [ItemShieldRow](ItemShieldRow.md) | 2 | [Items and shops](../areas/items.md) | Shield sub-record. |
| [ItemShopMaskRow](ItemShopMaskRow.md) | 2 | [Items and shops](../areas/items.md) | Shop availability of one item. |
| [ItemWeaponRecord](ItemWeaponRecord.md) | 8 | [Items and shops](../areas/items.md) | The 8-byte weapon sub-record of an item whose category kind is 0 or 5 (sub_1402B8C74). |
| [JobChangeListAddon](JobChangeListAddon.md) | 19024 | [Job data](../areas/job-data.md) | The Change Job list screen object (the list addon, reached as [[[root]+0x10]+0x58]+0x78 and as field 15 of the screen object): 19 cell records of 148 bytes, 19 cell gadgets of 256 bytes, and the cursor state; every ar... |
| [JobListWord](JobListWord.md) | 2 | [Job list and unlock](../areas/job-list.md) | One entry of g_RuntimeJobList: the job id in bits 0..9, bit 13 locked (not unlocked by any party member) and bit 14 current job. |
| [JobMasteryIdRow](JobMasteryIdRow.md) | 4 | [Job data](../areas/job-data.md) | One job id. |
| [JobNeedLevelRow](JobNeedLevelRow.md) | 12 | [Job data](../areas/job-data.md) | The required job levels for one job index: 24 nibbles. |
| [JobRecord](JobRecord.md) | 148 |  | Only the listed offsets are verified; the rest of the 148 bytes is copied wholesale. |
| [JobTableRow](JobTableRow.md) | 49 | [Job data](../areas/job-data.md) | One 49-byte row of the stock job table: skillset, always-on abilities, equipment classes, growth constants, move, jump, evade, status and element sets and three look bytes. |
| [JobTreeAddon](JobTreeAddon.md) | 13312 |  | STOCK layout (20 panels). |
| [JobTreePanel](JobTreePanel.md) | 456 |  | Stride 456 bytes (stock: 20 panels). |
| [KeyRepeatPreset](KeyRepeatPreset.md) | 6 | [Input](../areas/input.md) | One row of the KeyRepeatPresets table. |
| [KeyTrack](KeyTrack.md) |  | [UI framework](../areas/ui-framework.md) | A keyframe track of one property of one target: sorted keys, the first four stored inline. |
| [KeyTrackKey](KeyTrackKey.md) | 16 | [UI framework](../areas/ui-framework.md) | One keyframe: its frame, the curve that shapes the interval to the next key, and the value. |
| [LauncherButtonIdRow](LauncherButtonIdRow.md) | 4 | [UI framework](../areas/ui-framework.md) | One row of UiLauncherButtonOrder. |
| [LauncherFocusRow](LauncherFocusRow.md) | 24 | [UI framework](../areas/ui-framework.md) | One row of UiLauncherFocusNeighborsAlt. |
| [LayoutPointer](LayoutPointer.md) | 8 | [Battle](../areas/battle.md) | One row of the StatusPanelLayoutsLanguage0 table. |
| [LegacyAbilityMenuSkillsetByTabRow](LegacyAbilityMenuSkillsetByTabRow.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the LegacyAbilityMenuSkillsetByTab table. |
| [LegacyBounceProfileRow](LegacyBounceProfileRow.md) | 2 | [UI framework](../areas/ui-framework.md) | One row of the LegacyBounceProfile table. |
| [LegacyButtonIconGroupStartsRow](LegacyButtonIconGroupStartsRow.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of a LegacyButtonIconGroupStarts table. |
| [LegacyButtonIconPiecesRow](LegacyButtonIconPiecesRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of a LegacyButtonIconPieces table. |
| [LegacyButtonIconScalesRow](LegacyButtonIconScalesRow.md) | 4 | [UI framework](../areas/ui-framework.md) | One row of a LegacyButtonIconScales table. |
| [LegacyCellRectsRow](LegacyCellRectsRow.md) | 20 | [UI framework](../areas/ui-framework.md) | One row of the LegacyCellRects table. |
| [LegacyCursorRowsLang0Row](LegacyCursorRowsLang0Row.md) | 24 | [UI framework](../areas/ui-framework.md) | One row of the LegacyCursorRowsLang0 table. |
| [LegacyCursorRowsLangOtherRow](LegacyCursorRowsLangOtherRow.md) | 24 | [UI framework](../areas/ui-framework.md) | One row of the LegacyCursorRowsLangOther table. |
| [LegacyItemCursorTemplatesRow](LegacyItemCursorTemplatesRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the LegacyItemCursorTemplates table. |
| [LegacyItemListBodyGridARow](LegacyItemListBodyGridARow.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the LegacyItemListBodyGridA table. |
| [LegacyItemListBodyGridBRow](LegacyItemListBodyGridBRow.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the LegacyItemListBodyGridB table. |
| [LegacyItemScriptRecord](LegacyItemScriptRecord.md) | 1 | [UI framework](../areas/ui-framework.md) | First byte of one record of an item page layout script; the handler of the opcode returns the start of the next record. |
| [LegacyJobScreenLayoutLang0Row](LegacyJobScreenLayoutLang0Row.md) | 6592 | [UI framework](../areas/ui-framework.md) | One row of the LegacyJobScreenLayoutLang0 table. |
| [LegacyListRowSlotRow](LegacyListRowSlotRow.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the LegacyListRowSlot table. |
| [LegacyMenuNode](LegacyMenuNode.md) | 88 | [UI framework](../areas/ui-framework.md) | One row of the LegacyMenuNodesLanguage0 table and the tables that share its shape. |
| [LegacyMenuRowCountsRow](LegacyMenuRowCountsRow.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the LegacyMenuRowCounts table. |
| [LegacyMenuRowIconsRow](LegacyMenuRowIconsRow.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the LegacyMenuRowIcons table. |
| [LegacyMenuRowListPointersRow](LegacyMenuRowListPointersRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the LegacyMenuRowListPointers table. |
| [LegacyMenuRowResultRecord](LegacyMenuRowResultRecord.md) | 16 | [UI framework](../areas/ui-framework.md) | One row of the LegacyMenuRowResults table. |
| [LegacyMenuTaskSetupsRow](LegacyMenuTaskSetupsRow.md) | 48 | [UI framework](../areas/ui-framework.md) | One row of the LegacyMenuTaskSetups table. |
| [LegacyRowCellDescriptorsRow](LegacyRowCellDescriptorsRow.md) | 24 | [UI framework](../areas/ui-framework.md) | One row of the LegacyRowCellDescriptors table. |
| [LegacyTask12CommandsARow](LegacyTask12CommandsARow.md) | 480 | [UI framework](../areas/ui-framework.md) | One row of the LegacyTask12CommandsA table. |
| [LegacyTask12CommandsBRow](LegacyTask12CommandsBRow.md) | 64 | [UI framework](../areas/ui-framework.md) | One row of the LegacyTask12CommandsB table. |
| [LegacyTitleMenuOffsetsRow](LegacyTitleMenuOffsetsRow.md) | 2 | [UI framework](../areas/ui-framework.md) | One row of the LegacyTitleMenuOffsets table. |
| [LegacyUiScriptRecord](LegacyUiScriptRecord.md) | 2 | [UI framework](../areas/ui-framework.md) | Header of one record of a legacy menu layout script; the record is {opcode, length, arguments} and the next record starts length bytes later. |
| [ListPageRangeStart](ListPageRangeStart.md) | 2 | [UI framework](../areas/ui-framework.md) | One row of the LegacyListPageRangesLang0 table. |
| [LocationMarker](LocationMarker.md) | 8 | [Event system](../areas/event-system.md) | One row of the LocationMarkerOffsets table. |
| [LookPoolRecord](LookPoolRecord.md) | 13014 | [Graphics](../areas/graphics.md) | One of the 15 sprite records at 0x140D005A0 (stride 0x32D6) that hold the loaded graphics of a look; records are shared by every unit that has the same sprite number. |
| [LookQueueEntry](LookQueueEntry.md) | 32 | [Graphics](../areas/graphics.md) | One entry of the 16-entry load queue that Battle_BuildRosterTeam, Battle_AddJoinedUnit and the scene preview code fill (LookQueue_Add) and CharaPalette_ReloadForShape consumes; entry n starts at 0x141856728 + 32 * n, ... |
| [MapDrawIndexListRecord](MapDrawIndexListRecord.md) | 24 | [Graphics](../areas/graphics.md) | One row of the MapDrawIndexLists table. |
| [MapResourceFileListPointer](MapResourceFileListPointer.md) | 8 | [Resource](../areas/resource.md) | One row of the MapResourceFilesLanguage0 table. |
| [MenuCursorDefault](MenuCursorDefault.md) | 16 | [Battle](../areas/battle.md) | One row of the MenuCursorDefaults table. |
| [MenuListWord](MenuListWord.md) | 2 | [Items and shops](../areas/items.md) | One entry of g_MenuList, the array the shop, equip, item and ability screens reuse: the id in bits 0..9, bit 14 "cannot equip / cannot learn / current", and the list-kind-specific bits 12 and 13. |
| [MonsterSkillsetRow](MonsterSkillsetRow.md) | 5 | [Job data](../areas/job-data.md) | One 5-byte monster skillset: one flag byte and four low ability id bytes. |
| [MoveBlockerRecord](MoveBlockerRecord.md) | 7 | [Battle](../areas/battle.md) | One entry of g_MoveBlockers: another unit on the map as the move-range builder sees it. |
| [MoveFindRow](MoveFindRow.md) | 24 | [Battle](../areas/battle.md) | One row of the MoveFindItems table. |
| [MoveRangeScratch](MoveRangeScratch.md) | 128 | [Battle](../areas/battle.md) | The move-range builder's scratch block at g_MoveRangeScratch, filled by Battle_MoveRangeSetup from the unit record. |
| [MovieControl](MovieControl.md) | 32 | [UI framework](../areas/ui-framework.md) | ffto::Game::Movie::MovieControl (vtable 0x1407154B0), at g_MovieControl: pause overlay and hold-to-skip of a playing movie. |
| [MovieController](MovieController.md) |  | [UI framework](../areas/ui-framework.md) | ffto::Game::GameUI::MovieController (vtables 0x140702D20 and 0x140702D30): the movie host at *(qword_143CD9DC8) + 0xC8. |
| [MusicSlotRecordsRow](MusicSlotRecordsRow.md) | 12 | [Event system](../areas/event-system.md) | One row of the MusicSlotRecords table. |
| [NameSlotTable](NameSlotTable.md) |  | [Graphics](../areas/graphics.md) | A name-to-slot table of the render device (constant buffers, textures, samplers): names hashed into a tree, each with a dense slot id. |
| [NexResourceHandle](NexResourceHandle.md) | 168 | [Resource](../areas/resource.md) | The resource handle an nxd file is loaded through (NxdTable_CreateHandle; root.nxl uses the same layout with the NxlResourceHandle vtable): the common resource handle plus two callback pairs. |
| [NxdDataAbilityReactionVoiceTypeRow](NxdDataAbilityReactionVoiceTypeRow.md) | 48 | [Data access](../areas/data.md) | One row of the nxd.ability_reaction_voice_type table (data table). |
| [NxdDataAbilityRow](NxdDataAbilityRow.md) | 68 | [Ability data](../areas/ability-data.md) | One row of the nxd.ability table (English text table; the other languages share the layout). |
| [NxdDataAchievementArrayRow](NxdDataAchievementArrayRow.md) | 28 | [Data access](../areas/data.md) | One row of the nxd.achievement_groups table (data table). |
| [NxdDataAchievementRow](NxdDataAchievementRow.md) | 28 | [Data access](../areas/data.md) | One row of the nxd.achievement table (English text table; the other languages share the layout). |
| [NxdDataBattleEventOpcodeRow](NxdDataBattleEventOpcodeRow.md) | 8 | [Battle](../areas/battle.md) | One row of the nxd.battle_event_opcode table (data table). |
| [NxdDataBattleObjectiveRow](NxdDataBattleObjectiveRow.md) | 16 | [Battle](../areas/battle.md) | One row of the nxd.battle_objective table (English text table; the other languages share the layout). |
| [NxdDataBattleRow](NxdDataBattleRow.md) | 4 | [Battle](../areas/battle.md) | One row of the nxd.battle table (data table). |
| [NxdDataBattleSignalRow](NxdDataBattleSignalRow.md) | 16 | [Battle](../areas/battle.md) | One row of the nxd.battle_signal table (English text table; the other languages share the layout). |
| [NxdDataBattleVoiceGroupRateRow](NxdDataBattleVoiceGroupRateRow.md) | 208 | [Data access](../areas/data.md) | One row of the nxd.battle_voice_group_rate table (data table). |
| [NxdDataBattleVoiceRow](NxdDataBattleVoiceRow.md) | 44 | [Data access](../areas/data.md) | One row of the nxd.battle_voice table (data table). |
| [NxdDataBGMModeRow](NxdDataBGMModeRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.bgm_mode table (English text table; the other languages share the layout). |
| [NxdDataBGMTransitionRow](NxdDataBGMTransitionRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.bgm_transition table (data table). |
| [NxdDataBookRow](NxdDataBookRow.md) | 44 | [Items and shops](../areas/items.md) | One row of the nxd.book table (English text table; the other languages share the layout). |
| [NxdDataBraveStoryVoiceRow](NxdDataBraveStoryVoiceRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.brave_story_voice table (data table). |
| [NxdDataBrightnessRow](NxdDataBrightnessRow.md) | 12 | [Display](../areas/display.md) | One row of the nxd.brightness table (data table). |
| [NxdDataC_Mes_Id_SampleRow](NxdDataC_Mes_Id_SampleRow.md) | 24 | [Battle](../areas/battle.md) | One row of the nxd.battle_message_text table (English text table; the other languages share the layout). |
| [NxdDataCaptionFreeWordRow](NxdDataCaptionFreeWordRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.caption_free_word table (English text table; the other languages share the layout). |
| [NxdDataCaptionRow](NxdDataCaptionRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.caption table (data table). |
| [NxdDataChapterFileRow](NxdDataChapterFileRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.chapter_file table (data table). |
| [NxdDataChapterRow](NxdDataChapterRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.chapter table (English text table; the other languages share the layout). |
| [NxdDataCharaColorSkinRow](NxdDataCharaColorSkinRow.md) | 12 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.chara_color_skin table (data table). |
| [NxdDataCharaControlIdRow](NxdDataCharaControlIdRow.md) | 12 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.chara_control_id table (data table). |
| [NxdDataCharacterSortInfoRow](NxdDataCharacterSortInfoRow.md) | 8 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.character_sort_info table (data table). |
| [NxdDataCharaNameRow](NxdDataCharaNameRow.md) | 24 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.chara_name table (English text table; the other languages share the layout). |
| [NxdDataCharaPartsDrawParamRow](NxdDataCharaPartsDrawParamRow.md) | 12 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.chara_parts_draw_param table (data table). |
| [NxdDataCharaRow](NxdDataCharaRow.md) | 8 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.chara table (data table). |
| [NxdDataCharaZodiacStoneCLUTRow](NxdDataCharaZodiacStoneCLUTRow.md) | 16 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.chara_zodiac_stone_clut table (data table). |
| [NxdDataCharCLUTRow](NxdDataCharCLUTRow.md) | 24 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.char_clut table (data table). |
| [NxdDataCharMouseCollisionRow](NxdDataCharMouseCollisionRow.md) | 20 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.char_mouse_collision table (data table). |
| [NxdDataCharShapeLUTParamRow](NxdDataCharShapeLUTParamRow.md) | 20 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.char_shape_lut_param table (data table). |
| [NxdDataCharShapeRow](NxdDataCharShapeRow.md) | 48 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.char_shape table (data table). |
| [NxdDataCharShapeShadowSizeRow](NxdDataCharShapeShadowSizeRow.md) | 12 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.char_shape_shadow_size table (data table). |
| [NxdDataCharTacticalViewParamRow](NxdDataCharTacticalViewParamRow.md) | 32 | [Unit rendering](../areas/unit-rendering.md) | One row of the nxd.char_tactical_view_param table (data table). |
| [NxdDataCollectionRow](NxdDataCollectionRow.md) | 44 | [Data access](../areas/data.md) | One row of the nxd.collection table (English text table; the other languages share the layout). |
| [NxdDataConfigCategoryRow](NxdDataConfigCategoryRow.md) | 16 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_category table (data table). |
| [NxdDataConfigItemButtonTypeRow](NxdDataConfigItemButtonTypeRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_item_button_type table (data table). |
| [NxdDataConfigItemCursorMoveTypeRow](NxdDataConfigItemCursorMoveTypeRow.md) | 20 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_item_cursor_move_type table (data table). |
| [NxdDataConfigItemEnableDOFRow](NxdDataConfigItemEnableDOFRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_item_enable_dof table (data table). |
| [NxdDataConfigItemForwardEnabledTypeRow](NxdDataConfigItemForwardEnabledTypeRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_item_forward_enabled_type table (data table). |
| [NxdDataConfigItemResolutionRow](NxdDataConfigItemResolutionRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_item_resolution table (data table). |
| [NxdDataConfigItemRow](NxdDataConfigItemRow.md) | 76 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_item table (data table). |
| [NxdDataConfigItemScreenModeRow](NxdDataConfigItemScreenModeRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_item_screen_mode table (data table). |
| [NxdDataConfigItemTextLanguageRow](NxdDataConfigItemTextLanguageRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_item_text_language table (data table). |
| [NxdDataConfigItemVoiceLanguageRow](NxdDataConfigItemVoiceLanguageRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_item_voice_language table (data table). |
| [NxdDataConfigPadAssignRow](NxdDataConfigPadAssignRow.md) | 20 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_pad_assign table (data table). |
| [NxdDataConfigPadListRow](NxdDataConfigPadListRow.md) | 20 | [UI framework](../areas/ui-framework.md) | One row of the nxd.config_pad_list table (data table). |
| [NxdDataContinuousBattleTimelineRow](NxdDataContinuousBattleTimelineRow.md) | 8 | [Battle](../areas/battle.md) | One row of the nxd.continuous_battle_timeline table (data table). |
| [NxdDataContinuousSortieConfirmRow](NxdDataContinuousSortieConfirmRow.md) | 108 | [Battle](../areas/battle.md) | One row of the nxd.continuous_sortie_confirm table (data table). |
| [NxdDataCursorMoveTypeRow](NxdDataCursorMoveTypeRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the nxd.cursor_move_type table (data table). |
| [NxdDataDebugFidG2DRow](NxdDataDebugFidG2DRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.debug_fid_g2d table (data table). |
| [NxdDataDebugFIdSoundRow](NxdDataDebugFIdSoundRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.debug_fid_sound table (data table). |
| [NxdDataDebugMapRow](NxdDataDebugMapRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.debug_map table (data table). |
| [NxdDataDebugSceneSelectCategoryRow](NxdDataDebugSceneSelectCategoryRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.debug_scene_select_category table (data table). |
| [NxdDataDeepDungeonRow](NxdDataDeepDungeonRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.deep_dungeon table (English text table; the other languages share the layout). |
| [NxdDataDepthBiasRow](NxdDataDepthBiasRow.md) | 12 | [Graphics](../areas/graphics.md) | One row of the nxd.depth_bias table (data table). |
| [NxdDataDifficultyLevelRow](NxdDataDifficultyLevelRow.md) | 28 | [UI framework](../areas/ui-framework.md) | One row of the nxd.difficulty_level table (data table). |
| [NxdDataDLCPathListRow](NxdDataDLCPathListRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.dlc_path_list table (data table). |
| [NxdDataEggRow](NxdDataEggRow.md) | 24 | [Job data](../areas/job-data.md) | One row of the nxd.egg table (data table). |
| [NxdDataEnhancedBattleEventRow](NxdDataEnhancedBattleEventRow.md) | 40 | [Event system](../areas/event-system.md) | One row of the nxd.enhanced_battle_event table (data table). |
| [NxdDataEnhancedWorldEventRow](NxdDataEnhancedWorldEventRow.md) | 32 | [Event system](../areas/event-system.md) | One row of the nxd.enhanced_world_event table (data table). |
| [NxdDataEntryAreaRow](NxdDataEntryAreaRow.md) | 8 | [Battle](../areas/battle.md) | One row of the nxd.entry_area table (data table). |
| [NxdDataEntryNoRow](NxdDataEntryNoRow.md) | 28 | [Battle](../areas/battle.md) | One row of the nxd.entry_no table (data table). |
| [NxdDataEventCharaDrawRow](NxdDataEventCharaDrawRow.md) | 20 | [Event system](../areas/event-system.md) | One row of the nxd.event_chara_draw table (data table). |
| [NxdDataEventFlagRow](NxdDataEventFlagRow.md) | 8 | [Event system](../areas/event-system.md) | One row of the nxd.event_flag table (data table). |
| [NxdDataEventIdRow](NxdDataEventIdRow.md) | 44 | [Event system](../areas/event-system.md) | One row of the nxd.event_id table (data table). |
| [NxdDataFacilityVoicePatternRow](NxdDataFacilityVoicePatternRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.facility_voice_pattern table (data table). |
| [NxdDataFloorCursorSpeedRow](NxdDataFloorCursorSpeedRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the nxd.floor_cursor_speed table (data table). |
| [NxdDataForwardEnabledTypeRow](NxdDataForwardEnabledTypeRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the nxd.forward_enabled_type table (data table). |
| [NxdDataGameFlagRow](NxdDataGameFlagRow.md) | 8 | [Event system](../areas/event-system.md) | One row of the nxd.game_flag table (data table). |
| [NxdDataGameModeTypesRow](NxdDataGameModeTypesRow.md) | 24 | [Battle](../areas/battle.md) | One row of the nxd.game_mode_types table (data table). |
| [NxdDataGameProgressRow](NxdDataGameProgressRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.game_progress table (data table). |
| [NxdDataGeneralJobRow](NxdDataGeneralJobRow.md) | 124 | [Job data](../areas/job-data.md) | One row of the nxd.general_job table (data table). |
| [NxdDataGossipRow](NxdDataGossipRow.md) | 48 | [Data access](../areas/data.md) | One row of the nxd.gossip table (English text table; the other languages share the layout). |
| [NxdDataGuideCategoryRow](NxdDataGuideCategoryRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.guide_category table (data table). |
| [NxdDataGuidePageRow](NxdDataGuidePageRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.guide_page table (English text table; the other languages share the layout). |
| [NxdDataGuideRow](NxdDataGuideRow.md) | 48 | [Data access](../areas/data.md) | One row of the nxd.guide table (English text table; the other languages share the layout). |
| [NxdDataIconGroupRow](NxdDataIconGroupRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.icon_group table (data table). |
| [NxdDataIconRow](NxdDataIconRow.md) | 16 | [UI framework](../areas/ui-framework.md) | One row of the nxd.icon table (data table). |
| [NxdDataItemRow](NxdDataItemRow.md) | 48 | [Items and shops](../areas/items.md) | One row of the nxd.item table (English text table; the other languages share the layout). |
| [NxdDataJingleRow](NxdDataJingleRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.jingle table (data table). |
| [NxdDataJobCommandRow](NxdDataJobCommandRow.md) | 36 | [Job data](../areas/job-data.md) | One row of the nxd.job_command table (English text table; the other languages share the layout). |
| [NxdDataJobRow](NxdDataJobRow.md) | 64 | [Job data](../areas/job-data.md) | One row of the nxd.job table (English text table; the other languages share the layout). |
| [NxdDataJobTypeRow](NxdDataJobTypeRow.md) | 16 | [Job data](../areas/job-data.md) | One row of the nxd.job_type table (data table). |
| [NxdDataJournalRow](NxdDataJournalRow.md) | 40 | [Data access](../areas/data.md) | One row of the nxd.journal table (English text table; the other languages share the layout). |
| [NxdDataLandRow](NxdDataLandRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.land table (English text table; the other languages share the layout). |
| [NxdDataLandscapeHeightRow](NxdDataLandscapeHeightRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.landscape_height table (English text table; the other languages share the layout). |
| [NxdDataLanguageRow](NxdDataLanguageRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.language table (data table). |
| [NxdDataLauncherGuideRow](NxdDataLauncherGuideRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.launcher_guide table (English text table; the other languages share the layout). |
| [NxdDataLoadingSettingsRow](NxdDataLoadingSettingsRow.md) | 4 | [Display](../areas/display.md) | One row of the nxd.loading_settings table (data table). |
| [NxdDataLoreAffiliationRow](NxdDataLoreAffiliationRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.lore_affiliation table (English text table; the other languages share the layout). |
| [NxdDataLoreDictionaryCategoryRow](NxdDataLoreDictionaryCategoryRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.lore_dictionary_category table (English text table; the other languages share the layout). |
| [NxdDataLoreDictionaryRow](NxdDataLoreDictionaryRow.md) | 84 | [Data access](../areas/data.md) | One row of the nxd.lore_dictionary table (English text table; the other languages share the layout). |
| [NxdDataLoreNameAliasRow](NxdDataLoreNameAliasRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.lore_name_alias table (English text table; the other languages share the layout). |
| [NxdDataMapRouteTableRow](NxdDataMapRouteTableRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.map_route_table table (data table). |
| [NxdDataMapRow](NxdDataMapRow.md) | 32 | [Battle](../areas/battle.md) | One row of the nxd.map table (data table). |
| [NxdDataMapVariationEventRow](NxdDataMapVariationEventRow.md) | 20 | [Battle](../areas/battle.md) | One row of the nxd.map_variation_event table (data table). |
| [NxdDataMapVariationRandomBattleRow](NxdDataMapVariationRandomBattleRow.md) | 8 | [Battle](../areas/battle.md) | One row of the nxd.map_variation_random_battle table (data table). |
| [NxdDataMessageWindowAnimationTypeRow](NxdDataMessageWindowAnimationTypeRow.md) | 28 | [UI framework](../areas/ui-framework.md) | One row of the nxd.message_window_animation_type table (data table). |
| [NxdDataMovieDataRow](NxdDataMovieDataRow.md) | 40 | [Data access](../areas/data.md) | One row of the nxd.movie_data table (data table). |
| [NxdDataNovel00Row](NxdDataNovel00Row.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.novel_00 table (English text table; the other languages share the layout). |
| [NxdDataNovel01Row](NxdDataNovel01Row.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.novel_01 table (English text table; the other languages share the layout). |
| [NxdDataNovel02Row](NxdDataNovel02Row.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.novel_02 table (English text table; the other languages share the layout). |
| [NxdDataNovel03Row](NxdDataNovel03Row.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.novel_03 table (English text table; the other languages share the layout). |
| [NxdDataNovel04Row](NxdDataNovel04Row.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.novel_04 table (English text table; the other languages share the layout). |
| [NxdDataNovelIconRow](NxdDataNovelIconRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.novel_icon table (data table). |
| [NxdDataOverrideAbilityActionDataRow](NxdDataOverrideAbilityActionDataRow.md) | 40 | [Ability data](../areas/ability-data.md) | One row of the nxd.override_ability_action_data table (data table). |
| [NxdDataOverrideEntryDataRow](NxdDataOverrideEntryDataRow.md) | 160 | [Battle](../areas/battle.md) | One row of the nxd.override_entry_data table (data table). |
| [NxdDataPauseRow](NxdDataPauseRow.md) | 24 | [Battle](../areas/battle.md) | One row of the nxd.pause table (data table). |
| [NxdDataPlaceNameRow](NxdDataPlaceNameRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.place_name table (English text table; the other languages share the layout). |
| [NxdDataPoachItemRow](NxdDataPoachItemRow.md) | 56 | [Items and shops](../areas/items.md) | One row of the nxd.poach_item table (English text table; the other languages share the layout). |
| [NxdDataPostEffectDepthLUTRow](NxdDataPostEffectDepthLUTRow.md) | 40 | [Graphics](../areas/graphics.md) | One row of the nxd.post_effect_depth_lut table (data table). |
| [NxdDataPostEffectDOFRow](NxdDataPostEffectDOFRow.md) | 28 | [Graphics](../areas/graphics.md) | One row of the nxd.post_effect_dof table (data table). |
| [NxdDataPostEffectGlareRow](NxdDataPostEffectGlareRow.md) | 24 | [Graphics](../areas/graphics.md) | One row of the nxd.post_effect_glare table (data table). |
| [NxdDataPostEffectLUTRow](NxdDataPostEffectLUTRow.md) | 20 | [Graphics](../areas/graphics.md) | One row of the nxd.post_effect_lut table (data table). |
| [NxdDataPostEffectRow](NxdDataPostEffectRow.md) | 16 | [Graphics](../areas/graphics.md) | One row of the nxd.post_effect table (data table). |
| [NxdDataProfitBonusItemRow](NxdDataProfitBonusItemRow.md) | 12 | [Errands](../areas/errands.md) | One row of the nxd.profit_bonus_item table (English text table; the other languages share the layout). |
| [NxdDataProfitClientNameRow](NxdDataProfitClientNameRow.md) | 8 | [Errands](../areas/errands.md) | One row of the nxd.profit_client_name table (English text table; the other languages share the layout). |
| [NxdDataProfitRow](NxdDataProfitRow.md) | 40 | [Errands](../areas/errands.md) | One row of the nxd.profit table (English text table; the other languages share the layout). |
| [NxdDataProfitTypeRow](NxdDataProfitTypeRow.md) | 20 | [Errands](../areas/errands.md) | One row of the nxd.profit_type table (data table). |
| [NxdDataPSPMovieFileRow](NxdDataPSPMovieFileRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.psp_movie_file table (data table). |
| [NxdDataRefinedBgAnimRow](NxdDataRefinedBgAnimRow.md) | 12 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_bg_anim table (data table). |
| [NxdDataRefinedBgMeshNodeInvisTypeRow](NxdDataRefinedBgMeshNodeInvisTypeRow.md) | 12 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_bg_mesh_node_invis_type table (data table). |
| [NxdDataRefinedBgMeshNodeRow](NxdDataRefinedBgMeshNodeRow.md) | 28 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_bg_mesh_node table (data table). |
| [NxdDataRefinedBgMeshPolygonCondRow](NxdDataRefinedBgMeshPolygonCondRow.md) | 20 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_bg_mesh_polygon_cond table (data table). |
| [NxdDataRefinedBgMeshPolygonRow](NxdDataRefinedBgMeshPolygonRow.md) | 24 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_bg_mesh_polygon table (data table). |
| [NxdDataRefinedBgSystemTextureRow](NxdDataRefinedBgSystemTextureRow.md) | 24 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_bg_system_texture table (data table). |
| [NxdDataRefinedBgTextureRow](NxdDataRefinedBgTextureRow.md) | 40 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_bg_texture table (data table). |
| [NxdDataRefinedBgUITextureFramesRow](NxdDataRefinedBgUITextureFramesRow.md) | 12 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_bg_ui_texture_frames table (data table). |
| [NxdDataRefinedBgUITextureRow](NxdDataRefinedBgUITextureRow.md) | 20 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_bg_ui_texture table (data table). |
| [NxdDataRefinedPermanentVFXRow](NxdDataRefinedPermanentVFXRow.md) | 12 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_permanent_vfx table (data table). |
| [NxdDataRefinedVFXCameraControlRow](NxdDataRefinedVFXCameraControlRow.md) | 20 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_vfx_camera_control table (data table). |
| [NxdDataRefinedVFXTextureRow](NxdDataRefinedVFXTextureRow.md) | 32 | [Graphics](../areas/graphics.md) | One row of the nxd.refined_vfx_texture table (data table). |
| [NxdDataResolutionRow](NxdDataResolutionRow.md) | 16 | [Display](../areas/display.md) | One row of the nxd.resolution table (data table). |
| [NxdDataRouteRow](NxdDataRouteRow.md) | 28 | [Data access](../areas/data.md) | One row of the nxd.route table (data table). |
| [NxdDataScenarioIdRow](NxdDataScenarioIdRow.md) | 16 | [Event system](../areas/event-system.md) | One row of the nxd.scenario_id table (data table). |
| [NxdDataScionFilesRow](NxdDataScionFilesRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.scion_files table (data table). |
| [NxdDataScionLabelsRow](NxdDataScionLabelsRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.scion_labels table (data table). |
| [NxdDataScreenModeRow](NxdDataScreenModeRow.md) | 8 | [Display](../areas/display.md) | One row of the nxd.screen_mode table (data table). |
| [NxdDataSeadEventRow](NxdDataSeadEventRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.sead_event table (data table). |
| [NxdDataSeadStateParameterRow](NxdDataSeadStateParameterRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.sead_state_parameter table (data table). |
| [NxdDataSeDefineRow](NxdDataSeDefineRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.se_define table (data table). |
| [NxdDataSeSystemRow](NxdDataSeSystemRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.se_system table (data table). |
| [NxdDataShopVoiceRow](NxdDataShopVoiceRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.shop_voice table (data table). |
| [NxdDataSortieConfirmRow](NxdDataSortieConfirmRow.md) | 48 | [Battle](../areas/battle.md) | One row of the nxd.sortie_confirm table (data table). |
| [NxdDataSoundEnhancedResourceRow](NxdDataSoundEnhancedResourceRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.sound_enhanced_resource table (data table). |
| [NxdDataSoundEnhancedRow](NxdDataSoundEnhancedRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.sound_enhanced table (data table). |
| [NxdDataSpeakerRow](NxdDataSpeakerRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.speaker table (English text table; the other languages share the layout). |
| [NxdDataSpellMessageRow](NxdDataSpellMessageRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.spell_message table (data table). |
| [NxdDataSubQuestMessageRow](NxdDataSubQuestMessageRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.sub_quest_message table (data table). |
| [NxdDataSystemBonusEntitlementRow](NxdDataSystemBonusEntitlementRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.system_bonus_entitlement table (data table). |
| [NxdDataSystemBonusItemContentsRow](NxdDataSystemBonusItemContentsRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.system_bonus_item_contents table (data table). |
| [NxdDataSystemBonusItemRow](NxdDataSystemBonusItemRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.system_bonus_item table (English text table; the other languages share the layout). |
| [NxdDataSystemBonusSpecialItemRow](NxdDataSystemBonusSpecialItemRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.system_bonus_special_item table (English text table; the other languages share the layout). |
| [NxdDataSystemParamRow](NxdDataSystemParamRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.system_param table (data table). |
| [NxdDataTelemetryAchievementGradeRow](NxdDataTelemetryAchievementGradeRow.md) | 4 | [Data access](../areas/data.md) | One row of the nxd.telemetry_achievement_grade table (data table). |
| [NxdDataTelemetryAchievementRow](NxdDataTelemetryAchievementRow.md) | 64 | [Data access](../areas/data.md) | One row of the nxd.telemetry_achievement table (English text table; the other languages share the layout). |
| [NxdDataTelemetryEventDefinitionRow](NxdDataTelemetryEventDefinitionRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.telemetry_event_definition table (data table). |
| [NxdDataTelemetryEventRow](NxdDataTelemetryEventRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.telemetry_event table (data table). |
| [NxdDataTelemetryObjectRow](NxdDataTelemetryObjectRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.telemetry_object table (data table). |
| [NxdDataTelemetryPropertyRow](NxdDataTelemetryPropertyRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.telemetry_property table (data table). |
| [NxdDataTelemetryPropertyValueRow](NxdDataTelemetryPropertyValueRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.telemetry_property_value table (data table). |
| [NxdDataTelemetryStatExtractionRow](NxdDataTelemetryStatExtractionRow.md) | 28 | [Data access](../areas/data.md) | One row of the nxd.telemetry_stat_extraction table (data table). |
| [NxdDataTelemetryStatRow](NxdDataTelemetryStatRow.md) | 32 | [Data access](../areas/data.md) | One row of the nxd.telemetry_stat table (data table). |
| [NxdDataTownImageRow](NxdDataTownImageRow.md) | 4 | [Data access](../areas/data.md) | One row of the nxd.town_image table (data table). |
| [NxdDataTownRow](NxdDataTownRow.md) | 52 | [Data access](../areas/data.md) | One row of the nxd.town table (English text table; the other languages share the layout). |
| [NxdDataTransitionRow](NxdDataTransitionRow.md) | 20 | [Display](../areas/display.md) | One row of the nxd.transition table (data table). |
| [NxdDataUDSActivityRow](NxdDataUDSActivityRow.md) | 28 | [Data access](../areas/data.md) | One row of the nxd.uds_activity table (data table). |
| [NxdDataUIAbilityIconRow](NxdDataUIAbilityIconRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_ability_icon table (data table). |
| [NxdDataUIAddonPriorityRow](NxdDataUIAddonPriorityRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_addon_priority table (data table). |
| [NxdDataUIAddonRow](NxdDataUIAddonRow.md) | 36 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_addon table (data table). |
| [NxdDataUIAnnounceRow](NxdDataUIAnnounceRow.md) | 28 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_announce table (data table). |
| [NxdDataUIAttributiveRow](NxdDataUIAttributiveRow.md) | 156 | [Data access](../areas/data.md) | One row of the nxd.ui_attributive table (data table). |
| [NxdDataUIButtonGuideRow](NxdDataUIButtonGuideRow.md) | 40 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_button_guide table (data table). |
| [NxdDataUIButtonRow](NxdDataUIButtonRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_button table (data table). |
| [NxdDataUIChronicleCharaListRow](NxdDataUIChronicleCharaListRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.ui_chronicle_chara_list table (data table). |
| [NxdDataUIChroniclePeriodRow](NxdDataUIChroniclePeriodRow.md) | 40 | [Data access](../areas/data.md) | One row of the nxd.ui_chronicle_period table (English text table; the other languages share the layout). |
| [NxdDataUIClassicSubtitlesRow](NxdDataUIClassicSubtitlesRow.md) | 28 | [Data access](../areas/data.md) | One row of the nxd.ui_classic_subtitles table (English text table; the other languages share the layout). |
| [NxdDataUIColorRow](NxdDataUIColorRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_color table (data table). |
| [NxdDataUICreditLineArtRow](NxdDataUICreditLineArtRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.ui_credit_line_art table (data table). |
| [NxdDataUICreditRowRow](NxdDataUICreditRowRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.ui_credit_row table (data table). |
| [NxdDataUIDialogRow](NxdDataUIDialogRow.md) | 60 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_dialog table (data table). |
| [NxdDataUIElementAttributeRow](NxdDataUIElementAttributeRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.ui_element_attribute table (English text table; the other languages share the layout). |
| [NxdDataUIEndCreditRow](NxdDataUIEndCreditRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.ui_end_credit table (data table). |
| [NxdDataUIEquipAbilitySlotRow](NxdDataUIEquipAbilitySlotRow.md) | 16 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_equip_ability_slot table (data table). |
| [NxdDataUIEquipDetailNumParamRow](NxdDataUIEquipDetailNumParamRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_equip_detail_num_param table (data table). |
| [NxdDataUIFilePathExchangeRow](NxdDataUIFilePathExchangeRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_file_path_exchange table (data table). |
| [NxdDataUIFontSetRow](NxdDataUIFontSetRow.md) | 100 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_font_set table (data table). |
| [NxdDataUIFontTypeRow](NxdDataUIFontTypeRow.md) | 24 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_font_type table (data table). |
| [NxdDataUIItemCategoryRow](NxdDataUIItemCategoryRow.md) | 32 | [Data access](../areas/data.md) | One row of the nxd.ui_item_category table (English text table; the other languages share the layout). |
| [NxdDataUiJobAbilityHelpRow](NxdDataUiJobAbilityHelpRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.ui_job_ability_help table (English text table; the other languages share the layout). |
| [NxdDataUIKeyAssignRow](NxdDataUIKeyAssignRow.md) | 48 | [Input](../areas/input.md) | One row of the nxd.ui_key_assign table (data table). |
| [NxdDataUIKeyboardKeyIconRow](NxdDataUIKeyboardKeyIconRow.md) | 8 | [Input](../areas/input.md) | One row of the nxd.ui_keyboard_key_icon table (data table). |
| [NxdDataUIKeyboardLayoutRow](NxdDataUIKeyboardLayoutRow.md) | 16 | [Input](../areas/input.md) | One row of the nxd.ui_keyboard_layout table (data table). |
| [NxdDataUIKeyboardTypeRow](NxdDataUIKeyboardTypeRow.md) | 28 | [Input](../areas/input.md) | One row of the nxd.ui_keyboard_type table (data table). |
| [NxdDataUIKeyConfigRow](NxdDataUIKeyConfigRow.md) | 16 | [Input](../areas/input.md) | One row of the nxd.ui_key_config table (data table). |
| [NxdDataUIKeyDefineRow](NxdDataUIKeyDefineRow.md) | 32 | [Input](../areas/input.md) | One row of the nxd.ui_key_define table (data table). |
| [NxdDataUILoadTexturePathRow](NxdDataUILoadTexturePathRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_load_texture_path table (data table). |
| [NxdDataUIMenuButtonLeftRow](NxdDataUIMenuButtonLeftRow.md) | 32 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_menu_button_left table (data table). |
| [NxdDataUIMenuSortListRow](NxdDataUIMenuSortListRow.md) | 16 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_menu_sort_list table (data table). |
| [NxdDataUIMenuTabRow](NxdDataUIMenuTabRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_menu_tab table (data table). |
| [NxdDataUIModalRow](NxdDataUIModalRow.md) | 24 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_modal table (data table). |
| [NxdDataUIMouseCollisionRow](NxdDataUIMouseCollisionRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_mouse_collision table (data table). |
| [NxdDataUIOpCreditRow](NxdDataUIOpCreditRow.md) | 32 | [Data access](../areas/data.md) | One row of the nxd.ui_op_credit table (data table). |
| [NxdDataUIPadDefineRow](NxdDataUIPadDefineRow.md) | 16 | [Input](../areas/input.md) | One row of the nxd.ui_pad_define table (data table). |
| [NxdDataUIPadGuideRow](NxdDataUIPadGuideRow.md) | 44 | [Input](../areas/input.md) | One row of the nxd.ui_pad_guide table (data table). |
| [NxdDataUIRow](NxdDataUIRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.ui_text table (English text table; the other languages share the layout). |
| [NxdDataUISituationSubtitlesRow](NxdDataUISituationSubtitlesRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.ui_situation_subtitles table (English text table; the other languages share the layout). |
| [NxdDataUISituationSubtitlesShowtimeRow](NxdDataUISituationSubtitlesShowtimeRow.md) | 8 | [Data access](../areas/data.md) | One row of the nxd.ui_situation_subtitles_showtime table (data table). |
| [NxdDataUIStatusEffectCategoryRow](NxdDataUIStatusEffectCategoryRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.ui_status_effect_category table (English text table; the other languages share the layout). |
| [NxdDataUIStatusEffectRow](NxdDataUIStatusEffectRow.md) | 36 | [Data access](../areas/data.md) | One row of the nxd.ui_status_effect table (English text table; the other languages share the layout). |
| [NxdDataUISubMenuRow](NxdDataUISubMenuRow.md) | 20 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_sub_menu table (data table). |
| [NxdDataUISubTabRow](NxdDataUISubTabRow.md) | 16 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_sub_tab table (data table). |
| [NxdDataUISubtitlesComponentRow](NxdDataUISubtitlesComponentRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.ui_subtitles_component table (data table). |
| [NxdDataUISubtitlesRow](NxdDataUISubtitlesRow.md) | 52 | [Data access](../areas/data.md) | One row of the nxd.ui_subtitles table (English text table; the other languages share the layout). |
| [NxdDataUISubtitlesTimelineRow](NxdDataUISubtitlesTimelineRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.ui_subtitles_timeline table (data table). |
| [NxdDataUISystemParamRow](NxdDataUISystemParamRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_system_param table (data table). |
| [NxdDataUITitleCreditRow](NxdDataUITitleCreditRow.md) | 20 | [Data access](../areas/data.md) | One row of the nxd.ui_title_credit table (data table). |
| [NxdDataUIUnitStatusNumParamRow](NxdDataUIUnitStatusNumParamRow.md) | 16 | [UI framework](../areas/ui-framework.md) | One row of the nxd.ui_unit_status_num_param table (data table). |
| [NxdDataUnitBarProfitResultMessageRow](NxdDataUnitBarProfitResultMessageRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.unit_bar_profit_result_message table (data table). |
| [NxdDataUnitCommunMessageRow](NxdDataUnitCommunMessageRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.unit_commun_message table (data table). |
| [NxdDataUnitHelpMessageRow](NxdDataUnitHelpMessageRow.md) | 44 | [Data access](../areas/data.md) | One row of the nxd.unit_help_message table (data table). |
| [NxdDataUnitPartMessageRow](NxdDataUnitPartMessageRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.unit_part_message table (data table). |
| [NxdDataUnitVoiceRow](NxdDataUnitVoiceRow.md) | 28 | [Data access](../areas/data.md) | One row of the nxd.unit_voice table (data table). |
| [NxdDataUnitWarnMessageRow](NxdDataUnitWarnMessageRow.md) | 12 | [Data access](../areas/data.md) | One row of the nxd.unit_warn_message table (data table). |
| [NxdDataUserSituationRow](NxdDataUserSituationRow.md) | 96 | [Data access](../areas/data.md) | One row of the nxd.user_situation table (data table). |
| [NxdDataVoicePatternRow](NxdDataVoicePatternRow.md) | 24 | [Data access](../areas/data.md) | One row of the nxd.voice_pattern table (data table). |
| [NxdDataVoicePatternSituationRow](NxdDataVoicePatternSituationRow.md) | 16 | [Data access](../areas/data.md) | One row of the nxd.voice_pattern_situation table (data table). |
| [NxdDataWorldMapProgressInfoRow](NxdDataWorldMapProgressInfoRow.md) | 44 | [Data access](../areas/data.md) | One row of the nxd.world_map_progress_info table (English text table; the other languages share the layout). |
| [NxdDataWorldSituationBalloonRow](NxdDataWorldSituationBalloonRow.md) | 76 | [Data access](../areas/data.md) | One row of the nxd.world_situation_balloon table (data table). |
| [NxdDataZodiacStoneOwnerTimelineRow](NxdDataZodiacStoneOwnerTimelineRow.md) | 16 | [Items and shops](../areas/items.md) | One row of the nxd.zodiac_stone_owner_timeline table (data table). |
| [NxdDataZodiacStoneRow](NxdDataZodiacStoneRow.md) | 40 | [Items and shops](../areas/items.md) | One row of the nxd.zodiac_stone table (English text table; the other languages share the layout). |
| [NxdTable](NxdTable.md) | 80 | [Data access](../areas/data.md) | One table object of the nxd registry (NxdRegistry_LoadRootNxl allocates one per root.nxl line); NxdTable_BindRows fills its entries from the loaded file and every row lookup reads it. |
| [OpeningSpriteListsRow](OpeningSpriteListsRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the OpeningSpriteLists table. |
| [OpeningStepMapsRow](OpeningStepMapsRow.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the OpeningStepMaps table. |
| [OptionChoice](OptionChoice.md) | 4 | [UI framework](../areas/ui-framework.md) | One row of the LegacyOptionsDefaultChoices table. |
| [OptionTextBase](OptionTextBase.md) | 4 | [UI framework](../areas/ui-framework.md) | One row of the LegacyOptionsTextBases table. |
| [PaletteColour](PaletteColour.md) | 2 | [UI framework](../areas/ui-framework.md) | One row of a UI palette block. |
| [PaletteCyclePair](PaletteCyclePair.md) | 4 | [Battle](../areas/battle.md) | One row of the EquipPanelPaletteCycle table. |
| [PaletteFormat](PaletteFormat.md) | 16 | [Graphics](../areas/graphics.md) | One row of the PaletteFormats table. |
| [PaletteIdWord](PaletteIdWord.md) | 2 | [Battle](../areas/battle.md) | One row of the StatusPanelPaletteIds table. |
| [PaletteIndexByteRow](PaletteIndexByteRow.md) | 1 | [Graphics](../areas/graphics.md) | One row of GfxColourCubeIndexImage. |
| [PanelStateOffset](PanelStateOffset.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the PanelStateOffsets table. |
| [PartyFaceIndexRow](PartyFaceIndexRow.md) | 1 | [Graphics](../areas/graphics.md) | One face record index. |
| [PartyFaceRecordRow](PartyFaceRecordRow.md) | 12 | [Graphics](../areas/graphics.md) | One portrait rectangle record. |
| [PartyHandWord](PartyHandWord.md) | 2 | [Items and shops](../areas/items.md) | One equipment slot of a party unit: the item id in bits 0..9 and bit 15 as the Outfitter-session pending flag. |
| [PartyUnitRecord](PartyUnitRecord.md) | 640 | [Unit data](../areas/unit-data.md) | A unit as the party, status and job screens read it (55 records at g_PartyUnitRecords, reached through g_PartyUnits). |
| [PoachListEntry](PoachListEntry.md) | 48 | [Items and shops](../areas/items.md) | One entry of the poacher list that PoachList_Build fills: a poach id the party holds. |
| [PopupBounceStep](PopupBounceStep.md) | 2 | [Battle](../areas/battle.md) | One row of the PopupBounceCurve table. |
| [PortraitCodeRow](PortraitCodeRow.md) | 2 | [Graphics](../areas/graphics.md) | One portrait code word. |
| [PoseCodeFlag](PoseCodeFlag.md) | 1 | [Event system](../areas/event-system.md) | One row of the EventPoseCodeFlags table. |
| [PostBattleCalc](PostBattleCalc.md) | 3400 | [Battle](../areas/battle.md) | The per-formula post-processing object of a battle: a virtual function table pointer and 106 rows of 32 bytes, one per formula id, that sub_14030A11C runs after a formula handler. |
| [PostBattleCalcRow](PostBattleCalcRow.md) | 32 | [Battle](../areas/battle.md) | One row of PostBattleCalc: an entry thunk, its argument, and the callback the thunk jumps to. |
| [PowerOfTen](PowerOfTen.md) | 4 | [Data access](../areas/data.md) | One row of the PowersOfTen table. |
| [PrimeNumbersRow](PrimeNumbersRow.md) | 1 | [Math](../areas/math.md) | One row of the PrimeNumbers table. |
| [RandomEncounterRow](RandomEncounterRow.md) | 24 | [Event system](../areas/event-system.md) | One row of the RandomEncounters table. |
| [RangeRowMasksRow](RangeRowMasksRow.md) | 2 | [Battle](../areas/battle.md) | One row of the RangeRowMasks table. |
| [RenderContext](RenderContext.md) | 6032 | [Graphics](../areas/graphics.md) | The per-thread draw state every pass fills before it packs a command: sort key, clip rectangle, render target, blend and raster words, vertex/index buffers and three binding tables (constant buffers, textures, sampler... |
| [Renderer](Renderer.md) |  | [Graphics](../areas/graphics.md) | The renderer object (global g_Renderer): output size, the render-target table and the per-type target slot tables, and the UI manager. |
| [Rgb555Colour](Rgb555Colour.md) | 2 | [UI framework](../areas/ui-framework.md) | One row of the LegacyCursorPalette table. |
| [RgbaColourRow](RgbaColourRow.md) | 4 | [Graphics](../areas/graphics.md) | One row of GfxColourCubePalette. |
| [RoadPointListPointer](RoadPointListPointer.md) | 8 | [Event system](../areas/event-system.md) | One row of the RoadPointLists table. |
| [RuntimeJobListEntry](RuntimeJobListEntry.md) | 2 | [Job data](../areas/job-data.md) | One entry of the Change Job list as built by the game. |
| [SaveEquipSet](SaveEquipSet.md) | 88 | [Save data](../areas/save-data.md) | One saved equipment set of a unit (three per unit record). |
| [SaveErrorMessage](SaveErrorMessage.md) | 8 | [Save data](../areas/save-data.md) | One row of the SaveErrorMessages table. |
| [SaveFieldDescriptor](SaveFieldDescriptor.md) | 88 | [Save data](../areas/save-data.md) | One field of a saved record, as the save walker reads it (built on the stack by each schema function). |
| [SaveManager](SaveManager.md) |  | [Save data](../areas/save-data.md) | The two singletons the save path runs on, with the fields it uses: the save-I/O state object that holds the frame step's command and sub-state, and the save manager object that holds the 50-slot image the `fftsave.bin... |
| [SaveRequestRecord](SaveRequestRecord.md) | 328 | [Save data](../areas/save-data.md) | One queued file request of the save container manager: the consumer object, the entry name, the delivery buffer and its status. |
| [ScenarioSetupRow](ScenarioSetupRow.md) | 24 | [Event system](../areas/event-system.md) | One row of the ScenarioSetup table: the scene setup of one story event, keyed by the event number; read field by field by ScenarioSetup_ApplyRecord (scene variables) and turned into the per-event word. |
| [SceneSpriteFaceRow](SceneSpriteFaceRow.md) | 4 | [Graphics](../areas/graphics.md) | One face number. |
| [SceneUnitSlot](SceneUnitSlot.md) | 1352 | [Graphics](../areas/graphics.md) | One of the 16 scene-unit records at 0x140D30038 (stride 0x548) that SceneUnit_BuildFromQueueEntry builds for a queued unit; the code addresses it by the pointer it returns, the in-use dword sits 8 bytes before that po... |
| [SceneWindowColourRow](SceneWindowColourRow.md) | 20 | [UI framework](../areas/ui-framework.md) | One row of BattleSceneWindowColours. |
| [SceneWindowTemplateRow](SceneWindowTemplateRow.md) | 84 | [UI framework](../areas/ui-framework.md) | One row of BattleSceneWindowTemplatesLang0. |
| [ScreenTaskSetRow](ScreenTaskSetRow.md) | 64 | [UI framework](../areas/ui-framework.md) | One row of the ScreenTaskSets table: up to four task slots started together. |
| [ScriptedActorPresetsRow](ScriptedActorPresetsRow.md) | 8 | [Battle](../areas/battle.md) | One row of the ScriptedActorPresets table. |
| [SectorAndSize](SectorAndSize.md) | 8 | [Unit rendering](../areas/unit-rendering.md) | One row of the BattleSpriteFilesLanguage0 table and the tables that share its shape. |
| [SectorOnly](SectorOnly.md) | 4 | [Resource](../areas/resource.md) | One row of the MapBlockSectorsLanguage0 table and the tables that share its shape. |
| [SettlementEventPick](SettlementEventPick.md) | 10 | [Event system](../areas/event-system.md) | One row of the SettlementEventPicks table. |
| [ShopEntry](ShopEntry.md) | 40 | [Items and shops](../areas/items.md) | One entry of a shop item list (buy, sell or equip), built per list index by ShopEntry_Fill from word_141811470 and drawn by ShopItemList_DrawRow. |
| [ShopRowCallbackTable](ShopRowCallbackTable.md) | 56 | [Items and shops](../areas/items.md) | The seven qword row handlers at 0x141876AD0..0x141876B00 that the list gadget calls per visible row; the shop, equip and item screens install different functions in the same slots. |
| [ShopScreenPaletteRow](ShopScreenPaletteRow.md) | 2 | [Graphics](../areas/graphics.md) | One row of the ShopScreenPalette table. |
| [SkillsetRow](SkillsetRow.md) | 25 | [Job data](../areas/job-data.md) | One 25-byte skillset: three bytes of ability bit-9 flags followed by 22 low ability id bytes. |
| [SlideCurveStep](SlideCurveStep.md) | 2 | [UI framework](../areas/ui-framework.md) | One row of the PanelSlideCurve table. |
| [SlotPermutationRow](SlotPermutationRow.md) | 16 | [Graphics](../areas/graphics.md) | One row of SceneSlotPermutations. |
| [SpriteAnimScriptsRow](SpriteAnimScriptsRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the SpriteAnimScripts table. |
| [SpriteClassicFileRow](SpriteClassicFileRow.md) | 8 | [Graphics](../areas/graphics.md) | Where one classic sprite file is and how long it is. |
| [SpriteDirectionFlag](SpriteDirectionFlag.md) | 2 | [Unit rendering](../areas/unit-rendering.md) | One row of the SpriteDirection16MirrorFlags table. |
| [SpriteDirectionTablesRow](SpriteDirectionTablesRow.md) | 1 | [Graphics](../areas/graphics.md) | One row of SpriteDirectionTables. |
| [SpriteHdEntryRow](SpriteHdEntryRow.md) | 4 | [Graphics](../areas/graphics.md) | One HD sheet entry number. |
| [SpriteKindFlagRow](SpriteKindFlagRow.md) | 1 | [Graphics](../areas/graphics.md) | One row of SpriteEffectKindFlags. |
| [SpriteLayerByteRow](SpriteLayerByteRow.md) | 1 | [Graphics](../areas/graphics.md) | One row of SpriteLayerByteRows. |
| [SpriteLookAttributeRow](SpriteLookAttributeRow.md) | 4 | [Graphics](../areas/graphics.md) | One look attribute row. |
| [SpriteMotionByKindRow](SpriteMotionByKindRow.md) | 1 | [Graphics](../areas/graphics.md) | One row of SpriteMotionByKind. |
| [SpritePaletteLimit](SpritePaletteLimit.md) | 1 | [Unit rendering](../areas/unit-rendering.md) | One row of the SpritePaletteLimits table. |
| [SpritePieceTemplate](SpritePieceTemplate.md) | 24 | [Event system](../areas/event-system.md) | One row of the WorldMapSpritePieceTemplates table. |
| [StatusIconFlagMaskRow](StatusIconFlagMaskRow.md) | 4 | [Battle](../areas/battle.md) | One row of BattleStatusIconFlagMasks. |
| [StatusPanelFrameLine](StatusPanelFrameLine.md) | 7 | [Battle](../areas/battle.md) | One row of the StatusPanelFrameLines table. |
| [StatusPropertyRow](StatusPropertyRow.md) | 16 | [Battle](../areas/battle.md) | Properties of one status. |
| [StringPointerRow](StringPointerRow.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of a string pointer table (ResumeKindNames, SoundPackPathPatterns, UiCoreNameKeys, DeflateErrorMessages). |
| [SurfacePairConstant](SurfacePairConstant.md) | 2 | [Battle](../areas/battle.md) | One row of the SurfacePairConstants table. |
| [TerrainPropertiesRow](TerrainPropertiesRow.md) | 1 | [Battle](../areas/battle.md) | One byte of a TerrainProperties block (two blocks of 64). |
| [TextPackPathsRow](TextPackPathsRow.md) | 8 | [Resource](../areas/resource.md) | One row of the TextPackPaths table. |
| [TextPointerRow](TextPointerRow.md) | 8 | [Resource](../areas/resource.md) | One row of a table of text pointers (audio loader errors, mixer names, XML status names, value type names). |
| [TextureIdRow](TextureIdRow.md) | 4 | [Graphics](../areas/graphics.md) | One row of SpriteShapeHdTexture. |
| [TextureWindowWordRow](TextureWindowWordRow.md) | 2 | [Graphics](../areas/graphics.md) | One row of GfxTextureWindowParams. |
| [TownMenuKind](TownMenuKind.md) | 4 | [Event system](../areas/event-system.md) | One row of the TownMenuKindBySettlement table. |
| [TriggerConditionArgCount](TriggerConditionArgCount.md) | 1 | [Event system](../areas/event-system.md) | One row of the TriggerConditionArgCounts table. |
| [TrigSample](TrigSample.md) | 4 | [Math](../areas/math.md) | One row of the CosineTable table. |
| [UIAddonFFTOConfig](UIAddonFFTOConfig.md) | 3416 | [UI framework](../areas/ui-framework.md) | The General Options screen object (3416 bytes, `Mem_Alloc(3416)` in 0x140182478): base `UIAddonMenuBase`, vtable 0x14070DB30 with 18 entries (RTTI locator at 0x14070DB28). |
| [UIAddonFFTOTitle](UIAddonFFTOTitle.md) | 240 | [UI framework](../areas/ui-framework.md) | The title menu screen object (240 bytes, `Mem_Alloc(240)` in UIAddonFFTOTitle_Create): base `UIAddonMenuBase`, primary vtable 0x14070A4B0 and a second vtable 0x14070A460 at +48 (the `UIFFTOMenuFunctionBase` part). |
| [UIAddonFingerCursor](UIAddonFingerCursor.md) |  | [UI framework](../areas/ui-framework.md) | The finger cursor addon: the loaded cursor widget (ffto_finger_cursor.uib), the parts it moves, and the glide state of GUICursorHand_StepToward. |
| [UIAgentCursor](UIAgentCursor.md) |  | [UI framework](../areas/ui-framework.md) | The cursor agent: element 1 of the addon manager's agent vector (global qword_143CD9DA8, vector at +16). |
| [UIAgentFFTOSystem](UIAgentFFTOSystem.md) | 1472 | [UI framework](../areas/ui-framework.md) | The System agent: entry 37 of the agent manager's array (`*(qword_143CD9DA8 + 16) + 37 * 8`, as Boot_Update reads it); 1472 bytes, constructor 0x140181C94, vtable 0x14070DF00. |
| [UIAgentFFTOTitle](UIAgentFFTOTitle.md) | 1448 | [UI framework](../areas/ui-framework.md) | The title screens' agent (1448 bytes, `Mem_Alloc(0x5A8)` in `UIAgentManager_CreateAgents` at 0x1401CFA4D; vtable 0x14070A5B0, constructor 0x1401C2AE4). |
| [UIGadgetFFTOConfigConfirmWindow](UIGadgetFFTOConfigConfirmWindow.md) |  | [UI framework](../areas/ui-framework.md) | The confirm window gadget of General Options (+2400; vtables 0x140712448 and 0x1407124A0): a message and up to three option buttons loaded from a UIDialog row. |
| [UIListGadget](UIListGadget.md) |  | [UI framework](../areas/ui-framework.md) | The row list gadget used by General Options (constructor 0x14028C458, bound by 0x14028C5C4 with tag 151 and the part name `List`). |
| [UIManager](UIManager.md) |  | [UI framework](../areas/ui-framework.md) | The UI manager object at Renderer.ui_manager: the shader selectors of the UI technique and the shared layer quad buffers. |
| [UiNumberField](UiNumberField.md) | 32 | [Battle](../areas/battle.md) | One row of the StatusNumbersActorA table and the tables that share its shape. |
| [UiRect](UiRect.md) | 8 | [UI framework](../areas/ui-framework.md) | One screen or VRAM rectangle of a panel. |
| [UIRender](UIRender.md) |  | [UI framework](../areas/ui-framework.md) | The UI render object (the command ring): the slot ids it resolved by name when it was created, used by every UI draw. |
| [UiScriptRecord](UiScriptRecord.md) |  | [UI framework](../areas/ui-framework.md) | One record of a UI script: an opcode byte, a length byte and the arguments. |
| [UiSpriteCell](UiSpriteCell.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of the MessageWindowTagCellsLanguage2 table and the tables that share its shape. |
| [UnitEditorRange](UnitEditorRange.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the UnitEditorRanges tables. |
| [UnitEditorWidget](UnitEditorWidget.md) | 24 | [UI framework](../areas/ui-framework.md) | One row of the UnitEditorWidgets tables. |
| [UnitJobFlagsBlock](UnitJobFlagsBlock.md) | 146 | [Job data](../areas/job-data.md) | The job flag block (g_UnitJobFlags). |
| [UnitSaveRecord](UnitSaveRecord.md) | 600 | [Unit data](../areas/unit-data.md) | A unit as the save keeps it (54 records at g_UnitSaveData; copied whole into the save slot at +1304 + 600 n). |
| [UnitSpritePosePackRow](UnitSpritePosePackRow.md) | 2 | [Graphics](../areas/graphics.md) | One row of the UnitSpritePosePack table. |
| [UnitWorkRecord](UnitWorkRecord.md) | 512 | [Unit data](../areas/unit-data.md) | The working copy of a unit: the 21 battle units (g_BattleUnits) and temporary copies for previews and the job screens. |
| [WeaponHitSoundCuesRow](WeaponHitSoundCuesRow.md) | 1 | [Battle](../areas/battle.md) | One row of BattleWeaponHitSoundCues. |
| [WeatherBySeasonRow](WeatherBySeasonRow.md) | 56 | [Math](../areas/math.md) | The whole WeatherBySeason object. |
| [WindowCellRecordRow](WindowCellRecordRow.md) | 12 | [UI framework](../areas/ui-framework.md) | One row of UiLegacyWindowCellLayoutBase. |
| [WindowColourSetRow](WindowColourSetRow.md) | 4 | [UI framework](../areas/ui-framework.md) | One row of UiLegacyWindowColourSetsLang1. |
| [WindowCurvePointer](WindowCurvePointer.md) | 8 | [UI framework](../areas/ui-framework.md) | One row of the WindowCurvePointers table. |
| [WindowGroupStartRow](WindowGroupStartRow.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of UiLegacyWindowGroupStartsLang0. |
| [WindowGrowStep](WindowGrowStep.md) | 1 | [UI framework](../areas/ui-framework.md) | One row of the WindowGrowSteps table. |
| [WindowPatternWord](WindowPatternWord.md) | 2 | [UI framework](../areas/ui-framework.md) | One row of the WindowPatternTiles table. |
| [WorldMapRoad](WorldMapRoad.md) | 8 | [Event system](../areas/event-system.md) | One row of the WorldMapRoads table. |
