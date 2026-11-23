# Tables

Where the game keeps its data tables, NXD files and the fixed tables inside the executable: what each holds, how it is keyed, how big its rows are, and which code reads it. Describes the tables; it does not reproduce their contents.

674 records. Format of a record: [kinds/table.json](../../kinds/table.json). Data: [data/tables.jsonl](../../data/tables.jsonl).

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [Ability](Ability.md) | NXD file | 39 |  | The ability rows the game reads through AbilityTable_GetRow, loaded lazily and cached. |
| [AbilityActionRecords](AbilityActionRecords.md) | Executable |  | 368 records of 20 bytes (ids 0..0x16F) | The action record of each action ability. |
| [AbilityActionWorking](AbilityActionWorking.md) | Executable (filled at run time) |  | 368 records of 20 bytes | Working copy of AbilityActionRecords built at first use and read by every action builder. |
| [AbilityAnim](AbilityAnim.md) | Executable |  | 454 rows of 3 bytes | Battle presentation of each ability: charge type, execution motion and text selector. |
| [AbilityAux](AbilityAux.md) | Executable |  | 512 rows of 8 bytes | The per-ability auxiliary records: classic JP cost, learn percent and two flag fields. |
| [AbilityEffectNumbers](AbilityEffectNumbers.md) | Executable |  | 454 rows of 2 bytes | Battle effect number and flag of each ability. |
| [AbilityEventPairs](AbilityEventPairs.md) | Executable |  | 15 rows of 4 bytes | Pairs (key, event variable) that mark achievements when the job screen learns something; the object starts 0x30 earlier and also holds an unreferenced 16-byte list and a vtable. |
| [AbilityKind1_ItemByAbility](AbilityKind1_ItemByAbility.md) | Executable |  | 14 rows of 1 byte | Item-command table: ability 368 + i maps to one item id; the only table that pairs an Item-command ability with its item. |
| [AbilityKind2_ThrowCategory](AbilityKind2_ThrowCategory.md) | Executable |  | 12 rows of 1 byte | Throw table: ability 382 + i maps to one equip category; an item is throwable when its category matches a row of one of the unit throw abilities. |
| [AbilityKind3_JumpReach](AbilityKind3_JumpReach.md) | Executable |  | 12 rows of 2 bytes | Horizontal and vertical reach of each Jump ability. |
| [AbilityKind4_Charge](AbilityKind4_Charge.md) | Executable |  | 8 rows of 2 bytes | Charge time and power of each Charge ability. |
| [AbilityKind5_MathMask](AbilityKind5_MathMask.md) | Executable |  | 8 rows of 1 byte | Arithmeticks bit mask of each ability. |
| [AbilityKind6_PassiveIndex](AbilityKind6_PassiveIndex.md) | Executable |  | 90 rows of 1 byte | Running index of every passive ability. |
| [AudioBusAndEffectNames](AudioBusAndEffectNames.md) | Executable |  | 36 text pointers then 5 function pointers | Names of the audio mixer: eight bus names, the master output name, a second bus list, one shared string, nineteen effect names (reverb, echo, biquad, band pass, compressor, delay, pitch shifter, equalisers, chorus, fl... |
| [AudioCueLoadErrorNames](AudioCueLoadErrorNames.md) | Executable |  | 7 rows of 8 bytes | Names of the error codes of the audio cue sheet loader: no error, failed to register file, failed to open, failed to load wave bank, invalid wave bank path, failed to calculate work size, failed to allocate memory. |
| [AudioDspCoefficientBlockPointers](AudioDspCoefficientBlockPointers.md) | Executable |  | 80 rows of 8 bytes (82 in the sweep run) | Pointer lists to the 1024-byte float coefficient blocks of the audio library DSP; 32 distinct blocks, the pointer pattern is a, b, b, a repeated per channel pair. |
| [AudioTableValueTypeNames](AudioTableValueTypeNames.md) | Executable |  | 13 rows of 8 bytes | Names of the value types of the audio library data tables: signed and unsigned 8 / 16 / 32 / 64 bit integers, 32 and 64 bit floats, string, variable length data and chunk data. |
| [AudioTableValueTypeNamesAlt](AudioTableValueTypeNamesAlt.md) | Executable |  | 13 rows of 8 bytes | The same value types as AudioTableValueTypeNames in the audio library own spelling; slot 12 is a GUID. Verdict: text. |
| [BannerWordCells](BannerWordCells.md) | Executable (initialised data) |  | 204 rows of 12 bytes | Sprite cells that build the 64 banner word images. |
| [BannerWordColours](BannerWordColours.md) | Executable (initialised data) |  | 4 rows of 4 bytes | Corner colours of the banner word gradient. |
| [BannerWordRanges](BannerWordRanges.md) | Executable |  | 65 rows of 4 bytes | For each of 64 banner word images, which run of sprite cells builds it. |
| [BattleEffectLabelRectsLang0](BattleEffectLabelRectsLang0.md) | Executable |  | 60 rows of 4 bytes | Texture rectangles of the effect label pictures for text language 0. |
| [BattleEffectLabelRectsLang1](BattleEffectLabelRectsLang1.md) | Executable |  | 60 rows of 4 bytes | Texture rectangles of the effect label pictures for text language 1. |
| [BattleEffectLabelRectsLang2](BattleEffectLabelRectsLang2.md) | Executable |  | 60 rows of 4 bytes | Texture rectangles of the effect label pictures for text language 2. |
| [BattleEffectLabelRectsLang3](BattleEffectLabelRectsLang3.md) | Executable |  | 60 rows of 4 bytes | Texture rectangles of the effect label pictures for text language 3. |
| [BattleMenuRowScreenCodes](BattleMenuRowScreenCodes.md) | Executable |  | 24 rows of 1 bytes | Per battle-menu row id, the screen or message code its confirm opens. |
| [BattlePanelNumbersActor](BattlePanelNumbersActor.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the battle unit panel, actor side (HP and MP with maxima, Wt, At, level, experience). |
| [BattlePanelNumbersTarget](BattlePanelNumbersTarget.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the battle unit panel, target side. |
| [BattleRangeMarks](BattleRangeMarks.md) | Executable (filled at run time) |  | 2560 entries of 1 byte | Range-mark array: 512 records of 5 bytes, index x + y * width + 256 * layer (layer 1 at +0x500). |
| [BattleSceneWindowColours](BattleSceneWindowColours.md) | Executable |  | 6 rows of 20 bytes | Corner colours (four per row) of the battle scene window gradients. |
| [BattleSceneWindowTemplatesDefault](BattleSceneWindowTemplatesDefault.md) | Executable |  | 920 bytes of window records | Window records (rectangles, flags, pointers) of the battle scene screen, default for other languages. |
| [BattleSceneWindowTemplatesLang0](BattleSceneWindowTemplatesLang0.md) | Executable |  | 800 bytes of window records | Window records (rectangles, flags, pointers) of the battle scene screen, text language 0. |
| [BattleSpriteFilesLanguage0](BattleSpriteFilesLanguage0.md) | Executable (initialised data) |  | 170 rows of 8 bytes | Where each battle sprite sheet's data is, for text language 0. |
| [BattleSpriteFilesOtherLanguages](BattleSpriteFilesOtherLanguages.md) | Executable (initialised data) |  | 170 rows of 8 bytes | Where each battle sprite sheet's data is, for text languages other than 0. |
| [BattleSpriteHdTextures](BattleSpriteHdTextures.md) | Executable |  | 170 rows of 4 bytes (172 to the next symbol) | Per battle sprite sheet, its HD texture id. |
| [BattleStatusIconFlagMasks](BattleStatusIconFlagMasks.md) | Executable |  | 40 rows of 4 bytes (42 to the next symbol) | Per status id the bit mask that marks the status on the battle scene object (drawing side). |
| [BattleTiles](BattleTiles.md) | Executable (filled at run time) |  | 512 records of 8 bytes | The battle map tile table: flags and movement cost per tile, filled by the map setup from the map's level record. |
| [BattleUnits](BattleUnits.md) | Executable (filled at run time) |  | 21 records of 512 bytes | The live battle unit table: hit points, magic points, tile, facing, charge time and action words. |
| [BattleWeaponHitSoundCues](BattleWeaponHitSoundCues.md) | Executable |  | 3 rows of 32 bytes | Sound cue (+1) played when an attack effect hits, per weapon type, in three variants. |
| [BlendModeAlpha](BlendModeAlpha.md) | Executable |  | 4 rows of 1 bytes | Alpha for each of the four semi-transparency modes (half, add, subtract, quarter). |
| [BoneLinkPairs](BoneLinkPairs.md) | Executable |  | 33 rows of 16 bytes | The 33 bone name pairs that define the chains of a model skeleton (spine, neck, head, arms, hands, fingers, legs, toes, jaw, face, nose flap, forearm and shin extension bones, waist, tail segments). |
| [C_Mes_Id_Sample](C_Mes_Id_Sample.md) | NXD file | 172 |  | The battle message text table: CMesId_GetText reads one row by message id and the registry result is cached in g_CMesIdTable. |
| [CalendarDaysBeforeMonth](CalendarDaysBeforeMonth.md) | Executable |  | 12 rows of 2 bytes | Days of a non-leap year before each month. |
| [CalendarDaysPerMonth](CalendarDaysPerMonth.md) | Executable |  | 13 rows of 1 byte | Days per month for the new-game birthday picker (February 28); right behind it a table of the 12 zodiac sign start dates (month, day) and a dword table of 7 values (75 to 465, step 65). |
| [CalendarTrackedDates](CalendarTrackedDates.md) | Executable |  | 64 rows of 2 bytes | Month and day of 63 tracked dates; slot 0 is the player's date from event variables 95 and 96. |
| [CharaRectSizeTable](CharaRectSizeTable.md) | Executable (constant) |  |  | Width and height of a frame rectangle by its size code, in 8-pixel units (width at 2 * code, height at 2 * code + 4 words): read by CharaRender_DrawFrame. |
| [ChargeMotionPairs](ChargeMotionPairs.md) | Executable (constant) |  |  | 2 bytes per charge type of g_AbilityAnim: +0 the motion sub_140206C14 sets, +1 the motion BattleAnim_SetChargeMotion sets (each + 1; 0 = none) |
| [CharGridOrder](CharGridOrder.md) | Executable |  | 97 rows of 1 bytes | Which symbol each cell of the 97-cell character selection grid shows. |
| [ClassicLoadWindowDefault](ClassicLoadWindowDefault.md) | Executable (initialised data, written at run time) |  | ? | Window template and live fields of the classic load menu, one of three language variants. |
| [ClassicSaveListLanguage0](ClassicSaveListLanguage0.md) | Executable (initialised data, written at run time) |  | 1 rows of 176 bytes | Template and cursor of the classic save list, language 0 variant. |
| [ClassicSaveWindowALanguage0](ClassicSaveWindowALanguage0.md) | Executable (initialised data) |  | 1 bytes | Classic save / load menu window template A, language 0. |
| [ClassicSaveWindowAOtherLanguages](ClassicSaveWindowAOtherLanguages.md) | Executable (initialised data) |  | 1 bytes | Classic save / load menu window template A, other languages. |
| [ClassicSaveWindowBLanguage0](ClassicSaveWindowBLanguage0.md) | Executable (initialised data) |  | 1 bytes | Classic save / load menu window template B, language 0. |
| [ClassicSaveWindowBOtherLanguages](ClassicSaveWindowBOtherLanguages.md) | Executable (initialised data) |  | 1 bytes | Classic save / load menu window template B, other languages. |
| [ClutFadeStep32](ClutFadeStep32.md) | Executable (constant) |  | 63 rows of 32 entries of 1 byte | Step table of the 32-step palette fade, same layout. |
| [ClutFadeStep8](ClutFadeStep8.md) | Executable (constant) |  | 63 rows of 8 entries of 1 byte | Step table of the 8-step palette fade: row = distance + 31, entry = how far the channel moves on that step; the entries of a row add up to the distance. |
| [CommandKind](CommandKind.md) | Executable |  | 256 rows of 1 byte | The command kind of each skillset id: the battle range and action builders switch on it to decide how the skillset acts. |
| [CommandKindMessageOffsets](CommandKindMessageOffsets.md) | Executable |  | 24 rows of 1 bytes | Offset of the screen / message code of each battle command kind (code = 0x1000 + offset). |
| [CommandKindParams](CommandKindParams.md) | Executable (initialised data) |  | 16 rows of 4 bytes | Two small values for each battle command kind; the same 16 rows sit in front of the stock menu step table. |
| [CommandMenuSteps](CommandMenuSteps.md) | Executable (initialised data) |  | 61 rows of 32 bytes | The 61 rows of the stock battle menu step table with the task pointer of the command menu task. |
| [CosineTable](CosineTable.md) | Executable |  | 4097 rows of 4 bytes | Shared cosine lookup: 4097 signed 32-bit samples (the last repeats the first so an interpolation can read index + 1), then 12 bytes of padding up to the sine table. |
| [DeflateErrorMessages](DeflateErrorMessages.md) | Executable |  | 10 rows of 8 bytes | Result code messages of the embedded compression library in its usual order: need dictionary, stream end, (empty), file error, stream error, data error, insufficient memory, buffer error, incompatible version, (empty). |
| [DissolveOffsets](DissolveOffsets.md) | Executable (initialised data) |  | 32 rows of 64 bytes | Pixel-order table of a dissolve (reveal) effect: 32 steps, each with 32 offsets. |
| [EaseCurvesSetA](EaseCurvesSetA.md) | Executable |  | 56 rows of 4 bytes | Easing curve set for legacy screen animations: 6 curves of 9 samples (linear up, linear down, ease up, ease down, bump, constant 1.0) plus a short tail. |
| [EaseCurvesSetB](EaseCurvesSetB.md) | Executable |  | 44 rows of 4 bytes | Easing curve set b: 44 samples in 9-sample curves (five-step ramps, S-curves and two bumps). |
| [EaseCurvesSetC](EaseCurvesSetC.md) | Executable |  | 20 rows of 4 bytes | Easing curve set c: 20 samples of small step curves (0, 0x800, 0x1000 ramps). |
| [EaseCurvesSetD](EaseCurvesSetD.md) | Executable |  | 36 rows of 4 bytes | Easing curve set d: 36 samples (4 curves of 9: ramp, S-curve, bumps). |
| [EaseCurvesSetE](EaseCurvesSetE.md) | Executable |  | 72 rows of 4 bytes | Easing curve set e: 72 samples (8 curves of 9), the shapes of set a plus a decay curve. |
| [EaseCurvesSetF](EaseCurvesSetF.md) | Executable |  | 120 rows of 4 bytes | Easing curve set f: 120 samples, curves of 33 steps (long ramps and S-curves) for slower animations. |
| [EaseCurvesSetG](EaseCurvesSetG.md) | Executable |  | 6 rows of 8 bytes | Six start and end factors (0 to 1.0, 1.0 to 0, ...) used as ramp endpoints. |
| [EaseCurvesSetH](EaseCurvesSetH.md) | Executable |  | 5 rows of 12 bytes | Short 3-sample curves; the 0x80-byte object ends with a list of byte pairs (cell step offsets) that this reader does not use. |
| [EffectBlendWeights](EffectBlendWeights.md) | Executable |  | 5 rows of 7 bytes | Four ramps of seven 0..255 blend weights for the flash effect and a fifth row listing five palette slots. |
| [EffectFileLocatorsLang0](EffectFileLocatorsLang0.md) | Executable |  | 512 rows of 8 bytes | Pack file number and size of every battle effect file (text language 0). |
| [EffectFileLocatorsLangOther](EffectFileLocatorsLangOther.md) | Executable |  | 512 rows of 8 bytes | Pack file number and size of every battle effect file (text language 1, 2 or 3 (and when no language record exists)). |
| [EffectFlashProfiles](EffectFlashProfiles.md) | Executable |  | 4 rows of 14 bytes | Seven parameter words per screen flash profile (timing and strength values; the high byte of the last word picks a blend weight row). |
| [EffectKindRecords](EffectKindRecords.md) | Executable |  | 22 rows of 4 bytes | One row per effect kind: the sequence handler kind that runs it and a parameter word. |
| [EffectNumberPseudo](EffectNumberPseudo.md) | Executable |  | 37 rows of 2 bytes | Effect number per pseudo effect word. |
| [EffectPaletteSeeds](EffectPaletteSeeds.md) | Executable |  | 6 rows of 3 bytes | Six 5-bit RGB colours packed into the effect palette at the start of the palette effect. |
| [EffectPoseBlendKeys](EffectPoseBlendKeys.md) | Executable |  | 10 blocks of 16 bytes | Ten blocks of 16-bit fixed point (4096 = 1.0) ramp values copied by a sprite effect update. |
| [EffectSpriteSpawnRecords](EffectSpriteSpawnRecords.md) | Executable |  | 12 rows of 46 bytes | One record per effect sprite group: sprite definition index, frame window, live limit, parameter block and the number of sprites to create. |
| [ElementColours](ElementColours.md) | Executable |  | 9 rows of 3 bytes | RGB tint per element for effect flashes. |
| [ElementMaskOrder](ElementMaskOrder.md) | Executable |  | 9 rows of 1 byte | The element bit mask of each element slot of ElementColours: 0 (none), then the bits 0x80, 0x04, 0x08, 0x10, 0x02, 0x01, 0x20, 0x40. |
| [EmbeddedTimImageA](EmbeddedTimImageA.md) | Executable (initialised data) |  | 1 block of 2368 bytes | A 4-bit image with its 16-colour palette in the legacy container format (magic 0x10, flags, palette block, image block), read by the world map code. |
| [EquipmentOrderListPointers](EquipmentOrderListPointers.md) | Executable |  | 4 rows of 8 bytes | Pointers to the four saved equipment order lists; the next eleven pointers of the run belong to other lists. |
| [EquipPanelCellsLanguage0A](EquipPanelCellsLanguage0A.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Sprite cells of the equipment / ability status panel, language 0, variant a. |
| [EquipPanelCellsLanguage0B](EquipPanelCellsLanguage0B.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 0, variant b. |
| [EquipPanelCellsLanguage0V0](EquipPanelCellsLanguage0V0.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 0, variant 0 (19 cells). |
| [EquipPanelCellsLanguage0V1](EquipPanelCellsLanguage0V1.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 0, variant 1 (19 cells). |
| [EquipPanelCellsLanguage0V2](EquipPanelCellsLanguage0V2.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 0, variant 2 (19 cells). |
| [EquipPanelCellsLanguage0V3](EquipPanelCellsLanguage0V3.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 0, variant 3 (19 cells). |
| [EquipPanelCellsLanguage2A](EquipPanelCellsLanguage2A.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 2, variant a. |
| [EquipPanelCellsLanguage2B](EquipPanelCellsLanguage2B.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 2, variant b. |
| [EquipPanelCellsLanguage2V0](EquipPanelCellsLanguage2V0.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 2, variant 0 (19 cells). |
| [EquipPanelCellsLanguage2V1](EquipPanelCellsLanguage2V1.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 2, variant 1 (19 cells). |
| [EquipPanelCellsLanguage2V2](EquipPanelCellsLanguage2V2.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 2, variant 2 (19 cells). |
| [EquipPanelCellsLanguage2V3](EquipPanelCellsLanguage2V3.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 2, variant 3 (19 cells). |
| [EquipPanelCellsLanguage3A](EquipPanelCellsLanguage3A.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 3, variant a. |
| [EquipPanelCellsLanguage3B](EquipPanelCellsLanguage3B.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 3, variant b. |
| [EquipPanelCellsLanguage3V0](EquipPanelCellsLanguage3V0.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 3, variant 0 (19 cells). |
| [EquipPanelCellsLanguage3V1](EquipPanelCellsLanguage3V1.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 3, variant 1 (19 cells). |
| [EquipPanelCellsLanguage3V2](EquipPanelCellsLanguage3V2.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 3, variant 2 (19 cells). |
| [EquipPanelCellsLanguage3V3](EquipPanelCellsLanguage3V3.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 3, variant 3 (19 cells). |
| [EquipPanelColourPairs](EquipPanelColourPairs.md) | Executable (initialised data) |  | 11 rows of 4 bytes | Gradient colour pairs of the result panel, one colour per variant. |
| [EquipPanelPaletteCycle](EquipPanelPaletteCycle.md) | Executable (initialised data) |  | 19 rows of 4 bytes | Two-phase palette ids of the 19 equipment panel cells (a blinking highlight). |
| [EquipPanelRects](EquipPanelRects.md) | Executable (initialised data) |  | 10 rows of 8 bytes | The panel origins and VRAM staging rectangles of the equip screen panels: two palette row rectangles, then screen rectangles and two texture strip rectangles. |
| [EquipScreenPalette](EquipScreenPalette.md) | Executable (initialised data) |  | 256 rows of 2 bytes | UI palette block (four rows of 64 colours) the equipment screen uploads to the CLUT area of VRAM. Verdict: designer-data. |
| [ErrandActive](ErrandActive.md) | Executable memory (saved with the game) |  | 8 rows of 9 entries of 1 byte | The eight active errand slot records, nine bytes each: flags, errand id, town and the three dispatched unit ids. |
| [ErrandBlob](ErrandBlob.md) | Executable |  | 1 block of 2768 bytes | The errand data block: 96 errand records and every table the errand scoring and rewards read. |
| [ErrandDelay](ErrandDelay.md) | Executable memory (saved with the game) |  | 96 entries of 1 byte | The per-errand delay byte, one per errand id 0..95, saved with the game. |
| [ErrandJobFitCategory](ErrandJobFitCategory.md) | Executable |  | 8 rows of 22 bytes | Score a unit adds for the errand category by job column. |
| [ErrandJobFitType](ErrandJobFitType.md) | Executable |  | 3 rows of 22 bytes | Second score of a unit by errand type and job column; column 22 of the last row reads two padding bytes. |
| [ErrandTreasureMilestones](ErrandTreasureMilestones.md) | Executable |  | 8 rows of 1 byte | Treasure-count milestones of the artefact pool (rising from 1 to 31); event variables 801.. are the counters. |
| [ErrandTreasureMilestones2](ErrandTreasureMilestones2.md) | Executable |  | 8 rows of 1 byte | Treasure-count milestones of the second pool (rising from 1 to 16). |
| [EventCommandHandlers](EventCommandHandlers.md) | Executable |  | 54 rows of 8 bytes | Handler registry read by EventCmd_Run: one function pointer per event command. |
| [EventGenericLookSets](EventGenericLookSets.md) | Executable |  | 8 rows of 32 bytes | Eight sets of generic sprite sheets that event scenes give to their placeholder actors. |
| [EventMenuNodesDefault](EventMenuNodesDefault.md) | Executable (initialised data) |  | 63 rows of 88 bytes | Legacy menu node array of the event task group, default language. |
| [EventMenuNodesLanguage0](EventMenuNodesLanguage0.md) | Executable (initialised data) |  | 63 rows of 88 bytes | Legacy menu node array of the event task group, language 0 (63 nodes of 88 bytes, mutable at run time). |
| [EventMenuNodesLanguage2](EventMenuNodesLanguage2.md) | Executable (initialised data) |  | 63 rows of 88 bytes | Legacy menu node array of the event task group, language 2. |
| [EventMenuNodesLanguage3](EventMenuNodesLanguage3.md) | Executable (initialised data) |  | 63 rows of 88 bytes | Legacy menu node array of the event task group, language 3. |
| [EventOperandLengths](EventOperandLengths.md) | Executable |  | 256 rows of 1 byte | Operand byte count of every event script opcode; the instruction length reader and three other event functions use it. |
| [EventPanelRowsDefault](EventPanelRowsDefault.md) | Executable (initialised data) |  | 14 rows of 56 bytes | Event panel rows used by the 0x7D event task, for every language except language 0. |
| [EventPanelRowsLanguage0](EventPanelRowsLanguage0.md) | Executable (initialised data) |  | 14 rows of 56 bytes | Event panel rows for language 0. |
| [EventPoseCodeFlags](EventPoseCodeFlags.md) | Executable |  | 83 rows of 1 bytes | Small per-code values read by an event unit block step. |
| [EventSideYawTargets](EventSideYawTargets.md) | Executable |  | 4 rows of 2 bytes | The four facing yaw angles an event turn command may snap to. |
| [EventSoundGroups](EventSoundGroups.md) | Executable |  | 56 rows of 4 bytes | Four sound effect numbers per group, played together by one event command. |
| [EventSpriteHdTextures](EventSpriteHdTextures.md) | Executable |  | 144 rows of 4 bytes | Per event character sprite, its HD texture id. |
| [EventUnitNumbersA](EventUnitNumbersA.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields (hp, hpmax, mp, mpmax, wt, wtmax, at, atmax, level, exp) of the legacy dialogue unit panel, first unit. |
| [EventUnitNumbersB](EventUnitNumbersB.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the legacy dialogue unit panel, second unit. |
| [EventViewerList](EventViewerList.md) | Executable (initialised data) |  | 88 rows of 2 bytes | Story event numbers of the scenes in the replay list. |
| [EventWorkBufferPointers](EventWorkBufferPointers.md) | Executable (initialised data) |  | 8 rows of 8 bytes | Descriptor {flags, count, 8 buffer pointers} of event work buffers. |
| [FaceG2dEntryByFace](FaceG2dEntryByFace.md) | Executable (constant) |  | 206 entries of 4 bytes | g2d (pack) entry number per face number 0..205 for the HD layer (row 0 -1, rows 155..158 -1); four readers, each bounding the face with 0xCD. |
| [FaceSlotShapeIds](FaceSlotShapeIds.md) | Executable |  | 82 rows of 4 bytes | Sprite shape number for each dialogue face slot below 0x52. |
| [FastForwardMultipliers](FastForwardMultipliers.md) | Executable (constant) |  | 3 entries of 4 bytes | Game steps per displayed frame by fast-forward level: 1, 3, 5 (GlobalWork_GetSpeedMultiplier). |
| [FastForwardStates](FastForwardStates.md) | Executable (filled at run time) |  | 256 bytes | Whether fast-forward is allowed in each battle state; filled from the GameModeTypes NXD table. |
| [FormulaHandlers](FormulaHandlers.md) | Executable |  | 106 rows of 8 bytes | Dispatch table of the 106 ability formula handlers. |
| [FrameSetsDefault](FrameSetsDefault.md) | Executable |  | 142 rows of 8 bytes | Sprite frame sets of the widget animations, the default (language 1) variant. |
| [FrameSetsLanguage0](FrameSetsLanguage0.md) | Executable |  | 142 rows of 8 bytes | Sprite frame sets of the widget animations, language 0 variant. |
| [FrameSetsLanguage2](FrameSetsLanguage2.md) | Executable |  | 142 rows of 8 bytes | Sprite frame sets of the widget animations, language 2 variant. |
| [FrameSetsLanguage3](FrameSetsLanguage3.md) | Executable |  | 142 rows of 8 bytes | Sprite frame sets of the widget animations, language 3. |
| [GameModeTypes](GameModeTypes.md) | NXD file | 88 |  | Per game-mode flags. |
| [GfxBitExpandTables](GfxBitExpandTables.md) | Executable |  | 16 + 32 + 64 rows of 1 byte | Lookup tables that expand 4, 5 and 6 bit colour channels to 8 bits in the texture format converters. |
| [GfxBlueNoiseTexturePaths](GfxBlueNoiseTexturePaths.md) | Executable |  | 16 rows of 8 bytes | File paths of the sixteen 64 by 64 blue noise textures the renderer loads at set-up. |
| [GfxColourCubeIndexImage](GfxColourCubeIndexImage.md) | Executable |  | 1024 bytes (size inferred) | 8-bit index image drawn with the colour cube palette (size word 32 stored by the set-up). |
| [GfxColourCubePalette](GfxColourCubePalette.md) | Executable |  | 256 rows of 4 bytes | 256-colour palette whose entries step by 8 in red, green and blue; the palette of the index image at 0x14078E2B0. |
| [GfxTextureWindowParams](GfxTextureWindowParams.md) | Executable |  | 4 words (head of a 2048-byte object) | Texture window parameter words (mask x / y, offset x / y) of a draw mode command. |
| [GlyphAdvanceExceptions](GlyphAdvanceExceptions.md) | Executable |  | 32 rows of 1 bytes | Advance widths of the 32 glyphs 2416..2447, an exception list that Glyph_GetAdvance consults before the main table. |
| [GlyphAdvanceWidths](GlyphAdvanceWidths.md) | Executable |  | 2912 rows of 1 bytes | Advance width of each message glyph (the proportional-font metrics of the legacy text drawer). |
| [GradientWindowVertexPalette](GradientWindowVertexPalette.md) | Executable |  | 12 rows of 1 bytes | Which palette colour each of the 12 vertices of a gradient window takes. |
| [GridArrowCells](GridArrowCells.md) | Executable (initialised data) |  | 5 rows of 12 bytes | Five sprite cells of the grid screen (arrows and page markers). |
| [GridAvailableTemplate](GridAvailableTemplate.md) | Executable (initialised data) |  | 54 rows of 1 bytes | Initial availability flags of the grid screen entries. |
| [GridHelpRowsDefault](GridHelpRowsDefault.md) | Executable (initialised data) |  | 31 rows of 24 bytes | Cursor rows of the grid screen text helper, default language. |
| [GridHelpRowsLanguage0](GridHelpRowsLanguage0.md) | Executable (initialised data) |  | 31 rows of 24 bytes | Cursor rows of the grid screen text helper, language 0. |
| [GridMenuNodesDefault](GridMenuNodesDefault.md) | Executable (initialised data) |  | 5 rows of 88 bytes | Legacy menu nodes of the grid screen, default language. |
| [GridMenuNodesLanguage0](GridMenuNodesLanguage0.md) | Executable (initialised data) |  | 5 rows of 88 bytes | Legacy menu nodes of the grid screen, language 0. |
| [GUIFontSlots](GUIFontSlots.md) | Executable (filled at run time) |  | 18 records of FontSlot | Per-UIFontType render slots (16 B each): byte +145 'loaded', signed byte at 16*(id+9) = renderer font slot. |
| [HdSheetEntryBySlot](HdSheetEntryBySlot.md) | Executable (filled at run time) |  | 30 entries of 4 bytes | HD sheet first-entry numbers per sheet slot; unit slots 20 to 28 follow pool index 0 to 8 and index 29 belongs to pool index 9; -1 means not set. |
| [HdSheetGroups](HdSheetGroups.md) | Executable (filled at run time) |  | 20 records of HdSheetGroup | The battle HD layer's 20 sheet groups (21144 bytes each): one sheet entry and up to 128 textures per group. |
| [HdSlotClut](HdSlotClut.md) | Executable (filled at run time) |  | 379 entries of 2 bytes | Palette id of each single-texture slot of the battle HD layer. |
| [HdSlotEntry](HdSlotEntry.md) | Executable (filled at run time) |  | 379 entries of 4 bytes | Sheet entry of each single-texture slot of the battle HD layer (-1 none): the cache key of HdLayer_BuildTextures with g_HdSlotClut. |
| [IdRemapPairs](IdRemapPairs.md) | Executable |  | 406 rows of 56 bytes (2842 pairs) | An id alias table: IdRemap_Lookup scans every row for the id; an unknown id maps to itself. |
| [InflictRecords](InflictRecords.md) | Executable |  | 128 rows of 6 bytes | Statuses an attack, item or ability inflicts or cures. |
| [InventoryCounts](InventoryCounts.md) | Executable memory (saved with the game) |  | 261 entries of 1 byte | The party's inventory: one count per item id 0..260, saved with the game. |
| [Item](Item.md) | NXD file | 45 |  | The item rows (the Item-en table), read through ItemTable_GetRow and ItemTable_GetRowById and used by the text resolver for the category 'Item'. The item records the game keeps in the executable are a separate table. |
| [ItemAccessoryRecords](ItemAccessoryRecords.md) | Executable |  | 32 records of 2 bytes (ids 0xD0..0xEF) | Accessory evade values. |
| [ItemAccessoryRecordsHigh](ItemAccessoryRecordsHigh.md) | Executable |  | 1 record of 2 bytes (id 0x104) | Accessory sub-record of item 260. |
| [ItemArmorRecords](ItemArmorRecords.md) | Executable |  | 64 records of 2 bytes (ids 0x90..0xCF) | Head and body armor HP and MP bonuses. |
| [ItemArmorRecordsHigh](ItemArmorRecordsHigh.md) | Executable |  | 2 records of 2 bytes (ids 0x102, 0x103) | Armor sub-records of items 258 and 259. |
| [ItemAttributes](ItemAttributes.md) | Executable |  | 85 rows of 26 bytes | Equipment attribute records: stat, move and jump bonuses, status groups and elements an item adds to its wearer. |
| [ItemCategoryFirstIds](ItemCategoryFirstIds.md) | Executable |  | 14 rows of 2 bytes | First item id of every category: Item_FindCategoryIndex returns the last category whose first id is not above the item id (entries 1..12 are compared). |
| [ItemCategoryIconCells](ItemCategoryIconCells.md) | Executable |  | 40 rows of 2 bytes (rows 0..36 used) | Texture position of the category icon drawn beside each shop item row. |
| [ItemCategoryTypes](ItemCategoryTypes.md) | Executable |  | 14 rows of 4 bytes | Record kind of each category: which sub-record table an item of the category has. |
| [ItemChemistRecords](ItemChemistRecords.md) | Executable |  | 16 records of 3 bytes (ids 0xF0..0xFF) | Formula, amount and inflict index of the chemist items (the Item-command items 240..253 and two more). |
| [ItemEquipPalettes](ItemEquipPalettes.md) | Executable |  | 145 records of 2 bytes (ids 0..0x8F) | Palette selectors of weapons and shields. |
| [ItemEquipPalettesHigh](ItemEquipPalettesHigh.md) | Executable |  | 2-byte rows, count not established | Palette selectors read by Item_GetEquipPalette for the kinds 4 and 5. |
| [ItemKind6Records](ItemKind6Records.md) | Executable |  | 0 records (empty range) | Base of the kind 6 sub-records. |
| [ItemKind9Records](ItemKind9Records.md) | Executable |  | 0 records (empty range) | Base of the kind 9 sub-records. |
| [ItemKindFirstCategories](ItemKindFirstCategories.md) | Executable |  | 10 rows of 4 bytes | First category of each record kind. |
| [ItemListScriptLanguage0](ItemListScriptLanguage0.md) | Executable (initialised data) |  | 1 script of 198 bytes | The UI script that lays out and runs the item list screen's widgets, language 0 (198 bytes, then a block of rectangles). |
| [ItemListScriptLanguage1](ItemListScriptLanguage1.md) | Executable (initialised data) |  | 1 script of 198 bytes | The UI script that lays out and runs the item list screen's widgets, language 1 (198 bytes, then a block of rectangles). |
| [ItemListScriptLanguage2](ItemListScriptLanguage2.md) | Executable (initialised data) |  | 1 script of 198 bytes | The UI script that lays out and runs the item list screen's widgets, language 2 (198 bytes, then a block of rectangles). |
| [ItemListScriptLanguage3](ItemListScriptLanguage3.md) | Executable (initialised data) |  | 1 script of 198 bytes | The UI script that lays out and runs the item list screen's widgets, language 3 (198 bytes, then a block of rectangles). |
| [ItemNewFlags](ItemNewFlags.md) | Executable memory (saved with the game) |  | 261 rows of 2 entries of 1 byte | Two flag bytes per item id 0..260, set at a new game; I: the shop 'new item' badges (byte 1 cleared when the item is first sold, byte 0 when it is first obtained). |
| [ItemRecords](ItemRecords.md) | Executable |  | 261 records of 12 bytes | The item records the executable keeps for equipment and chemist data. |
| [ItemScreenPalette](ItemScreenPalette.md) | Executable |  | 256 rows of 2 bytes | 256 colours (15-bit) uploaded to the video page row used by the legacy item and map title textures. |
| [ItemShieldRecords](ItemShieldRecords.md) | Executable |  | 16 records of 2 bytes (ids 0x80..0x8F) | Shield evade values. |
| [ItemShopMask](ItemShopMask.md) | Executable |  | 256 rows of 2 bytes | Which shops sell which item: a mask word whose bit for shop s is 0x8000 >> s. |
| [ItemWeaponRecords](ItemWeaponRecords.md) | Executable |  | 128 records of 8 bytes (ids 0..0x7F) | Weapon sub-records of the first 128 items; two more in ItemWeaponRecordsHigh. |
| [ItemWeaponRecordsHigh](ItemWeaponRecordsHigh.md) | Executable |  | 2 records of 8 bytes (ids 0x100, 0x101) | Weapon sub-records of items 256 and 257. |
| [Job](Job.md) | NXD file | 46 |  | The job rows (the Job-en table), read through JobTable_GetRow. |
| [JobAbilityPairList](JobAbilityPairList.md) | Executable (constant) |  |  | 146 entries of 8 bytes (word 0 = job, word 1 = skillset or ability id, words 2..3 unused by the producers); a list ends at the entry whose word 1 is 0xFFFF. sub_14000E114 initialises all 146 (0, 0xFFFF). |
| [JobCommand](JobCommand.md) | NXD file | 41 |  | The job command rows (the JobCommand-en table), read through JobCommandTable_GetRow. |
| [JobLearnListScriptLang1](JobLearnListScriptLang1.md) | Executable |  | 1 script of 493 bytes | UI script (layout of the job learn list) for text language 1. |
| [JobLearnListScriptLang2](JobLearnListScriptLang2.md) | Executable |  | 1 script of 493 bytes | UI script (layout of the job learn list) for text language 2. |
| [JobLearnListScriptLang3](JobLearnListScriptLang3.md) | Executable |  | 1 script of 493 bytes | UI script (layout of the job learn list) for text language 3. |
| [JobMasteryIds](JobMasteryIds.md) | Executable |  | 2 rows of 4 bytes | The two jobs whose full mastery gates job index 20 (Knight and Black Mage by id). |
| [JobNeedLevelRows](JobNeedLevelRows.md) | Executable |  | 22 rows of 12 bytes | Prerequisite job levels of each unlockable job. |
| [JobTable](JobTable.md) | Executable |  | 174 rows of 49 bytes | The stock job table: per job the skillset, always-on abilities, equipment classes, stat growth, base move / jump / evade, status and element sets and the look bytes of marker-130 units. |
| [JobUnitRowsScriptLang0](JobUnitRowsScriptLang0.md) | Executable |  | 1 script of 217 bytes | UI script (layout of the job screen's unit rows) for text language 0. |
| [JobUnitRowsScriptLang1](JobUnitRowsScriptLang1.md) | Executable |  | 1 script of 217 bytes | UI script (layout of the job screen's unit rows) for text language 1. |
| [JobUnitRowsScriptLang2](JobUnitRowsScriptLang2.md) | Executable |  | 1 script of 217 bytes | UI script (layout of the job screen's unit rows) for text language 2. |
| [JobUnitRowsScriptLang3](JobUnitRowsScriptLang3.md) | Executable |  | 1 script of 217 bytes | UI script (layout of the job screen's unit rows) for text language 3. |
| [KeyRepeatPresets](KeyRepeatPresets.md) | Executable |  | 8 rows of 6 bytes | Key-repeat timing presets, one row per value of a 3-bit input option. |
| [LegacyAbilityMenuSkillsetByTab](LegacyAbilityMenuSkillsetByTab.md) | Executable |  | 4 rows of 1 byte | Four skillset ids, one per tab of the legacy ability menu; the same object continues with two 7-entry dword tables (run starts 0, 6 ... 36 and 0, 60 ... 360) that cut the page art into per-page ranges. |
| [LegacyBounceProfile](LegacyBounceProfile.md) | Executable |  | 11 rows of 2 bytes | Symmetric 11-sample arc used to animate a cursor or row; the rest of the 0xBA-byte object holds small cell records. |
| [LegacyButtonIconGroupStartsLang0](LegacyButtonIconGroupStartsLang0.md) | Executable |  | 15 rows of 1 byte | Cumulative piece start index of each button icon group for text language 0; language 1 (default), 2 and 3 share another list (LegacyButtonIconGroupStartsLang1). |
| [LegacyButtonIconGroupStartsLang1](LegacyButtonIconGroupStartsLang1.md) | Executable |  | 15 rows of 1 byte | Piece start indexes of the button icon groups for text languages 1, 2 and 3 (80 pieces; three identical copies at 0x140691D00, 0x140691CF0 and 0x140691A60). |
| [LegacyButtonIconPiecesLang0](LegacyButtonIconPiecesLang0.md) | Executable |  | 81 rows of 12 bytes | Texture rectangle and draw offset of each button icon piece, text language 0 (81 pieces; the other languages have 80). |
| [LegacyButtonIconPiecesLang1](LegacyButtonIconPiecesLang1.md) | Executable |  | 80 rows of 12 bytes | Texture rectangle and draw offset of each button icon piece, text language 1. |
| [LegacyButtonIconPiecesLang2](LegacyButtonIconPiecesLang2.md) | Executable |  | 80 rows of 12 bytes | Texture rectangle and draw offset of each button icon piece, text language 2. |
| [LegacyButtonIconPiecesLang3](LegacyButtonIconPiecesLang3.md) | Executable |  | 80 rows of 12 bytes | Texture rectangle and draw offset of each button icon piece, text language 3. |
| [LegacyButtonIconScalesLang0](LegacyButtonIconScalesLang0.md) | Executable |  | 81 rows of 4 bytes | Scale pair of each button icon piece for text language 0. |
| [LegacyButtonIconScalesLang1](LegacyButtonIconScalesLang1.md) | Executable |  | 80 rows of 4 bytes | Scale pair of each button icon piece for text languages 1, 2 and 3 (three identical copies); language 0 has its own with 81 rows (LegacyButtonIconScalesLang0). |
| [LegacyCellRects](LegacyCellRects.md) | Executable (initialised data) |  | 5 rows of 20 bytes | Five 20-byte rectangle records (size, texture position and flag bytes) of legacy item page cells; the rest of the 0xD0-byte object holds pointers and floats. |
| [LegacyCursorPalette](LegacyCursorPalette.md) | Executable (initialised data) |  | 24 rows of 2 bytes | Palette words of the legacy cursor highlight (a pale ramp). |
| [LegacyCursorPositions](LegacyCursorPositions.md) | Executable |  | 31 rows of 2 bytes | Cursor (x, y) positions of the legacy item pages (from +0x10) and a 5-byte group list at +0; the tail of the 0x90-byte object holds three save file name strings. |
| [LegacyCursorRowsLang0](LegacyCursorRowsLang0.md) | Executable (initialised data) |  | about 33 rows of 24 bytes | Cursor row table of a legacy menu, language 0 variant: 24-byte rows holding the cursor x, y and a key; the candidate address is the third halfword of the first row (base + 4). |
| [LegacyCursorRowsLangOther](LegacyCursorRowsLangOther.md) | Executable (initialised data) |  | about 33 rows of 24 bytes | Cursor row table of the same legacy menu for the languages other than 0; 30 bytes differ from the language 0 table. |
| [LegacyItemCursorTemplates](LegacyItemCursorTemplates.md) | Executable |  | 5 rows of 8 bytes | Five pointer slots (first empty) to the cursor window templates of the legacy item pages. |
| [LegacyItemListBodyGridA](LegacyItemListBodyGridA.md) | Executable (initialised data) |  | 1 grid (0x1280 bytes) | Cell code grid of a large legacy list body (variant a). |
| [LegacyItemListBodyGridB](LegacyItemListBodyGridB.md) | Executable (initialised data) |  | 1 grid (0xBA0 bytes) | Cell code grid of a large legacy list body (variant b). |
| [LegacyItemListLayoutLang0](LegacyItemListLayoutLang0.md) | Executable (initialised data) |  | 1 script (0x190 bytes) | Layout script of the item list page of the legacy party menu, language 0 variant. |
| [LegacyItemListLayoutLang1](LegacyItemListLayoutLang1.md) | Executable (initialised data) |  | 1 script (0x190 bytes) | Layout script of the item list page of the legacy party menu, language 1 variant. |
| [LegacyItemListLayoutLang2](LegacyItemListLayoutLang2.md) | Executable (initialised data) |  | 1 script (0x190 bytes) | Layout script of the item list page of the legacy party menu, language 2 variant. |
| [LegacyItemListLayoutLang3](LegacyItemListLayoutLang3.md) | Executable (initialised data) |  | 1 script (0x190 bytes) | Layout script of the item list page of the legacy party menu, language 3 variant. |
| [LegacyItemUseLayoutLang0](LegacyItemUseLayoutLang0.md) | Executable (initialised data) |  | 1 script (0x100 bytes) | Layout script of the item use page of the legacy party menu (using an item on a unit), language 0 variant. |
| [LegacyItemUseLayoutLang1](LegacyItemUseLayoutLang1.md) | Executable (initialised data) |  | 1 script (0x100 bytes) | Layout script of the item use page of the legacy party menu (using an item on a unit), language 1 variant. |
| [LegacyItemUseLayoutLang2](LegacyItemUseLayoutLang2.md) | Executable (initialised data) |  | 1 script (0x100 bytes) | Layout script of the item use page of the legacy party menu (using an item on a unit), language 2 variant. |
| [LegacyItemUseLayoutLang3](LegacyItemUseLayoutLang3.md) | Executable (initialised data) |  | 1 script (0x100 bytes) | Layout script of the item use page of the legacy party menu (using an item on a unit), language 3 variant. |
| [LegacyJobChoiceLayoutLang0](LegacyJobChoiceLayoutLang0.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Layout script of the job choice page of the legacy party menu (the page that lists a unit's jobs and applies a change), language 0 variant. |
| [LegacyJobChoiceLayoutLang1](LegacyJobChoiceLayoutLang1.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Layout script of the job choice page of the legacy party menu (the page that lists a unit's jobs and applies a change), language 1 variant. |
| [LegacyJobChoiceLayoutLang2](LegacyJobChoiceLayoutLang2.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Layout script of the job choice page of the legacy party menu (the page that lists a unit's jobs and applies a change), language 2 variant. |
| [LegacyJobChoiceLayoutLang3](LegacyJobChoiceLayoutLang3.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Layout script of the job choice page of the legacy party menu (the page that lists a unit's jobs and applies a change), language 3 variant. |
| [LegacyJobDetailLayoutLang0](LegacyJobDetailLayoutLang0.md) | Executable (initialised data) |  | 1 script (0x1F0 bytes) | Layout script of the job detail page of the legacy party menu (four pages of the chosen job), language 0 variant. |
| [LegacyJobDetailLayoutLang1](LegacyJobDetailLayoutLang1.md) | Executable (initialised data) |  | 1 script (0x1F0 bytes) | Layout script of the job detail page of the legacy party menu (four pages of the chosen job), language 1 variant. |
| [LegacyJobDetailLayoutLang2](LegacyJobDetailLayoutLang2.md) | Executable (initialised data) |  | 1 script (0x1F0 bytes) | Layout script of the job detail page of the legacy party menu (four pages of the chosen job), language 2 variant. |
| [LegacyJobDetailLayoutLang3](LegacyJobDetailLayoutLang3.md) | Executable (initialised data) |  | 1 script (0x280 bytes) | Layout script of the job detail page of the legacy party menu (four pages of the chosen job), language 3 variant. |
| [LegacyJobScreenLayoutLang0](LegacyJobScreenLayoutLang0.md) | Executable (initialised data) |  | 1 record (0x19B0 bytes) | Language 0 variant of the legacy page layout: a header of row sizes and a grid of cell codes (the other languages are smaller blocks). |
| [LegacyListPageRangesLang0](LegacyListPageRangesLang0.md) | Executable (initialised data) |  | 120 rows of 2 bytes | Cumulative start ids that cut a long entry list (names of the legacy list page) into categories; language 0 variant. |
| [LegacyListPageRangesLang1](LegacyListPageRangesLang1.md) | Executable (initialised data) |  | 120 rows of 2 bytes | Cumulative start ids that cut a long entry list (names of the legacy list page) into categories; language 1 variant. |
| [LegacyListPageRangesLang2](LegacyListPageRangesLang2.md) | Executable (initialised data) |  | 120 rows of 2 bytes | Cumulative start ids that cut a long entry list (names of the legacy list page) into categories; language 2 variant. |
| [LegacyListRowSlot](LegacyListRowSlot.md) | Executable |  | 48 rows of 1 byte | Sparse byte map from a list row code to a slot number; nearly all entries are 0. |
| [LegacyMenuNodesDefault](LegacyMenuNodesDefault.md) | Executable (initialised data, written at run time) |  | 63 rows of 88 bytes | Legacy menu tree, language 1 (default). |
| [LegacyMenuNodesLanguage0](LegacyMenuNodesLanguage0.md) | Executable (initialised data, written at run time) |  | 63 rows of 88 bytes | Legacy battle / scene menu tree, language 0: 63 nodes of 88 bytes; mutable at run time. |
| [LegacyMenuNodesLanguage2](LegacyMenuNodesLanguage2.md) | Executable (initialised data, written at run time) |  | 63 rows of 88 bytes | Legacy menu tree, language 2. |
| [LegacyMenuNodesLanguage3](LegacyMenuNodesLanguage3.md) | Executable (initialised data, written at run time) |  | 63 rows of 88 bytes | Legacy menu tree, language 3. |
| [LegacyMenuRowCounts](LegacyMenuRowCounts.md) | Executable |  | 48 rows of 1 byte | Number of rows of each legacy menu (the list is LegacyMenuRowListPointers). |
| [LegacyMenuRowIcons](LegacyMenuRowIcons.md) | Executable |  | 16 rows of 1 bytes | A run of 16 consecutive row codes followed by a table of 88 u16 cell ids: menu row decoration data of the legacy menus. |
| [LegacyMenuRowListPointers](LegacyMenuRowListPointers.md) | Executable |  | 48 rows of 8 bytes | Pointers to the byte lists of row ids of each legacy menu; the matching row counts are LegacyMenuRowCounts. |
| [LegacyMenuRowResults](LegacyMenuRowResults.md) | Executable (initialised data) |  | 31 rows of 16 bytes | Per legacy menu, the result code of each row (and which menus remember the row per unit). |
| [LegacyMenuTaskSetups](LegacyMenuTaskSetups.md) | Executable |  | 4 rows of 48 bytes | Per menu state, the three pane tasks of the legacy menu with their task ids and owner ids. |
| [LegacyOptionsDefaultChoices](LegacyOptionsDefaultChoices.md) | Executable (initialised data) |  | 12 rows of 4 bytes | Default choice of each of the 12 options of the legacy options screen. |
| [LegacyOptionsTextBases](LegacyOptionsTextBases.md) | Executable (initialised data) |  | 12 rows of 4 bytes | Per option of the legacy options screen, the message id of its first choice label. |
| [LegacyRowCellDescriptors](LegacyRowCellDescriptors.md) | Executable |  | 9 rows of 24 bytes (from this address) | Sprite cell descriptors of the item list row drawer, 24 bytes each. |
| [LegacyTask10CellsSlot0](LegacyTask10CellsSlot0.md) | Executable (initialised data) |  | 28 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 0, variant 0. |
| [LegacyTask10CellsSlot1](LegacyTask10CellsSlot1.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 0, variant 1. |
| [LegacyTask10CellsSlot10](LegacyTask10CellsSlot10.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 2, variant 2. |
| [LegacyTask10CellsSlot11](LegacyTask10CellsSlot11.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 2, variant 3. |
| [LegacyTask10CellsSlot12](LegacyTask10CellsSlot12.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 3, variant 0. |
| [LegacyTask10CellsSlot13](LegacyTask10CellsSlot13.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 3, variant 1. |
| [LegacyTask10CellsSlot14](LegacyTask10CellsSlot14.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 3, variant 2. |
| [LegacyTask10CellsSlot15](LegacyTask10CellsSlot15.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 3, variant 3. |
| [LegacyTask10CellsSlot2](LegacyTask10CellsSlot2.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 0, variant 2. |
| [LegacyTask10CellsSlot3](LegacyTask10CellsSlot3.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 0, variant 3. |
| [LegacyTask10CellsSlot4](LegacyTask10CellsSlot4.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 1, variant 0. |
| [LegacyTask10CellsSlot5](LegacyTask10CellsSlot5.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 1, variant 1. |
| [LegacyTask10CellsSlot6](LegacyTask10CellsSlot6.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 1, variant 2. |
| [LegacyTask10CellsSlot7](LegacyTask10CellsSlot7.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 1, variant 3. |
| [LegacyTask10CellsSlot8](LegacyTask10CellsSlot8.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 2, variant 0. |
| [LegacyTask10CellsSlot9](LegacyTask10CellsSlot9.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 2, variant 1. |
| [LegacyTask12CommandsA](LegacyTask12CommandsA.md) | Executable (initialised data) |  | 1 block (0x1E0 bytes) | Command row block of the legacy scene task 12 (text labels and live pointers). |
| [LegacyTask12CommandsB](LegacyTask12CommandsB.md) | Executable (initialised data) |  | 1 block (length unknown) | Command row block of the legacy scene task 12 for the other mode. |
| [LegacyTask12LayoutLang0](LegacyTask12LayoutLang0.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Cell list of the legacy scene task 12, language 0 variant. |
| [LegacyTask12LayoutLang1](LegacyTask12LayoutLang1.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Cell list of the legacy scene task 12, language 1 variant. |
| [LegacyTask12LayoutLang2](LegacyTask12LayoutLang2.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Cell list of the legacy scene task 12, language 2 variant. |
| [LegacyTask12LayoutLang3](LegacyTask12LayoutLang3.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Cell list of the legacy scene task 12, language 3 variant. |
| [LegacyTask13LayoutMode13](LegacyTask13LayoutMode13.md) | Executable (initialised data) |  | 1 block (0x1C0 bytes) | Layout block of the legacy scene task 13 for mode 13. |
| [LegacyTask13LayoutOther](LegacyTask13LayoutOther.md) | Executable (initialised data) |  | 1 block (0x1C0 bytes) | Layout block of the legacy scene task 13 for every other mode. |
| [LegacyTitleMenuOffsets](LegacyTitleMenuOffsets.md) | Executable |  | 6 rows of 2 bytes | Six signed offsets applied to the opening menu slots; the same 0x30-byte object continues with a float (0.01), a list of cell ids and two 5-byte lists. |
| [LocationMarkerOffsets](LocationMarkerOffsets.md) | Executable |  | 48 rows of 8 bytes | Per world-map location slot, a small position and kind record used to build its marker. |
| [LookPool](LookPool.md) | Executable (filled at run time) |  | 15 records of LookPoolRecord | The 15 look pool records (stride 0x32D6); byte +0 is the claim, byte +1 the sprite low byte. |
| [LookPoolFaceValue](LookPoolFaceValue.md) | Executable (filled at run time) |  | 10 entries of 4 bytes | Battle face value per look pool record 0..9: sub_14026E838 stores the scene unit's sprite byte; cleared to -1 by sub_140210AF0, saved and restored by sub_140304BEC; ten readers use it as a face number behind the 0xCD ... |
| [MapBlockSectorsLanguage0](MapBlockSectorsLanguage0.md) | Executable (initialised data) |  | 128 rows of 4 bytes | Per battle map, where its 4096-byte map block is, for text language 0. |
| [MapBlockSectorsOtherLanguages](MapBlockSectorsOtherLanguages.md) | Executable (initialised data) |  | 128 rows of 4 bytes | Per battle map, where its 4096-byte map block is, for the other text languages. |
| [MapDrawIndexLists](MapDrawIndexLists.md) | Executable |  | 50 rows of 24 bytes | Per battle map, two lists of map draw-record indices that the two map draw passes treat specially. |
| [MapResourceFilesDefault](MapResourceFilesDefault.md) | Executable |  | 128 rows of 8 bytes | Per battle map, where its resource files are, for text languages other than 0 (the copy of MapResourceFilesLanguage0 that the reader picks when the language record is not 0). |
| [MapResourceFilesLanguage0](MapResourceFilesLanguage0.md) | Executable |  | 128 rows of 8 bytes | Per battle map, where its resource files are, for text language 0. |
| [MathBytePopcount](MathBytePopcount.md) | Executable |  | 256 rows of 1 byte | Number of set bits of each byte value, used to count the bits of a 32-bit mask four bytes at a time. |
| [MenuCursorDefaults](MenuCursorDefaults.md) | Executable (initialised data) |  | 31 rows of 16 bytes | Menu numbers with a pointer to the default record of each battle command menu. |
| [MessageWindowTagCellsDefault](MessageWindowTagCellsDefault.md) | Executable (initialised data) |  | 20 rows of 12 bytes | Message window decoration cells, default (language 1) variant. |
| [MessageWindowTagCellsLanguage0](MessageWindowTagCellsLanguage0.md) | Executable (initialised data) |  | 20 rows of 12 bytes | Message window decoration cells, language 0 variant. |
| [MessageWindowTagCellsLanguage2](MessageWindowTagCellsLanguage2.md) | Executable (initialised data) |  | 20 rows of 12 bytes | Sprite cells (4 per window kind 5..9) decorating message windows, language 2 variant. |
| [MessageWindowTagCellsLanguage3](MessageWindowTagCellsLanguage3.md) | Executable (initialised data) |  | 20 rows of 12 bytes | Message window decoration cells, language 3 variant. |
| [MonsterFaceIndexByJob](MonsterFaceIndexByJob.md) | Executable (constant) |  | 48 entries of 4 bytes | Face record index per monster job 94..141 (values 62 to 77, three jobs per family); Unit_GetFaceIndex reads it through the virtual base 0x140715378, 392 bytes inside the HD sheet entry table before it (2026-11-08). |
| [MoveBlockers](MoveBlockers.md) | Executable (filled at run time) |  | 112 entries of 1 byte | Up to 16 entries of 7 bytes, one per other unit on the map (record MoveBlockerRecord); an unused entry has id 0xFF. |
| [MoveFindItems](MoveFindItems.md) | Executable (initialised data, written at run time) |  | 128 rows of 24 bytes | Move-Find Item and trap data: per map, up to four hidden tiles with a trap kind and a common and a rare item. |
| [MoveTerrainCost](MoveTerrainCost.md) | Executable (filled at run time) |  | 64 entries of 1 byte | Movement cost per terrain type for the unit being built (0xFF = cannot enter), copied by Battle_MoveRangeSetup from one of the six sets of g_MoveTerrainCostSets and adjusted for weather and abilities. |
| [MoveTerrainCostSets](MoveTerrainCostSets.md) | Executable (constant) |  | 6 rows of 64 entries of 1 byte | Six constant cost sets by terrain type: walking, open (Fly / Teleport), float, water (two modes), one more water mode, lava walking. |
| [MoveTileFlags](MoveTileFlags.md) | Executable (filled at run time) |  | 512 entries of 1 byte | Per-tile flag byte of the move-range builder: 0x01 frontier, 0x02 one-axis slope, 0x04 occupied, 0x08 unit that can be stepped onto, 0x10 standable, 0x20 mountable ally, 0x40 steep, 0x80 blocked. |
| [MusicSlotRecords](MusicSlotRecords.md) | Executable |  | 101 rows of 12 bytes (extent of the object) | Per event sound id: an enable flag and two numbers loaded into the music state when the slot is activated. |
| [NxdDataAbilityReactionVoiceType](NxdDataAbilityReactionVoiceType.md) | NXD file | 330 | 4 rows of 48 bytes | Four rows of numeric voice-reaction parameters selected by an ability's reaction voice type; columns not decoded. |
| [NxdDataAchievement](NxdDataAchievement.md) | NXD file | 195 | 51 rows of 28 bytes, text in 7 languages | Per achievement: link to its telemetry record, a few story-progress numbers and the description text. |
| [NxdDataAchievementArray](NxdDataAchievementArray.md) | NXD file | 213 | 7 rows of 28 bytes | Seven achievement groupings: arrays of achievement ids per group. |
| [NxdDataBattle](NxdDataBattle.md) | NXD file | 83 | 713 rows of 4 bytes | Index of battle ids: the rows carry no data column besides the first one at +0; other tables key off these ids. |
| [NxdDataBattleEventOpcode](NxdDataBattleEventOpcode.md) | NXD file | 221 | 40 rows of 8 bytes | Index of the battle event opcode numbers (40 rows); rows carry only a designer comment slot. |
| [NxdDataBattleObjective](NxdDataBattleObjective.md) | NXD file | 47 | 69 rows of 16 bytes, text in 7 languages | Win-condition captions shown in the battle system menu, with a flag marking protect-the-unit objectives. |
| [NxdDataBattleSignal](NxdDataBattleSignal.md) | NXD file | 214 | 71 rows of 16 bytes, text in 7 languages | Short in-battle banner texts (titles) with a flag for evasion messages. |
| [NxdDataBattleVoice](NxdDataBattleVoice.md) | NXD file | 183 | 53 rows of 44 bytes | Battle voice cue definitions: numeric voice ids, group and probability parameters per cue. |
| [NxdDataBattleVoiceGroupRate](NxdDataBattleVoiceGroupRate.md) | NXD file | 184 | 6 rows of 208 bytes | Six rows of 50 percentage weights, one per battle voice group, choosing how often each voice group plays. |
| [NxdDataBGMMode](NxdDataBGMMode.md) | NXD file | 281 | 97 rows of 24 bytes, text in 7 languages | Music player list: per entry a tab index, title text and a reference to the sound resource to play. |
| [NxdDataBGMTransition](NxdDataBGMTransition.md) | NXD file | 306 | 14 rows of 20 bytes | Music transition parameters: a sound resource reference and two fade-like float values per row. |
| [NxdDataBook](NxdDataBook.md) | NXD file | 148 | 5 rows of 44 bytes, text in 7 languages | The five lore books: titles, descriptions, icon and sound references. |
| [NxdDataBraveStoryVoice](NxdDataBraveStoryVoice.md) | NXD file | 233 | 34 rows of 16 bytes | Voice line references for the Brave Story scenes, keyed by scene and line; each row points at a packed audio entry and a timing float. |
| [NxdDataBrightness](NxdDataBrightness.md) | NXD file | 137 | 11 rows of 12 bytes | Eleven screen brightness steps and their multiplier. |
| [NxdDataCaption](NxdDataCaption.md) | NXD file | 87 | 13 rows of 16 bytes | Caption slots whose content is a typed reference (union) to another table's row. |
| [NxdDataCaptionFreeWord](NxdDataCaptionFreeWord.md) | NXD file | 86 | 8 rows of 12 bytes, text in 7 languages | Free-form caption words used by the caption system. |
| [NxdDataChapter](NxdDataChapter.md) | NXD file | 206 | 6 rows of 16 bytes, text in 7 languages | The six chapter titles with a story-progress number each. |
| [NxdDataChapterFile](NxdDataChapterFile.md) | NXD file | 239 | 13 rows of 8 bytes | Maps chapter file slots to chapter numbers. |
| [NxdDataChara](NxdDataChara.md) | NXD file | 274 | 131 rows of 8 bytes | Index of 131 character ids with one flag column. |
| [NxdDataCharaColorSkin](NxdDataCharaColorSkin.md) | NXD file | 276 | 5 rows of 12 bytes | Skin colour variants gated by a story-progress condition (UserSituation link). |
| [NxdDataCharaControlId](NxdDataCharaControlId.md) | NXD file | 218 | 87 rows of 12 bytes | Maps character control ids (up to 1006) to a character number. |
| [NxdDataCharacterSortInfo](NxdDataCharacterSortInfo.md) | NXD file | 44 | 19 rows of 8 bytes | Sort order data of characters for list screens. |
| [NxdDataCharaName](NxdDataCharaName.md) | NXD file | 93 | 1024 rows of 24 bytes, text in 7 languages | Character names (1024 ids), a typed reference column and a generic-unit flag. |
| [NxdDataCharaPartsDrawParam](NxdDataCharaPartsDrawParam.md) | NXD file | 305 | 2 rows of 12 bytes | Two rows of part-draw switches. |
| [NxdDataCharaZodiacStoneCLUT](NxdDataCharaZodiacStoneCLUT.md) | NXD file | 302 | 25 rows of 16 bytes | Palette byte blobs for the 25 zodiac stone looks. |
| [NxdDataCharCLUT](NxdDataCharCLUT.md) | NXD file | 210 | 16 rows of 24 bytes | Character palette (colour lookup) definitions: a byte blob of colours per palette id and variant, plus a skin colour link. |
| [NxdDataCharMouseCollision](NxdDataCharMouseCollision.md) | NXD file | 334 | 36 rows of 20 bytes | Mouse pick boxes of characters: three size floats per shape id. |
| [NxdDataCharShape](NxdDataCharShape.md) | NXD file | 174 | 159 rows of 48 bytes | Per body shape: links to shadow size, palette and palette-parameter rows, and a height value. |
| [NxdDataCharShapeLUTParam](NxdDataCharShapeLUTParam.md) | NXD file | 217 | 24 rows of 20 bytes | Shape palette parameters: two floats and two shorts per row. |
| [NxdDataCharShapeShadowSize](NxdDataCharShapeShadowSize.md) | NXD file | 176 | 12 rows of 12 bytes | Twelve shadow sizes (a float per row). |
| [NxdDataCharTacticalViewParam](NxdDataCharTacticalViewParam.md) | NXD file | 292 | 6 rows of 32 bytes | Tactical-camera view parameters as float arrays per view and variant. |
| [NxdDataCollection](NxdDataCollection.md) | NXD file | 121 | 43 rows of 44 bytes, text in 7 languages | Collection entries (43): name, description and numeric parameters. |
| [NxdDataConfigCategory](NxdDataConfigCategory.md) | NXD file | 249 | 16 rows of 16 bytes | Settings menu categories: the item ids each contains and a UI text key for the title. |
| [NxdDataConfigItem](NxdDataConfigItem.md) | NXD file | 250 | 61 rows of 76 bytes | Settings menu rows (61): pad list, name and description UI text keys and value-kind parameters. |
| [NxdDataConfigItemButtonType](NxdDataConfigItemButtonType.md) | NXD file | 288 | 2 rows of 12 bytes | Option values for the button-style setting. |
| [NxdDataConfigItemCursorMoveType](NxdDataConfigItemCursorMoveType.md) | NXD file | 268 | 2 rows of 20 bytes | Option values for the cursor-movement setting. |
| [NxdDataConfigItemEnableDOF](NxdDataConfigItemEnableDOF.md) | NXD file | 271 | 3 rows of 12 bytes | Option values for the depth-of-field setting. |
| [NxdDataConfigItemForwardEnabledType](NxdDataConfigItemForwardEnabledType.md) | NXD file | 323 | 3 rows of 12 bytes | Option values for the fast-forward enable setting, with UI text keys. |
| [NxdDataConfigItemResolution](NxdDataConfigItemResolution.md) | NXD file | 252 | 9 rows of 8 bytes | Option list of the resolution setting (nine rows pointing at Resolution). |
| [NxdDataConfigItemScreenMode](NxdDataConfigItemScreenMode.md) | NXD file | 251 | 3 rows of 12 bytes | Option values for the screen-mode setting. |
| [NxdDataConfigItemTextLanguage](NxdDataConfigItemTextLanguage.md) | NXD file | 260 | 7 rows of 12 bytes | Option values for the text-language setting (seven languages). |
| [NxdDataConfigItemVoiceLanguage](NxdDataConfigItemVoiceLanguage.md) | NXD file | 259 | 2 rows of 12 bytes | Option values for the voice-language setting (two). |
| [NxdDataConfigPadAssign](NxdDataConfigPadAssign.md) | NXD file | 270 | 4 rows of 20 bytes | Pad button assignment presets keyed by two ids. |
| [NxdDataConfigPadList](NxdDataConfigPadList.md) | NXD file | 273 | 4 rows of 20 bytes | Four pad lists used by settings rows. |
| [NxdDataContinuousBattleTimeline](NxdDataContinuousBattleTimeline.md) | NXD file | 231 | 46 rows of 8 bytes | Timeline steps for chained battles (46 rows). |
| [NxdDataContinuousSortieConfirm](NxdDataContinuousSortieConfirm.md) | NXD file | 230 | 27 rows of 108 bytes | Sortie confirmation parameters for chained battles, keyed by battle and part. |
| [NxdDataCursorMoveType](NxdDataCursorMoveType.md) | NXD file | 267 | 2 rows of 8 bytes | Two cursor movement types. |
| [NxdDataDebugFidG2D](NxdDataDebugFidG2D.md) | NXD file | 212 | 1285 rows of 12 bytes | Debug 2D resource id list (1285 rows). |
| [NxdDataDebugFIdSound](NxdDataDebugFIdSound.md) | NXD file | 89 | 691 rows of 8 bytes | Debug sound id list (691 rows). |
| [NxdDataDebugGameFlowSettings](NxdDataDebugGameFlowSettings.md) | NXD file | 102 | 0 rows of 0 bytes | Debug table with no rows and no layout columns in the retail file. |
| [NxdDataDebugMap](NxdDataDebugMap.md) | NXD file | 78 | 80 rows of 16 bytes | Debug map list (80 rows) with comment text. |
| [NxdDataDebugNovelPageDefine](NxdDataDebugNovelPageDefine.md) | NXD file | 300 | 0 rows of 0 bytes | Debug table with no rows and no layout columns. |
| [NxdDataDebugRefinedBgAnim](NxdDataDebugRefinedBgAnim.md) | NXD file | 79 | 0 rows of 0 bytes | Debug table with no rows and no layout columns. |
| [NxdDataDebugRefinedBgTexture](NxdDataDebugRefinedBgTexture.md) | NXD file | 80 | 0 rows of 0 bytes | Debug triple-keyed table with no rows and no layout columns. |
| [NxdDataDebugSceneSelect](NxdDataDebugSceneSelect.md) | NXD file | 58 | 0 rows of 0 bytes | Debug scene picker rows; empty in the retail file. |
| [NxdDataDebugSceneSelectCategory](NxdDataDebugSceneSelectCategory.md) | NXD file | 110 | 8 rows of 12 bytes | Eight debug scene picker categories with names. |
| [NxdDataDeepDungeon](NxdDataDeepDungeon.md) | NXD file | 101 | 10 rows of 12 bytes, text in 7 languages | Ten deep-dungeon floors or entries: name and description text. |
| [NxdDataDepthBias](NxdDataDepthBias.md) | NXD file | 315 | 12 rows of 12 bytes | Twelve depth-bias values for effect textures. |
| [NxdDataDifficultyLevel](NxdDataDifficultyLevel.md) | NXD file | 111 | 3 rows of 28 bytes | The three play modes: UI text key and numeric parameters. |
| [NxdDataDLCPathList](NxdDataDLCPathList.md) | NXD file | 335 | 1 rows of 12 bytes | A path list for downloadable content (one row). |
| [NxdDataEgg](NxdDataEgg.md) | NXD file | 310 | 49 rows of 24 bytes | Per egg (a job grouping): three job ids and a parameter. |
| [NxdDataEnhancedBattleEvent](NxdDataEnhancedBattleEvent.md) | NXD file | 163 | 2274 rows of 40 bytes | Battle event scripting rows keyed by battle, step and sub-step: event type and character control id with other parameters. |
| [NxdDataEnhancedWorldEvent](NxdDataEnhancedWorldEvent.md) | NXD file | 199 | 540 rows of 32 bytes | World-map event rows keyed by event, step and sub-step: event type and parameters. |
| [NxdDataEntryArea](NxdDataEntryArea.md) | NXD file | 244 | 2519 rows of 8 bytes | Deployment areas: per battle and slot, a position value. |
| [NxdDataEntryNo](NxdDataEntryNo.md) | NXD file | 109 | 512 rows of 28 bytes | Per entry number (512): link to the sortie confirmation row plus parameters. |
| [NxdDataEventCharaDraw](NxdDataEventCharaDraw.md) | NXD file | 234 | 24 rows of 20 bytes | Event character draw settings keyed by event and slot; a character control id and parameters. |
| [NxdDataEventFlag](NxdDataEventFlag.md) | NXD file | 219 | 1024 rows of 8 bytes | Index of 1024 event flag slots; rows carry only a designer comment slot. |
| [NxdDataEventId](NxdDataEventId.md) | NXD file | 156 | 887 rows of 44 bytes | Per story event (887): sortie confirm link, sound state parameter and parameters. |
| [NxdDataFacilityVoicePattern](NxdDataFacilityVoicePattern.md) | NXD file | 203 | 7 rows of 20 bytes | Facility voice sound file paths (seven patterns). |
| [NxdDataFloorCursorSpeed](NxdDataFloorCursorSpeed.md) | NXD file | 262 | 4 rows of 8 bytes | Four cursor speeds. |
| [NxdDataForwardEnabledType](NxdDataForwardEnabledType.md) | NXD file | 324 | 3 rows of 8 bytes | Three fast-forward permission types. |
| [NxdDataGameFlag](NxdDataGameFlag.md) | NXD file | 91 | 32 rows of 8 bytes | Index of 32 game flags. |
| [NxdDataGameProgress](NxdDataGameProgress.md) | NXD file | 92 | 307 rows of 20 bytes | Story progress steps keyed by progress group and value, linked to world-map progress info rows. |
| [NxdDataGeneralJob](NxdDataGeneralJob.md) | NXD file | 189 | 21 rows of 124 bytes | Per general job (21): arrays of required jobs, levels, positions and experience, and tree placement parameters. |
| [NxdDataGossip](NxdDataGossip.md) | NXD file | 181 | 23 rows of 48 bytes, text in 7 languages | Tavern rumours (23): title, text, story-progress condition and icon. |
| [NxdDataGuide](NxdDataGuide.md) | NXD file | 187 | 242 rows of 48 bytes, text in 7 languages | Guide entries (242): page reference, conditions, title and sort order. |
| [NxdDataGuideCategory](NxdDataGuideCategory.md) | NXD file | 301 | 13 rows of 16 bytes | Guide categories. |
| [NxdDataGuidePage](NxdDataGuidePage.md) | NXD file | 188 | 409 rows of 24 bytes, text in 7 languages | Guide pages keyed by guide id and page index: icon id arrays and text slots. |
| [NxdDataIcon](NxdDataIcon.md) | NXD file | 118 | 1400 rows of 16 bytes | Icon id to image file path (1400 rows). |
| [NxdDataIconGroup](NxdDataIconGroup.md) | NXD file | 29 | 75 rows of 12 bytes | Icon group parameters (75 rows). |
| [NxdDataJingle](NxdDataJingle.md) | NXD file | 319 | 11 rows of 12 bytes | Eleven jingles pointing at sound resources. |
| [NxdDataJobType](NxdDataJobType.md) | NXD file | 200 | 124 rows of 16 bytes | Per job look type (124): male and female icon ids. |
| [NxdDataJournal](NxdDataJournal.md) | NXD file | 122 | 117 rows of 40 bytes, text in 7 languages | Journal entries (117): story-progress condition, title and text. |
| [NxdDataLand](NxdDataLand.md) | NXD file | 94 | 64 rows of 20 bytes, text in 7 languages | Terrain feature entries (64): linked ability, name, description and icon. |
| [NxdDataLandscapeHeight](NxdDataLandscapeHeight.md) | NXD file | 287 | 76 rows of 8 bytes, text in 7 languages | Terrain height description texts (76). |
| [NxdDataLanguage](NxdDataLanguage.md) | NXD file | 261 | 7 rows of 12 bytes | The seven game languages. |
| [NxdDataLauncherGuide](NxdDataLauncherGuide.md) | NXD file | 277 | 50 rows of 16 bytes, text in 7 languages | Launcher guide captions keyed by page and line. |
| [NxdDataLoadingSettings](NxdDataLoadingSettings.md) | NXD file | 129 | 11 rows of 4 bytes | Eleven loading screen settings. |
| [NxdDataLoreAffiliation](NxdDataLoreAffiliation.md) | NXD file | 241 | 23 rows of 16 bytes, text in 7 languages | Lore affiliations (23): icon and caption. |
| [NxdDataLoreDictionary](NxdDataLoreDictionary.md) | NXD file | 237 | 241 rows of 84 bytes, text in 7 languages | Lore dictionary entries keyed by entry and part: names, descriptions, sort orders, icons and links. |
| [NxdDataLoreDictionaryCategory](NxdDataLoreDictionaryCategory.md) | NXD file | 246 | 3 rows of 16 bytes, text in 7 languages | Three lore dictionary category names. |
| [NxdDataLoreNameAlias](NxdDataLoreNameAlias.md) | NXD file | 240 | 52 rows of 12 bytes, text in 7 languages | Lore name aliases (52). |
| [NxdDataMap](NxdDataMap.md) | NXD file | 60 | 129 rows of 32 bytes | Per map (129): parameters; map content lives in map files. |
| [NxdDataMapRouteTable](NxdDataMapRouteTable.md) | NXD file | 98 | 314 rows of 12 bytes | Route points between map entries keyed by route and step. |
| [NxdDataMapVariationEvent](NxdDataMapVariationEvent.md) | NXD file | 207 | 14 rows of 20 bytes | Map variations tied to events (14). |
| [NxdDataMapVariationRandomBattle](NxdDataMapVariationRandomBattle.md) | NXD file | 208 | 7 rows of 8 bytes | Map variations for random battles (7). |
| [NxdDataMessageWindowAnimationType](NxdDataMessageWindowAnimationType.md) | NXD file | 245 | 9 rows of 28 bytes | Message window animation parameters (nine types). |
| [NxdDataMovieData](NxdDataMovieData.md) | NXD file | 65 | 22 rows of 40 bytes | Movie list (22): file path, sound file id and flags. |
| [NxdDataNovel00](NxdDataNovel00.md) | NXD file | 164 | 256 rows of 8 bytes, text in 7 languages | Story novel text pages, book 0 (256 rows). |
| [NxdDataNovel01](NxdDataNovel01.md) | NXD file | 165 | 256 rows of 8 bytes, text in 7 languages | Story novel text pages, book 1. |
| [NxdDataNovel02](NxdDataNovel02.md) | NXD file | 166 | 255 rows of 8 bytes, text in 7 languages | Story novel text pages, book 2. |
| [NxdDataNovel03](NxdDataNovel03.md) | NXD file | 167 | 255 rows of 8 bytes, text in 7 languages | Story novel text pages, book 3. |
| [NxdDataNovel04](NxdDataNovel04.md) | NXD file | 168 | 39 rows of 8 bytes, text in 7 languages | Story novel text pages, book 4 (39 rows). |
| [NxdDataNovelIcon](NxdDataNovelIcon.md) | NXD file | 220 | 131 rows of 20 bytes | Icons of the novel pages (131). |
| [NxdDataOverrideAbilityActionData](NxdDataOverrideAbilityActionData.md) | NXD file | 247 | 368 rows of 40 bytes | Ability data override rows: each field is -1 (keep the stock value) or a replacement for range, area, formula, status, CT or MP cost. |
| [NxdDataOverrideEntryData](NxdDataOverrideEntryData.md) | NXD file | 96 | 516 rows of 160 bytes | Per-battle unit entry overrides (516 rows, keyed by battle and slot): sprite, job, skills, gear, level and facing. |
| [NxdDataPause](NxdDataPause.md) | NXD file | 282 | 13 rows of 24 bytes | Pause overlay settings (13) with a sound event link. |
| [NxdDataPlaceName](NxdDataPlaceName.md) | NXD file | 85 | 257 rows of 20 bytes, text in 7 languages | Place names (257 ids up to 100050). |
| [NxdDataPostEffect](NxdDataPostEffect.md) | NXD file | 228 | 2 rows of 16 bytes | Two post effect definitions with an effect file path. |
| [NxdDataPostEffectDepthLUT](NxdDataPostEffectDepthLUT.md) | NXD file | 284 | 30 rows of 40 bytes | Depth lookup parameters (30). |
| [NxdDataPostEffectDOF](NxdDataPostEffectDOF.md) | NXD file | 227 | 34 rows of 28 bytes | Depth-of-field parameters (34). |
| [NxdDataPostEffectGlare](NxdDataPostEffectGlare.md) | NXD file | 256 | 19 rows of 24 bytes | Glare parameters (19). |
| [NxdDataPostEffectLUT](NxdDataPostEffectLUT.md) | NXD file | 285 | 31 rows of 20 bytes | Colour lookup parameters (31). |
| [NxdDataProfit](NxdDataProfit.md) | NXD file | 182 | 96 rows of 40 bytes, text in 7 languages | Errand definitions (96): title, client name link and parameters. |
| [NxdDataProfitBonusItem](NxdDataProfitBonusItem.md) | NXD file | 242 | 8 rows of 12 bytes, text in 7 languages | Errand bonus item names (8). |
| [NxdDataProfitClientName](NxdDataProfitClientName.md) | NXD file | 193 | 85 rows of 8 bytes, text in 7 languages | Errand client names (85). |
| [NxdDataProfitType](NxdDataProfitType.md) | NXD file | 243 | 8 rows of 20 bytes | Errand types (8) with three bonus item links. |
| [NxdDataPSPMovieFile](NxdDataPSPMovieFile.md) | NXD file | 66 | 22 rows of 12 bytes | Original-version movie file entries (22). |
| [NxdDataRefinedBgAnim](NxdDataRefinedBgAnim.md) | NXD file | 49 | 280 rows of 12 bytes | Remastered background animations keyed by map and slot. |
| [NxdDataRefinedBgMeshNode](NxdDataRefinedBgMeshNode.md) | NXD file | 153 | 1429 rows of 28 bytes | Remastered background mesh nodes keyed by map, group and node. |
| [NxdDataRefinedBgMeshNodeInvisType](NxdDataRefinedBgMeshNodeInvisType.md) | NXD file | 312 | 1 rows of 12 bytes | Mesh node invisibility type (one row). |
| [NxdDataRefinedBgMeshPolygon](NxdDataRefinedBgMeshPolygon.md) | NXD file | 232 | 4037 rows of 24 bytes | Remastered background polygons keyed by map and index (4037), linked to conditions. |
| [NxdDataRefinedBgMeshPolygonCond](NxdDataRefinedBgMeshPolygonCond.md) | NXD file | 326 | 78 rows of 20 bytes | Polygon condition rows (78). |
| [NxdDataRefinedBgSystemTexture](NxdDataRefinedBgSystemTexture.md) | NXD file | 141 | 870 rows of 24 bytes | System textures of remastered backgrounds, triple keyed. |
| [NxdDataRefinedBgTexture](NxdDataRefinedBgTexture.md) | NXD file | 71 | 1338 rows of 40 bytes | Textures of remastered backgrounds, triple keyed (1338 rows). |
| [NxdDataRefinedBgUITexture](NxdDataRefinedBgUITexture.md) | NXD file | 223 | 20 rows of 20 bytes | UI textures of remastered backgrounds, with frame id arrays. |
| [NxdDataRefinedBgUITextureFrames](NxdDataRefinedBgUITextureFrames.md) | NXD file | 222 | 17 rows of 12 bytes | Frame texture file paths of background UI textures. |
| [NxdDataRefinedPermanentVFX](NxdDataRefinedPermanentVFX.md) | NXD file | 321 | 21 rows of 12 bytes | Permanent effect definitions (21). |
| [NxdDataRefinedVFXCameraControl](NxdDataRefinedVFXCameraControl.md) | NXD file | 317 | 1 rows of 20 bytes | Effect camera control parameters (one row). |
| [NxdDataRefinedVFXTexture](NxdDataRefinedVFXTexture.md) | NXD file | 202 | 487 rows of 32 bytes | Effect textures (487) linked to depth bias and camera control. |
| [NxdDataResolution](NxdDataResolution.md) | NXD file | 257 | 9 rows of 16 bytes | The nine selectable resolutions (width and height). |
| [NxdDataRoute](NxdDataRoute.md) | NXD file | 97 | 51 rows of 28 bytes | Road records (51): parameters of world-map roads. |
| [NxdDataScenarioId](NxdDataScenarioId.md) | NXD file | 59 | 350 rows of 16 bytes | Scenario ids (350) with arrays of the event ids that belong to each. |
| [NxdDataScionFiles](NxdDataScionFiles.md) | NXD file | 169 | 498 rows of 8 bytes | File names of the voice archives (498). |
| [NxdDataScionLabels](NxdDataScionLabels.md) | NXD file | 170 | 3323 rows of 12 bytes | Voice line labels (3323): archive file link and packed entry id. |
| [NxdDataScreenMode](NxdDataScreenMode.md) | NXD file | 266 | 3 rows of 8 bytes | Three screen modes. |
| [NxdDataSeadEvent](NxdDataSeadEvent.md) | NXD file | 99 | 15 rows of 16 bytes | Sound event definitions (15). |
| [NxdDataSeadStateParameter](NxdDataSeadStateParameter.md) | NXD file | 235 | 41 rows of 12 bytes | Sound state parameters (41). |
| [NxdDataSeDefine](NxdDataSeDefine.md) | NXD file | 69 | 304 rows of 16 bytes | Sound effect definitions (304), each a typed reference. |
| [NxdDataSeSystem](NxdDataSeSystem.md) | NXD file | 201 | 169 rows of 8 bytes | System sound effects (169). |
| [NxdDataShopVoice](NxdDataShopVoice.md) | NXD file | 178 | 131 rows of 16 bytes | Shop voice lines keyed by shop and line, each pointing at a packed audio entry. |
| [NxdDataSortieConfirm](NxdDataSortieConfirm.md) | NXD file | 54 | 375 rows of 48 bytes | Sortie confirmation screens (375): map link, UI text keys for event, max units and threat rating. |
| [NxdDataSoundEnhanced](NxdDataSoundEnhanced.md) | NXD file | 280 | 254 rows of 24 bytes | Enhanced music cue definitions (254) linked to sound resources. |
| [NxdDataSoundEnhancedResource](NxdDataSoundEnhancedResource.md) | NXD file | 279 | 110 rows of 12 bytes | Sound resource file paths (110). |
| [NxdDataSpeaker](NxdDataSpeaker.md) | NXD file | 26 | 304 rows of 8 bytes, text in 7 languages | Speaker names (304 ids). |
| [NxdDataSpellMessage](NxdDataSpellMessage.md) | NXD file | 146 | 1182 rows of 12 bytes | Spell voice lines keyed by spell and line, pointing at packed audio entries. |
| [NxdDataSubQuestMessage](NxdDataSubQuestMessage.md) | NXD file | 320 | 3 rows of 12 bytes | Three sub-quest message sound links. |
| [NxdDataSystemBonusEntitlement](NxdDataSystemBonusEntitlement.md) | NXD file | 293 | 31 rows of 20 bytes | Bonus entitlements (31): download path link and parameters. |
| [NxdDataSystemBonusItem](NxdDataSystemBonusItem.md) | NXD file | 297 | 3 rows of 24 bytes, text in 7 languages | Bonus item list (3): title, description and a typed reference. |
| [NxdDataSystemBonusItemContents](NxdDataSystemBonusItemContents.md) | NXD file | 296 | 12 rows of 12 bytes | Bonus item contents, keyed by bonus and slot, typed references. |
| [NxdDataSystemBonusSpecialItem](NxdDataSystemBonusSpecialItem.md) | NXD file | 295 | 6 rows of 24 bytes, text in 7 languages | Special bonus items (6): typed reference, quantity and caption. |
| [NxdDataSystemParam](NxdDataSystemParam.md) | NXD file | 84 | 71 rows of 12 bytes | System parameter values (71). |
| [NxdDataTelemetryAchievement](NxdDataTelemetryAchievement.md) | NXD file | 173 | 54 rows of 64 bytes, text in 7 languages | Achievement definitions for the platform (54): id strings, names, descriptions and parameters. |
| [NxdDataTelemetryAchievementGrade](NxdDataTelemetryAchievementGrade.md) | NXD file | 135 | 5 rows of 4 bytes | Five achievement grades. |
| [NxdDataTelemetryEvent](NxdDataTelemetryEvent.md) | NXD file | 133 | 8 rows of 20 bytes | Telemetry event list (8). |
| [NxdDataTelemetryEventDefinition](NxdDataTelemetryEventDefinition.md) | NXD file | 131 | 8 rows of 20 bytes | Telemetry event definitions (8) with names. |
| [NxdDataTelemetryObject](NxdDataTelemetryObject.md) | NXD file | 314 | 109 rows of 20 bytes | Telemetry object list (109). |
| [NxdDataTelemetryProperty](NxdDataTelemetryProperty.md) | NXD file | 130 | 28 rows of 12 bytes | Telemetry property names (28). |
| [NxdDataTelemetryPropertyValue](NxdDataTelemetryPropertyValue.md) | NXD file | 132 | 37 rows of 12 bytes | Telemetry property value lists (37). |
| [NxdDataTelemetryStat](NxdDataTelemetryStat.md) | NXD file | 134 | 52 rows of 32 bytes | Telemetry statistics (52). |
| [NxdDataTelemetryStatExtraction](NxdDataTelemetryStatExtraction.md) | NXD file | 318 | 50 rows of 28 bytes | Telemetry statistic extraction rules (50). |
| [NxdDataTown](NxdDataTown.md) | NXD file | 52 | 48 rows of 52 bytes, text in 7 languages | Per town (48): description, place name link, condition and parameters. |
| [NxdDataTownImage](NxdDataTownImage.md) | NXD file | 158 | 27 rows of 4 bytes | Town image indices (27). |
| [NxdDataTransition](NxdDataTransition.md) | NXD file | 100 | 26 rows of 20 bytes | Screen transition parameters (26). |
| [NxdDataUDSActivity](NxdDataUDSActivity.md) | NXD file | 313 | 74 rows of 28 bytes | Activity records for the platform's activity feed (74). |
| [NxdDataUI](NxdDataUI.md) | NXD file | 19 | 4050 rows of 8 bytes, text in 7 languages | The general UI text table: 4050 strings keyed by UI text key. |
| [NxdDataUIAbilityIcon](NxdDataUIAbilityIcon.md) | NXD file | 31 | 55 rows of 8 bytes | Ability icon variants (55). |
| [NxdDataUIAddon](NxdDataUIAddon.md) | NXD file | 24 | 264 rows of 36 bytes | UI add-on definitions (264): UI file path and flags. |
| [NxdDataUIAddonPriority](NxdDataUIAddonPriority.md) | NXD file | 81 | 8 rows of 12 bytes | UI add-on priorities (8). |
| [NxdDataUIAnnounce](NxdDataUIAnnounce.md) | NXD file | 68 | 123 rows of 28 bytes | Announcement banner definitions (123). |
| [NxdDataUIAttributive](NxdDataUIAttributive.md) | NXD file | 229 | 39 rows of 156 bytes | Attributive text variants (39 rows of 3 string groups). |
| [NxdDataUIButton](NxdDataUIButton.md) | NXD file | 322 | 21 rows of 12 bytes | UI button definitions (21). |
| [NxdDataUIButtonGuide](NxdDataUIButtonGuide.md) | NXD file | 33 | 1152 rows of 40 bytes | Button guide footer layouts keyed by screen and slot (1152). |
| [NxdDataUIChronicleCharaList](NxdDataUIChronicleCharaList.md) | NXD file | 283 | 168 rows of 24 bytes | Chronicle character lists keyed by period and slot. |
| [NxdDataUIChroniclePeriod](NxdDataUIChroniclePeriod.md) | NXD file | 275 | 31 rows of 40 bytes, text in 7 languages | Chronicle periods (31): condition, type, character list, icon, caption and balloon links. |
| [NxdDataUIClassicSubtitles](NxdDataUIClassicSubtitles.md) | NXD file | 128 | 93 rows of 28 bytes, text in 7 languages | Classic-mode movie subtitles keyed by movie and line, with start and end seconds. |
| [NxdDataUIColor](NxdDataUIColor.md) | NXD file | 20 | 201 rows of 12 bytes | Named UI colours (201). |
| [NxdDataUICreditLineArt](NxdDataUICreditLineArt.md) | NXD file | 304 | 19 rows of 8 bytes | Credit line art UI names (19). |
| [NxdDataUICreditRow](NxdDataUICreditRow.md) | NXD file | 309 | 1227 rows of 24 bytes | Credit rows (1227): type, caption array and icon. |
| [NxdDataUIDialog](NxdDataUIDialog.md) | NXD file | 34 | 241 rows of 60 bytes | Dialog definitions (241): text and option UI text keys. |
| [NxdDataUIElementAttribute](NxdDataUIElementAttribute.md) | NXD file | 55 | 8 rows of 12 bytes, text in 7 languages | Element attribute names (8). |
| [NxdDataUIEndCredit](NxdDataUIEndCredit.md) | NXD file | 307 | 1201 rows of 20 bytes | End credit script rows (1201). |
| [NxdDataUIEquipAbilitySlot](NxdDataUIEquipAbilitySlot.md) | NXD file | 62 | 12 rows of 16 bytes | Equipment screen ability slot layout (12). |
| [NxdDataUIEquipDetailNumParam](NxdDataUIEquipDetailNumParam.md) | NXD file | 198 | 9 rows of 12 bytes | Equipment detail number fields, keyed by field and variant. |
| [NxdDataUIFilePathExchange](NxdDataUIFilePathExchange.md) | NXD file | 125 | 5 rows of 12 bytes | UI file replacement mapping (5). |
| [NxdDataUIFontSet](NxdDataUIFontSet.md) | NXD file | 21 | 100 rows of 100 bytes | Font sets (100) as groups of font type ids. |
| [NxdDataUIFontType](NxdDataUIFontType.md) | NXD file | 27 | 19 rows of 24 bytes | Font types (19) with file path. |
| [NxdDataUIItemCategory](NxdDataUIItemCategory.md) | NXD file | 38 | 35 rows of 32 bytes, text in 7 languages | Item category names and parameters (35). |
| [NxdDataUiJobAbilityHelp](NxdDataUiJobAbilityHelp.md) | NXD file | 303 | 35 rows of 12 bytes, text in 7 languages | Job ability help texts (35). |
| [NxdDataUIKeyAssign](NxdDataUIKeyAssign.md) | NXD file | 25 | 256 rows of 48 bytes | Key assignment table (256): main and alternate key codes. |
| [NxdDataUIKeyboardKeyIcon](NxdDataUIKeyboardKeyIcon.md) | NXD file | 332 | 167 rows of 8 bytes | Keyboard key icon map (167). |
| [NxdDataUIKeyboardLayout](NxdDataUIKeyboardLayout.md) | NXD file | 328 | 26 rows of 16 bytes | Keyboard layouts (26). |
| [NxdDataUIKeyboardType](NxdDataUIKeyboardType.md) | NXD file | 327 | 6 rows of 28 bytes | Keyboard types (6). |
| [NxdDataUIKeyConfig](NxdDataUIKeyConfig.md) | NXD file | 331 | 12 rows of 16 bytes | Key configuration groups (12). |
| [NxdDataUIKeyDefine](NxdDataUIKeyDefine.md) | NXD file | 35 | 256 rows of 32 bytes | Key definition table (256). |
| [NxdDataUILoadTexturePath](NxdDataUILoadTexturePath.md) | NXD file | 143 | 32 rows of 8 bytes | Loading screen texture paths (32). |
| [NxdDataUIMenuButtonLeft](NxdDataUIMenuButtonLeft.md) | NXD file | 180 | 8 rows of 32 bytes | Left menu buttons (8). |
| [NxdDataUIMenuSortList](NxdDataUIMenuSortList.md) | NXD file | 43 | 33 rows of 16 bytes | Menu sort option lists keyed by menu and slot. |
| [NxdDataUIMenuTab](NxdDataUIMenuTab.md) | NXD file | 95 | 6 rows of 8 bytes | Menu tabs keyed by menu and slot (6). |
| [NxdDataUIModal](NxdDataUIModal.md) | NXD file | 333 | 27 rows of 24 bytes | Modal window definitions (27). |
| [NxdDataUIMouseCollision](NxdDataUIMouseCollision.md) | NXD file | 329 | 21 rows of 12 bytes | UI mouse pick boxes (21). |
| [NxdDataUIOpCredit](NxdDataUIOpCredit.md) | NXD file | 316 | 130 rows of 32 bytes | Opening credit rows keyed by credit and part. |
| [NxdDataUIPadDefine](NxdDataUIPadDefine.md) | NXD file | 28 | 61 rows of 16 bytes | Pad button definitions (61). |
| [NxdDataUIPadGuide](NxdDataUIPadGuide.md) | NXD file | 278 | 15 rows of 44 bytes | Pad guide layouts (15). |
| [NxdDataUISituationSubtitles](NxdDataUISituationSubtitles.md) | NXD file | 224 | 74 rows of 8 bytes, text in 7 languages | Situation subtitle captions keyed by situation and line. |
| [NxdDataUISituationSubtitlesShowtime](NxdDataUISituationSubtitlesShowtime.md) | NXD file | 226 | 7 rows of 8 bytes | Subtitle display times (7). |
| [NxdDataUIStatusEffect](NxdDataUIStatusEffect.md) | NXD file | 57 | 45 rows of 36 bytes, text in 7 languages | Status effect names and captions (45) with a type. |
| [NxdDataUIStatusEffectCategory](NxdDataUIStatusEffectCategory.md) | NXD file | 56 | 13 rows of 24 bytes, text in 7 languages | Status effect category names (13 rows of 3 forms). |
| [NxdDataUISubMenu](NxdDataUISubMenu.md) | NXD file | 139 | 3 rows of 20 bytes | Sub menu definitions (3). |
| [NxdDataUISubTab](NxdDataUISubTab.md) | NXD file | 61 | 59 rows of 16 bytes | Sub tabs keyed by tab group and slot (59). |
| [NxdDataUISubtitles](NxdDataUISubtitles.md) | NXD file | 138 | 662 rows of 52 bytes, text in 7 languages | Event subtitles keyed by event and line, linked to voice labels. |
| [NxdDataUISubtitlesComponent](NxdDataUISubtitlesComponent.md) | NXD file | 162 | 79 rows of 16 bytes | Subtitle window components (79). |
| [NxdDataUISubtitlesTimeline](NxdDataUISubtitlesTimeline.md) | NXD file | 142 | 94 rows of 24 bytes | Subtitle timelines (94). |
| [NxdDataUISystemParam](NxdDataUISystemParam.md) | NXD file | 23 | 301 rows of 8 bytes | UI system parameter values (301). |
| [NxdDataUITitleCredit](NxdDataUITitleCredit.md) | NXD file | 308 | 1201 rows of 20 bytes | Title credit script rows (1201). |
| [NxdDataUIUnitStatusNumParam](NxdDataUIUnitStatusNumParam.md) | NXD file | 197 | 19 rows of 16 bytes | Unit status number fields (19). |
| [NxdDataUnitBarProfitResultMessage](NxdDataUnitBarProfitResultMessage.md) | NXD file | 205 | 240 rows of 12 bytes | Errand result message voice entries keyed by errand and slot. |
| [NxdDataUnitCommunMessage](NxdDataUnitCommunMessage.md) | NXD file | 192 | 72 rows of 12 bytes | Unit common message voice entries keyed by unit and slot. |
| [NxdDataUnitHelpMessage](NxdDataUnitHelpMessage.md) | NXD file | 194 | 572 rows of 44 bytes | Unit help message voice entries keyed by unit and line. |
| [NxdDataUnitPartMessage](NxdDataUnitPartMessage.md) | NXD file | 191 | 59 rows of 12 bytes | Unit part message voice entries. |
| [NxdDataUnitVoice](NxdDataUnitVoice.md) | NXD file | 204 | 10 rows of 28 bytes | Unit voice type definitions (10). |
| [NxdDataUnitWarnMessage](NxdDataUnitWarnMessage.md) | NXD file | 190 | 59 rows of 12 bytes | Unit warning message voice entries. |
| [NxdDataUserSituation](NxdDataUserSituation.md) | NXD file | 90 | 499 rows of 96 bytes | Story situation conditions keyed by situation and slot: up to three check types with indices, values and success flags. |
| [NxdDataVoicePattern](NxdDataVoicePattern.md) | NXD file | 185 | 110 rows of 24 bytes | Voice patterns (110). |
| [NxdDataVoicePatternSituation](NxdDataVoicePatternSituation.md) | NXD file | 196 | 18 rows of 16 bytes | Voice pattern situations keyed by pattern and slot, with story-condition links. |
| [NxdDataWorldMapProgressInfo](NxdDataWorldMapProgressInfo.md) | NXD file | 123 | 91 rows of 44 bytes, text in 7 languages | World-map progress steps keyed by group and step: towns, roads, caption and condition links. |
| [NxdDataWorldSituationBalloon](NxdDataWorldSituationBalloon.md) | NXD file | 286 | 90 rows of 76 bytes | World situation balloons keyed by period and slot (90). |
| [NxdDataZodiacStone](NxdDataZodiacStone.md) | NXD file | 119 | 27 rows of 40 bytes, text in 7 languages | Zodiac stones keyed by stone and variant: condition link, owner timeline, name, summary, description and icons. |
| [NxdDataZodiacStoneOwnerTimeline](NxdDataZodiacStoneOwnerTimeline.md) | NXD file | 238 | 11 rows of 16 bytes | Zodiac stone owner timelines (11). |
| [OpeningSpriteLists](OpeningSpriteLists.md) | Executable (initialised data) |  | 152 rows of 8 bytes | Per-language pointer sets of the opening sprite cell lists: four sets of 12 pointers, then four sets of 26. |
| [OpeningStepMaps](OpeningStepMaps.md) | Executable |  | 40 rows of 1 bytes | Byte step maps of the opening sequence plus three resource path strings (the title texture and two message texture files). |
| [PaletteFormats](PaletteFormats.md) | Executable |  | 2 rows of 16 bytes | Two palette format descriptors (16- and 256-colour palettes). |
| [PanelCellGroupPointers](PanelCellGroupPointers.md) | Executable (initialised data) |  | 32 rows of 8 bytes | Pointers to the sprite cell groups of the status window frame (four languages of eight modes). |
| [PanelScreenPalette](PanelScreenPalette.md) | Executable (initialised data) |  | 256 rows of 2 bytes | UI palette block of the second panel screen; the first 62 bytes equal EquipScreenPalette. |
| [PanelSlideCurve](PanelSlideCurve.md) | Executable |  | 12 rows of 2 bytes | Easing curve (symmetric, peak 144) a battle unit panel uses to slide a part of the panel in and out. |
| [PanelStateOffsets](PanelStateOffsets.md) | Executable |  | 16 rows of 1 bytes | A short list of signed offsets a unit panel row builder adds to a position; the bytes 0x2E, 0, 0, 0, 0, 0, 13, 13, 31, 31, 0, 0, -2, -1, -1, -1. |
| [PartyFaceIndex](PartyFaceIndex.md) | Executable |  | 74 rows of 1 byte | Maps a unit marker or job to a face record index. |
| [PartyFaceRecords](PartyFaceRecords.md) | Executable |  | 90 rows of 12 bytes | Portrait rectangle and variant of each party face. |
| [PoachCount](PoachCount.md) | Executable memory (saved with the game) |  | 97 entries of 1 byte | Poach count per type, 97 bytes based at the badge block plus 522; the poach add routine clamps each byte to 99. |
| [PoachersDenStock](PoachersDenStock.md) | Executable memory (saved with the game) |  | 261 entries of 1 byte | Poachers' Den stock: one count per item id 0..260 (PoachersDen_AddStock adds to it, clamped 0..255); the shop list builder Shop_BuildItemList lists the ids with stock when the shop id is 100 or above. |
| [PoachItem](PoachItem.md) | NXD file | 236 |  | The poach rows (the PoachItem-en table), read through PoachTable_GetRowById. |
| [PoachNewFlags](PoachNewFlags.md) | Executable memory (saved with the game) |  | 97 entries of 2 bytes | Two new-flag bytes per poach type at the badge block plus 813; a new game fills them with 0x0101 and the badge routine clears the high byte. |
| [PoachOrder](PoachOrder.md) | Executable memory (saved with the game) |  | 97 entries of 1 byte | The player-visible order of collected poach types, 97 bytes at the badge block plus 619; maintained together with the sort list. |
| [PoachSort](PoachSort.md) | Executable memory (saved with the game) |  | 97 entries of 1 byte | The user reordering of the poach types, 97 bytes at the badge block plus 716. |
| [PopupBounceCurve](PopupBounceCurve.md) | Executable |  | 13 rows of 2 bytes | Arc of offsets for a bouncing pop-up over 13 frames. |
| [PortraitCodes](PortraitCodes.md) | Executable |  | 211 rows of 2 bytes in each of five byte-identical copies (0x1406807C0, 0x140680070, 0x140681A90, 0x1406829F0, 0x140683A70) | Portrait code word of each generic look. |
| [PowersOfTen](PowersOfTen.md) | Executable |  | 10 rows of 4 bytes | Powers of ten used to split a number into decimal digits for text. |
| [PrimeNumbers](PrimeNumbers.md) | Executable |  | 54 rows of 1 byte | Primes below 256. |
| [RandomEncounters](RandomEncounters.md) | Executable (initialised data) |  | 57 rows of 24 bytes | Random encounters: per battleground and arrival road, the chance and formations by story progress. |
| [RangeRowMasks](RangeRowMasks.md) | Executable |  | 8 rows of 2 bytes | Bit-run masks (a triangle) used to build the diamond of the range overlay; 8 distances. |
| [ReactionGates](ReactionGates.md) | Executable |  | 32 bytes | One byte per reaction id: the reaction executor refuses an id whose byte has 1 in its low two bits. |
| [RecordBlockSectors](RecordBlockSectors.md) | Executable |  | 93 rows of 4 bytes | Sector start of each block of a packed data file that event commands load. |
| [RecordBlockSectors767](RecordBlockSectors767.md) | Executable (initialised data) |  | 115 rows of 4 bytes | Sector starts of 114 blocks of 16 sectors (32 KiB) of a second packed file; block 112 is empty. |
| [ResumeKindNames](ResumeKindNames.md) | Executable |  | 4 rows of 8 bytes (the run continues with two more string pointers) | Short names of the four kinds of a resume (suspend) save entry: main, world, attack, fturn. |
| [RoadPointLists](RoadPointLists.md) | Executable |  | 48 rows of 8 bytes | Per road, the list of way points that gets drawn once the road is open. |
| [RuntimeJobList](RuntimeJobList.md) | Executable (filled at run time) |  | 48 rows of 2 bytes | The Change Job list the game builds each time the job screen fills; the list length is a separate int16 at 0x143C510D8. |
| [SaveErrorMessages](SaveErrorMessages.md) | Executable |  | 48 rows of 8 bytes | Result code of the save-data layer to message number for the save and load screens. |
| [SaveFieldDescriptorLists](SaveFieldDescriptorLists.md) | Executable (built on the stack by code) |  | 11 / 108 / 76 / 2 descriptors of 88 bytes | The save schema: every saved record type has a function that builds an array of 88-byte field descriptors on the stack and hands it to FieldSchema_Run. |
| [ScenarioSetup](ScenarioSetup.md) | Executable (initialised data) |  | 887 rows of 24 bytes | Per story event / scenario: its scene setup record (map and battle settings). |
| [SceneMenuNodesADefault](SceneMenuNodesADefault.md) | Executable (initialised data) |  | 7 rows of 88 bytes | Seven legacy menu nodes of the scene menus, first group, default language. |
| [SceneMenuNodesALanguage0](SceneMenuNodesALanguage0.md) | Executable (initialised data) |  | 7 rows of 88 bytes | Seven legacy menu nodes of the scene menus, first group, language 0. |
| [SceneMenuNodesBDefault](SceneMenuNodesBDefault.md) | Executable (initialised data) |  | 7 rows of 88 bytes | Seven legacy menu nodes of the scene menus, second group, default language. |
| [SceneMenuNodesBLanguage0](SceneMenuNodesBLanguage0.md) | Executable (initialised data) |  | 7 rows of 88 bytes | Seven legacy menu nodes of the scene menus, second group, language 0. |
| [SceneSlotPermutations](SceneSlotPermutations.md) | Executable |  | 24 rows of 16 bytes | The 24 permutations of the four slots 0..3, walked by a sprite effect update to pick a slot order. |
| [SceneSpriteToFace](SceneSpriteToFace.md) | Executable |  | 160 rows of 4 bytes | Face number of each scene sprite id, read by the sprite-id-to-shape function and five inline copies of it. |
| [SceneTaskSlots](SceneTaskSlots.md) | Executable (filled at run time) |  | 1512 entries of 1 byte | Nine scene-task data records of 0xA8 bytes, parsed from u16 token streams during the battle map setup and captured in a kind-1 snapshot. |
| [SceneTaskTable](SceneTaskTable.md) | Executable (constant) |  | 16 entries of 8 bytes (scene task ids 0..15) | The 16-entry table of scene task handlers that the two scene loops call once per frame. |
| [SceneUnitSlots](SceneUnitSlots.md) | Executable (filled at run time) |  | 16 records of SceneUnitSlot | The 16 scene-unit records (stride 0x548); the in-use dword is 8 bytes before each. |
| [ScreenTaskSets](ScreenTaskSets.md) | Executable |  | 9 rows of 64 bytes | The window tasks started together for each legacy screen set (four handlers, their slot numbers, their expected tags). |
| [ScriptedActorPresets](ScriptedActorPresets.md) | Executable |  | 6 rows of 8 bytes | Scripted unit presets of one scene: a null-terminated list of 6 record pointers copied into the sprite palette and pose tables. |
| [SettlementEventPicks](SettlementEventPicks.md) | Executable (initialised data) |  | 11 rows of 10 bytes | Per settlement, which scene numbers a settlement event may pick (each of four values listed twice, so each has weight 2 of 8). |
| [ShopScreenPalette](ShopScreenPalette.md) | Executable |  | 16 rows of 2 bytes (first block) | 16 colours (15-bit) copied into the video page by the shop screen set-up. |
| [SineTable](SineTable.md) | Executable |  | 4097 rows of 4 bytes | Shared sine lookup, same layout as the cosine table; 4097 samples and 8 bytes of padding up to the next object. |
| [SkillsetTable](SkillsetTable.md) | Executable |  | 176 rows of 25 bytes | Ability slots of the stock skillsets. |
| [SkillsetTableMonster](SkillsetTableMonster.md) | Executable |  | 48 rows of 5 bytes | Monster skillsets: four ability slots per set. |
| [SkillsetTableSpecial](SkillsetTableSpecial.md) | Executable |  | 3 rows of 25 bytes | Three further skillsets in the same layout as SkillsetTable, selected by Skillset_GetAbility for the ids above the monster range. |
| [SoundPackPathPatterns](SoundPackPathPatterns.md) | Executable |  | 7 rows of 8 bytes | Seven sound pack path patterns: the common UI sound pack, the novel pack, the common sound pack, the per movie sound effect, voice and music packs (movie number %04d) and the per music pack (music number %05u). |
| [SpecialSheetHdTextures](SpecialSheetHdTextures.md) | Executable |  | 119 rows of 4 bytes (121 to the next symbol) | HD texture ids for the per-ability sheets of sprite sheet 0x9A. Verdict: engine-data. |
| [SpriteAnimScripts](SpriteAnimScripts.md) | Executable |  | 18 rows of 8 bytes | Eighteen sprite animation frame lists of the opening / title sprites: each frame is a cell group index and a number of ticks. |
| [SpriteClassicFilesByShape](SpriteClassicFilesByShape.md) | Executable |  | 170 rows of 8 bytes | Classic sprite file locator per shape, used for the palette load of the HD sheet. |
| [SpriteClassicFilesByShapeB](SpriteClassicFilesByShapeB.md) | Executable |  | 170 rows of 8 bytes | Second copy of the classic sprite file locator table, read when the language code is 0; byte-identical to SpriteClassicFilesByShape. |
| [SpriteDirection16MirrorFlags](SpriteDirection16MirrorFlags.md) | Executable |  | 16 rows of 2 bytes | Which of 16 facing directions draw a sprite mirrored. |
| [SpriteDirectionTables](SpriteDirectionTables.md) | Executable |  | 184 bytes in six sub-tables | Small per-facing tables read by the sprite record code: mirror flag words, frame flag masks, walk phase steps and palette base words. |
| [SpriteEffectKindFlags](SpriteEffectKindFlags.md) | Executable |  | 32 rows of 1 byte | One flag byte per sprite record kind read by the effect placement code. |
| [SpriteHdEntryByShape](SpriteHdEntryByShape.md) | Executable |  | 170 rows of 4 bytes | First HD sheet entry of every look in the g2d pack. |
| [SpriteLayerByteRows](SpriteLayerByteRows.md) | Executable |  | 3 rows of 24 bytes (80 to the next symbol) | Three rows of per-kind bytes stored into the sprite object (+18 / +19). |
| [SpriteLookAttributes](SpriteLookAttributes.md) | Executable |  | 170 rows of 4 bytes | Per look: which frame file and animation sequence file kind it uses, the pose remap flag and a scale byte. |
| [SpriteMotionByKind](SpriteMotionByKind.md) | Executable |  | 2 rows of 16 bytes | Motion number per sprite kind class, in two variants chosen by a flag test. |
| [SpritePaletteLimits](SpritePaletteLimits.md) | Executable |  | 208 rows of 1 bytes | Per sprite sheet, the highest palette number its units may use. |
| [SpritePieceTemplates](SpritePieceTemplates.md) | Executable (initialised data) |  | 221 rows of 24 bytes | Sprite piece templates of the world-map objects: thirteen sets of 17 pieces. |
| [SpriteShapeHdTexture](SpriteShapeHdTexture.md) | Executable |  | 82 rows of 4 bytes (84 to the next symbol) | HD texture id per sprite shape (effect and scene sprites), -1 for none. |
| [StatsNumbersLive](StatsNumbersLive.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Eight stat number fields (At, Atmagic, Def, Defmgc, Ar, Armagic, Av, Avmagic) of a legacy screen. |
| [StatsNumbersUnitA](StatsNumbersUnitA.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Fifteen number fields of the legacy unit page, variant a. |
| [StatsNumbersUnitB](StatsNumbersUnitB.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Fifteen number fields of the legacy unit page, variant b (two labels differ). |
| [StatsPanelCellsDefault](StatsPanelCellsDefault.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Detailed stats panel cells, language 1 / default. |
| [StatsPanelCellsLanguage0](StatsPanelCellsLanguage0.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the detailed stats panel (Move, Jump, weapon power, At / Def / Ar / Av), language 0. |
| [StatsPanelCellsLanguage2](StatsPanelCellsLanguage2.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Detailed stats panel cells, language 2. |
| [StatsPanelCellsLanguage3](StatsPanelCellsLanguage3.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Detailed stats panel cells, language 3. |
| [StatsPanelNumbers](StatsPanelNumbers.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Number fields of the detailed stats panel (attack, defence, evasion pairs). |
| [StatusGroupMasks](StatusGroupMasks.md) | Executable (constant) |  | 10 rows of 5 entries of 1 byte | The ten party-wide status group masks, five bytes each: a group test ANDs these bytes against the unit status bytes at +0x61..+0x65. |
| [StatusIconFlags](StatusIconFlags.md) | Executable (constant) |  |  | The per-status flag words the status panel update reads: index status+1, no bound check. |
| [StatusNumbersActorA](StatusNumbersActorA.md) | Executable (initialised data, written at run time) |  | 7 rows of 32 bytes | Number fields of the acting unit's status panel (variant A). |
| [StatusNumbersActorB](StatusNumbersActorB.md) | Executable (initialised data) |  | 6 rows of 32 bytes | Number fields of the acting unit's status panel (variant B, no AT). |
| [StatusNumbersTargetA](StatusNumbersTargetA.md) | Executable (initialised data, written at run time) |  | 7 rows of 32 bytes | Number fields of the target unit's status panel (variant A). |
| [StatusNumbersTargetB](StatusNumbersTargetB.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Number fields of the target unit's status panel with the hit chance (variant B). |
| [StatusPanelFrameLines](StatusPanelFrameLines.md) | Executable |  | 8 rows of 7 bytes | Eight one-pixel shaded border lines of the battle status panel (light and dark pairs). |
| [StatusPanelLayoutsDefault](StatusPanelLayoutsDefault.md) | Executable (initialised data) |  | 8 rows of 8 bytes | Per status panel kind, its layout block, for text languages 1 and every language that has no table of its own. |
| [StatusPanelLayoutsLanguage0](StatusPanelLayoutsLanguage0.md) | Executable (initialised data) |  | 8 rows of 8 bytes | Per status panel kind, its layout block, language 0. |
| [StatusPanelLayoutsLanguage2](StatusPanelLayoutsLanguage2.md) | Executable (initialised data) |  | 8 rows of 8 bytes | Per status panel kind, its layout block, text language 2. |
| [StatusPanelLayoutsLanguage3](StatusPanelLayoutsLanguage3.md) | Executable (initialised data) |  | 8 rows of 8 bytes | Per status panel kind, its layout block, text language 3. |
| [StatusPanelPaletteIds](StatusPanelPaletteIds.md) | Executable (initialised data) |  | 22 rows of 2 bytes | Palette ids of the battle status panel parts. |
| [StatusProperties](StatusProperties.md) | Executable |  | 40 rows of 16 bytes | Per status: priority, countdown, group flags, the statuses it cancels and the statuses that block it. |
| [SteamApiImportSlots](SteamApiImportSlots.md) | Executable |  | 11 rows of 8 bytes (the tail of the import table) | Import address slots of eleven functions of the Steam API library (find or create user interface, unregister call result, context init, get user handle, restart app if necessary, API init, register / unregister callba... |
| [SurfacePairConstants](SurfacePairConstants.md) | Executable |  | 63 rows of 2 bytes | Per surface type, two bytes that are 25 everywhere; their two destination words have no other reader. |
| [TerrainProperties](TerrainProperties.md) | Executable |  | 2 blocks of 64 bytes | Two 64-byte blocks indexed by terrain type: the ability id the terrain gives and a flag byte whose bit 0x80 marks harmful terrain. |
| [TextPackPaths](TextPackPaths.md) | Executable |  | 45 rows of 8 bytes | Pointers to the file paths of 45 text resources (event help, spell, sample, world, opening, join text, the system text sets, battle and menu tutorials, scenario pages). |
| [TextPools](TextPools.md) | Executable (filled at load) |  | 32 pointers | The thirty-two text pool pointers the generic text decoder indexes by a text id's kind bits. |
| [TownMenuKindBySettlement](TownMenuKindBySettlement.md) | Executable |  | 44 rows of 4 bytes | Per settlement, whether it offers the three-row town menu (Outfitter, Tavern, Warriors' Guild). |
| [TriggerConditionArgCounts](TriggerConditionArgCounts.md) | Executable |  | 40 rows of 1 bytes | Argument count per trigger-condition opcode of the battle event condition lists. |
| [UiCoreNameKeys](UiCoreNameKeys.md) | Executable |  | 43 rows of 8 bytes | The 43 fixed names the UI system registers first: widget events (Show, Hide, Enable, Disable, FocusIn, FocusOut, CursorOver, CursorOut, Click, Check, Open, Close, gauge and scroll events, In / Out), widget part names ... |
| [UiEquipScreenNodeNames](UiEquipScreenNodeNames.md) | Executable |  | 9 rows of 8 bytes | Names of the nodes and animations of the HD equipment screen. |
| [UiEventCommandNames](UiEventCommandNames.md) | Executable |  | 8 rows of 8 bytes | Command words of the event window markup (forced, wait, cursor, cursor end, no set, value set, time, branch). |
| [UiEventWindowFontAndNameNodeRun](UiEventWindowFontAndNameNodeRun.md) | Executable |  | 2 rows of 8 bytes at the head (the sweep run holds 182 slots) | Head list of 2 node name pointers (Normalfont, TextName); the run continues into class vtables (13 class vtables: event, common parts, gil and character number, notice dialog, main menu parts, horoscope affinity, job ... |
| [UiGlyphCodeTriples](UiGlyphCodeTriples.md) | Executable |  | 73 rows of 3 bytes | Scan list used to turn a character code 1..72 into a glyph slot (row index). |
| [UiGuideTipPageNamesRun](UiGuideTipPageNamesRun.md) | Executable |  | 6 rows of 8 bytes at the head (the sweep run holds 896 slots) | Head list of 6 node name pointers (page01 to page06); the run continues into class vtables (54 class vtables: guide, bar (profit, gossip, main list), menu base, shop, end slate, classic band / loading / subtitles, end... |
| [UiLauncherButtonOrder](UiLauncherButtonOrder.md) | Executable |  | 8 rows of 4 bytes (7 used) | Button ids of the start launcher in focus order. |
| [UiLauncherControllerGuideLabelsRun](UiLauncherControllerGuideLabelsRun.md) | Executable |  | 15 rows of 8 bytes at the head (the sweep run holds 25 slots) | Head list of 15 node name pointers (Controller button label nodes (L2, L1, select, d-pad, left stick, L3, R2, R1, right buttons, right stick, R3, start)); the run continues into class vtables (UIAddonFFTOLauncher (sec... |
| [UiLauncherFocusNeighborsAlt](UiLauncherFocusNeighborsAlt.md) | Executable |  | 7 rows of 24 bytes | Directional focus neighbours of the seven buttons of the start launcher, alternate layout (the default layout of the same shape is at 0x14070A8D0). |
| [UiLauncherModeNamesRun](UiLauncherModeNamesRun.md) | Executable |  | 2 rows of 8 bytes at the head (the sweep run holds 99 slots) | Head list of 2 node name pointers (EnhancedMode and ClassicMode node names); the run continues into class vtables (6 class vtables: launcher, title cushion, launcher agent, start config (two) and its agent). |
| [UiLegacyLayoutScriptOps](UiLegacyLayoutScriptOps.md) | Executable |  | 22 rows of 8 bytes | Handlers of the 22 opcodes of the legacy layout script (the record language of the job choice, job detail and other legacy pages: {opcode, length, arguments} until opcode 22). |
| [UiLegacyWindowCellLayoutBase](UiLegacyWindowCellLayoutBase.md) | Executable |  | about 81 rows of 12 bytes | Cell records (kind, size, offset) of a legacy list window, base set. |
| [UiLegacyWindowColourSetsLang1](UiLegacyWindowColourSetsLang1.md) | Executable |  | colour dwords (about 1888 bytes) | Colour set of a legacy list window, text language 1. |
| [UiLegacyWindowColourSetsLang2](UiLegacyWindowColourSetsLang2.md) | Executable |  | colour dwords (about 2000 bytes) | Colour set of a legacy list window, text language 2. |
| [UiLegacyWindowColourSetsLang3](UiLegacyWindowColourSetsLang3.md) | Executable |  | colour dwords (about 1632 bytes) | Colour set of a legacy list window, text language 3. |
| [UiLegacyWindowGroupStartsLang0](UiLegacyWindowGroupStartsLang0.md) | Executable |  | 12 rows of 1 byte (+4 padding) | Cumulative start indexes of 12 cell groups of a legacy list window, text language 0. |
| [UiLegacyWindowGroupStartsLang1](UiLegacyWindowGroupStartsLang1.md) | Executable |  | 12 rows of 1 byte (+4 padding) | Cumulative start indexes of 12 cell groups of a legacy list window, text language 1. |
| [UiLegacyWindowGroupStartsLang2](UiLegacyWindowGroupStartsLang2.md) | Executable |  | 12 rows of 1 byte (+4 padding) | Cumulative start indexes of 12 cell groups of a legacy list window, text language 2. |
| [UiLegacyWindowGroupStartsLang3](UiLegacyWindowGroupStartsLang3.md) | Executable |  | 12 rows of 1 byte (+4 padding) | Cumulative start indexes of 12 cell groups of a legacy list window, text language 3. |
| [UiPartyMemberPartNodeNamesRun](UiPartyMemberPartNodeNamesRun.md) | Executable |  | 6 rows of 8 bytes at the head (the sweep run holds 353 slots) | Head list of 6 node name pointers (six party member part nodes (parts, parts00 to parts04)); the run continues into class vtables (19 class vtables: save / load, system top, subtitles, novel, brave story (Darlavon, tr... |
| [UiRadioButtonNodeNamesRun](UiRadioButtonNodeNamesRun.md) | Executable |  | 4 rows of 8 bytes at the head (the sweep run holds 659 slots) | Head list of 4 node name pointers (RadioButton01 to RadioButton04); the run continues into class vtables (39 class vtables: system message, battle command, warning, announce, battle (continuous, dialog, flytext, join,... |
| [UiStartupScreenNodeNamesRun](UiStartupScreenNodeNamesRun.md) | Executable |  | 3 rows of 8 bytes at the head (the sweep run holds 557 slots) | Head list of 3 node name pointers (ShowEnFrDe, ShowJa, ShowTitle); the run continues into class vtables (41 class vtables: startup, text input, poach, employ and item screens, guide). |
| [UiStoryButtonNodeNamesRun](UiStoryButtonNodeNamesRun.md) | Executable |  | 10 rows of 8 bytes at the head (the sweep run holds 451 slots) | Head list of 10 node name pointers (ButtonArazlamL00..L02, S00..S03, Darlavon00..02); the run continues into class vtables (27 class vtables: brave story top, achievement notifications, novel manager callback, world m... |
| [UiTabButtonNodeNamesRun](UiTabButtonNodeNamesRun.md) | Executable |  | 3 rows of 8 bytes at the head (the sweep run holds 237 slots) | Head list of 3 node name pointers (TabButton01 to TabButton03); the run continues into class vtables (16 class vtables: brave story glossary, work history, zodiac stone, journal, collection, books). |
| [UnitEditorRangesA](UnitEditorRangesA.md) | Executable (initialised data) |  | 22 rows of 8 bytes | Value ranges of the 22 editable fields of the unit editor screen, mode A (level 1..99, brave / faith 0..100, three ability id ranges 144..171, 172..207, 208..239, ...). |
| [UnitEditorRangesB](UnitEditorRangesB.md) | Executable (initialised data) |  | 22 rows of 8 bytes | Value ranges of the unit editor, mode B: rows 0..13 equal mode A, rows 14..18 each allow 1..356 where mode A allows 1..187 twice and then three ranges 428..453, 454..485, 486..509, rows 19..21 equal mode A. Verdict: d... |
| [UnitEditorWidgetsDefault](UnitEditorWidgetsDefault.md) | Executable (initialised data) |  | 22 rows of 24 bytes | Widget records of the 22 editable fields of the unit editor screen, every other language. |
| [UnitEditorWidgetsLanguage0](UnitEditorWidgetsLanguage0.md) | Executable (initialised data) |  | 22 rows of 24 bytes | Widget records of the 22 editable fields of the unit editor screen, text language 0. |
| [UnitEquipOverride](UnitEquipOverride.md) | Executable (filled at run time) |  |  | Five override equipment words per unit, ten bytes per unit index: when the pair is non-zero the equip pickers use it in place of the unit record's own hand words. |
| [UnitJobFlags](UnitJobFlags.md) | Executable (filled at run time) |  | 1 block of 146 bytes (21 + 125 flag bytes) | The job flag block: 21 per-job "new" flags and 125 per-job-type disable flags. |
| [UnitLookPoolIndex](UnitLookPoolIndex.md) | Executable (filled at run time) |  | 21 entries of 4 bytes | Look pool index of each battle unit by its unit index (+444): written by SceneUnit_BuildFromQueueEntry when it builds the unit's scene unit, read back by it on the resume path (load mode 1) and by sub_1401D46B0; insid... |
| [UnitPageNumberFieldsA](UnitPageNumberFieldsA.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Number fields of the second unit page, first panel. |
| [UnitPageNumberFieldsB](UnitPageNumberFieldsB.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Number fields of the second unit page, second panel. |
| [UnitPanelCellsLanguage0](UnitPanelCellsLanguage0.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the unit status page, language 0 (18 cells). |
| [UnitPanelCellsLanguage1](UnitPanelCellsLanguage1.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the unit status page, language 1 (18 cells). |
| [UnitPanelCellsLanguage2](UnitPanelCellsLanguage2.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the unit status page, language 2 (18 cells). |
| [UnitPanelCellsLanguage3](UnitPanelCellsLanguage3.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the unit status page, language 3 (18 cells). |
| [UnitPanelNumberFieldsA](UnitPanelNumberFieldsA.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Number fields (Move, Jump, Wt, weapon powers, At, Def, Ar, Av and their magic pairs) of the unit status page, first panel. |
| [UnitPanelNumberFieldsB](UnitPanelNumberFieldsB.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Number fields of the unit status page, second panel. |
| [UnitPanelScriptBlock0](UnitPanelScriptBlock0.md) | Executable (initialised data) |  | 1 rectangle and 1 script block | A panel window rectangle followed by a UI script block of the unit panel page (block 0). |
| [UnitPanelScriptBlock1](UnitPanelScriptBlock1.md) | Executable (initialised data) |  | 1 rectangle and 1 script block | A panel window rectangle followed by a UI script block of the unit panel page (block 1). |
| [UnitPanelScriptBlock2](UnitPanelScriptBlock2.md) | Executable (initialised data) |  | 1 rectangle and 1 script block | A panel window rectangle followed by a UI script block of the unit panel page (block 2). |
| [UnitPanelScriptBlock3](UnitPanelScriptBlock3.md) | Executable (initialised data) |  | 1 rectangle and 1 script block | A panel window rectangle followed by a UI script block of the unit panel page (block 3). |
| [UnitSaveSlots](UnitSaveSlots.md) | Executable (filled at run time) |  | 54 records of 600 bytes | The live unit save table: the units as the save keeps them. |
| [UnitSceneSlotIndex](UnitSceneSlotIndex.md) | Executable (filled at run time) |  | 21 entries of 4 bytes | Scene-unit slot of each battle unit by its unit index (+444), -1 none: written by SceneUnit_BuildFromQueueEntry (a slot taken by another unit clears that unit's entry) and sub_14026A048, cleared by sub_140210AF0, read... |
| [UnitSpritePosePack](UnitSpritePosePack.md) | Executable (initialised data) |  | 107 offsets | Offset index and pose records for drawing a unit sprite as a rotated quad: 107 offsets, records of 28 bytes. |
| [UnitStatusNumbersMode0](UnitStatusNumbersMode0.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the legacy unit info message window, actor with level and experience. |
| [UnitStatusNumbersMode1](UnitStatusNumbersMode1.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Number fields of the legacy unit info message window, actor with hit chance. |
| [UnitStatusNumbersMode2](UnitStatusNumbersMode2.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Number fields of the legacy unit info message window, target with hit chance. |
| [UnitStatusNumbersMode3](UnitStatusNumbersMode3.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the legacy unit info message window, target with level and experience. |
| [WeatherBySeason](WeatherBySeason.md) | Executable |  | 56 bytes: 4 + 4 + 4 x 10 + 4 + 4 | Four calendar season boundaries (month and day) and, per season, ten weighted weather level adjustments. |
| [WindowCurvePointers](WindowCurvePointers.md) | Executable |  | 5 rows of 8 bytes | Pointers to the five window open / close animation step lists. |
| [WindowGrowSteps](WindowGrowSteps.md) | Executable |  | 12 rows of 1 bytes | Per-frame edge movement of the window grow animation for each window style. |
| [WindowPatternTiles](WindowPatternTiles.md) | Executable (initialised data) |  | 2088 rows of 2 bytes | Line patterns of the legacy window frames (borders and gradient rows) as 16-bit words, in a block of 2088 words. |
| [WorldMapRoads](WorldMapRoads.md) | Executable |  | 51 rows of 8 bytes | The 51 world-map roads: their two end locations, travel cost and drawn way points; event variable 556 + n opens road n. |
| [XmlStatusNames](XmlStatusNames.md) | Executable |  | 27 rows of 8 bytes | Names of the XML parser status codes (success, no attribute, wrong attribute type, file not found, could not be opened, read error, parsing errors per node kind, empty document, mismatched element, cannot convert text... |
