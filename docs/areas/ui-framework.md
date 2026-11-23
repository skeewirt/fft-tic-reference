# UI framework

GUI nodes, text/font rendering, widgets, input, hit testing and the UI render/command pipeline.

Functions: 782, Structures: 138, Globals: 8, Registries: 17, File formats: 7, Flows: 7, Observed behaviours: 30, Tables: 234.

## Functions (782)

| Name | Address | Purpose |
|---|---|---|
| [Achievement_CounterReached](../functions/Achievement_CounterReached.md) | `0x1400DC984` | Tells whether an achievement's counter has reached its threshold. |
| [Achievement_LookupTelemetryRow](../functions/Achievement_LookupTelemetryRow.md) | `0x1400DEFAC` | Looks up an achievement's telemetry row (part read). |
| [Achievement_RowExists](../functions/Achievement_RowExists.md) | `0x1400DCB3C` | Tests that the Achievement row of key 9 exists. |
| [AchievementOther_CounterMatch](../functions/AchievementOther_CounterMatch.md) | `0x1400DE08C` | Counter test of the deep-dungeon-clear and side-story achievement classes. |
| [AchievementOtherJournal_Match](../functions/AchievementOtherJournal_Match.md) | `0x1400DDFD4` | Match function of the Chronicle-event achievement class (vtable 0x1407031E8). |
| [AchievementOtherNovel_Match](../functions/AchievementOtherNovel_Match.md) | `0x1400DDF1C` | Match function of the book-read achievement class (vtable 0x1407032A8). |
| [AdditionalKerning_Lookup](../functions/AdditionalKerning_Lookup.md) | `0x1403BA2D4` | Looks up the (left, right) glyph pair in the .ker table's std::map and returns its extra (x, y) kerning (0 when missing); builds the map first when it is dirty. |
| [BattleMsg_BannerHandlerA](../functions/BattleMsg_BannerHandlerA.md) | `0x1400E8930` | Handler body that shows the centre banner after its agent's vfunc +16 returns true: it calls UIMessageBanner_Show with the battle banner object, the descriptor and the enable flag. |
| [BattleMsg_BannerHandlerB](../functions/BattleMsg_BannerHandlerB.md) | `0x1400E8A84` | Second handler body on the banner path: like BattleMsg_BannerHandlerA it calls UIMessageBanner_Show with the battle banner object, the descriptor and the enable flag after its agent's vfunc +16 test. |
| [BattleMsg_InitHandlerTable](../functions/BattleMsg_InitHandlerTable.md) | `0x1400E28D0` | Fills an object's battle-message handler slots from the table based at a1+2528. |
| [BattleMsg_ShowPrompt](../functions/BattleMsg_ShowPrompt.md) | `0x1400EE908` | Builds a class 1 / subtype 27 message descriptor from a dword of the object and shows it in the banner; then calls sub_140111B74 twice. |
| [BgmMode_BuildLists](../functions/BgmMode_BuildLists.md) | `0x1401C850C` | Builds the two track lists of the music player screen from the BGMMode table. |
| [BgmMode_DrawRow](../functions/BgmMode_DrawRow.md) | `0x1401C7DAC` | Draws one row of the music player list. |
| [BgmMode_OnTabButton](../functions/BgmMode_OnTabButton.md) | `0x1401C8250` | Switches the music player's list when a tab button is pressed. |
| [BgmMode_PlaySelected](../functions/BgmMode_PlaySelected.md) | `0x1401C811C` | Plays the track under the cursor of the music player. |
| [BgmMode_SwitchTab](../functions/BgmMode_SwitchTab.md) | `0x1401C8308` | Moves the music player between its two lists on the tab input actions. |
| [BgmMode_ToggleTitleLanguage](../functions/BgmMode_ToggleTitleLanguage.md) | `0x1401C8438` | Toggles the alternate track titles of the music player. |
| [Book_ShowGuide](../functions/Book_ShowGuide.md) | `0x14016620C` | Opens the guide that explains the reading shelf. |
| [BookProgress_ResetConfirmInput](../functions/BookProgress_ResetConfirmInput.md) | `0x140372990` | Two-row question about the record of a book (table index 20): one answer clears the book's progress record. |
| [BookShelf_Fill](../functions/BookShelf_Fill.md) | `0x140166E08` | Fills the five slots of the Reading Materials shelf. |
| [Boot_MovieFrame](../functions/Boot_MovieFrame.md) | `0x1402F2E40` | Per-frame handler of the boot movie: ends it on the skip rules and copies the decoded frame into three textures. |
| [ButtonIcon_Draw](../functions/ButtonIcon_Draw.md) | `0x1402BE284` | Draws one animated button icon: the sprite pieces of an icon group with a press animation. |
| [ChroniclePeriod_GetIcon](../functions/ChroniclePeriod_GetIcon.md) | `0x1401E58B4` | Returns a Chronicle period's icon. |
| [ChroniclePeriod_ListUnlocked](../functions/ChroniclePeriod_ListUnlocked.md) | `0x1401E572C` | Lists the Chronicle periods that are unlocked. |
| [ChronicleTimeline_LayoutChapters](../functions/ChronicleTimeline_LayoutChapters.md) | `0x140178384` | Lays out the timeline bar by the number of periods in each chapter section. |
| [ChronicleTimeline_Setup](../functions/ChronicleTimeline_Setup.md) | `0x140173E08` | Sets up the Chronicle timeline bar from the unlocked periods. |
| [ClassicCursorRows_Select](../functions/ClassicCursorRows_Select.md) | `0x14036E28C` | Moves the cursor of a legacy menu to the row chosen in the state record. |
| [ClassicItemListPage_Run](../functions/ClassicItemListPage_Run.md) | `0x140393E70` | Legacy party menu item list page: draws the list body and its header. |
| [ClassicItemUi_OpAdvanceOpening](../functions/ClassicItemUi_OpAdvanceOpening.md) | `0x14039D1EC` | Slot 22 of the item page script: advances the opening stage. |
| [ClassicItemUi_OpDrawIconCell](../functions/ClassicItemUi_OpDrawIconCell.md) | `0x14039B210` | Slot 6 of the item page script: a picture cell from a row callback's descriptor. |
| [ClassicItemUi_OpDrawLine](../functions/ClassicItemUi_OpDrawLine.md) | `0x14039B110` | Slot 7 of the item page script: a line between two points. |
| [ClassicItemUi_OpDrawNumber](../functions/ClassicItemUi_OpDrawNumber.md) | `0x14039BE28` | Slot 13 of the item page script: a number or a gauge from a row callback. |
| [ClassicItemUi_OpDrawWindow](../functions/ClassicItemUi_OpDrawWindow.md) | `0x14039B2C8` | Slot 0 of the item page script: a bordered window and its fill. |
| [ClassicItemUi_OpDrawWindowOpening](../functions/ClassicItemUi_OpDrawWindowOpening.md) | `0x14039B81C` | Slot 18 of the item page script: the opening window. |
| [ClassicItemUi_OpFillRect](../functions/ClassicItemUi_OpFillRect.md) | `0x14039AF2C` | Slot 3 of the item page script: a flat-coloured rectangle. |
| [ClassicItemUi_OpFillTiles](../functions/ClassicItemUi_OpFillTiles.md) | `0x14039B914` | Slot 17 of the item page script: a rectangle filled with 16-pixel tiles. |
| [ClassicItemUi_OpIf](../functions/ClassicItemUi_OpIf.md) | `0x14039AD90` | Slot 1 of the item page script: the conditional record. |
| [ClassicItemUi_OpIfElse](../functions/ClassicItemUi_OpIfElse.md) | `0x14039AE40` | Slot 2 of the item page script: the conditional record with an else branch. |
| [ClassicItemUi_OpQueueRect](../functions/ClassicItemUi_OpQueueRect.md) | `0x14039D14C` | Slot 20 of the item page script: a rectangle from the record. |
| [ClassicItemUi_OpQueueScreenRect](../functions/ClassicItemUi_OpQueueScreenRect.md) | `0x14039D1B0` | Slot 21 of the item page script: the fixed screen rectangle. |
| [ClassicItemUi_OpQueueScreenRectOnce](../functions/ClassicItemUi_OpQueueScreenRectOnce.md) | `0x14039D0FC` | Slot 19 of the item page script: the fixed screen rectangle after a window animation. |
| [ClassicItemUi_OpScrollList](../functions/ClassicItemUi_OpScrollList.md) | `0x14039C784` | Slot 16 of the item page script: a scrolling list. |
| [ClassicItemUi_OpSetBlendFlag](../functions/ClassicItemUi_OpSetBlendFlag.md) | `0x14039BD14` | Slot 14 of the item page script: the semi-transparency word. |
| [ClassicItemUi_OpSetDrawMode](../functions/ClassicItemUi_OpSetDrawMode.md) | `0x14039BD28` | Slot 24 of the item page script: a draw-mode change. |
| [ClassicItemUi_OpSetPageWord](../functions/ClassicItemUi_OpSetPageWord.md) | `0x14039BC98` | Slot 12 of the item page script: the texture-page attribute word. |
| [ClassicItemUi_OpSetPaletteWord](../functions/ClassicItemUi_OpSetPaletteWord.md) | `0x14039BBD0` | Slot 9 of the item page script: the palette word. |
| [ClassicItemUi_OpSetPaletteWordAlt](../functions/ClassicItemUi_OpSetPaletteWordAlt.md) | `0x14039BC1C` | Slot 10 of the item page script: the palette word with an alternate operand set. |
| [ClassicItemUi_OpSetPriority](../functions/ClassicItemUi_OpSetPriority.md) | `0x14039BE14` | Slot 15 of the item page script: the priority word. |
| [ClassicItemUi_OpSetTint](../functions/ClassicItemUi_OpSetTint.md) | `0x14039BDD0` | Slot 11 of the item page script: the tint colour. |
| [ClassicItemUsePage_Run](../functions/ClassicItemUsePage_Run.md) | `0x1403934B0` | Legacy party menu item use page: picks an item and applies it to a unit. |
| [ClassicJobDetailPage_Run](../functions/ClassicJobDetailPage_Run.md) | `0x140392DB8` | Legacy party menu job detail page: four pages of the chosen job with page switching. |
| [ClassicListPage_BuildRangeList](../functions/ClassicListPage_BuildRangeList.md) | `0x14037B8FC` | Builds the list of entry ids of the current category of a legacy list page and hands it to the list drawer. |
| [ClassicMenu_HubStep](../functions/ClassicMenu_HubStep.md) | `0x14036D314` | Step of the controller that sits under the other screens (table index 1): after a screen closes it decides, from flag masks of the state dword, which screen opens next. |
| [ClassicMenu_LoadPageArtPack](../functions/ClassicMenu_LoadPageArtPack.md) | `0x140343770` | Loads the art pack of a legacy menu page (0..5) into the shared menu texture buffer. |
| [ClassicMenu_PopTownMenu](../functions/ClassicMenu_PopTownMenu.md) | `0x140345EFC` | Pops a menu screen and lowers the window counters for the windows it opened. |
| [ClassicMenu_RunScreenStack](../functions/ClassicMenu_RunScreenStack.md) | `0x140246078` | The task that runs the classic menus, world map and towns: each frame it calls the input step of the screen on top of a stack of controllers. |
| [ClassicMenu_ScreenWipeStep](../functions/ClassicMenu_ScreenWipeStep.md) | `0x1402CC42C` | Step of a screen wipe (table index 35): a frame-counted fade and slide of the picture layers, with a phase in the record. |
| [ClassicPartyMenu_Run](../functions/ClassicPartyMenu_Run.md) | `0x14033E4C4` | Per-frame driver of the legacy party menu: prepares the shared header state and runs the handler of the current mode. |
| [ClassicSubtitles_SetState](../functions/ClassicSubtitles_SetState.md) | `0x140196C80` | Plays the state of the classic subtitle window. |
| [ClassicSubtitles_Step](../functions/ClassicSubtitles_Step.md) | `0x1401969CC` | Per-frame step of the classic-movie subtitle window: finds the line whose time window holds the movie time and sets its text and layout state. |
| [ClassicUi_OpAnimatedFrame](../functions/ClassicUi_OpAnimatedFrame.md) | `0x140390744` | Opcode 18: a window frame that grows open over the first 8 page redraws. |
| [ClassicUi_OpDrawCell](../functions/ClassicUi_OpDrawCell.md) | `0x1403901D4` | Opcodes 4 and 5: queues one sprite cell. |
| [ClassicUi_OpDrawNumber](../functions/ClassicUi_OpDrawNumber.md) | `0x140390BA4` | Opcode 13: draws a number or a row of gauge cells for a value supplied by the page. |
| [ClassicUi_OpIf](../functions/ClassicUi_OpIf.md) | `0x140390024` | Opcode 1: runs the next records only when a page condition holds, otherwise skips them. |
| [ClassicUi_OpIfElse](../functions/ClassicUi_OpIfElse.md) | `0x1403900D4` | Opcode 2: as opcode 1 with an else branch. |
| [ClassicUi_OpQueueRect](../functions/ClassicUi_OpQueueRect.md) | `0x140391B04` | Slot 20 of the layout script table: a rectangle from the record. |
| [ClassicUi_OpQueueScreenRect](../functions/ClassicUi_OpQueueScreenRect.md) | `0x140391B68` | Slot 21 of the layout script table: the fixed screen rectangle. |
| [ClassicUi_OpQueueScreenRectOnce](../functions/ClassicUi_OpQueueScreenRectOnce.md) | `0x140391AA4` | Slot 19 of the layout script table: the fixed screen rectangle once. |
| [ClassicUi_OpScrollList](../functions/ClassicUi_OpScrollList.md) | `0x1403911B4` | Slot 16 of the layout script table: the scrolling list. |
| [ClassicUi_OpSetBlendWord](../functions/ClassicUi_OpSetBlendWord.md) | `0x140390B0C` | Opcode 12: composes the blend and mode word of the following cells. |
| [ClassicUi_OpSetLayer](../functions/ClassicUi_OpSetLayer.md) | `0x1403901C0` | Opcode 14: sets the layer word used by the following cells. |
| [ClassicUi_OpSetPriority](../functions/ClassicUi_OpSetPriority.md) | `0x140390B88` | Opcode 15: sets the draw priority word unless a plate is being built. |
| [ClassicUi_OpSetTexturePageA](../functions/ClassicUi_OpSetTexturePageA.md) | `0x140390A44` | Opcode 9: sets the texture page and palette word used by the following cells. |
| [ClassicUi_OpSetTexturePageB](../functions/ClassicUi_OpSetTexturePageB.md) | `0x140390A90` | Opcode 10: as opcode 9 with a second set of arguments for an alternate display mode. |
| [ClassicUi_OpTileGrid](../functions/ClassicUi_OpTileGrid.md) | `0x140390800` | Opcode 17: fills a rectangle with 8 x 8 tiles. |
| [ClassicUi_OpWindowFrame](../functions/ClassicUi_OpWindowFrame.md) | `0x140390294` | Opcode 0: draws a bordered window of a given size at a position. |
| [ClassicUi_RunLayoutScript](../functions/ClassicUi_RunLayoutScript.md) | `0x14038FFB8` | Runs one layout script of the legacy menus: a list of records that draw windows, cells and numbers. |
| [ComponentDrawContext_Build](../functions/ComponentDrawContext_Build.md) | `0x1403EDCA4` | Creates the child draw context of a component: copy of the parent (0x258 bytes), composed matrix, opacity and colour. |
| [ComponentEffects_Collect](../functions/ComponentEffects_Collect.md) | `0x1403E809C` | Copies every enabled effect group of the component's property block into the draw context and reports whether an offscreen layer is needed. |
| [ComponentLayer_Begin](../functions/ComponentLayer_Begin.md) | `0x1403E8FA4` | Decides whether a component needs its own offscreen layer and opens it. |
| [ComponentLayer_DrawMaskComponent](../functions/ComponentLayer_DrawMaskComponent.md) | `0x1403E647C` | Draws a component's mask component (ctx+392, with the Mask node as its property block ctx+400) into a fresh layer record; called by ComponentLayer_Begin the first time a layer with a mask is opened. |
| [ConfigMenu_ConfirmDiscard](../functions/ConfigMenu_ConfirmDiscard.md) | `0x14018E650` | Opens UIDialog 63 when settings changes are pending and Back is pressed. |
| [ConfigMenu_DrawRowValue](../functions/ConfigMenu_DrawRowValue.md) | `0x140190194` | Draws a row's value by item type, optionally stepping it first. |
| [ConfigMenu_EnableRowWidgets](../functions/ConfigMenu_EnableRowWidgets.md) | `0x140193A20` | Enables or disables a row's arrows, slider and switch collisions. |
| [ConfigMenu_LockList](../functions/ConfigMenu_LockList.md) | `0x140193958` | Turns the row list's input off or on (gadget +128, the rows' widgets, the tab collisions). |
| [ConfigMenu_OnDefaultsConfirm](../functions/ConfigMenu_OnDefaultsConfirm.md) | `0x140194C00` | Answer of the screen's own confirm window (0 = do it, anything else = cancel): hides the window and returns the screen to its list. |
| [ConfigMenu_ReadSettings](../functions/ConfigMenu_ReadSettings.md) | `0x14018C72C` | Reads the game settings' values per ConfigItem id into +648 of the add-on, every frame. |
| [ConfigMenu_SetHelpText](../functions/ConfigMenu_SetHelpText.md) | `0x1401928AC` | Sets the help line (the Text part of Config/TextArea) from the item's help text id. |
| [ConfigMenu_SetTabTitles](../functions/ConfigMenu_SetTabTitles.md) | `0x14018E6CC` | Sets the tab button titles from the ConfigCategory rows and the MainTab header. |
| [ConfigMenu_ShowTab](../functions/ConfigMenu_ShowTab.md) | `0x14018EA74` | Fills the row list of a tab from its ConfigCategory and sets the tab states and header. |
| [ConfigMenu_UpdateFooter](../functions/ConfigMenu_UpdateFooter.md) | `0x140192790` | Chooses the guide bar key (UIButtonGuide row) for the current row and state. |
| [ConfirmWindow_Layout](../functions/ConfirmWindow_Layout.md) | `0x14029C9E8` | Lays the window out from its dialog row. |
| [ConfirmWindow_OnInput](../functions/ConfirmWindow_OnInput.md) | `0x14029ECF8` | Input of the confirm window (its vtable +64). |
| [ConfirmWindow_SetArgs](../functions/ConfirmWindow_SetArgs.md) | `0x14029C9A8` | Copies the message arguments from a vector {allocator, begin, end, capacity}. |
| [ConfirmWindow_SetDialog](../functions/ConfirmWindow_SetDialog.md) | `0x14029C6E0` | Loads a UIDialog row into the confirm window gadget. |
| [ConfirmWindow_ShowHide](../functions/ConfirmWindow_ShowHide.md) | `0x14029CE9C` | Shows or hides the confirm window. |
| [CreditRoll_AddPictureLine](../functions/CreditRoll_AddPictureLine.md) | `0x1401BEF44` | Credit roll line type 5: draws a picture line. |
| [CreditRoll_QueueMusic](../functions/CreditRoll_QueueMusic.md) | `0x1401BF828` | Queues a music change of the credit roll at a roll position. |
| [CreditRoll_StartMusic](../functions/CreditRoll_StartMusic.md) | `0x1401BF8C4` | Starts the credit roll's first music. |
| [CreditRoll_Step](../functions/CreditRoll_Step.md) | `0x1401CB254` | Steps the credit roll: reads the script rows and builds one line widget per row until the screen is full or the script ends. |
| [CursorFrame_FromCycle](../functions/CursorFrame_FromCycle.md) | `0x1402E30A4` | Returns the animation frame of the screen cursor for the current tick. |
| [EquipDetail_Refresh](../functions/EquipDetail_Refresh.md) | `0x14029F950` | Refreshes the item detail panel for one selected item: it builds the item's large picture path, then binds the picture and the item name to the panel's parts. |
| [EquipDetail_SetHelpText](../functions/EquipDetail_SetHelpText.md) | `0x1402A0A08` | Writes one help line of the equipment detail panel: line 0 = the item's description from Item-en, line 1 = three lines built by sub_1402A0E58, line 2 = weapon notes. |
| [EquipScreen_InitVram](../functions/EquipScreen_InitVram.md) | `0x14033DE68` | Uploads the palette and strips of the equipment screen to VRAM and resets the equipment lists. |
| [Errand_BoardConfirmInput](../functions/Errand_BoardConfirmInput.md) | `0x1402ED9C8` | Confirm step of an errand window (table index 9): cancel returns to the board, confirm opens the next window (kind 10). |
| [Errand_FinishDayPage](../functions/Errand_FinishDayPage.md) | `0x140379180` | Step of the page of an entry of list 41 (table index 42): shows the day text of the entry, then returns to the list. |
| [Errand_FinishListInput](../functions/Errand_FinishListInput.md) | `0x140378E10` | Input step of a list (table index 41): confirm opens the entry's page (kind 42). |
| [Errand_PickInput](../functions/Errand_PickInput.md) | `0x14036A190` | Choice step of an errand window (table index 12): collects a cancel or a pick, then returns to the board or paints the next board. |
| [Errand_ProfitEndStep](../functions/Errand_ProfitEndStep.md) | `0x1402D35F8` | Step of the errand end sequence (table index 55): waits, sends the profit-end notification and goes through a short prompt. |
| [Errand_ProgressListInput](../functions/Errand_ProgressListInput.md) | `0x140377D28` | Input step of a list of entries (table index 38): confirm opens the next list through sub_140377E9C (kind 39). |
| [Errand_ReportDialogueStep](../functions/Errand_ReportDialogueStep.md) | `0x14036FD50` | Step of the errand report dialogue (table index 16): shows the report, prints the result texts and closes through sub_14037085C. |
| [Errand_ReportListInput](../functions/Errand_ReportListInput.md) | `0x14036F94C` | Input step of the list of errands with a report ready (table index 14): confirm computes the rewards and opens the report prompt (kind 15). |
| [Errand_RunningConfirmInput](../functions/Errand_RunningConfirmInput.md) | `0x140371790` | Two-row confirm for a running errand (table index 19): the first row sets a bit in the active errand's record and prints a notice. |
| [Errand_RunningListInput](../functions/Errand_RunningListInput.md) | `0x140371174` | Input step of the list of running errands (table index 18): confirm opens a question about the entry (kind 19), unless the entry is flagged. |
| [Errand_StartConfirmInput](../functions/Errand_StartConfirmInput.md) | `0x14036A650` | Two-row confirm of the errand start (table index 13): the first row calls Errand_Start. |
| [Errand_StatusMenuInput](../functions/Errand_StatusMenuInput.md) | `0x140377530` | Step of a two-row menu (table index 37): the first row opens one list and the second row opens another (kind 41, the errand finish list). |
| [Errand_UnitListInput](../functions/Errand_UnitListInput.md) | `0x14037808C` | Input step of a list of entries (table index 39): confirm opens the page of the entry (kind 40). |
| [Errand_UnitStatusInput](../functions/Errand_UnitStatusInput.md) | `0x1403787A4` | Input step of a unit's status page for an errand in progress (table index 40): two direction presses page through the units of the errand. |
| [ErrandUnitPick_Input](../functions/ErrandUnitPick_Input.md) | `0x14036CC50` | Input step of the unit picker of the errand board (table index 36): reads the unit grid's result code and starts the errand when it is confirmed. |
| [EventVarEditor_DrawPage](../functions/EventVarEditor_DrawPage.md) | `0x14036DC28` | Draws one page of the event variable editor: ten variable numbers with their current values. |
| [EventVarEditor_ListInput](../functions/EventVarEditor_ListInput.md) | `0x14036DD60` | Input step of the event variable editor list (table index 11): moves through the variables and opens the value editor. |
| [EventVarEditor_Open](../functions/EventVarEditor_Open.md) | `0x14036DB30` | Opens the event variable editor: creates its window and pushes kind 11. |
| [EventVarEditor_ValueInput](../functions/EventVarEditor_ValueInput.md) | `0x14036E064` | Input step of the number entry above the event variable list (table index 48): confirm writes the entered value to the variable. |
| [EventViewer_StartReplay](../functions/EventViewer_StartReplay.md) | `0x1402D28C8` | Starts the replay of an event from the Chronicle. |
| [FontPaletteBlock_Equals](../functions/FontPaletteBlock_Equals.md) | `0x1403DCB8C` | Equality test of two font palette blocks (the first 68 bytes of the 80-byte UIFontSet row) used to find an existing SDFPalette entry before appending a new one. |
| [FreeCursor_StepFromSticks](../functions/FreeCursor_StepFromSticks.md) | `0x14016D440` | Moves a screen-space pointer (the finger cursor) from the left stick or from four direction actions and hit-tests what is under it. |
| [Glossary_OnSortInput](../functions/Glossary_OnSortInput.md) | `0x140173AC4` | Handles the glossary's sort command. |
| [GlossaryCharacterPage_Fill](../functions/GlossaryCharacterPage_Fill.md) | `0x140177004` | Fills the glossary's character page, whose entry comes through a pair of table 283. |
| [GlossaryDetail_Fill](../functions/GlossaryDetail_Fill.md) | `0x140172B70` | Fills the glossary detail page (part read). |
| [GlossaryList_DrawRow](../functions/GlossaryList_DrawRow.md) | `0x140172604` | Draws one row of the glossary list. |
| [GradientWindow_ColourFromPaletteA](../functions/GradientWindow_ColourFromPaletteA.md) | `0x140220640` | Colours the 12 vertices of a gradient window from palette A. |
| [GradientWindow_ColourFromPaletteB](../functions/GradientWindow_ColourFromPaletteB.md) | `0x1402206A8` | As GradientWindow_ColourFromPaletteA with palette B (0x142FEC4F0). |
| [GridAvailability_Reset](../functions/GridAvailability_Reset.md) | `0x1402FC6D8` | Resets the availability flags of the grid screen entries. |
| [GridScreen_Task](../functions/GridScreen_Task.md) | `0x1402FC870` | Task of the legacy grid screen screen: a grid of five columns of unit portraits with a cursor and a help window. |
| [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md) | `0x14040A664` | Shared owner handler for the keyframe events (type 40) a state posts: acts on the state entry the event points at (sound triggers, nested state links, state resets, part triggers). |
| [GUIBounds_ExpandByPoint](../functions/GUIBounds_ExpandByPoint.md) | `0x1403DF670` | Grows the double-precision draw bounds in the renderer (r+152..+176) to include one float point. |
| [GUICollisionNode_ContainsPoint](../functions/GUICollisionNode_ContainsPoint.md) | `0x1403FDCC8` | The Collision node's shape test, in the node's local space. |
| [GUICollisionNode_EllipseContains](../functions/GUICollisionNode_EllipseContains.md) | `0x1403FDD54` | Ellipse / ring-sector point test: normalises the point into [-1,1] over the node's size, rejects outside the unit circle or inside innerRatio, and for sweep > 0 rejects the angular part measured from 'up'. |
| [GUIComponent_ApplyAnimChannels](../functions/GUIComponent_ApplyAnimChannels.md) | `0x1404015C0` | Component-level counterpart of GUINode_ApplyAnimChannels: samples the tracks of the channel set that is addressed to '#Component' (the component itself) and writes them into the component's effect fields. |
| [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md) | `0x140409C28` | For every active state of the component (vector comp+616 .. +624), evaluates the state's animation channels at the state's time and writes the sampled values onto the nodes (and the component itself) they target. |
| [GUIComponent_Ctor](../functions/GUIComponent_Ctor.md) | `0x1404087A4` | Base constructor for UISystem GUIComponent (vtable 0x1407225F8); layer node embedded at +272, kind at +536. |
| [GUIComponent_CursorLeave](../functions/GUIComponent_CursorLeave.md) | `0x14040A298` | Component virtual +48: the GUI cursor target moved away; plays CursorOut unless the component keeps its cursor look while focused, and posts event 13. |
| [GUIComponent_Disable](../functions/GUIComponent_Disable.md) | `0x140408FF8` | Mirror of GUIComponent_Enable: clears +554, plays the Disable state (Enable stopped) and posts event 11. |
| [GUIComponent_Enable](../functions/GUIComponent_Enable.md) | `0x140408EBC` | Marks a component enabled (+554 = 1) and plays its Enable state (Disable stopped); optionally enables the components its reference nodes point at. |
| [GUIComponent_GetFlag556](../functions/GUIComponent_GetFlag556.md) | `0x14040A52C` | Trivial virtual accessor: returns byte c+556. |
| [GUIComponent_Init](../functions/GUIComponent_Init.md) | `0x140408E78` | Initializes a component from its definition; copies the component object id (+8) into the layer node (+0x140). |
| [GUIComponent_LoadDef](../functions/GUIComponent_LoadDef.md) | `0x1403F5764` | Builds a runtime component from its UIB component record (0x40 bytes): property block, node tree, states. |
| [GUIComponent_LoadProps](../functions/GUIComponent_LoadProps.md) | `0x1403F4EC8` | Reads a component's property block from the UIB file into the runtime component: the enable byte and values of every effect group (colour transform, offsets, single float, drop shadow, glow, opacity, clip, mask). |
| [GUIComponent_OnClick](../functions/GUIComponent_OnClick.md) | `0x14040A444` | Component virtual +72: a completed click; plays the Click state and posts event 16. |
| [GUIComponent_OnDown](../functions/GUIComponent_OnDown.md) | `0x14040A324` | Component virtual +56: the confirm button / mouse button went down on the component; sets the pressed flag, plays the Down state and posts event 14. |
| [GUIComponent_OnFocusGained](../functions/GUIComponent_OnFocusGained.md) | `0x14040A534` | Component virtual +96: plays the component's FocusIn state (if the UIB has one; UnitJob has none, so nothing plays there) and posts event 19 to its owners. |
| [GUIComponent_OnFocusLost](../functions/GUIComponent_OnFocusLost.md) | `0x14040A5D4` | Component virtual +104: plays FocusOut and posts event 20 (JobTree_OnCursorLeave). |
| [GUIComponent_OnUp](../functions/GUIComponent_OnUp.md) | `0x14040A3B4` | Component virtual +64: the press ended; clears the pressed flag, plays the Up state and posts event 15. |
| [GUIComponent_ResetEffects](../functions/GUIComponent_ResetEffects.md) | `0x140408B40` | Resets a component to defaults: clears the effect enable bytes and frees its child list. |
| [GUIComponent_SetAllocatedSize](../functions/GUIComponent_SetAllocatedSize.md) | `0x1403F2EF8` | Stores the size taken from a reference node (ref+64 / +68) as the component's allocated size comp+528 / +532, swapped for the rotated layout mode, and resizes the component root when it asks for it. |
| [GUIComponent_StopAllStates](../functions/GUIComponent_StopAllStates.md) | `0x14040996C` | Stops every state of a component. |
| [GUIComponent_TickTree](../functions/GUIComponent_TickTree.md) | `0x140409284` | Runs GUIComponent_UpdateNodeTree on the component's root node (comp+272) when the component is active, else clears the visible flags once. |
| [GUIComponent_Update](../functions/GUIComponent_Update.md) | `0x14040A1C8` | Base per-frame update of a component: advance the state timers, apply the state animations, then update the node tree. |
| [GUIComponent_UpdateNodeTree](../functions/GUIComponent_UpdateNodeTree.md) | `0x1404092EC` | Recursive layout / update walk over a component's node tree (started at comp+272 by sub_140409284): re-sorts layers by sort order, queues or runs the text relayout for dirty text nodes, and calls the update method of ... |
| [GUIComponentCustom_Create](../functions/GUIComponentCustom_Create.md) | `0x140406048` | Allocates a 648-byte GUIComponentCustom from the UI pool (pages of 64), constructs it, links it into the owner's child list and registers it by id. |
| [GUIComponentCustom_CursorEnter](../functions/GUIComponentCustom_CursorEnter.md) | `0x14040A20C` | Cursor-enter handler of a custom component (vtable slot +40): plays the CursorOver state and tells the node's owners. |
| [GUIComponentGauge_Step](../functions/GUIComponentGauge_Step.md) | `0x14040DEC4` | While the gauge value is animating (+688), eases three displayed fractions toward the target fraction using float tracks of the Increase / Decrease states, drives the GaugeBar / GaugeInc / GaugeDec states from them an... |
| [GUIComponentGauge_Update](../functions/GUIComponentGauge_Update.md) | `0x14040DE78` | Gauge component per-frame update (vtable slot 4): advances the states, runs the value animation step, applies tracks, updates the tree. |
| [GUIComponentList_FindSlotNode](../functions/GUIComponentList_FindSlotNode.md) | `0x14040C1DC` | Finds the layer node of slot number `slot`: the part named 'ListItem' for slot 0 and 'ListItem#n' for slot n. |
| [GUIComponentList_GetHScroll](../functions/GUIComponentList_GetHScroll.md) | `0x14040C0EC` | Same as GUIComponentList_GetVScroll for the horizontal bar (key +5064 = 'HScroll'). |
| [GUIComponentList_GetItemComponent](../functions/GUIComponentList_GetItemComponent.md) | `0x14040C270` | The component currently showing item `item`, or null when that item is not in the shown window. |
| [GUIComponentList_GetSlotComponent](../functions/GUIComponentList_GetSlotComponent.md) | `0x14040C228` | The component (a ListItem) behind a slot node: the slot node must be a reference node (kind 12). |
| [GUIComponentList_GetVScroll](../functions/GUIComponentList_GetVScroll.md) | `0x14040C080` | Returns the list's vertical scroll bar component (the 'VScroll' child reference node), or null. |
| [GUIComponentList_IsItemVisible](../functions/GUIComponentList_IsItemVisible.md) | `0x14040C2FC` | True when the item's cell lies inside the list's viewport with at most half a cell cut off at each edge. |
| [GUIComponentList_ItemToSlot](../functions/GUIComponentList_ItemToSlot.md) | `0x14040C158` | Maps an item index to the recycled slot (a 'ListItem#n' node) that currently shows it, or -1 when the item is outside the window of shown items. |
| [GUIComponentList_LayoutSlots](../functions/GUIComponentList_LayoutSlots.md) | `0x14040CB60` | Places the recycled slot nodes of a list for the current scroll offset, re-binds slots that now show a different item (resetting their visuals and clearing focus / cursor on them) and posts event 31. |
| [GUIComponentList_SetItemCount](../functions/GUIComponentList_SetItemCount.md) | `0x14040CA1C` | Sets the number of list items; when it changed, invalidates the bound slots and marks both the scroll bars and the layout dirty. |
| [GUIComponentList_SetScrollX](../functions/GUIComponentList_SetScrollX.md) | `0x14040C8B0` | Sets the list's horizontal scroll offset, through the horizontal bar when there is one, and marks the layout dirty. |
| [GUIComponentList_SetScrollY](../functions/GUIComponentList_SetScrollY.md) | `0x14040C92C` | Vertical twin of GUIComponentList_SetScrollX: via the 'VScroll' bar, stores list+680 and sets the layout-dirty byte +685. |
| [GUIComponentList_UpdateScrollBars](../functions/GUIComponentList_UpdateScrollBars.md) | `0x14040CA50` | Gives the horizontal and vertical scroll bars their ranges from the item count and cell size, shows a bar only when the content is larger than the viewport, and clears the dirty byte +684. |
| [GUIComponentProps_Copy](../functions/GUIComponentProps_Copy.md) | `0x1403DF454` | Copies a component's 254-byte render-property block (the effect enable bytes and values: blend, colour transform, offsets, drop shadow, glow, clip and the two mask names) from one component to another. |
| [GUIComponentRef_Draw](../functions/GUIComponentRef_Draw.md) | `0x1403EDB20` | Draws a component reference node: finds the component, builds a draw context from its property block, opens an offscreen layer when the component has effects, draws its children, then composites the layer. |
| [GUIComponentRef_DrawChildren](../functions/GUIComponentRef_DrawChildren.md) | `0x1403E9A2C` | Draws the node tree of the component a reference node points at, or (when the layer mask path is active) just clears the current layer record's draw counter. |
| [GUIComponentScrollBar_StepKnob](../functions/GUIComponentScrollBar_StepKnob.md) | `0x14040BBF0` | While the bar has a pending move (+681), eases the shown position toward the target using the ScrollUp / ScrollDown state tracks, then sizes and places the Knob part inside the Base part and posts event 27. |
| [GUIComponentScrollBar_Update](../functions/GUIComponentScrollBar_Update.md) | `0x14040BBA4` | Scroll bar per-frame update (vtable slot 4): advances the states, applies their tracks, repositions the knob and then updates the node tree. |
| [GUICore_BeginFrame](../functions/GUICore_BeginFrame.md) | `0x1403D6234` | Start of a UI frame in the GUI core: stores the frame times and the frame counters, advances the random state, refreshes the viewport transform and dispatches the queued events. |
| [GUICore_CommitFrame](../functions/GUICore_CommitFrame.md) | `0x1403D67D4` | Per-frame UI commit: resets the renderer, runs every widget's draw, then expands each layer's bounds for its effects. |
| [GUICore_Ctor](../functions/GUICore_Ctor.md) | `0x1403D5348` | Constructs the GUI core: widget lists, the UI renderer, the focus key strings, the screen size and the per-frame worker slots. |
| [GUICore_DispatchEvent](../functions/GUICore_DispatchEvent.md) | `0x1403D694C` | Hands one raw UI event to each registered handler (core+56..+64, vtable slot 1) until one consumes it, then to the core's own message handler (core+8). |
| [GUICore_DrawOutsideBars](../functions/GUICore_DrawOutsideBars.md) | `0x1403E5258` | Fills the part of the screen outside a transformed rectangle (the letterbox / pillarbox bars around the UI area) with a flat colour. |
| [GUICore_DrawWidget](../functions/GUICore_DrawWidget.md) | `0x1403E97A8` | Draws one widget: bumps the sort group when the widget's draw order word changes, fills the widget background, then builds the root draw context from the layer transform and draws the widget's main component tree. |
| [GUICore_FindWidgetByKey](../functions/GUICore_FindWidgetByKey.md) | `0x1403D69FC` | Finds the top-level widget that a key (name string + hash) names, walking the widget list; returns 0 when none matches. |
| [GUICore_FocusNode](../functions/GUICore_FocusNode.md) | `0x1401D2240` | Moves the GUI focus (and with it the finger cursor) onto a node, or clears the focus when the node is null. |
| [GUICore_GetFocus](../functions/GUICore_GetFocus.md) | `0x1403D6E28` | Resolves the focus key triple (core+1968) to the live widget and node; returns 0 when nothing is focused. |
| [GUICore_IsCursorTarget](../functions/GUICore_IsCursorTarget.md) | `0x1403D6BFC` | Same comparison as GUICore_IsFocusTarget against the cursor-target triple at core+1920 / +1936 / +1952. |
| [GUICore_IsFocusTarget](../functions/GUICore_IsFocusTarget.md) | `0x1403D6E8C` | Tests whether (widget, node) is the current GUI focus: compares the three keys (widget+16, node+504, node+280) with the focus triple at core+1968 / +1984 / +2000. |
| [GUICore_OnInputState](../functions/GUICore_OnInputState.md) | `0x1403D5A9C` | The UI core's input listener: turns the frame's input state into queued UI events and then pumps the queue through GUICore_DispatchEvent. |
| [GUICore_SetCursorTarget](../functions/GUICore_SetCursorTarget.md) | `0x1403D6A64` | Makes a node the GUI cursor target: stores its key triple in the core's cursor slot and sends it the cursor-enter virtual call (the old target gets the cursor-leave call). |
| [GUICore_SetFocusComponent](../functions/GUICore_SetFocusComponent.md) | `0x1403D6CE0` | Moves focus to a component node: the old focus node gets virtual +104 (focus lost, event 20), the new one virtual +96 (focus gained, event 19); stores the new key triple at core+1968. |
| [GUICore_TickWidget](../functions/GUICore_TickWidget.md) | `0x1403D7670` | Gives one widget its frame time and calls its tick (vtable slot 7, GUIWidget_Tick). |
| [GUICore_UpdateFrame](../functions/GUICore_UpdateFrame.md) | `0x1403D7030` | Per-frame UI update (raw event 1): finds the node under the mouse pointer and moves hover/focus onto it. |
| [GUICore_UpdateWidgets](../functions/GUICore_UpdateWidgets.md) | `0x1403D76E4` | Per-frame widget update (the second GUICore update function; see GUICore_UpdateFrame for the other): orders the widgets, wires the ten frame worker slots when a task object exists and updates every widget. |
| [GUICursor_UpdateIndex](../functions/GUICursor_UpdateIndex.md) | `0x1400FE194` | Chooses the cursor index the UI wants (g_GUICore + 1904) and shows or hides the OS cursor. |
| [GUICursorHand_GetTargetPoint](../functions/GUICursorHand_GetTargetPoint.md) | `0x1401D2FF8` | The hand's rest position for the focused component (left edge + hand+80, vertical centre + hand+84), or the screen centre (960, 540) when nothing is focused. |
| [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md) | `0x1401D37D8` | One step of the hand's travel: pos = roundf(pos + (target - pos) * k), per axis, written to the hand node. |
| [GUICursorHand_Update](../functions/GUICursorHand_Update.md) | `0x1401D2B00` | Per-frame update of the pointing-hand cursor: finds the focused component, computes where the hand belongs and moves it there. |
| [Guide_CompareSortOrder](../functions/Guide_CompareSortOrder.md) | `0x1400DB2B4` | Comparator for guide id lists. |
| [Guide_GetEntry](../functions/Guide_GetEntry.md) | `0x1400DB81C` | Fetches the Guide row of an id. |
| [Guide_IsUnlocked](../functions/Guide_IsUnlocked.md) | `0x1400DAA64` | Tells whether a guide counts as unlocked. |
| [Guide_MarkShown](../functions/Guide_MarkShown.md) | `0x1400DA454` | Marks a guide of window type 1 or 2 as seen. |
| [Guide_OpenWindow](../functions/Guide_OpenWindow.md) | `0x1401A9000` | Opens the window that shows a guide. |
| [Guide_QueueAutoShow](../functions/Guide_QueueAutoShow.md) | `0x1400EDFBC` | Queues a guide to be opened, with its input-pause delay. |
| [Guide_TryAutoShow](../functions/Guide_TryAutoShow.md) | `0x1400D6DAC` | The entry point that shows a guide automatically when the game reaches its moment. |
| [GuideBar_Layout](../functions/GuideBar_Layout.md) | `0x14013D758` | Rebuilds the guide bar: hides and resets all 8 slots, then lays out the visible rows of table 33 in two passes (left-aligned, then right-aligned). |
| [GuideBar_LayoutRow](../functions/GuideBar_LayoutRow.md) | `0x14013D844` | Configures one guide slot for table 33 row `row`: sets the text, the up to four button icons (keyboard / pad variants), places the slot at x and starts its on-animation. |
| [GuideBar_SetPage](../functions/GuideBar_SetPage.md) | `0x14013D5F4` | Selects the page of the button-guide bar: sets table key (+2224) and enabled-row bitmask (+2228) and rebuilds it with GuideBar_Layout. |
| [GuideEntry_Fill](../functions/GuideEntry_Fill.md) | `0x1400F74F4` | Fills a guide entry (label and one or two buttons) of a window from a UIButtonGuide row. |
| [GuideIcon_ToGlyph](../functions/GuideIcon_ToGlyph.md) | `0x1400F681C` | Maps a guide-bar icon number (UIButtonGuide guide_icon / guide_icon_2) and a variant byte to a glyph and draws it. |
| [GuideLesson_MarkRead](../functions/GuideLesson_MarkRead.md) | `0x1400D6EA8` | Marks a lesson (window types 4..6) as read. |
| [GuideLessons_AnyNewlyUnlockable](../functions/GuideLessons_AnyNewlyUnlockable.md) | `0x1400DB384` | Tells whether a lesson could be unlocked now but is not yet. |
| [GuideLessons_UpdateUnlocked](../functions/GuideLessons_UpdateUnlocked.md) | `0x1400DA5D8` | Marks the lessons whose conditions are met as unlocked. |
| [GuideList_BuildCategory](../functions/GuideList_BuildCategory.md) | `0x1400DAB10` | Builds the guide list of one tutorial tab. |
| [GuideList_BuildLessons](../functions/GuideList_BuildLessons.md) | `0x1400DAD58` | Builds the lesson list of one Lessons tab. |
| [GuideSlot_DrawButtons](../functions/GuideSlot_DrawButtons.md) | `0x14028BE4C` | Draws the buttons of one guide-bar slot: action buttons, fixed icons or keyboard key textures. |
| [GuideWindow_ShowPage](../functions/GuideWindow_ShowPage.md) | `0x14017D668` | Shows one page of an in-game guide: the GuidePage-en row (guide, page) gives the title, the text and an optional icon; the guide's page count is the size of its set. |
| [GUIFactory_FreeSlotGroup](../functions/GUIFactory_FreeSlotGroup.md) | `0x1403FECD0` | Returns a slot group to the pool: clears its occupancy bit, runs the group's destructor and, every time the live count crosses 32 modulo 64, drops empty pages. |
| [GUIFontRenderer_UploadPalette](../functions/GUIFontRenderer_UploadPalette.md) | `0x1403EDEA4` | Finds or appends an entry for a font palette block and writes it to the GPU structured buffer SDFPalette (192 bytes per entry) read by shader/SDFFont.tec. |
| [GUIFontSet_FontTypeForLanguage](../functions/GUIFontSet_FontTypeForLanguage.md) | `0x1403DCD50` | Picks the UIFontType id of a font-set row for the current game language. |
| [GUIFontSlotGroup_Destroy](../functions/GUIFontSlotGroup_Destroy.md) | `0x1403F3D28` | Destructor: releases all slot references, frees both vectors, and drops the name key. |
| [GUIFontSlotGroup_Init](../functions/GUIFontSlotGroup_Init.md) | `0x1403F3CAC` | Constructor of a per-widget group that owns slot references: sets two empty vectors, a name key and a trailing slot record. |
| [GUIFontSlotGroup_OnPartTableLoaded](../functions/GUIFontSlotGroup_OnPartTableLoaded.md) | `0x1403F40AC` | Called by GUIFontSlotGroup_Poll once the group's part-table slot (g+84, the .utexpt file) is loaded: copies the table's part rectangles into the group's vector, requests the texture the table names and posts event 42. |
| [GUIFontSlotGroup_OnTextureLoaded](../functions/GUIFontSlotGroup_OnTextureLoaded.md) | `0x1403F3FAC` | Called by GUIFontSlotGroup_Poll once the group's texture slot (g+80) is loaded: stores the whole-texture rectangle as the first entry of the group's part vector, marks the group loaded and posts event 41 to its owners. |
| [GUIFontSlotGroup_Poll](../functions/GUIFontSlotGroup_Poll.md) | `0x1403F3EA4` | Per-frame poll of one texture / font group: once its slots are loaded it runs the finishing steps and returns whether the group is complete. |
| [GUIFontSlotGroup_ReleaseAll](../functions/GUIFontSlotGroup_ReleaseAll.md) | `0x1403F3DFC` | Releases every slot id the group holds (+80, +84 and every dword of the vector at +56) with GUIFontSlots_Release and resets the state. |
| [GUIFontSlotGroup_SetImageByName](../functions/GUIFontSlotGroup_SetImageByName.md) | `0x1403F3DAC` | Acquires the kind-3 image slot for name and stores it as the group's image slot; on failure sets the failed flags. |
| [GUIFontSlots_AcquireImage](../functions/GUIFontSlots_AcquireImage.md) | `0x1403DB280` | Gets a kind-3 (image) slot for a name: reuses an existing one (refcount +1) or requests the resource and appends a new record. |
| [GUIFontSlots_AcquireTexturePart](../functions/GUIFontSlots_AcquireTexturePart.md) | `0x1403DA918` | Gets a kind-2 slot (texture part) for a path: reuses an existing record with the same name (refcount +1), otherwise requests the resource, appends a new 32-byte record with refcount 1 and returns its id. |
| [GUIFontSlots_FindImageByName](../functions/GUIFontSlots_FindImageByName.md) | `0x1403DB390` | Linear search of the image records for one whose name equals name; returns an image id (1-based index \| 0x03000000) or 0. |
| [GUIFontSlots_FindPartByName](../functions/GUIFontSlots_FindPartByName.md) | `0x1403DAB60` | Linear search of the kind-2 (texture part) records for a live record whose resource name equals name; returns its id or 0. |
| [GUIFontSlots_GetResource](../functions/GUIFontSlots_GetResource.md) | `0x1403DA594` | Returns the resource pointer (first qword of the record) of a live slot, or 0 when the id is bad or the refcount is 0. |
| [GUIFontSlots_GetSlot](../functions/GUIFontSlots_GetSlot.md) | `0x1403DB240` | Resolves a texture slot id to its record pointer: ids carry type 0x02 in the top byte and a 1-based index in the low 24 bits. |
| [GUIFontSlots_GetTextureRect](../functions/GUIFontSlots_GetTextureRect.md) | `0x1403E9590` | Writes the full-texture rectangle {0, 0, width, height} of a slot's texture into out; leaves out unchanged when the slot does not exist. |
| [GUIFontSlots_IsLoaded](../functions/GUIFontSlots_IsLoaded.md) | `0x1403DA3EC` | True when the slot exists, has a non-zero refcount and its loaded byte is set (the texture / image behind it finished loading). |
| [GUIFontSlots_Release](../functions/GUIFontSlots_Release.md) | `0x1403DA30C` | Drops one reference from a slot of the GUI slot registry (g_GUIFontSlots): decrements the record's u16 refcount, never below 0, and never frees anything. |
| [GUIFontTable_GetSetRow](../functions/GUIFontTable_GetSetRow.md) | `0x1403D9908` | Returns a pointer to the 80-byte UIFontSet row for a font-set key; out of range falls back to row 0, creating a default row if the table is empty. |
| [GUIFontTable_Load](../functions/GUIFontTable_Load.md) | `0x1403D9728` | Rebuilds the in-memory UIFontSet row vector from UI table id 21: each 80-byte row starts from UIFontSetRow_Default and is then overwritten field by field from the source record. |
| [GUIInputQueue_Pop](../functions/GUIInputQueue_Pop.md) | `0x1403DC32C` | Pops the oldest 68-byte input record of queue `port` (vector at q + 32 * port) into out; false when empty. |
| [GUILayer_BoundsAdd32](../functions/GUILayer_BoundsAdd32.md) | `0x1403E9560` | Saturating signed 32-bit addition (a + b clamped to INT_MIN .. INT_MAX). |
| [GUILayer_BoundsToRect](../functions/GUILayer_BoundsToRect.md) | `0x1403DF8D8` | Converts the double-precision draw bounds accumulated in the renderer (r+152..+176) into the integer rectangle {left, top, right, bottom} of the draws since the last flush. |
| [GUILayer_BuildRecord](../functions/GUILayer_BuildRecord.md) | `0x1403E6728` | Fills one 592-byte offscreen-layer record from a component draw context: size, blend, colour transform and every enabled effect. |
| [GUILayer_Compatible](../functions/GUILayer_Compatible.md) | `0x1403E7ADC` | Tests whether a draw context can share an existing layer: the blend type, colour transform, every effect group and their values must be equal (within 1.2e-7). |
| [GUILayer_ExpandBounds](../functions/GUILayer_ExpandBounds.md) | `0x1403E75DC` | The last step that fixes a layer's float rectangle (layer+208..+220): the union of the quad bounds drawn into the slot (the dirty rectangle) grown by the blur reach of the slot's effects and by 16 pixels, clamped to t... |
| [GUILayer_Flush](../functions/GUILayer_Flush.md) | `0x1403E90A8` | Closes the layer being built: merges the draws recorded so far into the layer's dirty rectangle and advances the layer count. |
| [GUILayer_ResetRecord](../functions/GUILayer_ResetRecord.md) | `0x1403E73A0` | Resets one layer record to its defaults (full target size, identity colour transform, every effect group off). |
| [GUILayer_Select](../functions/GUILayer_Select.md) | `0x1403E9298` | Finds an existing offscreen layer compatible with the context (same layer id and equal effect settings) or builds a new record, and makes it the current layer. |
| [GUILayer_SetCurrent](../functions/GUILayer_SetCurrent.md) | `0x1403E9218` | Flushes the batch and makes layer record `index` current; out-of-range indices select the next free slot (capped at 510). |
| [GUILayer_UpdateActiveFlag](../functions/GUILayer_UpdateActiveFlag.md) | `0x1403E6440` | Sets the context's 'draws into an offscreen layer' byte (ctx+554) from a request and, when it changed, re-selects the layer. |
| [GUILayerXform_MapPointFloat](../functions/GUILayerXform_MapPointFloat.md) | `0x1403F8C3C` | Same transform as GUILayerXform_MapPointInt without rounding; used by GUICore_UpdateFrame to bring the pointer into UI coordinates before the hit test. |
| [GUILayerXform_MapPointInt](../functions/GUILayerXform_MapPointInt.md) | `0x1403F8CA4` | Maps an integer point through the layer's 2x3 matrix (x' = x*m0 + y*m2 + m4, y' = x*m1 + y*m3 + m5) and rounds back to integers (roundf). |
| [GUILayerXform_Recompute](../functions/GUILayerXform_Recompute.md) | `0x1403F8A20` | Recomputes a GUI layer transform (one of the window-to-UI layers at GUICore + 216 + 144 * index): a letterbox fit of the UI size into the viewport, as a forward matrix, an inverse matrix and the scale. |
| [GUIList_SetCount](../functions/GUIList_SetCount.md) | `0x1402A3230` | Sizes and refreshes a list gadget: it stores the row count and column, rebinds the name key of the list node, and toggles the empty-list label. |
| [GUIMessageHandler_Dispatch](../functions/GUIMessageHandler_Dispatch.md) | `0x1403DC390` | Maps a raw UI event id to a virtual method of the handler (1->+16, 3->+32, 4->+40, 5->+48, 6->+56, 7..14 -> +64..+120 by id, 15..21 -> +128..+176, 22..25 -> +184..+208, 26 -> +216). |
| [GUINineGridNode_Draw](../functions/GUINineGridNode_Draw.md) | `0x1403EAF9C` | Draws a Ninegrid node (runtime kind 4): the node's part cut into 3 x 3 cells by the node's own borders and drawn into the node box. |
| [GUINode_ApplyAnimChannels](../functions/GUINode_ApplyAnimChannels.md) | `0x140400840` | Samples every keyframe track of one animation channel set at time t and stores the results into the node's transform / colour / opacity / per-kind fields. |
| [GUINode_ApplyStateAtFrame](../functions/GUINode_ApplyStateAtFrame.md) | `0x140409A98` | Evaluates all property tracks of a named state at one frame and writes the results into the nodes, recursing into the nested state links. |
| [GUINode_BuildFromFile](../functions/GUINode_BuildFromFile.md) | `0x1403F5A80` | Copies a UIB file node into its runtime GUINode (position, size, pivot, colours, then the type-specific block). |
| [GUINode_BuildLocalMatrix](../functions/GUINode_BuildLocalMatrix.md) | `0x1403F0270` | Builds a node's local 2x3 matrix from scale (+80/+84), pivot (+72/+76), rotation (+88) and position (+56/+60). |
| [GUINode_ClearVisibleSubtree](../functions/GUINode_ClearVisibleSubtree.md) | `0x1404095B8` | Sets the visible byte (+204) to 0 for a node and everything below it, following layer children and nested components. |
| [GUINode_ComputeRectInMatrix](../functions/GUINode_ComputeRectInMatrix.md) | `0x1403F033C` | Transforms the node's (0,0)-(w,h) corners by a 2x3 matrix and returns the rounded axis-aligned bounds {left, top, right, bottom}. |
| [GUINode_DrawChildren](../functions/GUINode_DrawChildren.md) | `0x1403E9A6C` | Draws the children of a node in order, dispatching on each child's kind. |
| [GUINode_DrawKind10](../functions/GUINode_DrawKind10.md) | `0x1403ED7D0` | Draw hook for runtime node kind 10 (file type 11): resolves the node's two names, opens a component layer for the referenced component and queues an 80-byte draw record. |
| [GUINode_DrawKind5](../functions/GUINode_DrawKind5.md) | `0x1403EBFA0` | Draw hook for runtime node kind 5: draws a string of characters (digits, a space, other characters) from one image part, each with its own advance; the draw counter makes it consume a layer slot. |
| [GUINode_DrawKind7](../functions/GUINode_DrawKind7.md) | `0x1403EC794` | Draw hook for runtime node kind 7: one quad of node size, textured when the node names an image part, flat otherwise; it also asks for the offscreen flag of the context when no part is found. |
| [GUINode_DrawKind8](../functions/GUINode_DrawKind8.md) | `0x1403ECA88` | Draw hook for runtime node kind 8: a chain of segments built from a vector of 552-byte elements (n+216 .. n+224) drawn as strips; unlike the other node draws it can re-select the layer in the middle of the node. |
| [GUINode_FindDescendant](../functions/GUINode_FindDescendant.md) | `0x1404091AC` | Finds a descendant node by interned name under `root` (searches the node's child components). |
| [GUINode_FindDescendant2](../functions/GUINode_FindDescendant2.md) | `0x140409214` | Two-step descendant lookup: the node `outer` under `root`, then the node `inner` under that. |
| [GUINode_FindGadgetPart](../functions/GUINode_FindGadgetPart.md) | `0x140409134` | Finds a named part inside a named gadget: looks up the gadget node, then searches the gadget's component layer for the part. |
| [GUINode_FindNthPartByKind](../functions/GUINode_FindNthPartByKind.md) | `0x1403F081C` | Returns the index-th (0-based) descendant part of the given kind in depth-first order; the worker is sub_1403F0850. |
| [GUINode_FindNthPartByKindRec](../functions/GUINode_FindNthPartByKindRec.md) | `0x1403F0850` | Recursive worker of GUINode_FindNthPartByKind (see that sheet). |
| [GUINode_FindPartByName](../functions/GUINode_FindPartByName.md) | `0x1403F0794` | Depth-first search of a layer node's part list (first child at +208, next sibling +32) for the part named `key`; descends into containers (kind +52 == 1). |
| [GUINode_FindState](../functions/GUINode_FindState.md) | `0x140409774` | Finds a named state (animation/visibility group) of a node in its state vector. |
| [GUINode_IsAncestorDirty](../functions/GUINode_IsAncestorDirty.md) | `0x1403EF834` | True when the node or any ancestor has its dirty byte (+149) set. |
| [GUINode_LoadTree](../functions/GUINode_LoadTree.md) | `0x1403F6C70` | Builds one node from its file record and, for a Layer, its children; a Reference node gets its component by name from the file's component array. |
| [GUINode_NameEqualsKnownKey](../functions/GUINode_NameEqualsKnownKey.md) | `0x1404007FC` | Tests a name key against one global key (string at qword_143CDA2A0+5144, interned id at +5152): id compare when both ids are non-zero, byte-wise string compare otherwise. |
| [GUINode_NewState](../functions/GUINode_NewState.md) | `0x1404096D4` | Creates the runtime state object of a component for a state name and adds it to the component's state vector. |
| [GUINode_PlayCursorOutState](../functions/GUINode_PlayCursorOutState.md) | `0x14040A0E4` | Stops the CursorOver state, starts the CursorOut state and clears the cursor-over flag +574 (mirror of GUINode_PlayCursorOverState). |
| [GUINode_PlayCursorOverState](../functions/GUINode_PlayCursorOverState.md) | `0x14040A094` | Stops the node's CursorOut state, starts its CursorOver state and sets the cursor-over flag (+574). |
| [GUINode_PlayShowHide](../functions/GUINode_PlayShowHide.md) | `0x1400F638C` | Plays a node's Show or Hide animation (default state names 'Show' and 'Hide'): stops the opposite one and starts the wanted one, optionally jumping to its end frame. |
| [GUINode_PlayState](../functions/GUINode_PlayState.md) | `0x1404000D8` | Starts a state: resets its time, sets the running flags (+105/+106) and the 60 fps frame time. |
| [GUINode_PlayStateAtFrame](../functions/GUINode_PlayStateAtFrame.md) | `0x140409824` | Starts the named state and jumps it to a given frame (a negative frame = its last frame). |
| [GUINode_PlayStateAtFrameEx](../functions/GUINode_PlayStateAtFrameEx.md) | `0x140409898` | GUINode_PlayStateAtFrame plus a flag byte that also sets the state's pause / hold / loop / keep-alive bytes. |
| [GUINode_PropagateField48](../functions/GUINode_PropagateField48.md) | `0x1403F0610` | Recursively assigns `value` to child->+48 for the node's children (linked via +32), descending when child kind (+52) == 1. |
| [GUINode_ResolvePins_Fraction](../functions/GUINode_ResolvePins_Fraction.md) | `0x1403EF890` | Resolves a node's edge pins against its parent size when the pins are stored as fractions of the parent (left/top/right/bottom flags in node+140). |
| [GUINode_ResolvePins_Offset](../functions/GUINode_ResolvePins_Offset.md) | `0x1403EFBE4` | Resolves edge pins stored as pixel offsets from the parent edges (same flag bits as GUINode_ResolvePins_Fraction). |
| [GUINode_ResolvePinsDispatch](../functions/GUINode_ResolvePinsDispatch.md) | `0x1403EF860` | Chooses how a node's edge pins are resolved against its parent: pins as fractions (node+141 = 0) or as pixel offsets (node+141 = 1). |
| [GUINode_SetCursorOverState](../functions/GUINode_SetCursorOverState.md) | `0x1400F5C78` | Plays the node's cursor animation states: on the cursor node CursorOver, on every other node CursorOut, honouring the Check / Uncheck pair of toggle nodes. |
| [GUINode_SetPivot](../functions/GUINode_SetPivot.md) | `0x1403EF704` | Sets the node pivot (+72 / +76), marks the node dirty and invalidates the resolved pivot pins. |
| [GUINode_SetPosition](../functions/GUINode_SetPosition.md) | `0x1403EF684` | Sets a node's integer position; the track sampler, the finger cursor's glide and the smooth-scroll animation all use it. |
| [GUINode_SetScale](../functions/GUINode_SetScale.md) | `0x1403EF738` | Sets a node's scale pair (+80 / +84, floats); the node is marked dirty when either value changed by more than 1.19e-7. |
| [GUINode_SetSize](../functions/GUINode_SetSize.md) | `0x1403EF6B4` | Sets node size (+64 / +68), marks the node dirty, invalidates resolved pins and, unless the node has an explicit pivot, re-centres the pivot at size / 2. |
| [GUINode_StopState](../functions/GUINode_StopState.md) | `0x140409ECC` | Stops a named state (+104 = 0, clears timers and flags) and recursively stops the nested states of kind 5. |
| [GUINode_UpdateColourAndMatrix](../functions/GUINode_UpdateColourAndMatrix.md) | `0x1403EFF08` | Per-node update that every node of every kind goes through each frame: resolves the node colour, multiplies it (and the opacity) with the parent's, derives the visible flag (+204) and, when the node is dirty, rebuilds... |
| [GUINode_UpdateStates](../functions/GUINode_UpdateStates.md) | `0x1404099F4` | Advances every enabled state (timeline) of a component node by dt, or stops it when it is no longer valid. |
| [GUINode_UpdateSubtree](../functions/GUINode_UpdateSubtree.md) | `0x1403F08C0` | Recursive per-frame colour / matrix pass over a node and its children (siblings via +32), run before the component tree pass; also rebuilds the text-board nodes (kind 8) that changed. |
| [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | `0x1403FFDF8` | The clock of a UIB state (timeline): advances its time and 60 fps frame, applies jump markers and looping, and posts the keyframe-event (40), loop (38) and finished (39) events to the state's owners. |
| [GUINodeState_Alloc](../functions/GUINodeState_Alloc.md) | `0x140405098` | Takes a 208-byte state object from the state pool and gives it its default values. |
| [GUINodeState_IsPastEnd](../functions/GUINodeState_IsPastEnd.md) | `0x140400118` | Rule used by GUINode_UpdateStates to decide whether a running state is to be advanced: false when restarted, true when held, otherwise frame >= end frame. |
| [GUIOwnerMap_Find](../functions/GUIOwnerMap_Find.md) | `0x1403DC1A8` | Looks an int key up in a std::map<int, T*> (red-black tree head at m+16) and returns the stored pointer or null. |
| [GUIOwners_PostEvent](../functions/GUIOwners_PostEvent.md) | `0x1403DC22C` | Delivers a component event to every owner registered on the node: each non-zero id (node +584..+596) is resolved in the actor table and its vtable slot 2, OnEvent(owner, node, ev), is called. |
| [GUIQuad_EmitGouraud](../functions/GUIQuad_EmitGouraud.md) | `0x1403E00AC` | Emits one coloured quad (the Rect node's draw): the rectangle pushed through a 2x3 matrix, four corner colours, drawn as four triangles around a centre vertex; optionally also an outline command. |
| [GUIRectNode_Draw](../functions/GUIRectNode_Draw.md) | `0x1403EC4B0` | Draws a Rect node (runtime kind 6): one quad with a colour per corner. |
| [GUIRenderer_ResetFrame](../functions/GUIRenderer_ResetFrame.md) | `0x1403E6160` | Per-frame reset of the GUI renderer: default draw states, clip bounds sentinels, the quad UV transform and all 512 layer records. |
| [GUIRenderer_RunDeferredDraws](../functions/GUIRenderer_RunDeferredDraws.md) | `0x1403E6348` | After the frame's UI commands are recorded, calls each deferred draw callback registered in the renderer. |
| [GUISlotVec16_Insert](../functions/GUISlotVec16_Insert.md) | `0x1403EE77C` | Inserts a 16-byte record into a std::vector-like container (allocator, begin, end, cap): reuses the first record whose first qword is 0, otherwise appends (growing by 1.5x). |
| [GUISlotVec32_Insert](../functions/GUISlotVec32_Insert.md) | `0x1403EE918` | The 32-byte-record twin of GUISlotVec16_Insert (used for the kind-2 texture-part vector). |
| [GUISwitch_SetOff](../functions/GUISwitch_SetOff.md) | `0x14040ABDC` | Sets a switch node off: plays its state and posts event 22 (constant at 0x140723390). |
| [GUISwitch_SetOn](../functions/GUISwitch_SetOn.md) | `0x14040AB40` | Sets a switch node on: plays its state and posts event 21. |
| [GUIText_DecodeUtf8](../functions/GUIText_DecodeUtf8.md) | `0x1403D8510` | Decodes one UTF-8 sequence (up to the old 6-byte form) into a code point and returns the pointer after it; the text layout's character reader. |
| [GUIText_Expand](../functions/GUIText_Expand.md) | `0x1403F0B10` | Runs the text formatter (qword_143CD9C00) over text with the argument vector (264-byte records) into out; returns 1 on success. |
| [GUITextBoard_CacheAuthoredBox](../functions/GUITextBoard_CacheAuthoredBox.md) | `0x14040E59C` | Once per component, snapshots the text node's authored rectangle and the component's authored size, the baseline GUITextBoardComponent_Update uses when it refits the board around the text. |
| [GUITextBoard_FindTextNode](../functions/GUITextBoard_FindTextNode.md) | `0x14040AAC0` | Returns the text node (kind 3) of a text-board component: the part found by name key qword_143CDA2A0+5000 under comp+272, or null. |
| [GUITextBoardComponent_Update](../functions/GUITextBoardComponent_Update.md) | `0x14040E3F0` | Update override of a text-board component class: fits the board's text node (kind 3 part named by qword_143CDA2A0+5000) to the text's extent, sizes the component to text plus margins (rounded up to even), and aligns t... |
| [GUITextLayout_IconsReady](../functions/GUITextLayout_IconsReady.md) | `0x1403DCE74` | True when every inline-icon texture requested by the layout is loaded; caches the answer in layout+100 / +101. |
| [GUITextNode_AlignVertical](../functions/GUITextNode_AlignVertical.md) | `0x1403DE4D0` | Ends the layout of a text node: flushes the pending line and shifts every line's y by the vertical alignment offset of the node box (node+256), then computes the text bounds. |
| [GUITextNode_ComputeBounds](../functions/GUITextNode_ComputeBounds.md) | `0x1403DEE64` | Computes the integer bounding box of the laid-out text (all glyphs and line extents) and stores it at layout+104..116. |
| [GUITextNode_Copy](../functions/GUITextNode_Copy.md) | `0x1403F0E24` | Copies a text node's configuration fields from src into dst and marks dst dirty. |
| [GUITextNode_Draw](../functions/GUITextNode_Draw.md) | `0x1403EA0B0` | Draws one text node: builds the shader palette from the node's UIFontSet row and colours, then emits glyph quads (and the shadow pass) through SDFFontRenderer. |
| [GUITextNode_FinishLine](../functions/GUITextNode_FinishLine.md) | `0x1403DDED8` | Closes the current text line: measures it, applies the overflow rule and the horizontal alignment to the line's glyph records, adjusts each glyph's y for the font baseline term, appends the 24-byte line record and adv... |
| [GUITextNode_HandleTag](../functions/GUITextNode_HandleTag.md) | `0x1403DD3A0` | Executes one in-string control code of a text node (newline, alignment, colour push / pop, size, spacing, icon, soft-hyphen suppression); returns 1 when it was a known code, 0 otherwise. |
| [GUITextNode_Init](../functions/GUITextNode_Init.md) | `0x1403F0BB4` | Constructor defaults of a text node: base init with type 3, vtable, empty containers and default colours / flags. |
| [GUITextNode_Layout](../functions/GUITextNode_Layout.md) | `0x1403DCF90` | Lays out one text node: resolves its font from the node's UIFontSet id and the game language, sets the glyph scale, then walks the string (colour/size tags) placing glyphs. |
| [GUITextNode_PlaceGlyph](../functions/GUITextNode_PlaceGlyph.md) | `0x1403DD780` | Places one character of the string into the node's glyph vector: looks up its advance, applies fixed-width centring, italic and kerning adjustments, appends a 36-byte glyph record and advances the pen; wraps the line ... |
| [GUITextNode_PlaceIcon](../functions/GUITextNode_PlaceIcon.md) | `0x1403DDC38` | Places an inline icon (an Icon table image) in the text flow as a glyph record of width size * f with char 0, requests its texture slot, and wraps the line when it does not fit. |
| [GUITextNode_SetRenderScale](../functions/GUITextNode_SetRenderScale.md) | `0x1403DD2F0` | Sets the text renderer's per-node state: glyph scale = (int16 size) / 64 and the font slot of the resolved UIFontType. |
| [GUITextNode_SetString](../functions/GUITextNode_SetString.md) | `0x1403F0F8C` | Sets a text node's string; marks the layout dirty only when it differs. |
| [GUITextNode_SetTextById](../functions/GUITextNode_SetTextById.md) | `0x1403F106C` | Looks up a localised text id and sets it on the node with argument expansion. |
| [GUITextNode_SetTextExpanded](../functions/GUITextNode_SetTextExpanded.md) | `0x1403F109C` | Expands placeholders in text using args into a temporary std::string, then sets the result on the node; uses the raw text if expansion reports nothing. |
| [GUITextNode_SetTextExpandedTemp](../functions/GUITextNode_SetTextExpandedTemp.md) | `0x1403F113C` | Sets a node's text with expansion using a throwaway, empty argument list that is freed afterwards. |
| [GUITextNode_SetTextFormat](../functions/GUITextNode_SetTextFormat.md) | `0x1403F1004` | printf-style setter: formats into a 2048-byte stack buffer and sets the node string. |
| [GUITextNode_UpdateLayout](../functions/GUITextNode_UpdateLayout.md) | `0x1403F1234` | Per-frame update of a text node: when its font is loaded (and its icons are, for icon nodes) refreshes the string from the text id and re-runs the layout, clearing the dirty byte on success. |
| [GUITextNode_WrapLine](../functions/GUITextNode_WrapLine.md) | `0x1403DE608` | Word wrap: when the glyph just placed does not fit the node width, finds the last line-break opportunity in the current line, finishes the line before it (soft-wrap flag set) and starts a new line with the glyphs afte... |
| [GUITextureSlot_Init](../functions/GUITextureSlot_Init.md) | `0x1403DAAF4` | Initialises one texture slot record from its source texture object, with two paths depending on a field of the texture. |
| [GUIVector32_Free](../functions/GUIVector32_Free.md) | `0x1403FD598` | Releases the vector's storage through its allocator (vtable +24) and resets begin / end / cap. |
| [GUIVector32_Init](../functions/GUIVector32_Init.md) | `0x1403FD550` | Constructs an empty vector of 32-byte elements: allocator pointer (from qword_143CDAA80 + 32) at +0, begin / end / cap = 0, extra fields zeroed. |
| [GUIWidget_AllResourcesLoaded](../functions/GUIWidget_AllResourcesLoaded.md) | `0x1403FB514` | Polls the widget's three resource vectors (texture refs, font / atlas groups, standalone refs) and returns 1 only when everything has finished loading. |
| [GUIWidget_AllResourcesLoadedThunk](../functions/GUIWidget_AllResourcesLoadedThunk.md) | `0x1403FC0D8` | Vtable entry: when byte w+82 is set it first runs sub_1403FCFEC, then returns GUIWidget_AllResourcesLoaded(w). |
| [GUIWidget_EnsureSlotGroup](../functions/GUIWidget_EnsureSlotGroup.md) | `0x1403FBE3C` | Makes sure the widget owns a texture slot group called `name` (a UI texture atlas) and starts loading its '<name without the first 17 characters>.utexpt' part table when it is new; with addRef set an existing group ge... |
| [GUIWidget_FindComponentById](../functions/GUIWidget_FindComponentById.md) | `0x1403F9D18` | Round-robin search of the widget's component vector for the component whose id (dword comp+8) equals the key's id (dword key+48); remembers where it found it. |
| [GUIWidget_FindComponentByName](../functions/GUIWidget_FindComponentByName.md) | `0x1403F96CC` | Finds a component of the widget by its name key (component+280 name pointer, +288 hash): first in the widget's std::map at +136, then by a round-robin scan of the component vector at +104..+112; a vector hit is put in... |
| [GUIWidget_FindComponentCached](../functions/GUIWidget_FindComponentCached.md) | `0x1403F9938` | Finds a component by two name keys (+280 and +504) with a caller-owned cache cell: if the cell still holds a component whose two keys match it is returned at once, otherwise the same map and vector search as GUIWidget... |
| [GUIWidget_FindFirstKind1Component](../functions/GUIWidget_FindFirstKind1Component.md) | `0x1403F9D6C` | Returns the first component of the widget whose type (comp+536) is 1 (index loop); sub_1403F9DA0 is the same search written with a pointer loop. |
| [GUIWidget_FindFirstKind1Component2](../functions/GUIWidget_FindFirstKind1Component2.md) | `0x1403F9DA0` | Same search as GUIWidget_FindFirstKind1Component, pointer-iterator form; used by most addon update methods. |
| [GUIWidget_FindRefNodeForComponent](../functions/GUIWidget_FindRefNodeForComponent.md) | `0x1403FA768` | Finds the component reference node (kind 12) of the widget that points at a given component, by the component's two names. |
| [GUIWidget_FindResourceByKey](../functions/GUIWidget_FindResourceByKey.md) | `0x1403FBDCC` | Linear search of the widget's pointer vector (widget+256 .. +264) for the entry whose name key equals `key`; returns the entry or 0. |
| [GUIWidget_FindResourceByName](../functions/GUIWidget_FindResourceByName.md) | `0x1403FBB80` | Linear search of the widget's resource-name vector (w+224..+232, pointers to name records) for the entry equal to a name key; returns the entry or null. |
| [GUIWidget_GetNodeScreenRect](../functions/GUIWidget_GetNodeScreenRect.md) | `0x1403FA86C` | A node's rectangle in UI (screen) pixels: its four corners pushed through its own 2x3 matrix (+160) and then each ancestor's, up to the root; result is the rounded bounds {left, top, right, bottom}. |
| [GUIWidget_Hide](../functions/GUIWidget_Hide.md) | `0x1403F93F8` | Mirror of GUIWidget_Show: marks a widget hidden, plays the Hide state of its root component (Show stopped) and posts event 6. |
| [GUIWidget_HitTestChildren](../functions/GUIWidget_HitTestChildren.md) | `0x1403FD844` | Depth-first walk of a node's children (first child at +208, next sibling at +32): layer nodes (kind 1) recurse, component nodes (kind 12) descend through GUIWidget_HitTestComponent, every other node whose kind is not ... |
| [GUIWidget_HitTestComponent](../functions/GUIWidget_HitTestComponent.md) | `0x1403FDB5C` | Descends into a component reference node (kind 12, e.g. |
| [GUIWidget_HitTestPoint](../functions/GUIWidget_HitTestPoint.md) | `0x1403FD5D4` | Hit-tests one point against a widget's node tree and appends the hits to q. |
| [GUIWidget_HitTestSubtree](../functions/GUIWidget_HitTestSubtree.md) | `0x1403FD67C` | Runs the hit test over a node's children (GUIWidget_HitTestChildren) under the accumulated transform. |
| [GUIWidget_NewSlotGroup](../functions/GUIWidget_NewSlotGroup.md) | `0x1403FB960` | Allocates a texture slot group from the global group pool, names it (default 'None'), registers the widget as one of its owners and appends it to the widget's group vector. |
| [GUIWidget_OnEvent](../functions/GUIWidget_OnEvent.md) | `0x1403FC3B4` | Widget's own event handler (vtable slot 2 of the GUIWidget vtable at 0x140721E10): maps the widget load / unload events onto two virtual methods. |
| [GUIWidget_PostReadyEvent](../functions/GUIWidget_PostReadyEvent.md) | `0x1403FC0FC` | Vtable entry: posts the event record xmmword_140723260 to the widget's owners (w+288) and returns whether the reply field was set. |
| [GUIWidget_ReleaseSlotGroup](../functions/GUIWidget_ReleaseSlotGroup.md) | `0x1403FBB20` | Removes a slot group from the widget's group vector and returns it to the pool. |
| [GUIWidget_Show](../functions/GUIWidget_Show.md) | `0x1403F930C` | Marks a widget shown and plays the Show state of its root component (Hide state stopped); posts owner event 5. |
| [GUIWidget_Tick](../functions/GUIWidget_Tick.md) | `0x1403FC14C` | Per-frame update of one widget: rebuilds the node lists when flagged, delivers the pending-ready event, ticks the main component, and posts the update event 4 to the widget's owners. |
| [GUIWidget_UpdateComponentsJob](../functions/GUIWidget_UpdateComponentsJob.md) | `0x1403F94EC` | Work-stealing worker: updates the node tree of the widget's components in chunks of 16, so several threads can share one widget's component vector. |
| [HelpMessage_Open](../functions/HelpMessage_Open.md) | `0x14036D948` | Opens the help message screen for a text id: starts the scripted message task and pushes kind 3. |
| [HelpMessage_Wait](../functions/HelpMessage_Wait.md) | `0x14036DA40` | Step of the help message screen (table index 3): waits until the message window has finished, then closes. |
| [IconBase_FormatPath](../functions/IconBase_FormatPath.md) | `0x1400FC1C0` | Builds the path of a numbered 'base' picture. |
| [IconImage_AcquireById](../functions/IconImage_AcquireById.md) | `0x1403DB6B8` | Loads the image of an icon id. |
| [IconPath_FromIconId](../functions/IconPath_FromIconId.md) | `0x1403DB140` | Builds the file path of an icon from its Icon id, using the IconGroup table to decide on the 4k texture variant. |
| [ImageDissolve_Step](../functions/ImageDissolve_Step.md) | `0x140372518` | One step of a dissolve that reveals an image through scattered pixels. |
| [Input_PauseFor](../functions/Input_PauseFor.md) | `0x1400F1C5C` | Makes the input module ignore input for a time. |
| [Inventory_BuildEquipList](../functions/Inventory_BuildEquipList.md) | `0x140288B94` | Builds the candidate list of items a unit may take from one menu group, in id order, and then orders that list either by a sort field or by the saved user order. |
| [Item_BuildAttributeLines](../functions/Item_BuildAttributeLines.md) | `0x14029F710` | Appends the equipment attribute lines of an item to the detail panel: the five stat bonuses, the move and jump bonuses and the element list. |
| [ItemCell_BindIconAndName](../functions/ItemCell_BindIconAndName.md) | `0x14029BEC4` | Binds an item's icon image and name text to a cell's parts; a missing Item-en row leaves both unset. |
| [ItemCell_SetItem](../functions/ItemCell_SetItem.md) | `0x14029ADE4` | Fills an item cell (icon image and name text) for an item id: formats the small item icon path and hands it with the id to ItemCell_BindIconAndName. |
| [ItemIcon_Set](../functions/ItemIcon_Set.md) | `0x14022A9E4` | Fills the small draw state of one classic item icon from the item record's two icon bytes: a 16 by 16 tile in a shared sheet and a palette selector. |
| [ItemList_GetPossessionIndex](../functions/ItemList_GetPossessionIndex.md) | `0x1402C437C` | Maps a possession-list row to the item or UI table row behind it: it switches on the list text id, walks the list element, and treats an entry at or above 261 as a UI table 0xEC row rather than an item. |
| [ItemObtainedPanel_Fill](../functions/ItemObtainedPanel_Fill.md) | `0x1401A4A40` | Fills the 'obtained' panel for a book or a collection entry (part read). |
| [JobScreen_BuildJobTabRows](../functions/JobScreen_BuildJobTabRows.md) | `0x14028A6E8` | The ability rows of one tab of a job on the job screen, for a party unit. |
| [JobScreen_FillStaticParty](../functions/JobScreen_FillStaticParty.md) | `0x14039231C` | Copies a work record's per-job arrays into the static party-shaped record at 0x143C51F10 that the job screen readers sub_140392800 / sub_14039284C / sub_140392884 read through qword_141D3B778. |
| [JobScreen_ShowJobAbilities](../functions/JobScreen_ShowJobAbilities.md) | `0x1402BA1FC` | Fills the job screen's detail panel for a job: the skillset header row and the four ability tabs of the current party unit. |
| [JobTreePanel_FillTexts](../functions/JobTreePanel_FillTexts.md) | `0x14029B140` | Fills the texts of one tree panel's name board from its job record: the job icon (JobTreePanel_SetJobIcon) and the level texts. |
| [JobTreePanel_SetJobIcon](../functions/JobTreePanel_SetJobIcon.md) | `0x14029B054` | Formats the job icon image path (j_NNN) of a tree panel from its job record; a LockUnreleased job gets the placeholder icon 24 instead. |
| [JobTreePanel_SetTextKey](../functions/JobTreePanel_SetTextKey.md) | `0x14029BC00` | Points a name-board text binding at a text key and clears the text node's fixed text id so the keyed text is used. |
| [JournalDetail_Fill](../functions/JournalDetail_Fill.md) | `0x14016B49C` | Fills the Events detail panel. |
| [JournalList_Build](../functions/JournalList_Build.md) | `0x140169D28` | Builds the Chronicle Events list from the Journal rows that are met. |
| [JournalList_DrawRow](../functions/JournalList_DrawRow.md) | `0x14016B0D4` | Draws one row of the Events list. |
| [JournalList_RestoreCursor](../functions/JournalList_RestoreCursor.md) | `0x1401699A8` | Puts the list cursor back on the replayed entry. |
| [JournalPanel_Tick](../functions/JournalPanel_Tick.md) | `0x140169404` | The replay panel's state steps. |
| [JournalReplay_StartEvent](../functions/JournalReplay_StartEvent.md) | `0x140169724` | Starts the replay of the chosen Events entry (action 2). |
| [JournalReplay_StartMovie](../functions/JournalReplay_StartMovie.md) | `0x140169854` | Starts the replay of a movie entry (action 3). |
| [JournalScreen_OnAction](../functions/JournalScreen_OnAction.md) | `0x1401694E4` | Handles the actions of the Events screen. |
| [KeyTrack_FindKey](../functions/KeyTrack_FindKey.md) | `0x14040222C` | Binary search in a keyframe track: returns the index of the last key whose frame (u16 at key+0) is <= frame, or -1 when every key is later. |
| [KeyTrackBool_Eval](../functions/KeyTrackBool_Eval.md) | `0x1403F4604` | Evaluates the boolean (visibility) track of a UIB state at an integer frame; the result drives node byte +144. |
| [KeyTrackVec2_Eval](../functions/KeyTrackVec2_Eval.md) | `0x140407C18` | Evaluates a two-float keyframe track (the scale track of a UIB state) at a frame: finds the key, eases between it and the next key with UIAnim_Curve and writes the interpolated pair. |
| [Launcher_DrawControlsPage](../functions/Launcher_DrawControlsPage.md) | `0x1401BB9D8` | Switches the launcher guide to its controls panel. |
| [Launcher_DrawInfoPage](../functions/Launcher_DrawInfoPage.md) | `0x1401BB77C` | Draws an information page of the launcher's guide. |
| [Launcher_DrawPage](../functions/Launcher_DrawPage.md) | `0x1401BB5EC` | Draws the current page of the launcher's guide pages. |
| [Launcher_DrawStartPage](../functions/Launcher_DrawStartPage.md) | `0x1401BBDD0` | Draws the guide page that carries the Start button. |
| [Launcher_FillControls](../functions/Launcher_FillControls.md) | `0x1401BBB30` | Fills the controls list of the launcher guide. |
| [LegacyMenu_BuildLocationList](../functions/LegacyMenu_BuildLocationList.md) | `0x1402B276C` | Builds the legacy location menu's list of unlocked world map locations. |
| [LegacyMenu_InitWorld](../functions/LegacyMenu_InitWorld.md) | `0x1402B2EB0` | Initialises the legacy world menu: loads its text resource and picks the screen state block of the current text language. |
| [LegacyMenu_LoadRowList](../functions/LegacyMenu_LoadRowList.md) | `0x1402B29D8` | Loads the row id list of the legacy menu named by the screen block into the live row array and starts the menu command screen. |
| [LegacyMenu_PickLocation](../functions/LegacyMenu_PickLocation.md) | `0x1402B28B0` | Confirms the highlighted location of the legacy location menu. |
| [LegacyMenu_StoreRow](../functions/LegacyMenu_StoreRow.md) | `0x1402378C8` | Stores the row chosen in the current legacy menu into the acting unit's row memory, for the menus that remember it. |
| [LegacyMenuTasks_Run](../functions/LegacyMenuTasks_Run.md) | `0x1402B4570` | Task body of the legacy menu panes: keeps three pane tasks in step with the menu state. |
| [LegacyOptions_DrawTask](../functions/LegacyOptions_DrawTask.md) | `0x140364FAC` | Task that draws the legacy options window and handles its cursor. |
| [LegacyOptions_Open](../functions/LegacyOptions_Open.md) | `0x140364D2C` | Opens the legacy options screen: unpacks the option word into the 12 live choices. |
| [LegacyOptions_RowTask](../functions/LegacyOptions_RowTask.md) | `0x140365F34` | Task that edits one option row of the legacy options screen and packs the choices back. |
| [LegacyTask12_Build](../functions/LegacyTask12_Build.md) | `0x14039A518` | Scene task 12: builds the plates and number fields of a battle-side panel from per-language cell lists. |
| [ListScroll_HandleStick](../functions/ListScroll_HandleStick.md) | `0x14028E5D0` | Mouse wheel or right stick scrolls a component list by whole rows, independent of the cursor. |
| [ListScroll_Step](../functions/ListScroll_Step.md) | `0x14028E720` | Scrolls a component list vertically by rows x row height, then re-homes the focus when the focused item left the view. |
| [LoreDictionary_BuildList](../functions/LoreDictionary_BuildList.md) | `0x1401E412C` | Builds the glossary list of one category. |
| [LoreDictionary_ClearNewMarks](../functions/LoreDictionary_ClearNewMarks.md) | `0x1401E4B24` | Clears the new mark of every listed glossary entry. |
| [LoreDictionary_CompareEntries](../functions/LoreDictionary_CompareEntries.md) | `0x1401E4370` | Comparator of two glossary list entries. |
| [LoreDictionary_CurrentRow](../functions/LoreDictionary_CurrentRow.md) | `0x1401E4BDC` | Returns the second key of the glossary row shown for an entry and page. |
| [LoreDictionary_GetAffiliationIconId](../functions/LoreDictionary_GetAffiliationIconId.md) | `0x1401E4924` | Returns the affiliation icon id of a glossary entry's current row. |
| [LoreDictionary_GetAffiliationIdByPair](../functions/LoreDictionary_GetAffiliationIdByPair.md) | `0x1401E5DE8` | Returns the affiliation id of the glossary row that a table 283 pair names. |
| [LoreDictionary_GetAffiliationName](../functions/LoreDictionary_GetAffiliationName.md) | `0x1401E4820` | Returns the affiliation name of a glossary row. |
| [LoreDictionary_GetAffiliationNameByPair](../functions/LoreDictionary_GetAffiliationNameByPair.md) | `0x1401E5F38` | Returns the affiliation name of the glossary row that a table 283 pair names. |
| [LoreDictionary_GetAliasName](../functions/LoreDictionary_GetAliasName.md) | `0x1401E4A20` | Returns the alias name of a glossary row. |
| [LoreDictionary_GetCategory](../functions/LoreDictionary_GetCategory.md) | `0x1401E46A0` | Returns a glossary row's category. |
| [LoreDictionary_GetClearMarkByPair](../functions/LoreDictionary_GetClearMarkByPair.md) | `0x1401E6090` | Returns the clear mark of the glossary row that a table 283 pair names. |
| [LoreDictionary_GetEntry](../functions/LoreDictionary_GetEntry.md) | `0x1401E5018` | Fetches a glossary row. |
| [LoreDictionary_GetFace](../functions/LoreDictionary_GetFace.md) | `0x1401E4720` | Returns a glossary row's face number. |
| [LoreDictionary_GetFaceByPair](../functions/LoreDictionary_GetFaceByPair.md) | `0x1401E5B6C` | Returns the face of the glossary row that a table 283 pair names. |
| [LoreDictionary_GetFullNameByPair](../functions/LoreDictionary_GetFullNameByPair.md) | `0x1401E5A90` | Returns the full name of the glossary row that a table 283 pair names. |
| [LoreDictionary_GetIcon](../functions/LoreDictionary_GetIcon.md) | `0x1401E47A0` | Returns the icon of a glossary entry's current row. |
| [LoreDictionary_GetPaletteByPair](../functions/LoreDictionary_GetPaletteByPair.md) | `0x1401E5D14` | Returns the palette of the glossary row that a table 283 pair names. |
| [LoreDictionary_GetPlainNameByPair](../functions/LoreDictionary_GetPlainNameByPair.md) | `0x1401E5934` | Returns the plain name of the glossary row that a table 283 pair names. |
| [LoreDictionary_GetSpriteShapeByPair](../functions/LoreDictionary_GetSpriteShapeByPair.md) | `0x1401E5C40` | Returns the sprite shape of the glossary row that a table 283 pair names. |
| [LoreDictionary_IndexOfKey](../functions/LoreDictionary_IndexOfKey.md) | `0x1401E4ED8` | Maps a glossary first key to its entry index (below 150). |
| [LoreDictionary_PageCount](../functions/LoreDictionary_PageCount.md) | `0x1401E4594` | Counts the pages of a glossary entry. |
| [LoreDictionary_SortList](../functions/LoreDictionary_SortList.md) | `0x1401E50D4` | Sorts a glossary list by a mode. |
| [MainTab_BindNodes](../functions/MainTab_BindNodes.md) | `0x1402AC048` | Finds the header (MainTab/Tab) nodes of a screen and keeps them in the controller: the tab, the TextMask mask node, the title text node and the other tab title boards. |
| [MainTab_SelectTab](../functions/MainTab_SelectTab.md) | `0x1402AC2E8` | Plays the header state that belongs to tab `index` and stops the other three. |
| [MapTitleLabel_SetText](../functions/MapTitleLabel_SetText.md) | `0x140149148` | Fills the 'Text' and 'Text00' nodes of the 'TextMapGrade' label of a window and plays its 'En' or 'Ja' state. |
| [MenuCtl_Entry17](../functions/MenuCtl_Entry17.md) | `0x14036FFE8` | Table index 17: a jump to sub_140370D58, a step with a state in record dword 4. |
| [MenuCtl_Entry22](../functions/MenuCtl_Entry22.md) | `0x140373784` | Two-row question with a fade (table index 22): the first answer ends with a fade to a new scene, the other leaves. |
| [MenuCtl_Entry24](../functions/MenuCtl_Entry24.md) | `0x140374304` | Input step of a list (table index 24): confirm opens the detail page (kind 25), the help action opens the list's help. |
| [MenuCtl_Entry25](../functions/MenuCtl_Entry25.md) | `0x14037472C` | Step of the detail page of a list entry with a picture (table index 25): sets the picture up, runs the paged text, then returns to the list. |
| [MenuCtl_Entry26](../functions/MenuCtl_Entry26.md) | `0x140371B2C` | Input step of a list (table index 26): confirm opens the page of the entry (sub_140371CAC), the help action opens the list's help. |
| [MenuCtl_Entry27](../functions/MenuCtl_Entry27.md) | `0x140371F68` | Step of the page of a list entry that has a picture dissolve and a book progress word (table index 27). |
| [MenuCtl_Entry28](../functions/MenuCtl_Entry28.md) | `0x140375538` | Step of the row menu that opens the other list screens (table index 28): each row opens one list builder. |
| [MenuCtl_Entry28_ResetRows](../functions/MenuCtl_Entry28_ResetRows.md) | `0x14037544C` | Sets the windows of the row menu (kind 28) to their idle styles before it opens a list. |
| [MenuCtl_Entry33](../functions/MenuCtl_Entry33.md) | `0x14037680C` | Input step of a list (table index 33): confirm opens the entry's page (kind 34). |
| [MenuCtl_Entry34](../functions/MenuCtl_Entry34.md) | `0x140376B58` | Step of the page of an entry of list 33 (table index 34): runs a text widget and returns to the list. |
| [MenuCtl_Entry43](../functions/MenuCtl_Entry43.md) | `0x140318BBC` | Step of a row menu with a short intro and a close animation (table index 43): its rows open kinds 44, 45 and 33 or print a notice. |
| [MenuCtl_Entry44](../functions/MenuCtl_Entry44.md) | `0x1403193CC` | Step of a list of 7 flagged entries opened from index 43 (table index 44): confirm marks the entry as seen and starts the scene for it. |
| [MenuCtl_Entry45](../functions/MenuCtl_Entry45.md) | `0x140319860` | Step of a list of 8 flagged entries opened from index 43 (table index 45): confirm marks the entry as seen and starts the event numbered for it. |
| [MenuCtl_Entry50](../functions/MenuCtl_Entry50.md) | `0x1402D18D0` | Short step of a controller that closes itself once its window is done (table index 50). |
| [MenuCtl_Entry51](../functions/MenuCtl_Entry51.md) | `0x1403462A4` | Step of a screen that runs the paged text widget under a window with a pending close mask (table index 51). |
| [MenuCtl_Entry52](../functions/MenuCtl_Entry52.md) | `0x140346428` | Yes or no step with a result (table index 52): confirm applies the number held in word 0x140D498D4 when it is below 512. |
| [MenuCtl_Entry53](../functions/MenuCtl_Entry53.md) | `0x1402D1ABC` | Step of a controller that walks through a chain of pages (table index 53), moving forward or backward with the record's direction. |
| [MenuCtl_Entry54](../functions/MenuCtl_Entry54.md) | `0x1402D1DA8` | Step of a one-shot window controller (table index 54): a state dword starts a window action, then it pops. |
| [MenuCtl_ListCursorStep](../functions/MenuCtl_ListCursorStep.md) | `0x140378B88` | Moves the cursor of a vertical list screen by one row on an up or down press. |
| [Movie_Start](../functions/Movie_Start.md) | `0x1400D8304` | Starts the playback of a movie from its MovieData row: picks the file, the sound banks, the subtitle window and the controller flags. |
| [MovieControl_IdleHint](../functions/MovieControl_IdleHint.md) | `0x14027A128` | While a movie plays unpaused, shows the 'Pause' button hint for about 5 seconds after any input. |
| [MovieControl_PausedTick](../functions/MovieControl_PausedTick.md) | `0x14027A1CC` | Paused frame of the movie overlay: a completed hold with byte +25 set takes the skip (state 3); the pause or back action resumes. |
| [MovieControl_TryOpenPause](../functions/MovieControl_TryOpenPause.md) | `0x14027A35C` | Opens the movie pause overlay on the pause action, with or without the Skip hint by MovieControl +25. |
| [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md) | `0x1400D8168` | Per-frame movie pause / skip handling of the GameUI MovieController (a virtual of its second vtable): publishes whether the playing movie can be skipped and runs the MovieControl state machine. |
| [MovieSound_LoadBank](../functions/MovieSound_LoadBank.md) | `0x1401D7608` | Loads one sound bank of a movie. |
| [MsgWindow_BuildFrame](../functions/MsgWindow_BuildFrame.md) | `0x14022BFEC` | Sets up the frame primitives of a message window and its decoration cells by window kind and language. |
| [Novel_GetPageText](../functions/Novel_GetPageText.md) | `0x1401E1C10` | Returns the text of a book page from the Novel table the book names. |
| [NovelReader_Open](../functions/NovelReader_Open.md) | `0x1401DFCD4` | Opens the book reader on a book (vtable slot at 0x143D36220). |
| [NovelReader_SendReadThrough](../functions/NovelReader_SendReadThrough.md) | `0x1401DFF60` | Reports that the book was read to the end. |
| [NovelReader_ShowPage](../functions/NovelReader_ShowPage.md) | `0x1401DFED0` | Shows one page of the open book (vtable slot at 0x143D36238). |
| [NumberFields_Draw](../functions/NumberFields_Draw.md) | `0x140242C84` | Draws a list of number fields (32-byte records) into a staging buffer. |
| [Opening_LoadMessageSprites](../functions/Opening_LoadMessageSprites.md) | `0x14037DB9C` | Loads the opening message textures and selects the language's sprite list for the opening text. |
| [PagedText_DrawPage](../functions/PagedText_DrawPage.md) | `0x14037A940` | Draws one page of a paged message window starting at a given line: rebuilds the window rectangle, positions the extra marker, draws the text and copies the window to the video page. |
| [PagedText_Init](../functions/PagedText_Init.md) | `0x14037A168` | Sets up a paged message window: reserves four sprite records and one window record, positions them from the info block, measures the message and draws its first page. |
| [PagedText_Step](../functions/PagedText_Step.md) | `0x14037A3F0` | Per-frame input of a paged message window: confirm turns to the next page, cancel closes it, and holding action 57 scrolls the text line by line. |
| [PagedText_WaitAndClose](../functions/PagedText_WaitAndClose.md) | `0x14036D870` | Step of a screen that only runs the paged text widget until it finishes (table index 2). |
| [PanelScreen_InitVram](../functions/PanelScreen_InitVram.md) | `0x14033D88C` | Uploads the palette and strips of the second panel screen to VRAM. |
| [RangeOverlay_BuildRowMasks](../functions/RangeOverlay_BuildRowMasks.md) | `0x140389B50` | Builds the 18 row words of the range overlay diamond for a given distance. |
| [ScenePresetOverrides_Apply](../functions/ScenePresetOverrides_Apply.md) | `0x140348038` | Copies the sprite palette and pose entries named by the current scene's preset list into the live sprite tables. |
| [ScreenReopen_Step](../functions/ScreenReopen_Step.md) | `0x1403797F8` | Step of a short controller (table index 49) that waits a few frames, then re-opens the screen whose kind is in its first dword. |
| [ScrollBar_SetPosition](../functions/ScrollBar_SetPosition.md) | `0x14040B994` | Game setter for the native scroll bar component (vtable 0x140722238, kind 8 at node+536). |
| [ScrollHelper_Bind](../functions/ScrollHelper_Bind.md) | `0x1402AADD8` | Binds a screen's scrolling gadget: finds the child named `VScroll` (a scroll bar node, type 8) and its guide part, records the binding and refits the gadget. |
| [SDFFont_GetKerning](../functions/SDFFont_GetKerning.md) | `0x1403A9114` | Kerning pair lookup: returns (x, y) kerning for a left / right code point pair of the current font, from the font's own kerning rows plus the second .ker table. |
| [SDFFont_ItalicShearWidth](../functions/SDFFont_ItalicShearWidth.md) | `0x1403A942C` | The horizontal overhang of an italic (sheared) glyph per unit of glyph multiplier: the shear slant times the font's metric unit, the current glyph scale and 48. |
| [ShopItemList_DrawRow](../functions/ShopItemList_DrawRow.md) | `0x1402A57AC` | Draws one shop list row: fills it (ShopItemList_FillRow), colours the owned count and the price, prints the price and shows the 'new' and 'selected' marks. |
| [ShopItemList_FillRow](../functions/ShopItemList_FillRow.md) | `0x1402A3578` | Fills one row of an item list (the shop's buy and sell lists and three other lists): icon and name, the equipped and owned counts and the category image of the entry's item. |
| [ShopItemList_SetPrice](../functions/ShopItemList_SetPrice.md) | `0x1402A5A80` | Prints a price into the row's 'TextPrice' part with UI text 1717 (1753 when greyed). |
| [ShopList_BuildEntries](../functions/ShopList_BuildEntries.md) | `0x14036B18C` | Builds the entries of the shop's item list from word_141811470: orders the list, sizes the list gadget and fills one entry per id (ShopEntry_Fill). |
| [ShopPage_OpDrawNumber](../functions/ShopPage_OpDrawNumber.md) | `0x140328D54` | Opcode 14 of the 20-entry page-script table at 0x140683938: draws a right-aligned number with blank padding and returns the next record. |
| [SpriteAnim_Step](../functions/SpriteAnim_Step.md) | `0x14038EDD4` | Advances one opening / title sprite animation by a tick and queues the cells of its current frame. |
| [StatusGlossary_Input](../functions/StatusGlossary_Input.md) | `0x14036E360` | Input step of a page of rows linked by direction (table index 56): moves between rows by a link table and shows each row's help text. |
| [StatusGlossary_Open](../functions/StatusGlossary_Open.md) | `0x14036E1D8` | Opens the help page of a list of cursor rows and pushes kind 56. |
| [Str_Format](../functions/Str_Format.md) | `0x1400261CC` | snprintf-style formatter (thin wrapper around sub_140026084). |
| [StringHandle_Release](../functions/StringHandle_Release.md) | `0x140026D9C` | Frees a {allocator, pointer} string-like member. |
| [sub_14002620C](../functions/sub_14002620C.md) | `0x14002620C` | A bounded string copy: it moves a source string into a caller buffer, stopping at either the destination capacity or an explicit source limit, and terminates the result. |
| [sub_1400ED328](../functions/sub_1400ED328.md) | `0x1400ED328` | Publishes a built list to the UI: it checks that the UI list module is open and hands the list parameters to the module's list setter with a "publish" flag. |
| [sub_1400EEC18](../functions/sub_1400EEC18.md) | `0x1400EEC18` | The handler for a scene message word: it resolves the 5-bit class and 11-bit index of the word and dispatches to the text setter of that class. |
| [sub_1400F4BCC](../functions/sub_1400F4BCC.md) | `0x1400F4BCC` | Plays a UI sound cue: looks key soundKey up in UI table 0x45 and starts the sound the row names, dispatching on the row's type word. |
| [sub_1400F4C54](../functions/sub_1400F4C54.md) | `0x1400F4C54` | The stop / state counterpart of sub_1400F4BCC: same table 0x45 lookup, but calls the stop-type function of each of the four handlers. |
| [sub_1400F4D38](../functions/sub_1400F4D38.md) | `0x1400F4D38` | Event handler (slot 2) of the UIDerivedWidget vtable at 0x140704578: forwards the event to the base handler, then plays the widget's own press / release cue when the event is type 12 or 16 and the owner is in the righ... |
| [sub_1400F5674](../functions/sub_1400F5674.md) | `0x1400F5674` | Focuses a GUI node (GUICore_FocusNode) with its byte +557 temporarily cleared while any 'character render' slot is active, so the focus switch does not trigger the node's 557 behaviour. |
| [sub_1400F5B0C](../functions/sub_1400F5B0C.md) | `0x1400F5B0C` | Moves the cursor on a list of GUI nodes: optionally focuses nodes[cursor], then updates every node's CursorOver / CursorOut animation (sub_1400F5C78) with 'is cursor' = (index == cursor). |
| [sub_1400F5BCC](../functions/sub_1400F5BCC.md) | `0x1400F5BCC` | Same as sub_1400F5B0C but takes the option struct as a pointer instead of two flags. |
| [sub_1400F6148](../functions/sub_1400F6148.md) | `0x1400F6148` | Three-way (-1 / 0 / 1) animation switch for a node with two named states (default A = qword_143CDA2A0+5240 / +4600 pair, B = +5256 / +4616 pair): plays one, stops the other, and sets node+416 accordingly. |
| [sub_1400F69BC](../functions/sub_1400F69BC.md) | `0x1400F69BC` | Looks up the button icon / name string for a control action id: the icon a key / pad rebinding table gives for (actionId, slot), else the default one from UI table 25. |
| [sub_1400F6B5C](../functions/sub_1400F6B5C.md) | `0x1400F6B5C` | Resolves a button id through an Nxd table (qword_143CDA2C0, found by NxdRegistry_Find index 35) and returns one of four glyph ids according to the player's pad layout (byte at qword_143CD9EE8 + 13726). |
| [sub_1400F6D58](../functions/sub_1400F6D58.md) | `0x1400F6D58` | Steps a cursor value by one with wrap-around when the 'vertical' direction pair is pressed (actions 35 / 36, masks 0x8000 / 0x2000), via sub_1400F6FA0. |
| [sub_1400F6DD4](../functions/sub_1400F6DD4.md) | `0x1400F6DD4` | Same as sub_1400F6D58 but for the other direction pair (actions 33 / 34, masks 0x1000 / 0x4000) via sub_1400F704C. |
| [sub_1400F6FA0](../functions/sub_1400F6FA0.md) | `0x1400F6FA0` | Reads the second direction pair (actions 35 = -1 and 36 = +1, masks 0x8000 and 0x2000): reports a step and whether it may wrap. |
| [sub_1400F704C](../functions/sub_1400F704C.md) | `0x1400F704C` | First direction pair: actions 33 = -1 (mask 0x1000 = 4096) and 34 = +1 (mask 0x4000), same protocol as sub_1400F6FA0. |
| [sub_1400F7378](../functions/sub_1400F7378.md) | `0x1400F7378` | Fills one button-guide entry of a panel: from row (tableKey, rowKey) of UI table 33 sets the IconButton part's label key and the Title text id. |
| [sub_1400FABC4](../functions/sub_1400FABC4.md) | `0x1400FABC4` | Two-pane grid cursor navigation (5 columns per row): moves a (pane, index) cursor with up / down / left / right and pane switch, and returns the flat index across both panes. |
| [sub_1400FC29C](../functions/sub_1400FC29C.md) | `0x1400FC29C` | Detects an 'opposite directions held at once' state on the pad / keyboard direction set: returns true when two opposite inputs of any axis are down together, which makes direction stepping ignore input. |
| [sub_1400FC6D8](../functions/sub_1400FC6D8.md) | `0x1400FC6D8` | 'Was this action pressed this frame' test for the direction helpers: checks the action's pressed / repeat flags, with an optional key-mask test. |
| [sub_1400FCE48](../functions/sub_1400FCE48.md) | `0x1400FCE48` | Checks that no 'busy' gate is active: returns 1 when the global gate variables at 0x142FF9F24..0x142FF9F50 are all clear (or the alternative gate function says OK). |
| [sub_14010824C](../functions/sub_14010824C.md) | `0x14010824C` | The Land ability help panel's content method: it reads the Land row's ability id and icon and fills the panel's text and icon slots. |
| [sub_140134B54](../functions/sub_140134B54.md) | `0x140134B54` | Focus-change handler (slot 27) of the UnitStatusHoroscopeAffinity addon: activates / deactivates the addon when focus enters or leaves id 1111 / 1517. |
| [sub_14013DD70](../functions/sub_14013DD70.md) | `0x14013DD70` | Fades a guide slot in or out: finds the slot of row `row`, sets its node visible byte and plays Gauge_on / Gauge_off. |
| [sub_140142014](../functions/sub_140142014.md) | `0x140142014` | Builds one row of an item list: its name text, the item's small picture path and the parts that draw them. |
| [sub_14014D57C](../functions/sub_14014D57C.md) | `0x14014D57C` | Fills a selection panel from one item: clears its text, stores the id, updates a named node, and sets the small item picture and name on the panel's parts. |
| [sub_140197BCC](../functions/sub_140197BCC.md) | `0x140197BCC` | The new-item flag handler for the item screens: it clears or focuses the per-item new-arrival flag that marks an item the player has not looked at yet. |
| [sub_1401D1E30](../functions/sub_1401D1E30.md) | `0x1401D1E30` | Activates the addon's root widget (a+24) through sub_1403F930C and marks the GUI core dirty. |
| [sub_1401D1E70](../functions/sub_1401D1E70.md) | `0x1401D1E70` | Returns whether the addon's first kind-1 component has the active-state flag set (state +4600 playing / done byte +105). |
| [sub_1401D1EAC](../functions/sub_1401D1EAC.md) | `0x1401D1EAC` | Deactivates the addon's root widget (a+24) through sub_1403F93F8. |
| [sub_1401D2344](../functions/sub_1401D2344.md) | `0x1401D2344` | Default addon handler (used by about 130 addon vtables): walks the root widget's child list and advances each child's three-stage readiness byte (+573), registering the addon id in the child's owner list. |
| [sub_1401D2E9C](../functions/sub_1401D2E9C.md) | `0x1401D2E9C` | Slot 6 of the UIAgentCursor vtable: reacts to an event addressed to the cursor's target node. |
| [sub_1401D80A8](../functions/sub_1401D80A8.md) | `0x1401D80A8` | Sets one UI slot's cue id and dispatches it: the slot number selects the subsystem (sound, text dispatch, and others) and the id selects what that subsystem plays or shows. |
| [sub_1401F3858](../functions/sub_1401F3858.md) | `0x1401F3858` | Refreshes a party/unit panel: it looks up the unit's sprite shape and shows or hides the lock and starting-team icons. |
| [sub_1402083B4](../functions/sub_1402083B4.md) | `0x1402083B4` | The ending-save add-on: it shows its panel, records the cleared game through the options writer and offers the resume path. |
| [sub_14022AFEC](../functions/sub_14022AFEC.md) | `0x14022AFEC` | Builds an item list screen: it initialises the screen-state record selected by a global screen index and fills the list cells with icons and text ids. |
| [sub_14022F868](../functions/sub_14022F868.md) | `0x14022F868` | The action list menu: a scene task that lists a unit's actions and reads the chosen cell. |
| [sub_140236468](../functions/sub_140236468.md) | `0x140236468` | A scene task that publishes the shared list object and keeps the selection and skip state in step. |
| [sub_1402366C0](../functions/sub_1402366C0.md) | `0x1402366C0` | Prepares the shared list object: it publishes the list pointer and fills the static word array the list uses for empty cells. |
| [sub_14023678C](../functions/sub_14023678C.md) | `0x14023678C` | Fills the item list cells of an inventory or equipment screen. |
| [sub_140242AFC](../functions/sub_140242AFC.md) | `0x140242AFC` | Initialises one 0x20-byte UI element: screen position, texture coordinates, size, and a packed flag word, from a source record and a rectangle. |
| [sub_14029554C](../functions/sub_14029554C.md) | `0x14029554C` | Pure this-adjusting thunk: forwards (a1 + 16, a2, a3) to sub_1402AB5B0, the gadget event dispatcher. |
| [sub_14029643C](../functions/sub_14029643C.md) | `0x14029643C` | Fills one row of a multi-column item list, choosing the row filler by a kind argument. |
| [sub_14029BCD4](../functions/sub_14029BCD4.md) | `0x14029BCD4` | Shows or hides one icon image slot and sets its icon by id: plays the node's Show / Hide state and, when the icon is shown, calls GuiImage_SetIconById. |
| [sub_1402A291C](../functions/sub_1402A291C.md) | `0x1402A291C` | Flushes two pending flags of a gadget pair: when the dword at a1+368 is set, clears it and calls the vtable +80 slot of the sub-object at a1+16; when the dword at a1+1072 is set, clears it and calls vtable +80 of the ... |
| [sub_1402A3470](../functions/sub_1402A3470.md) | `0x1402A3470` | Clears both list pages of a double-buffered list gadget: calls sub_14028D7BC(list, 0) twice and swaps the two page pointers at a1+56 / a1+64 after each call. |
| [sub_1402A6710](../functions/sub_1402A6710.md) | `0x1402A6710` | Refreshes one possession or shop panel row: it resolves the entry in the third argument either as an item id or as a UI table row and fills the row's icon, name and grey-out state. |
| [sub_1402A91E4](../functions/sub_1402A91E4.md) | `0x1402A91E4` | Shows or hides the node at gadget+104 with the generic Show / Hide state pair: show != 0 picks mode instant (0 animated show, 1 instant show); show == 0 picks mode -1 (animated hide) or -2 (instant hide); hands it to ... |
| [sub_1402A9C4C](../functions/sub_1402A9C4C.md) | `0x1402A9C4C` | Selects one of three 'tail' layouts on the node at gadget+16: plays TailNone / TailL / TailR for which = 0 / 1 / 2 and stops the other two. |
| [sub_1402A9D5C](../functions/sub_1402A9D5C.md) | `0x1402A9D5C` | Selects row layout 'Row1'..'Row3' of the node at gadget+16: plays the state for row index `row` (0-based) and stops the other two. |
| [sub_1402B2AAC](../functions/sub_1402B2AAC.md) | `0x1402B2AAC` | Builds the classic UI atlas bundle once per process from five game textures, including the classic item icon sheet. |
| [sub_1402BBBCC](../functions/sub_1402BBBCC.md) | `0x1402BBBCC` | The equip screen's confirm/refresh path. |
| [sub_1402C0554](../functions/sub_1402C0554.md) | `0x1402C0554` | Restores a list's cursor when the list is built again: it reads the list's saved entry (row, scroll, word) from the table at word_143760800 and puts the cursor back on the row that holds the saved word. |
| [sub_1402C20F0](../functions/sub_1402C20F0.md) | `0x1402C20F0` | Applies an item id to the first slot that does not already hold it and updates the equip block and the stat readout. |
| [sub_1402CD168](../functions/sub_1402CD168.md) | `0x1402CD168` | Posts a parameterised UI message from a kind and a value, after checking both against the small pair table the message system accepts. |
| [sub_1402D57C0](../functions/sub_1402D57C0.md) | `0x1402D57C0` | The Outfitter entry handler: it prepares and calls the menu function at 0x1402BE7E8, then runs the per-frame dispatcher. |
| [sub_1402D5818](../functions/sub_1402D5818.md) | `0x1402D5818` | A second Outfitter entry handler; it only clears the entry byte once and runs the per-frame dispatcher. |
| [sub_1402D58EC](../functions/sub_1402D58EC.md) | `0x1402D58EC` | The Outfitter slot-list handler: it tracks the selected slot, shows its help id, and on confirm either undoes a pending bit-15 purchase or opens the equip-change preview for the slot. |
| [sub_1402D5B50](../functions/sub_1402D5B50.md) | `0x1402D5B50` | The Outfitter's per-frame update entry: it clears a one-shot byte and calls the dispatcher. |
| [sub_1402D5CC4](../functions/sub_1402D5CC4.md) | `0x1402D5CC4` | Opens the Outfitter's equipment-change state: it backs up the selected unit's four editable hand words, builds the five candidate words from the shop list, refreshes the panel block, and on the leave message applies t... |
| [sub_1402D5FE4](../functions/sub_1402D5FE4.md) | `0x1402D5FE4` | The Outfitter/shop sell-or-confirm handler for the selected slot. |
| [sub_1402D62EC](../functions/sub_1402D62EC.md) | `0x1402D62EC` | Leaves the Outfitter to the equip screen: it starts the equip task, resets the task slots and switches the menu state. |
| [sub_1402D67C8](../functions/sub_1402D67C8.md) | `0x1402D67C8` | The equip screen's message handler for the leave messages 0, 6 and 7: it closes the screen, refreshes the job screen when the unit changed, and zeroes the session price accumulator. |
| [sub_1402D6914](../functions/sub_1402D6914.md) | `0x1402D6914` | The Outfitter/shop message handler. |
| [sub_1402D6E14](../functions/sub_1402D6E14.md) | `0x1402D6E14` | The Outfitter's commit/cancel message handler. |
| [sub_1402D6F10](../functions/sub_1402D6F10.md) | `0x1402D6F10` | The per-frame dispatcher of the Outfitter/equip screens: it builds a small message from the input state and calls one of the three screen handlers by menu id. |
| [sub_1402D6FB8](../functions/sub_1402D6FB8.md) | `0x1402D6FB8` | Builds the five (id, price) preview pairs for the equip panel from the live unit words and the override array, then posts the preview record. |
| [sub_1402D746C](../functions/sub_1402D746C.md) | `0x1402D746C` | Applies an id to a slot, then mirrors the selected unit's four hand words and the fifth word from the scratch record into the candidate array and refreshes the stat block. |
| [sub_1402D7640](../functions/sub_1402D7640.md) | `0x1402D7640` | Rebuilds the shop's displayed item list into the shared menu list and then syncs the candidate array from the selected unit's scratch record. |
| [sub_1402E1604](../functions/sub_1402E1604.md) | `0x1402E1604` | The second copy of the classic item-icon state setter; it fills the same 16 by 16 tile state from the item record's icon bytes. |
| [sub_1402E1C64](../functions/sub_1402E1C64.md) | `0x1402E1C64` | Second item list screen constructor. |
| [sub_1402F9F20](../functions/sub_1402F9F20.md) | `0x1402F9F20` | The main unit panel: it lays out the unit's equipment rows, choosing each row's text id and icon from the equipped item. |
| [sub_140311CB0](../functions/sub_140311CB0.md) | `0x140311CB0` | Builds one icon-bearing UI element: it sets the classic item tile from the id, then positions and scales the element. |
| [sub_140315B10](../functions/sub_140315B10.md) | `0x140315B10` | Builds the elements of an item or effect panel: for ordinary items it sets the classic icon, and for one special category it allocates and fills a block of effect entries. |
| [sub_140333FE0](../functions/sub_140333FE0.md) | `0x140333FE0` | Refreshes the equip preview: it zeroes or fills the five candidate words, rebuilds the stat block, and compares each unit hand word with the block to mark changed rows. |
| [sub_1403343E4](../functions/sub_1403343E4.md) | `0x1403343E4` | Refreshes an item detail or help panel for the selected record and builds the help text id that the panel shows. |
| [sub_1403358FC](../functions/sub_1403358FC.md) | `0x1403358FC` | The interaction handler of the equipment screen: it reads the current slot and the selected unit, builds and sorts the candidate list, fills the row gadgets, and performs the equip, unequip and job actions the player ... |
| [sub_140336444](../functions/sub_140336444.md) | `0x140336444` | The equip screen's item click: it applies a list id to a slot, refreshes the stat block and posts the panel record. |
| [sub_140336664](../functions/sub_140336664.md) | `0x140336664` | Fills one row of the equipment list from the shared display list at a given index: the item, its price and count, and three boolean flags the row gadget shows. |
| [sub_1403368C0](../functions/sub_1403368C0.md) | `0x1403368C0` | Builds the equipment screen's candidate list for the current slot: it asks the list builder for the items of the slot's group, filters them through the saved equipment order, publishes the result to the UI and fills t... |
| [sub_140336B88](../functions/sub_140336B88.md) | `0x140336B88` | Rebuilds the equipment order list for the current slot after the player picks a sort: it sorts the candidate list by the chosen field, then copies the sorted result into the saved order list of that slot. |
| [sub_140338250](../functions/sub_140338250.md) | `0x140338250` | Builds the item menu's display list for one group and, for the hand groups, filters it through the first saved item order list. |
| [sub_14033DDFC](../functions/sub_14033DDFC.md) | `0x14033DDFC` | The cursor restore of the unit-pointer screens: the same job as sub_1402C0554, reading its saved entries (row, scroll, word) from the table at xmmword_143829E10. |
| [sub_14033E038](../functions/sub_14033E038.md) | `0x14033E038` | Resets the item menu's text-cell block to its default ids before the menu is filled. |
| [sub_14036BBFC](../functions/sub_14036BBFC.md) | `0x14036BBFC` | The shop/equip detail screen's message handler: it builds the detail record from the scratch unit, applies a picked row, and closes the screen. |
| [sub_14036C2A8](../functions/sub_14036C2A8.md) | `0x14036C2A8` | Applies a picked id to a slot, copies the scratch record's hand words into the candidate array and refreshes the detail. |
| [sub_14036C320](../functions/sub_14036C320.md) | `0x14036C320` | Recomputes the two-handed word from the five candidate words and renders the equip detail record. |
| [sub_14036E5DC](../functions/sub_14036E5DC.md) | `0x14036E5DC` | The world map's location-record builder (proposed name WorldMap_BuildLocationRecords; corrected 2026-11-19, it was first read as a shop screen refresh): for every location it accepts, it builds a 64-byte WorldMapLocat... |
| [sub_14036EE50](../functions/sub_14036EE50.md) | `0x14036EE50` | Builds the new-arrival notice's item lists: it collects up to 128 item ids into two parallel 16-bit arrays. |
| [sub_1403793DC](../functions/sub_1403793DC.md) | `0x1403793DC` | Re-opens a classic menu screen: it prepares the screen of the given kind (27, 28, 29, 43, 44 or 45), then pushes a kind-49 record holding that kind onto the menu screen stack, so ScreenReopen_Step rebuilds the screen ... |
| [sub_1403DABF0](../functions/sub_1403DABF0.md) | `0x1403DABF0` | Unloads the texture-part resource of a kind-2 record: builds its name from the UITextureParts scheme prefix (the word UITextureParts, a colon, two slashes), finds the resource in the owning widget and unregisters it. |
| [sub_1403DC1E8](../functions/sub_1403DC1E8.md) | `0x1403DC1E8` | Zeroes 16 bytes (a small bounds / rect struct) and returns the pointer after it. |
| [sub_1403DC8D0](../functions/sub_1403DC8D0.md) | `0x1403DC8D0` | Loads the numbered key texture part (a key icon) into a widget: builds its path, asks the widget to load it and returns the name. |
| [sub_1403DC998](../functions/sub_1403DC998.md) | `0x1403DC998` | Releases and zeroes a 40-byte texture-part auxiliary record (the object GUIFontSlots_AcquireTexturePart allocates). |
| [TabBar_ClearClick](../functions/TabBar_ClearClick.md) | `0x1402A9BD8` | Releases the pressed state of the four tab nodes: for each existing node (kind 5) calls sub_14040ABDC(node, 0) and stops its 'Click' state. |
| [TabBar_Select](../functions/TabBar_Select.md) | `0x1402A9944` | Selects a tab: puts the cursor / focus on tab 'index' of the bar's nodes and plays Active on it and Deactive on all the others. |
| [TabBar_SetTable](../functions/TabBar_SetTable.md) | `0x1402A9730` | Sets up a row of up to four tab / button nodes from a row of UI table 139: one title text id per tab, the count and a 'focusable' byte; then picks the layout state ButtonNN for the count and selects tab 0. |
| [Tavern_RumorsListInput](../functions/Tavern_RumorsListInput.md) | `0x14036F07C` | Input step of the tavern rumor list (table index 6): reads the list widget's result and opens the chosen rumor. |
| [Tavern_RumorTextWait](../functions/Tavern_RumorTextWait.md) | `0x14036F398` | Step of the rumor text screen (table index 8): runs the paged text widget, then returns to the rumor list. |
| [TavernRumourPage_Show](../functions/TavernRumourPage_Show.md) | `0x1401A041C` | Shows a rumour's text and picture. |
| [TitleMenu_AddEntry](../functions/TitleMenu_AddEntry.md) | `0x1401C43B4` | Appends one row to the title menu: sets the row's label by kind and stores the kind. |
| [TitleMenu_Build](../functions/TitleMenu_Build.md) | `0x1401C34B4` | Fills the title menu's rows according to the save state and the cleared flag, plays the matching layout state and shows the menu with the cursor on the row the agent asks for. |
| [TitleMenu_FocusCurrent](../functions/TitleMenu_FocusCurrent.md) | `0x1401C4318` | Focuses the current row; with none, the first row of kind 2 (Continue) when a save exists, else of kind 0 (New Game). |
| [TitleMenu_IdleTimeout](../functions/TitleMenu_IdleTimeout.md) | `0x1401C41B0` | The title menu's idle timeout (vtable slot 14): after 8000 ticks without input the agent is told to go back to the opening. |
| [TitleMenu_MoveCursor](../functions/TitleMenu_MoveCursor.md) | `0x1401C4154` | Moves the current row by a delta, wrapping when its flag is set, and focuses the row's button node. |
| [TitleMenu_SelectKind](../functions/TitleMenu_SelectKind.md) | `0x1401C4448` | Sets the current row to the first row of a given kind (-1 when there is none). |
| [TitleMenu_StampInput](../functions/TitleMenu_StampInput.md) | `0x1401C40C8` | Records the time of the last input for the idle timeout. |
| [Town_GetMapPosition](../functions/Town_GetMapPosition.md) | `0x14015CC00` | Returns a location's map position. |
| [UI_FrameUpdate](../functions/UI_FrameUpdate.md) | `0x1400E3B20` | Per-frame update of the UI: sets the UI frame time, runs a pending cursor restart, updates the agents (the hand's glide) and hands the frame time to the GUI core. |
| [UI_GetHelpSlotState](../functions/UI_GetHelpSlotState.md) | `0x1402BB604` | Decides whether the shared help-description slot is visible and returns a masked UI state word for the caller. |
| [UIAddon_CanTakeInput](../functions/UIAddon_CanTakeInput.md) | `0x1401D21D8` | Vtable slot 3: true unless the add-on is showing (+42) or hiding (+43). |
| [UIAddon_LoadByPath](../functions/UIAddon_LoadByPath.md) | `0x1401D1A3C` | Loads an add-on's layout from a path: a path starting with '#' names a widget, any other path is a layout file. |
| [UIAddon_LoadByRow](../functions/UIAddon_LoadByRow.md) | `0x1401D1A00` | Loads a screen's layout: row of UI table 24 (`uiaddon.nxd`), whose `path` names the layout file. |
| [UIAddon_OnEventBase](../functions/UIAddon_OnEventBase.md) | `0x1401D1F7C` | Base event handler every add-on's own handler calls first. |
| [UIAddonFFTOConfig_BindNodes](../functions/UIAddonFFTOConfig_BindNodes.md) | `0x140188878` | Node binding of the General Options screen (vtable slot 4): picks the tabs by mode and binds Config, TabAll, ConfigList, SelectList, TextArea and ConfirmWindowAll. |
| [UIAddonFFTOConfig_Ctor](../functions/UIAddonFFTOConfig_Ctor.md) | `0x14018853C` | Constructor of the General Options screen add-on (3416 bytes): sets its vtable and builds the gadgets. |
| [UIAddonFFTOConfig_DeletingDtor](../functions/UIAddonFFTOConfig_DeletingDtor.md) | `0x1401886CC` | Vtable slot 0 of the General Options add-on: runs the destructor body and frees the object. |
| [UIAddonFFTOConfig_Dtor](../functions/UIAddonFFTOConfig_Dtor.md) | `0x140188700` | Destructor body of the General Options add-on: frees its vectors and gadgets. |
| [UIAddonFFTOConfig_OnClose](../functions/UIAddonFFTOConfig_OnClose.md) | `0x140188FA4` | On-close handler of the General Options screen (vtable slot 5): asks for a settings save and, after a display change, restarts the boot sequence. |
| [UIAddonFFTOConfig_OnEvent](../functions/UIAddonFFTOConfig_OnEvent.md) | `0x14018A344` | Node event handler of the General Options screen (vtable slot 2): draws rows, tracks the cursor, applies switches, sliders and tab clicks. |
| [UIAddonFFTOConfig_OnInput](../functions/UIAddonFFTOConfig_OnInput.md) | `0x1401892A8` | Input handler of the General Options screen (vtable slot 12): Back, restore defaults, tabs, value steps, then the row list's own input. |
| [UIAddonFFTOConfig_OnShown](../functions/UIAddonFFTOConfig_OnShown.md) | `0x14018A31C` | Slot 7 of the General Options screen: after it is shown the row list focuses its cursor row and the shown flag is set. |
| [UIAddonFFTOConfig_RefreshRowTexts](../functions/UIAddonFFTOConfig_RefreshRowTexts.md) | `0x1401890E0` | Vtable slot 13 of the General Options screen: sets every row's Title text again from its ConfigItem. |
| [UIAddonFFTOConfig_Update](../functions/UIAddonFFTOConfig_Update.md) | `0x140189D54` | Per-frame update of the General Options screen (vtable slot 14): queued dialogs, the display change states, the render device check and the sync of shown values with the game settings. |
| [UIAddonFFTOEvent_Ctor](../functions/UIAddonFFTOEvent_Ctor.md) | `0x140135A00` | Creates the four addons owned by the event UI agent, including the pause overlay. |
| [UIAddonFFTOTitle_Create](../functions/UIAddonFFTOTitle_Create.md) | `0x1401CB9B4` | Allocates and builds the title menu add-on (the screen of uiaddon row 244) and attaches it to the title agent. |
| [UIAddonFFTOTitle_Dtor](../functions/UIAddonFFTOTitle_Dtor.md) | `0x1401C3E64` | Destructor of the title menu add-on: puts the base class's vtables back and frees the 240 bytes. |
| [UIAddonFFTOTitle_OnEvent](../functions/UIAddonFFTOTitle_OnEvent.md) | `0x1401C4228` | The title add-on's event handler (vtable slot 2) for the nodes tagged 121 (the six menu buttons). |
| [UIAddonFFTOTitlePlaymode_Create](../functions/UIAddonFFTOTitlePlaymode_Create.md) | `0x1401CBA60` | Creates the second add-on of `UITitle_ShowMenu`: the play mode screen (uiaddon row 245, `ffto_title_playmode.uib`). |
| [UIAddonFingerCursor_Bind](../functions/UIAddonFingerCursor_Bind.md) | `0x1401D31E8` | Finds the parts of the cursor widget once it is loaded and resets the glide (vtable slot 4 of the addon). |
| [UIAddonFingerCursor_FreezePose](../functions/UIAddonFingerCursor_FreezePose.md) | `0x1401D3550` | Plays the main component's Loop state to its last frame and then stops every state of that component (the bob ends). |
| [UIAddonFingerCursor_PlayDefault](../functions/UIAddonFingerCursor_PlayDefault.md) | `0x1401D34B4` | Plays the Default pose state on the Hand component (vtable slot 6 of the addon). |
| [UIAddonFingerCursor_PlayLoop](../functions/UIAddonFingerCursor_PlayLoop.md) | `0x1401D3148` | (Re)starts the idle bob of the finger cursor: shows the cursor widget and plays the Loop state of its main component from frame 0 with looping switched on. |
| [UIAddonFingerCursor_ResetGlide](../functions/UIAddonFingerCursor_ResetGlide.md) | `0x1401D351C` | Makes the next placement of the cursor instant instead of a step (vtable slot 9 of the addon). |
| [UIAddonFingerCursor_ResetPose](../functions/UIAddonFingerCursor_ResetPose.md) | `0x1401D3694` | Takes the glove out of a pose, back to Default, and restarts the bob. |
| [UIAddonFingerCursor_SetPose](../functions/UIAddonFingerCursor_SetPose.md) | `0x1401D35AC` | Gives the glove one of its poses: stops the bob and plays the pose's state on the Hand component. |
| [UIAgent_AttachAddon](../functions/UIAgent_AttachAddon.md) | `0x1401D16C4` | Links a screen (add-on) to its agent and gives it an id. |
| [UIAgent_DetachAddon](../functions/UIAgent_DetachAddon.md) | `0x1401D183C` | Removes an add-on from its agent's list, hides it and calls its slot 5. |
| [UIAgent_IsActive](../functions/UIAgent_IsActive.md) | `0x1401D15B4` | Base virtual slot 2: true while the agent's add-on list is non-empty. |
| [UIAgent_SetState](../functions/UIAgent_SetState.md) | `0x1401CA59C` | Changes a UI agent's state machine: runs the current handler with phase 2 (exit), stores the new state, selects the handler for that state, and runs the new handler with phase 0 (enter). |
| [UIAgentCursor_Hide](../functions/UIAgentCursor_Hide.md) | `0x1401D2F24` | Hides the finger cursor: cancels a pending show, stops every state of the cursor widget's main component and hides the widget. |
| [UIAgentCursor_PopRequest](../functions/UIAgentCursor_PopRequest.md) | `0x1401D2A10` | Takes the last cursor request off the agent's request stack and applies it: mode, rest offset, static flag, show or hide. |
| [UIAgentCursor_SetStatic](../functions/UIAgentCursor_SetStatic.md) | `0x1401D2E0C` | Switches the finger cursor between its animated mode and a static mode in which it neither bobs nor glides. |
| [UIAgentCursor_Show](../functions/UIAgentCursor_Show.md) | `0x1401D2EF4` | Asks the finger cursor to appear and to restart its Loop animation. |
| [UIAgentFFTOSaveLoad_Ctor](../functions/UIAgentFFTOSaveLoad_Ctor.md) | `0x140182B38` | Builds the save/load UI agent: the base agent front, its vtable, two embedded state machines, five 264-byte summary slots, the embedded save-data handler and the lock and queue that carry save errors back to the screen. |
| [UIAgentFFTOSaveLoad_Update](../functions/UIAgentFFTOSaveLoad_Update.md) | `0x140182EDC` | The agent's per-frame virtual (vtable slot 1): it advances the saving overlay, drains queued save errors, and delivers phase 1 to the current agent state handler unless a save-error prompt is up. |
| [UIAgentFFTOSystem_Ctor](../functions/UIAgentFFTOSystem_Ctor.md) | `0x140181C94` | Constructor of the System agent (1472 bytes), entry 37 of the agent manager's array. |
| [UIAgentFFTOSystem_FreeAddons](../functions/UIAgentFFTOSystem_FreeAddons.md) | `0x140181DD0` | Frees the add-ons at +1448 / +1456 / +1464. |
| [UIAgentFFTOSystem_OnAddonEvent](../functions/UIAgentFFTOSystem_OnAddonEvent.md) | `0x140181ED0` | Agent vtable slot 6, the sink of its add-ons' events. |
| [UIAgentFFTOSystem_OpenConfig](../functions/UIAgentFFTOSystem_OpenConfig.md) | `0x140182478` | Makes the General Options add-on and starts the agent's open state. |
| [UIAgentFFTOSystem_ReturnToMenu](../functions/UIAgentFFTOSystem_ReturnToMenu.md) | `0x140182378` | Frees the config add-ons and shows the system menu again. |
| [UIAgentFFTOSystem_StateCloseConfig](../functions/UIAgentFFTOSystem_StateCloseConfig.md) | `0x14018290C` | State handler that closes the General Options screen. |
| [UIAgentFFTOSystem_StateExitGame](../functions/UIAgentFFTOSystem_StateExitGame.md) | `0x1401827E4` | State handler that exits the game: UI state 13 fade, then the application's quit request byte is set. |
| [UIAgentFFTOSystem_StateOpenConfig](../functions/UIAgentFFTOSystem_StateOpenConfig.md) | `0x140182860` | State handler that opens the General Options screen. |
| [UIAgentFFTOTitle_OnAddonEvent](../functions/UIAgentFFTOTitle_OnAddonEvent.md) | `0x1401C32D0` | The agent's sink (slot 6) for the events of its three add-ons: the menu, the play mode screen and the saving screen. |
| [UIAgentFFTOTitle_Tick](../functions/UIAgentFFTOTitle_Tick.md) | `0x1401C2D20` | Per-frame update of the title agent (vtable 0x14070A5B0 slot 1). |
| [UIAgentFFTOTitle_Update](../functions/UIAgentFFTOTitle_Update.md) | `0x1401C2D60` | The title agent's state machine (state byte at +88): builds the menu, runs the fade-driven transitions and starts the loads the menu rows choose. |
| [UIAgentManager_CreateAgents](../functions/UIAgentManager_CreateAgents.md) | `0x1401CF724` | The one-shot agent factory: allocates and constructs 54 UI agents in a fixed slot order, appends each pointer to the manager's agent vector and marks the manager ready. |
| [UIAgentManager_Ctor](../functions/UIAgentManager_Ctor.md) | `0x1401CF3DC` | Builds the singleton UI agent manager: stores its module vtable and allocator objects, starts the agent, addon, font-slot and queued-event containers empty, then calls UIAgentManager_CreateAgents to fill the agent vec... |
| [UIAnim_ApplyComponentTrack](../functions/UIAnim_ApplyComponentTrack.md) | `0x1403F7AC0` | Applies a state track aimed at the component itself (target kind 4002, property tags >= 5031) as an animated component-effect property. |
| [UIAnim_ApplyTrack](../functions/UIAnim_ApplyTrack.md) | `0x1403F6FC0` | Converts one state track aimed at a node (target kind 4001, property tags 5001..5030) into a queued property animation on that node. |
| [UIAnim_Curve](../functions/UIAnim_Curve.md) | `0x14040242C` | Easing curve evaluator for keyframes: maps the position t within a key interval (0 to 1) to the blend factor of that interval. |
| [UiAnim_DrawFrame](../functions/UiAnim_DrawFrame.md) | `0x140342070` | Advances one widget animation by a frame and draws the sprite pieces of the frame set the current step names. |
| [UIAnim_InterpToCurve](../functions/UIAnim_InterpToCurve.md) | `0x1403F8818` | Maps a UIB keyframe interpolation id to the easing curve id used by UIAnim_Curve: n -> n + 1 for 0 to 35, anything else -> 2 (linear). |
| [UIAnim_LerpColor](../functions/UIAnim_LerpColor.md) | `0x1404022A8` | Per-channel linear blend of two packed RGBA colours with truncation and clamping to 0..255. |
| [UIAnim_PlayStateTracks](../functions/UIAnim_PlayStateTracks.md) | `0x1403F6EA0` | Converts the tracks of one UIB state record (a timeline) into the runtime state object when a component is built: frame count, loop byte, absolute flag, key tracks and entries. |
| [UIAnim_SampleColorTrack](../functions/UIAnim_SampleColorTrack.md) | `0x140408328` | Samples a packed-RGBA colour keyframe track at a frame: the key before t blends to the next with its easing curve through UIAnim_LerpColor. |
| [UIAnim_SampleFloatTrack](../functions/UIAnim_SampleFloatTrack.md) | `0x140407B14` | Samples a float keyframe track at time t with the easing curve of the key before t. |
| [UIAnim_SampleInt2Track](../functions/UIAnim_SampleInt2Track.md) | `0x1404080C4` | Same as UIAnim_SampleFloatTrack for a track of integer pairs (position and size). |
| [UIAnim_SampleIntTrack](../functions/UIAnim_SampleIntTrack.md) | `0x140408218` | Samples an integer keyframe track at a (float) frame with the easing curve of the key before it. |
| [UIAnim_StoreKey](../functions/UIAnim_StoreKey.md) | `0x1403F8708` | Stores one keyframe of a UIB state track into the state's runtime key track for a target and property type. |
| [UIColor_CombineSlot](../functions/UIColor_CombineSlot.md) | `0x1403EE35C` | Colour combiner used by GUITextNode_Draw for each of the four font palette layers: picks or multiplies the draw colour, the node's per-layer colour and the UIFontSet row colour according to a mode. |
| [UICommand_Append](../functions/UICommand_Append.md) | `0x1403C4794` | Appends one 64-byte command record (type dword, then the draw state at +8) to the per-thread command block and reserves its vertex range. |
| [UICommand_ExecuteBatches](../functions/UICommand_ExecuteBatches.md) | `0x1403C1004` | Walks the frame sorted command list and draws it in batches, flushing a batch whenever the pipeline/state key changes. |
| [UICommand_MergeSortRange](../functions/UICommand_MergeSortRange.md) | `0x1403AE788` | Recursive stable merge sort over 16-byte records [lo, hi] keyed by the first qword (unsigned), ping-ponging between two buffers, with insertion sort for short ranges. |
| [UIDraw_SetStateFromSlot](../functions/UIDraw_SetStateFromSlot.md) | `0x1403DFC34` | Fills the draw-state flag word from a texture slot record: texture pointer, blend/permutation bits and the SDF flag. |
| [UIDrawState_Copy](../functions/UIDrawState_Copy.md) | `0x1403C46A4` | Copies the 48-byte draw state with the masks the command format keeps. |
| [UIFontSetRow_Default](../functions/UIFontSetRow_Default.md) | `0x1403DCAD0` | Fills an 80-byte UIFontSet row with engine defaults and returns the row pointer. |
| [UIGadget_GetOwnerWidget](../functions/UIGadget_GetOwnerWidget.md) | `0x1402A7A84` | Returns the owning widget of the gadget's owner node: node = *(g + 8); returns node + 496 (0 when there is no node). |
| [UIGadgetFFTORadioButtonMenu_Ctor](../functions/UIGadgetFFTORadioButtonMenu_Ctor.md) | `0x1402AD5BC` | Constructs the 304-byte radio-button menu gadget used by the battle command page (Move / Abilities / Wait / Status) and by other UIB screens. |
| [UIGadgetFFTORadioButtonMenu_Event](../functions/UIGadgetFFTORadioButtonMenu_Event.md) | `0x1402AD7F8` | Maintains the radio menu's selected/hover index from the UI event stream. |
| [UIGadgetFFTOVScrollText_ApplyScroll](../functions/UIGadgetFFTOVScrollText_ApplyScroll.md) | `0x1402AAD30` | Applies the scroll offset: moves the text node (g+40) to y = -scroll and re-centres the marker node (g+160) on the 'ScrollMark' part of the owner. |
| [UIGadgetFFTOVScrollText_HandleScrollInput](../functions/UIGadgetFFTOVScrollText_HandleScrollInput.md) | `0x1402AB0B8` | Mouse wheel / stick scrolling of a scroll-text gadget: moves the scroll bar by 20 units per wheel notch or by the stick axis; returns 1 when it scrolled. |
| [UIGadgetFFTOVScrollText_Refit](../functions/UIGadgetFFTOVScrollText_Refit.md) | `0x1402AB174` | After the text of a scroll-text gadget changed: lays the text out, sizes the text node to its laid-out height and sets up the scroll bar (range = text height, page = viewport height, position 0, bar visible only when ... |
| [UIGuide_GetKey](../functions/UIGuide_GetKey.md) | `0x1400EB70C` | Returns the guide key currently shown. |
| [UIGuide_Set](../functions/UIGuide_Set.md) | `0x1400EB65C` | Sets the guide bar's key and sub-row mask. |
| [UIGuide_Show](../functions/UIGuide_Show.md) | `0x1400EB5F4` | Shows or hides the guide bar (calls the guide agent's 0x14013C740). |
| [UIImage_DrawTiled](../functions/UIImage_DrawTiled.md) | `0x1403E0E80` | Fills a node rectangle with copies of a texture part, optionally mirroring every second column and row, emitting one quad (4 vertices of 24 bytes) per cell. |
| [UIImage_ResolvePart](../functions/UIImage_ResolvePart.md) | `0x1403E95E0` | Finds the texture slot and part rectangle for an Image node texture reference and part index. |
| [UIImageNode_Draw](../functions/UIImageNode_Draw.md) | `0x1403E9C48` | Draws one Image node: resolves its texture part, builds the node's colour, flips and draw state, then calls the draw routine its fill type selects. |
| [UILauncher_OnMenuAction](../functions/UILauncher_OnMenuAction.md) | `0x1401B924C` | The mode select screen's button handler. |
| [UIListGadget_Bind](../functions/UIListGadget_Bind.md) | `0x14028C5C4` | Binds a list gadget to its node. |
| [UIListGadget_Ctor](../functions/UIListGadget_Ctor.md) | `0x14028C458` | Constructor of the row list gadget (General Options +1744). |
| [UIListGadget_IsAnimating](../functions/UIListGadget_IsAnimating.md) | `0x14028D44C` | True while a 'Show', 'Slide_left' or 'Slide_right' state is running on the gadget's node +16, its list +24 or a visible slot component. |
| [UIListGadget_OnInput](../functions/UIListGadget_OnInput.md) | `0x14028E188` | Input of a list gadget: up / down / left / right moves of the cursor. |
| [UIListGadget_RefreshVisible](../functions/UIListGadget_RefreshVisible.md) | `0x14028DCA4` | Posts event 0x1E (draw row) for every visible row. |
| [UIListGadget_RestoreFocus](../functions/UIListGadget_RestoreFocus.md) | `0x14028DAEC` | Focuses the list's cursor row again. |
| [UIListGadget_SetCount](../functions/UIListGadget_SetCount.md) | `0x14028D7BC` | Sets the row count, scrolls to the top and redraws. |
| [UIListGadget_SetCursor](../functions/UIListGadget_SetCursor.md) | `0x14028D8F4` | Moves the cursor to a row and focuses the row. |
| [UIListGadget_Show](../functions/UIListGadget_Show.md) | `0x14028D038` | Plays the list's Show state. |
| [UIListGadget_StepColumn](../functions/UIListGadget_StepColumn.md) | `0x14028E4B0` | Pages or steps a column of the list. |
| [UIListGadget_StepRow](../functions/UIListGadget_StepRow.md) | `0x14028E55C` | Steps the list's cursor row. |
| [UIMenuFunction_OnInput](../functions/UIMenuFunction_OnInput.md) | `0x1402AB4D8` | The shared menu input of the `UIFFTOMenuFunctionBase` part (the title menu's part at +48). |
| [UIMessageBanner_Show](../functions/UIMessageBanner_Show.md) | `0x140111D20` | Shows a message in the centre banner: resolves the banner's 'Title' text node, fills the format arguments and stores the template text, then starts the banner state selected by the dword at banner+80. |
| [UIName_Assign](../functions/UIName_Assign.md) | `0x1403D87F4` | Copy-assignment of an interned name handle: takes a reference on src's entry, drops dst's old reference and copies pointer and id. |
| [UIName_Intern](../functions/UIName_Intern.md) | `0x1403D8A24` | Interns a UI name string: finds or adds it in the name table and fills `outKey` with its key id, adding one reference. |
| [UIName_Key](../functions/UIName_Key.md) | `0x1403D87BC` | Builds a lookup key for a node/state name: out->str = name, out->id = interned id (via the global name table qword_143CDA2A0). |
| [UIName_KeyIndexed](../functions/UIName_KeyIndexed.md) | `0x1403D8E5C` | Builds the name key for base, or 'base#index' when index is non-zero, via UIName_Key. |
| [UIName_ReleaseKey](../functions/UIName_ReleaseKey.md) | `0x1403D8D1C` | Drops one reference to an interned UI name; frees the string and shrinks the bucket when the count reaches zero. |
| [UIName_SetKey](../functions/UIName_SetKey.md) | `0x1403D8870` | Re-points a name handle at the interned entry for str (adds a reference to the new entry, drops the old one). |
| [UiNames_InstallCoreNames](../functions/UiNames_InstallCoreNames.md) | `0x1403D5934` | Registers the 43 core UI event and part names in the UI name table and loads the font data of the current text language. |
| [UiPage_ChoicePromptInput](../functions/UiPage_ChoicePromptInput.md) | `0x14036FB14` | Input step of a two-choice prompt page (entry 15 of tbl_UiScreenInputSteps, the page dispatcher's table at 0x140681400): moves a two-position cursor, and on confirm or cancel pops the page's records and either runs a ... |
| [UIPartRef_GetResource](../functions/UIPartRef_GetResource.md) | `0x1403DCA6C` | Returns the resource record of a part reference: the first element of its resource list, or a table entry by id, or the fallback pointer. |
| [UIPartRef_GetTextureSize](../functions/UIPartRef_GetTextureSize.md) | `0x1403DCA04` | Writes the pixel width and height of the texture a part reference points at (1 x 1 when it has none); the divisor that turns texel rectangles into UVs. |
| [UIPosFollow_SetTarget](../functions/UIPosFollow_SetTarget.md) | `0x1402AB394` | Starts a position follow: target = base offset (f+40 / f+44) + pos (x, y); records the follower node's current position as the start. |
| [UIPosFollow_Snap](../functions/UIPosFollow_Snap.md) | `0x1402AB3F0` | Finishes a position follow at once: puts the follower node at the target (int casts) and makes current = target. |
| [UIRender_AppendCommand](../functions/UIRender_AppendCommand.md) | `0x1403B83FC` | Appends a type-32 command to the calling thread's UIContext, tagged with the current layer; also marks the layer used. |
| [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md) | `0x1403AE1A0` | Programs the graphics pipeline from a draw state: shader permutation, blend/raster bits, texture, samplers and the cSDF constant buffer. |
| [UIRender_ClearLayerFlags](../functions/UIRender_ClearLayerFlags.md) | `0x1403B8574` | When a2 == 0, resets the per-frame bookkeeping of all 512 layer records and the active layer counter. |
| [UIRender_CreateBuffers](../functions/UIRender_CreateBuffers.md) | `0x1403AD990` | Allocates the UI renderer's command and vertex buffers and its 32 UIContext objects, and looks up the cUIRender / cUIRenderRemap / cSDF constant buffers and the g_Sampler / tTexture0 slots. |
| [UIRender_FlushBatch](../functions/UIRender_FlushBatch.md) | `0x1403AE0F0` | Issues one batched draw: sets the draw-call type bits of the thread state for the command kind, applies the draw state and submits the range. |
| [UIRender_GetThreadContext](../functions/UIRender_GetThreadContext.md) | `0x1403B8288` | Returns the UIContext slot (80 bytes) belonging to the calling thread, chosen by the thread state's position in the thread-state array. |
| [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md) | `0x1403B7188` | Loads the five UI shader containers and creates the UI renderer, its command ring, the SMAA / down-sampling helpers and their constant buffers. |
| [UIRender_QueueImageDraw](../functions/UIRender_QueueImageDraw.md) | `0x1403B84EC` | Appends a type-34 (image) command that carries a copy of the draw state, flagging the layer used and recording whether the draw state asks for a flag at bit 12. |
| [UIResourceHandle_Delete](../functions/UIResourceHandle_Delete.md) | `0x1403D99C0` | Scalar deleting destructor (vtable method) of the UIResourceHandle class: resets the vtable, runs the base destructor and frees the 104-byte object when bit 0 of flags is set. |
| [UIResourceHandle_New](../functions/UIResourceHandle_New.md) | `0x1403D9A00` | Factory: allocates a 104-byte UIResourceHandle through the allocator object at qword_143CDAA80 (+8) and constructs it. |
| [UISaveLoad_OnEvent](../functions/UISaveLoad_OnEvent.md) | `0x1401833C4` | Maps the save/load screen's event numbers 0..8 to state changes, stored selection values and pause-style prompts. |
| [UISaveLoad_Open](../functions/UISaveLoad_Open.md) | `0x140183580` | Opens the save/load screen: it selects the load mode, starts the screen's music transition, fades the UI to state 9, and sets the save/load agent's own state machine to state 1. |
| [UiScript_OpAdvanceOpening](../functions/UiScript_OpAdvanceOpening.md) | `0x140329FEC` | Slot 22: advances the window opening stage. |
| [UiScript_OpDrawIconCell](../functions/UiScript_OpDrawIconCell.md) | `0x140327CF4` | Slot 6: draws one picture cell whose source rectangle comes from a row callback. |
| [UiScript_OpDrawLine](../functions/UiScript_OpDrawLine.md) | `0x140327C3C` | Slot 7: queues a line between two points. |
| [UiScript_OpDrawLineRel](../functions/UiScript_OpDrawLineRel.md) | `0x140327C94` | Slot 28: queues a line from a point by an offset. |
| [UiScript_OpDrawNumber](../functions/UiScript_OpDrawNumber.md) | `0x140328920` | Slots 13, 25, 26 and 27: draws a number or a gauge for a value supplied by a row callback. |
| [UiScript_OpDrawWindow](../functions/UiScript_OpDrawWindow.md) | `0x140327DAC` | Slot 0: draws a bordered window of a given size and fills its inside. |
| [UiScript_OpDrawWindowOpening](../functions/UiScript_OpDrawWindowOpening.md) | `0x140328398` | Slot 18: draws a window that opens over a few redraws, then runs UiScript_OpDrawWindow on the same record. |
| [UiScript_OpFillRect](../functions/UiScript_OpFillRect.md) | `0x140327AF0` | Slot 3: queues a flat-coloured rectangle. |
| [UiScript_OpFillTiles](../functions/UiScript_OpFillTiles.md) | `0x140328490` | Slot 17: fills a rectangle with 16-pixel tiles of one texture cell. |
| [UiScript_OpIf](../functions/UiScript_OpIf.md) | `0x140327954` | Slot 1: runs the next records only while a row callback accepts the current row, otherwise skips them. |
| [UiScript_OpIfElse](../functions/UiScript_OpIfElse.md) | `0x140327A04` | Slot 2: as slot 1 with an else branch. |
| [UiScript_OpQueueRect](../functions/UiScript_OpQueueRect.md) | `0x140329F4C` | Slot 20: queues a rectangle from the record when no window animation is running. |
| [UiScript_OpQueueScreenRect](../functions/UiScript_OpQueueScreenRect.md) | `0x140329FB0` | Slot 21: queues the fixed screen rectangle of slot 19 while no window animation is running. |
| [UiScript_OpQueueScreenRectOnce](../functions/UiScript_OpQueueScreenRectOnce.md) | `0x140329EFC` | Slot 19: after a window animation, queues a fixed screen rectangle once and clears the animating byte. |
| [UiScript_OpScrollList](../functions/UiScript_OpScrollList.md) | `0x140329548` | Slot 16: draws a scrolling list: repeats the records that follow once per visible row, reads the up and down input, animates the scroll and draws the marks, thumb and cursor. |
| [UiScript_OpSetBlendFlag](../functions/UiScript_OpSetBlendFlag.md) | `0x140328878` | Slot 14: sets the semi-transparency word passed to the following primitives. |
| [UiScript_OpSetDrawMode](../functions/UiScript_OpSetDrawMode.md) | `0x14032888C` | Slot 24: queues a draw-mode change: a blend mode from +2 and 3. |
| [UiScript_OpSetPageWord](../functions/UiScript_OpSetPageWord.md) | `0x1403287FC` | Slot 12: composes the texture-page and blend attribute word of the following cells. |
| [UiScript_OpSetPaletteWord](../functions/UiScript_OpSetPaletteWord.md) | `0x140328734` | Slot 9: sets the palette word of the following cells. |
| [UiScript_OpSetPaletteWordAlt](../functions/UiScript_OpSetPaletteWordAlt.md) | `0x140328780` | Slot 10: as slot 9 with a second operand set for the alternate-value flag. |
| [UiScript_OpSetPriority](../functions/UiScript_OpSetPriority.md) | `0x14032890C` | Slot 15: sets the draw priority word. |
| [UiScript_OpSetTint](../functions/UiScript_OpSetTint.md) | `0x1403288C8` | Slot 11: sets the tint colour of the following cells. |
| [UiScript_Run](../functions/UiScript_Run.md) | `0x1403278EC` | Runs one UI script: the byte-coded layout and behaviour program of a list or panel screen. |
| [UIState_EndTransition](../functions/UIState_EndTransition.md) | `0x1401DDA5C` | Ends the UI fade state given (fade +24 = 0). |
| [UITable_GetRow](../functions/UITable_GetRow.md) | `0x1403DBD60` | Returns the in-memory row of an nxd table by table id and row index (null when the table or row is missing). |
| [UITable_GetRowByIndex](../functions/UITable_GetRowByIndex.md) | `0x1403DBDF4` | Returns the index-th sub-row of a key in a multi-row UI table, or null. |
| [UITable_GetRowByKeys](../functions/UITable_GetRowByKeys.md) | `0x1403DBCE4` | The row of (key1, key2) of a double-keyed table (for a triple-keyed table: the first leaf of child (key1, key2)), looked up by table id; its data pointer, or null. |
| [UITable_GetRowCount](../functions/UITable_GetRowCount.md) | `0x1403DBC20` | Number of sub-rows of a key in a multi-row UI table (the count field of the key's entry), or 0 when the table or key does not exist. |
| [UITexturePath_Select4k](../functions/UITexturePath_Select4k.md) | `0x1403DB0EC` | Copies a texture path into out (255 characters at most) and, when the path contains '_2k_', changes it to '_4k_'; returns true when the path contains _2k_ or _4k_. |
| [UITitle_OnMenuAction](../functions/UITitle_OnMenuAction.md) | `0x1401C3710` | Carries out the row the player chose on the title menu. |
| [UITitle_OpenPlayMode](../functions/UITitle_OpenPlayMode.md) | `0x1401C3968` | Kind 0 (New Game): starts UI state 19 and agent state 2, after which the agent hides the menu and shows the play mode screen. |
| [UITitle_ShowMenu](../functions/UITitle_ShowMenu.md) | `0x1401C2BCC` | Creates the title agent's three add-ons and builds the menu. |
| [UITitle_ShowPlayMode](../functions/UITitle_ShowPlayMode.md) | `0x1401C3CE0` | Hides the title menu add-on and shows the play mode add-on. |
| [UITitle_StartNewGamePlus](../functions/UITitle_StartNewGamePlus.md) | `0x1401C3A28` | Kind 1 (text 2226, New Game +): fades out and sets agent state 0x201, only when no save request is pending. |
| [UITitleMenu_BindNodes](../functions/UITitleMenu_BindNodes.md) | `0x1401C3EB0` | The title menu add-on's node binding (vtable slot 4): finds the TitleEnhanced and Menu nodes and the six MenuButton nodes, and tags them for the event handler. |
| [WindowPattern_Build](../functions/WindowPattern_Build.md) | `0x140332330` | Builds the pixel pattern of a legacy window frame row by row and, in mode 2, uploads it to VRAM. |
| [WindowPattern_FillRow](../functions/WindowPattern_FillRow.md) | `0x1403324F8` | Fills one row of a window frame pattern from a six-word template. |
| [WindowRect_AnimateCurve](../functions/WindowRect_AnimateCurve.md) | `0x1402DDFE8` | Opens or closes a window by moving two rectangles along one of the five animation step lists. |
| [WorldMap_ScreenInput](../functions/WorldMap_ScreenInput.md) | `0x1402D0EE0` | Input step of the world map screen (table index 0): moves between locations, opens a town menu or starts an encounter. |
| [WorldMapBaseScreen_Open](../functions/WorldMapBaseScreen_Open.md) | `0x1401582D0` | Opens a location's own world-map screen file. |
| [WorldMapLocationPanel_Fill](../functions/WorldMapLocationPanel_Fill.md) | `0x1401607D4` | Fills the world-map location info panel from a location record. |
| [WorldMapLocationPanel_Init](../functions/WorldMapLocationPanel_Init.md) | `0x14015F730` | Binds the location panel's nodes (worldmap_base_info.uib) once: the list, the tab buttons, the field and town info, and one node per item category. |
| [WorldMapNode_PlayTexChange](../functions/WorldMapNode_PlayTexChange.md) | `0x140158E30` | Plays the texture-change state of a location's base node. |
| [WorldMapProgress_GetObjectiveCaption](../functions/WorldMapProgress_GetObjectiveCaption.md) | `0x14015E0FC` | Returns the world-map objective line for a progress row. |
| [WorldMapRoute_Refresh](../functions/WorldMapRoute_Refresh.md) | `0x14015B3AC` | Shows or hides one route on the world map and sets its grey state. |
| [WorldMapRoute_SetGrey](../functions/WorldMapRoute_SetGrey.md) | `0x14015DFCC` | Plays a route's grey or default colour state. |
| [WorldMapRoute_StartGrow](../functions/WorldMapRoute_StartGrow.md) | `0x140157E88` | Starts the grow animation of a route between two locations. |
| [WorldMapRouteGrow_OnState](../functions/WorldMapRouteGrow_OnState.md) | `0x140162344` | Plays the state of the route-grow effect. |
| [WorldMapScreen_BindNodes](../functions/WorldMapScreen_BindNodes.md) | `0x140159304` | Binds the world-map screen's nodes: the widget's root, MapAll with its Route and Bases groups, the 48 base/point nodes, and each base's TextBoardMapName title. |
| [WorldMapScreen_ScrollToProgress](../functions/WorldMapScreen_ScrollToProgress.md) | `0x14015DAE4` | Computes the map scroll target of the current progress row. |
| [WorldMapScreen_SetProgress](../functions/WorldMapScreen_SetProgress.md) | `0x14015A754` | Stores the current story progress on the world-map screen and shows the objective line. |
| [WorldMapScreen_SetRoute](../functions/WorldMapScreen_SetRoute.md) | `0x140157D74` | Records the route being opened on the world-map screen. |
| [WorldMenu_AllocOverlayRecord](../functions/WorldMenu_AllocOverlayRecord.md) | `0x1403426F8` | Takes the next 36-byte world-menu record from a fixed array, registers it and returns its index. |
| [WorldMenu_AllocWindowRecord](../functions/WorldMenu_AllocWindowRecord.md) | `0x14034275C` | Takes the next 56-byte world-menu window record, registers it and returns its index. |
| [WorldMenu_RunTopCloseHook](../functions/WorldMenu_RunTopCloseHook.md) | `0x1402D0488` | Calls the second-table hook of the world-menu control on top of the control stack (V: callers run it right after decrementing the stack depth; I: it is the counterpart of the open hook). |
| [WorldMenu_RunTopOpenHook](../functions/WorldMenu_RunTopOpenHook.md) | `0x1402D0458` | Calls the first-table hook of the world-menu control on top of the control stack (V: callers such as Errand_BoardInput run it right after decrementing the stack depth; I: the hook re-initialises the control that becom... |
| [WorldMenu_SetFade](../functions/WorldMenu_SetFade.md) | `0x1402CD714` | Requests a UI fade state and then sets the world-menu mode word. |
| [WorldMenu_SetRecordsFrozen](../functions/WorldMenu_SetRecordsFrozen.md) | `0x1402CCC38` | Sets or clears bit 3 (value 8) of the flag word of every registered world-menu record: set when the argument is 0, cleared otherwise. |
| [ZodiacStone_AnyMet](../functions/ZodiacStone_AnyMet.md) | `0x14016BC30` | Tells whether any ZodiacStone row has its user_situation met. |
| [ZodiacStone_AnyMetAndNew](../functions/ZodiacStone_AnyMetAndNew.md) | `0x14016BDB8` | Tells whether any ZodiacStone row is met and still carries its new mark. |
| [ZodiacStone_ClearNewMarks](../functions/ZodiacStone_ClearNewMarks.md) | `0x14016BF68` | Clears the new mark of every ZodiacStone row that is met. |
| [ZodiacStone_FillDetail](../functions/ZodiacStone_FillDetail.md) | `0x14016E218` | Fills the stone's detail page (icons, name, description, Clear mark). |
| [ZodiacStone_FillTip](../functions/ZodiacStone_FillTip.md) | `0x14016D72C` | Fills the stone's tip (icon, name, summary). |
| [ZodiacStoneBoard_Setup](../functions/ZodiacStoneBoard_Setup.md) | `0x14016C414` | Sets up the Zodiac Stone board: for each of the 13 stones picks the row to show, plays the stone's state and sets its name. |

## Structures (138)

| Name | Size (bytes) | Summary |
|---|---|---|
| [AvailabilityFlag](../structs/AvailabilityFlag.md) | 1 | One row of the GridAvailableTemplate table. |
| [BgmModeScreen](../structs/BgmModeScreen.md) |  | The music player screen (UIAddonFFTOBGMMode): its two track lists and the state of the list and title language. |
| [CharGridCell](../structs/CharGridCell.md) | 1 | One row of the CharGridOrder table. |
| [ClassicSubtitleStepper](../structs/ClassicSubtitleStepper.md) |  | The stepper of the classic-movie subtitle window (ClassicSubtitles_Step): the current layout state and the keep-shown byte. |
| [CodePointerRow](../structs/CodePointerRow.md) | 8 | One row of UiLegacyLayoutScriptOps. |
| [ColourPair](../structs/ColourPair.md) | 4 | One row of the EquipPanelColourPairs table. |
| [CreditRoll](../structs/CreditRoll.md) |  | The credit roll object stepped by CreditRoll_Step: the script position, the line templates and the y position. |
| [CursorPosition](../structs/CursorPosition.md) | 2 | One row of the LegacyCursorPositions table. |
| [EaseEndpoints](../structs/EaseEndpoints.md) | 8 | One row of the EaseCurvesSetG table. |
| [EaseSample](../structs/EaseSample.md) | 4 | One row of the EaseCurvesSetA table. |
| [EaseSample3](../structs/EaseSample3.md) | 12 | One row of the EaseCurvesSetH table. |
| [FrameSetPointer](../structs/FrameSetPointer.md) | 8 | One row of the UiFrameSets tables. |
| [GlyphCodeTripleRow](../structs/GlyphCodeTripleRow.md) | 3 | One row of UiGlyphCodeTriples. |
| [GradientWindowVertexPaletteIndex](../structs/GradientWindowVertexPaletteIndex.md) | 1 | One row of the GradientWindowVertexPalette table. |
| [GridHelpRow](../structs/GridHelpRow.md) | 24 | One row of the GridHelpRows tables. |
| [GuideQueueEntry](../structs/GuideQueueEntry.md) | 12 | One entry of the queue of guides waiting to open, at [[qword_143CD9DA8+16]+264] +88. |
| [GuideSlot](../structs/GuideSlot.md) |  | One slot of a guide bar or window entry (GuideSlot_DrawButtons): up to four buttons given as actions or icon numbers. |
| [GUILayer](../structs/GUILayer.md) | 592 | A UI layer: a component drawn offscreen and composited with its effects (mask, drop shadow, glow). |
| [GUINode](../structs/GUINode.md) | 224 | Size from the 224-byte free in GUILayerNode's destructor. |
| [GUINodeState](../structs/GUINodeState.md) | 208 | One state (timeline) of a component: its clock, its loop range, its flags and the channel sets and entries it applies. |
| [GUINodeStateEntry](../structs/GUINodeStateEntry.md) | 64 | One entry of a state's entry list (GUINodeState.entries): a jump marker, a trigger, a state link, a state reset or a part trigger, built from the state's special tracks by UIAnim_ApplyTrack and UIAnim_ApplyComponentTr... |
| [JournalListEntry](../structs/JournalListEntry.md) | 12 | One 12-byte entry of the Chronicle Events list that JournalList_Build fills for each Journal row that is met. |
| [KeyTrack](../structs/KeyTrack.md) |  | A keyframe track of one property of one target: sorted keys, the first four stored inline. |
| [KeyTrackKey](../structs/KeyTrackKey.md) | 16 | One keyframe: its frame, the curve that shapes the interval to the next key, and the value. |
| [LauncherButtonIdRow](../structs/LauncherButtonIdRow.md) | 4 | One row of UiLauncherButtonOrder. |
| [LauncherFocusRow](../structs/LauncherFocusRow.md) | 24 | One row of UiLauncherFocusNeighborsAlt. |
| [LauncherGuide](../structs/LauncherGuide.md) |  | The launcher's guide pages state (UIAddonFFTOLauncher): the page set and the nodes the page builders use. |
| [LegacyAbilityMenuSkillsetByTabRow](../structs/LegacyAbilityMenuSkillsetByTabRow.md) | 1 | One row of the LegacyAbilityMenuSkillsetByTab table. |
| [LegacyBounceProfileRow](../structs/LegacyBounceProfileRow.md) | 2 | One row of the LegacyBounceProfile table. |
| [LegacyButtonIconGroupStartsRow](../structs/LegacyButtonIconGroupStartsRow.md) | 1 | One row of a LegacyButtonIconGroupStarts table. |
| [LegacyButtonIconPiecesRow](../structs/LegacyButtonIconPiecesRow.md) | 12 | One row of a LegacyButtonIconPieces table. |
| [LegacyButtonIconScalesRow](../structs/LegacyButtonIconScalesRow.md) | 4 | One row of a LegacyButtonIconScales table. |
| [LegacyCellRectsRow](../structs/LegacyCellRectsRow.md) | 20 | One row of the LegacyCellRects table. |
| [LegacyCursorRowsLang0Row](../structs/LegacyCursorRowsLang0Row.md) | 24 | One row of the LegacyCursorRowsLang0 table. |
| [LegacyCursorRowsLangOtherRow](../structs/LegacyCursorRowsLangOtherRow.md) | 24 | One row of the LegacyCursorRowsLangOther table. |
| [LegacyItemCursorTemplatesRow](../structs/LegacyItemCursorTemplatesRow.md) | 8 | One row of the LegacyItemCursorTemplates table. |
| [LegacyItemListBodyGridARow](../structs/LegacyItemListBodyGridARow.md) | 1 | One row of the LegacyItemListBodyGridA table. |
| [LegacyItemListBodyGridBRow](../structs/LegacyItemListBodyGridBRow.md) | 1 | One row of the LegacyItemListBodyGridB table. |
| [LegacyItemScriptRecord](../structs/LegacyItemScriptRecord.md) | 1 | First byte of one record of an item page layout script; the handler of the opcode returns the start of the next record. |
| [LegacyJobScreenLayoutLang0Row](../structs/LegacyJobScreenLayoutLang0Row.md) | 6592 | One row of the LegacyJobScreenLayoutLang0 table. |
| [LegacyListRowSlotRow](../structs/LegacyListRowSlotRow.md) | 1 | One row of the LegacyListRowSlot table. |
| [LegacyMenuNode](../structs/LegacyMenuNode.md) | 88 | One row of the LegacyMenuNodesLanguage0 table and the tables that share its shape. |
| [LegacyMenuRowCountsRow](../structs/LegacyMenuRowCountsRow.md) | 1 | One row of the LegacyMenuRowCounts table. |
| [LegacyMenuRowIconsRow](../structs/LegacyMenuRowIconsRow.md) | 1 | One row of the LegacyMenuRowIcons table. |
| [LegacyMenuRowListPointersRow](../structs/LegacyMenuRowListPointersRow.md) | 8 | One row of the LegacyMenuRowListPointers table. |
| [LegacyMenuRowResultRecord](../structs/LegacyMenuRowResultRecord.md) | 16 | One row of the LegacyMenuRowResults table. |
| [LegacyMenuTaskSetupsRow](../structs/LegacyMenuTaskSetupsRow.md) | 48 | One row of the LegacyMenuTaskSetups table. |
| [LegacyRowCellDescriptorsRow](../structs/LegacyRowCellDescriptorsRow.md) | 24 | One row of the LegacyRowCellDescriptors table. |
| [LegacyTask12CommandsARow](../structs/LegacyTask12CommandsARow.md) | 480 | One row of the LegacyTask12CommandsA table. |
| [LegacyTask12CommandsBRow](../structs/LegacyTask12CommandsBRow.md) | 64 | One row of the LegacyTask12CommandsB table. |
| [LegacyTitleMenuOffsetsRow](../structs/LegacyTitleMenuOffsetsRow.md) | 2 | One row of the LegacyTitleMenuOffsets table. |
| [LegacyUiScriptRecord](../structs/LegacyUiScriptRecord.md) | 2 | Header of one record of a legacy menu layout script; the record is {opcode, length, arguments} and the next record starts length bytes later. |
| [ListPageRangeStart](../structs/ListPageRangeStart.md) | 2 | One row of the LegacyListPageRangesLang0 table. |
| [MovieControl](../structs/MovieControl.md) | 32 | ffto::Game::Movie::MovieControl (vtable 0x1407154B0), at g_MovieControl: pause overlay and hold-to-skip of a playing movie. |
| [MovieController](../structs/MovieController.md) |  | ffto::Game::GameUI::MovieController (vtables 0x140702D20 and 0x140702D30): the movie host at *(qword_143CD9DC8) + 0xC8. |
| [NxdDataConfigCategoryRow](../structs/NxdDataConfigCategoryRow.md) | 16 | One row of the nxd.config_category table (data table). |
| [NxdDataConfigItemButtonTypeRow](../structs/NxdDataConfigItemButtonTypeRow.md) | 12 | One row of the nxd.config_item_button_type table (data table). |
| [NxdDataConfigItemCursorMoveTypeRow](../structs/NxdDataConfigItemCursorMoveTypeRow.md) | 20 | One row of the nxd.config_item_cursor_move_type table (data table). |
| [NxdDataConfigItemEnableDOFRow](../structs/NxdDataConfigItemEnableDOFRow.md) | 12 | One row of the nxd.config_item_enable_dof table (data table). |
| [NxdDataConfigItemForwardEnabledTypeRow](../structs/NxdDataConfigItemForwardEnabledTypeRow.md) | 12 | One row of the nxd.config_item_forward_enabled_type table (data table). |
| [NxdDataConfigItemResolutionRow](../structs/NxdDataConfigItemResolutionRow.md) | 8 | One row of the nxd.config_item_resolution table (data table). |
| [NxdDataConfigItemRow](../structs/NxdDataConfigItemRow.md) | 76 | One row of the nxd.config_item table (data table). |
| [NxdDataConfigItemScreenModeRow](../structs/NxdDataConfigItemScreenModeRow.md) | 12 | One row of the nxd.config_item_screen_mode table (data table). |
| [NxdDataConfigItemTextLanguageRow](../structs/NxdDataConfigItemTextLanguageRow.md) | 12 | One row of the nxd.config_item_text_language table (data table). |
| [NxdDataConfigItemVoiceLanguageRow](../structs/NxdDataConfigItemVoiceLanguageRow.md) | 12 | One row of the nxd.config_item_voice_language table (data table). |
| [NxdDataConfigPadAssignRow](../structs/NxdDataConfigPadAssignRow.md) | 20 | One row of the nxd.config_pad_assign table (data table). |
| [NxdDataConfigPadListRow](../structs/NxdDataConfigPadListRow.md) | 20 | One row of the nxd.config_pad_list table (data table). |
| [NxdDataCursorMoveTypeRow](../structs/NxdDataCursorMoveTypeRow.md) | 8 | One row of the nxd.cursor_move_type table (data table). |
| [NxdDataDifficultyLevelRow](../structs/NxdDataDifficultyLevelRow.md) | 28 | One row of the nxd.difficulty_level table (data table). |
| [NxdDataFloorCursorSpeedRow](../structs/NxdDataFloorCursorSpeedRow.md) | 8 | One row of the nxd.floor_cursor_speed table (data table). |
| [NxdDataForwardEnabledTypeRow](../structs/NxdDataForwardEnabledTypeRow.md) | 8 | One row of the nxd.forward_enabled_type table (data table). |
| [NxdDataIconGroupRow](../structs/NxdDataIconGroupRow.md) | 12 | One row of the nxd.icon_group table (data table). |
| [NxdDataIconRow](../structs/NxdDataIconRow.md) | 16 | One row of the nxd.icon table (data table). |
| [NxdDataLanguageRow](../structs/NxdDataLanguageRow.md) | 12 | One row of the nxd.language table (data table). |
| [NxdDataMessageWindowAnimationTypeRow](../structs/NxdDataMessageWindowAnimationTypeRow.md) | 28 | One row of the nxd.message_window_animation_type table (data table). |
| [NxdDataSystemParamRow](../structs/NxdDataSystemParamRow.md) | 12 | One row of the nxd.system_param table (data table). |
| [NxdDataUIAbilityIconRow](../structs/NxdDataUIAbilityIconRow.md) | 8 | One row of the nxd.ui_ability_icon table (data table). |
| [NxdDataUIAddonPriorityRow](../structs/NxdDataUIAddonPriorityRow.md) | 12 | One row of the nxd.ui_addon_priority table (data table). |
| [NxdDataUIAddonRow](../structs/NxdDataUIAddonRow.md) | 36 | One row of the nxd.ui_addon table (data table). |
| [NxdDataUIAnnounceRow](../structs/NxdDataUIAnnounceRow.md) | 28 | One row of the nxd.ui_announce table (data table). |
| [NxdDataUIButtonGuideRow](../structs/NxdDataUIButtonGuideRow.md) | 40 | One row of the nxd.ui_button_guide table (data table). |
| [NxdDataUIButtonRow](../structs/NxdDataUIButtonRow.md) | 12 | One row of the nxd.ui_button table (data table). |
| [NxdDataUIColorRow](../structs/NxdDataUIColorRow.md) | 12 | One row of the nxd.ui_color table (data table). |
| [NxdDataUIDialogRow](../structs/NxdDataUIDialogRow.md) | 60 | One row of the nxd.ui_dialog table (data table). |
| [NxdDataUIEquipAbilitySlotRow](../structs/NxdDataUIEquipAbilitySlotRow.md) | 16 | One row of the nxd.ui_equip_ability_slot table (data table). |
| [NxdDataUIEquipDetailNumParamRow](../structs/NxdDataUIEquipDetailNumParamRow.md) | 12 | One row of the nxd.ui_equip_detail_num_param table (data table). |
| [NxdDataUIFilePathExchangeRow](../structs/NxdDataUIFilePathExchangeRow.md) | 12 | One row of the nxd.ui_file_path_exchange table (data table). |
| [NxdDataUIFontSetRow](../structs/NxdDataUIFontSetRow.md) | 100 | One row of the nxd.ui_font_set table (data table). |
| [NxdDataUIFontTypeRow](../structs/NxdDataUIFontTypeRow.md) | 24 | One row of the nxd.ui_font_type table (data table). |
| [NxdDataUILoadTexturePathRow](../structs/NxdDataUILoadTexturePathRow.md) | 8 | One row of the nxd.ui_load_texture_path table (data table). |
| [NxdDataUIMenuButtonLeftRow](../structs/NxdDataUIMenuButtonLeftRow.md) | 32 | One row of the nxd.ui_menu_button_left table (data table). |
| [NxdDataUIMenuSortListRow](../structs/NxdDataUIMenuSortListRow.md) | 16 | One row of the nxd.ui_menu_sort_list table (data table). |
| [NxdDataUIMenuTabRow](../structs/NxdDataUIMenuTabRow.md) | 8 | One row of the nxd.ui_menu_tab table (data table). |
| [NxdDataUIModalRow](../structs/NxdDataUIModalRow.md) | 24 | One row of the nxd.ui_modal table (data table). |
| [NxdDataUIMouseCollisionRow](../structs/NxdDataUIMouseCollisionRow.md) | 12 | One row of the nxd.ui_mouse_collision table (data table). |
| [NxdDataUISubMenuRow](../structs/NxdDataUISubMenuRow.md) | 20 | One row of the nxd.ui_sub_menu table (data table). |
| [NxdDataUISubTabRow](../structs/NxdDataUISubTabRow.md) | 16 | One row of the nxd.ui_sub_tab table (data table). |
| [NxdDataUISystemParamRow](../structs/NxdDataUISystemParamRow.md) | 8 | One row of the nxd.ui_system_param table (data table). |
| [NxdDataUIUnitStatusNumParamRow](../structs/NxdDataUIUnitStatusNumParamRow.md) | 16 | One row of the nxd.ui_unit_status_num_param table (data table). |
| [OpeningSpriteListsRow](../structs/OpeningSpriteListsRow.md) | 8 | One row of the OpeningSpriteLists table. |
| [OpeningStepMapsRow](../structs/OpeningStepMapsRow.md) | 1 | One row of the OpeningStepMaps table. |
| [OptionChoice](../structs/OptionChoice.md) | 4 | One row of the LegacyOptionsDefaultChoices table. |
| [OptionTextBase](../structs/OptionTextBase.md) | 4 | One row of the LegacyOptionsTextBases table. |
| [PaletteColour](../structs/PaletteColour.md) | 2 | One row of a UI palette block. |
| [PanelStateOffset](../structs/PanelStateOffset.md) | 1 | One row of the PanelStateOffsets table. |
| [Rgb555Colour](../structs/Rgb555Colour.md) | 2 | One row of the LegacyCursorPalette table. |
| [SceneWindowColourRow](../structs/SceneWindowColourRow.md) | 20 | One row of BattleSceneWindowColours. |
| [SceneWindowTemplateRow](../structs/SceneWindowTemplateRow.md) | 84 | One row of BattleSceneWindowTemplatesLang0. |
| [ScreenTaskSetRow](../structs/ScreenTaskSetRow.md) | 64 | One row of the ScreenTaskSets table: up to four task slots started together. |
| [SlideCurveStep](../structs/SlideCurveStep.md) | 2 | One row of the PanelSlideCurve table. |
| [SpriteAnimScriptsRow](../structs/SpriteAnimScriptsRow.md) | 8 | One row of the SpriteAnimScripts table. |
| [StringPointerRow](../structs/StringPointerRow.md) | 8 | One row of a string pointer table (ResumeKindNames, SoundPackPathPatterns, UiCoreNameKeys, DeflateErrorMessages). |
| [UIAddonFFTOConfig](../structs/UIAddonFFTOConfig.md) | 3416 | The General Options screen object (3416 bytes, `Mem_Alloc(3416)` in 0x140182478): base `UIAddonMenuBase`, vtable 0x14070DB30 with 18 entries (RTTI locator at 0x14070DB28). |
| [UIAddonFFTOSaveLoad](../structs/UIAddonFFTOSaveLoad.md) | 1240 | The save/load screen's list add-on (1240 bytes, allocated in agent state 3 and constructed by `sub_140184C38` at 0x140184C38): a `UIAddonMenuBase` at +0 with a second `UIFFTOMenuFunctionBase` vtable at +48. |
| [UIAddonFFTOTitle](../structs/UIAddonFFTOTitle.md) | 240 | The title menu screen object (240 bytes, `Mem_Alloc(240)` in UIAddonFFTOTitle_Create): base `UIAddonMenuBase`, primary vtable 0x14070A4B0 and a second vtable 0x14070A460 at +48 (the `UIFFTOMenuFunctionBase` part). |
| [UIAddonFingerCursor](../structs/UIAddonFingerCursor.md) |  | The finger cursor addon: the loaded cursor widget (ffto_finger_cursor.uib), the parts it moves, and the glide state of GUICursorHand_StepToward. |
| [UIAgentBase](../structs/UIAgentBase.md) | 64 | The common front of every UI agent (64 bytes), built by sub_1401D14F4 (0x1401D14F4): the vtable, the UI module's allocator and the vector of attached add-ons. |
| [UIAgentCursor](../structs/UIAgentCursor.md) |  | The cursor agent: element 1 of the addon manager's agent vector (global qword_143CD9DA8, vector at +16). |
| [UIAgentFFTOSaveLoad](../structs/UIAgentFFTOSaveLoad.md) | 1592 | The save/load screen's UI agent (1592 bytes, vtable 0x14070DE48, slot 38 of the UI agent manager). |
| [UIAgentFFTOSystem](../structs/UIAgentFFTOSystem.md) | 1472 | The System agent: entry 37 of the agent manager's array (`*(qword_143CD9DA8 + 16) + 37 * 8`, as Boot_Update reads it); 1472 bytes, constructor 0x140181C94, vtable 0x14070DF00. |
| [UIAgentFFTOTitle](../structs/UIAgentFFTOTitle.md) | 1448 | The title screens' agent (1448 bytes, `Mem_Alloc(0x5A8)` in `UIAgentManager_CreateAgents` at 0x1401CFA4D; vtable 0x14070A5B0, constructor 0x1401C2AE4). |
| [UIAgentManager](../structs/UIAgentManager.md) | 184 | The singleton UI agent manager (IDB class UIAgentModule): a 184-byte module object that owns the 54-agent vector, the addon map, the queued-event vector and the font-slot vector. |
| [UIGadgetFFTOConfigConfirmWindow](../structs/UIGadgetFFTOConfigConfirmWindow.md) |  | The confirm window gadget of General Options (+2400; vtables 0x140712448 and 0x1407124A0): a message and up to three option buttons loaded from a UIDialog row. |
| [UIListGadget](../structs/UIListGadget.md) |  | The row list gadget used by General Options (constructor 0x14028C458, bound by 0x14028C5C4 with tag 151 and the part name `List`). |
| [UIManager](../structs/UIManager.md) |  | The UI manager object at Renderer.ui_manager: the shader selectors of the UI technique and the shared layer quad buffers. |
| [UiRect](../structs/UiRect.md) | 8 | One screen or VRAM rectangle of a panel. |
| [UIRender](../structs/UIRender.md) |  | The UI render object (the command ring): the slot ids it resolved by name when it was created, used by every UI draw. |
| [UiScriptRecord](../structs/UiScriptRecord.md) |  | One record of a UI script: an opcode byte, a length byte and the arguments. |
| [UiSpriteCell](../structs/UiSpriteCell.md) | 12 | One row of the MessageWindowTagCellsLanguage2 table and the tables that share its shape. |
| [UnitEditorRange](../structs/UnitEditorRange.md) | 8 | One row of the UnitEditorRanges tables. |
| [UnitEditorWidget](../structs/UnitEditorWidget.md) | 24 | One row of the UnitEditorWidgets tables. |
| [WindowCellRecordRow](../structs/WindowCellRecordRow.md) | 12 | One row of UiLegacyWindowCellLayoutBase. |
| [WindowColourSetRow](../structs/WindowColourSetRow.md) | 4 | One row of UiLegacyWindowColourSetsLang1. |
| [WindowCurvePointer](../structs/WindowCurvePointer.md) | 8 | One row of the WindowCurvePointers table. |
| [WindowGroupStartRow](../structs/WindowGroupStartRow.md) | 1 | One row of UiLegacyWindowGroupStartsLang0. |
| [WindowGrowStep](../structs/WindowGrowStep.md) | 1 | One row of the WindowGrowSteps table. |
| [WindowPatternWord](../structs/WindowPatternWord.md) | 2 | One row of the WindowPatternTiles table. |
| [WorldMapLocationRecord](../structs/WorldMapLocationRecord.md) | 64 | One 64-byte record per world-map location that the location-list builder accepts (location ids 0..46): what is on offer there and its state at the current story progress. |

## Globals (8)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_GameUIManager](../globals/g_GameUIManager.md) | `0x143CD9DC8` | `void *` | The game's UI manager object: the movie controller flags are at +0xE0 and the movie host at +200 (record MovieController). |
| [g_ListAlias](../globals/g_ListAlias.md) | `0x14184A9B0` | `uint8 *` | A second published alias of the list object, written by the task functions that open a list (the command task, the event runner and others). |
| [g_ListObject](../globals/g_ListObject.md) | `0x1418716A0` | `uint8[1024]` | The static list object: u16 cell words at +0 (stride 2), a property word array at +0xA4, the bare-id array at +0x148 and five byte arrays after it. |
| [g_ListObjectPtr](../globals/g_ListObjectPtr.md) | `0x141871698` | `uint8 *` | The published pointer to the static list object. |
| [g_StatusIconTileX](../globals/g_StatusIconTileX.md) | `0x143D1B588` | `uint16` | Tile x of the status/item icon the status screen last set, copied from the icon state. |
| [g_StatusIconTileY](../globals/g_StatusIconTileY.md) | `0x143D1B58A` | `uint16` | Tile y of the status/item icon the status screen last set, copied from the icon state. |
| [g_StatusIconWord](../globals/g_StatusIconWord.md) | `0x143D1B590` | `uint16` | The packed page-and-palette word of the status/item icon the status screen last set. |
| [g_UIChosenItemId](../globals/g_UIChosenItemId.md) | `0x143C518F0` | `uint16` | The 16-bit UI field that holds the item id the player picked in the shop list. |

## Registries (17)

| Name | Summary |
|---|---|
| [AchievementNotificationTypes](../registries/AchievementNotificationTypes.md) | The type number of each achievement notification class: the virtual function at +8 of the notification's vtable returns it, and the achievement classes compare it in their match functions. |
| [ClassicItemScriptOpcodes](../registries/ClassicItemScriptOpcodes.md) | The 25-slot handler table (image address 0x1406932A0) that the item pages of the legacy party menu run inline (ClassicItemUsePage_Run); the slot layout equals that of UiScriptOpcodes up to slot 24 where both have a ha... |
| [ClassicLayoutScriptOpcodesPart](../registries/ClassicLayoutScriptOpcodesPart.md) | The slots of the 22-slot layout script table (image address 0x140693110, run by ClassicUi_RunLayoutScript, end opcode 22): the long list handler and three small rectangle handlers. |
| [ClassicMenuControllers](../registries/ClassicMenuControllers.md) | The per-screen controllers of the classic menu system: one contiguous array of input steps at 0x140681400, 55 filled slots (0 to 45 and 48 to 56; 46, 47 and 57 are null), with a further entry at index 58. |
| [ClassicSubtitleState](../registries/ClassicSubtitleState.md) | The state names of the classic-movie subtitle window and the UIClassicSubtitles line_layout value that picks each. |
| [CreditLineType](../registries/CreditLineType.md) | The line types of UICreditRow (line_type) and the builder CreditRoll_Step calls for each. |
| [GuideIconGlyph](../registries/GuideIconGlyph.md) | The guide icon numbers (UIButtonGuide guide_icon / guide_icon_2) and the glyph GuideIcon_ToGlyph draws for them. |
| [MovieControllerFlag](../registries/MovieControllerFlag.md) | The movie controller flag bits Movie_Start sets from the MovieData row (MovieController +24). |
| [TitleMenuEntryKinds](../registries/TitleMenuEntryKinds.md) | The six kinds of row of the Enhanced title menu: the kind byte stored in each row, the text id of its label (UI table, nxd id 19) and what choosing it does. |
| [TitleModeSelectButtons](../registries/TitleModeSelectButtons.md) | The button ids of the mode select screen as `UILauncher_OnMenuAction` handles them. |
| [UIAddonRows](../registries/UIAddonRows.md) | Rows of the screen table (`uiaddon.nxd`, nxd id 24) that the title screens use: each row's `path` names the layout file a screen loads. |
| [UIAgentSlots](../registries/UIAgentSlots.md) | The 54 UI agents the manager appends at construction, in slot order: six generic agents and 48 FFTO screens. |
| [UIAnimCurves](../registries/UIAnimCurves.md) | The easing curves of UI keyframes: curve id to blend function of the position t within a key interval (UIAnim_Curve). |
| [UIButtonGuideKeysOfGeneralOptions](../registries/UIButtonGuideKeysOfGeneralOptions.md) | The guide bar keys (`UIButtonGuide` rows, UI table 33) the settings screen uses, with the text id of each sub-row; 'right' marks sub-rows drawn on the right (byte +37 `Unknown25`). |
| [UIDialogRowsOfSettings](../registries/UIDialogRowsOfSettings.md) | The UIDialog rows (nxd 34, `UITable_GetRow(34, row)`) the settings screens and neighbours use, and the UI texts they quote. |
| [UiScriptOpcodes](../registries/UiScriptOpcodes.md) | The 29-slot handler table (image address 0x1406838F0) that UiScript_Run indexes with the opcode byte of each record; the conditional handlers also index it for the records they govern. |
| [UISoundIdsOfSettings](../registries/UISoundIdsOfSettings.md) | The UI sound ids (`sub_1400F4BCC(_, id)`, UI table 0x45) the settings screen plays. |

## File formats (7)

| Name | Extension | Summary |
|---|---|---|
| [ConfigCategoryTable](../formats/ConfigCategoryTable.md) | `.nxd` | `configcategory.nxd` (nxd 249): the tabs of the settings screens; `config_items` are the rows of a tab and `name_text` its title. |
| [ConfigItemTable](../formats/ConfigItemTable.md) | `.nxd` | `configitem.nxd` (nxd 250): one row per setting of the settings screens. |
| [ConfigScreenLayout](../formats/ConfigScreenLayout.md) | `.uib` | `ffto_config_enhanced_ver02.uib` and `ffto_config_parts.uib` (pack 0008): the layout of the settings screen and its row, switch, select and slider parts. |
| [ItemIconPath](../formats/ItemIconPath.md) | `.utexpt with .tex` | The two per-item picture paths: a detail picture (Icon table row 12) and a list picture (row 13), both formatted from the item id and both texture-parts URIs. |
| [TexturePartFile](../formats/TexturePartFile.md) | `.utexpt` | The part file that names the texture a UI image part shows (ui/ffto/icon/<kind>/textureparts/<name>.utexpt). |
| [TitleMenuLayout](../formats/TitleMenuLayout.md) | `.uib` | `ui/ffto/title/ffto_title_enhanced.uib` (pack 0008), the layout of the Enhanced title menu: nine components, of which `Menu` carries the row layouts the add-on plays by name. |
| [TitleScreenLayout](../formats/TitleScreenLayout.md) | `.uib` | `ffto_title_enhanced.uib` (pack 0008): the title screen behind the menu: backdrop, logo, version, copyright and the `Menu` component with its six buttons. |

## Flows (7)

| Name | Summary |
|---|---|
| [ChronicleEventReplay](../flows/ChronicleEventReplay.md) | What happens when the player replays an entry of the Chronicle Events list: from the action to the event running. |
| [CursorGloveFrame](../flows/CursorGloveFrame.md) | What happens to the finger cursor's glove in one UI frame, in order: its Loop clock advances, scrubs the Hand's Loop, the Hand's IconHand position is sampled as an integer, and the cursor reference node glides toward ... |
| [GeneralOptionsOpenAndClose](../flows/GeneralOptionsOpenAndClose.md) | How the settings screen opens from the mode select or the in-game menu and closes again, through the System agent. |
| [MovieStart](../flows/MovieStart.md) | How a movie starts and ends: row read, controller flags, sound banks, subtitle window, skip rules. |
| [ScreenAddonCreation](../flows/ScreenAddonCreation.md) | How a screen (add-on) is made and shown: allocate, construct, attach to the agent, load its layout from the screen table, then show or hide it. |
| [TitleMenuAction](../flows/TitleMenuAction.md) | From a press on a title menu row to the action: the button event reaches the agent, which dispatches on the row's kind. |
| [UIAgentLifecycle](../flows/UIAgentLifecycle.md) | From the manager's construction to its teardown: the 184-byte manager is built once, fills a 54-slot agent vector, attaches addons to agents, ticks them each frame, changes their states, and finally deletes every agen... |

## Observed behaviours (30)

| Name | Scope | Summary |
|---|---|---|
| [AchievementClassesMatchByColumn](../behaviors/AchievementClassesMatchByColumn.md) | engine (achievements) | Which Achievement column an achievement class tests: a counter, a book or a Chronicle event. |
| [BattleCommandMenuStates](../behaviors/BattleCommandMenuStates.md) | battle, own turn: command menu, Abilities list, Move tile selection, target selection, facing prompt | How to tell the screens of an own battle turn apart and which row the command menu cursor is on, from game state only: the glove position, the focused widget and the text of the instruction-message widget. |
| [BattleHudAndUnitFields](../behaviors/BattleHudAndUnitFields.md) | the Jobs screen and a battle's first turn | What the game shows from the Jobs screen into a battle, as seen live. |
| [BattleTextOverlaysAndPreview](../behaviors/BattleTextOverlaysAndPreview.md) | battle: event dialogue, notice banner, attack / item preview, deployment placement | Where the battle's dialogue, notices and action preview are drawn, how placement works, and what the preview numbers meant in play, as seen live. |
| [BookPageTextIsReadFromTheNovelTableOfPageTable](../behaviors/BookPageTextIsReadFromTheNovelTableOfPageTable.md) | engine (book reader) | A book's pages are the rows of one of five Novel tables, chosen by the Book page_table value; the page number is the row key and the text is the row's string. |
| [ClearMarkAppearsOnFourScreens](../behaviors/ClearMarkAppearsOnFourScreens.md) | engine (Zodiac Stone, Events, Chronicle period, glossary) | Four tables carry a one-byte clear_mark column; each shows a node 'Clear' that plays 'Enable' when the byte is set and 'Disable' otherwise. |
| [CursorGloveBob](../behaviors/CursorGloveBob.md) | finger cursor (the glove on the Job Tree) | The glove's idle bob: a 40-frame, looping, position track on the IconHand node of the Hand component, played on the UI frame time, sampled as an integer, and added to the glove's glide only in the node matrices. |
| [GlossaryPagesAreMetRowsOfOneEntry](../behaviors/GlossaryPagesAreMetRowsOfOneEntry.md) | engine (glossary) | A glossary entry is a first key; its rows (second key) are pages that appear as their user_situation is met, and a row flagged replaces_previous overwrites the page before it instead of being a page of its own. |
| [GuideBarLayout](../behaviors/GuideBarLayout.md) | the footer button guide bar | The guide bar shows one UIButtonGuide key at a time: up to 8 slots, left ones first then right ones from x 1920; a sub-row mask hides sub-rows. |
| [GuideListsAndAutoShowRule](../behaviors/GuideListsAndAutoShowRule.md) | engine (tutorials and lessons) | A guide's window type, category and bit number decide where it is listed, where its seen or unlocked bit lives and when it opens by itself. |
| [GUITextNodeStringSource](../behaviors/GUITextNodeStringSource.md) | where a text node's string comes from: the UI table or the code | A text node shows the string of its UI table text id while that id is not 0; with text id 0 it keeps a string set in code. |
| [IconGroup4kPaths](../behaviors/IconGroup4kPaths.md) | engine (icon paths) | Icons in a group with select_4k set load their '_4k_' file instead of a '_2k_' one; the stock data names no '_2k_' path. |
| [JobsEquipmentShopScreens](../behaviors/JobsEquipmentShopScreens.md) | Units > Status, Jobs, equipment list, Outfitter (Buy) | Screen identities, cell layouts and the memory handles (job byte, item id, gil) of the world map management screens, as seen live. |
| [JobTreeLayerList](../behaviors/JobTreeLayerList.md) | the layer slots of a UI frame and, for the Job Tree screen, which component opens each one and how its float rectangle is made | A UI layer is not tied to a component by any pointer: the layer records hold no component link (only the mask component of a masked layer is stored). |
| [ListGadgetInputPath](../behaviors/ListGadgetInputPath.md) | why a list cursor moves only when the screen calls the list input | A list gadget's cursor moves by pad or keyboard only when the screen's input handler calls the list's own input; the Left / Right branches of the settings screen return before that call. |
| [MovieSkipKinds](../behaviors/MovieSkipKinds.md) | engine (movies) | Classic movies and the first four movies end on one press; the enhanced story movies open the pause window, from which they can be skipped. |
| [SettingsCloseSavesSystemFile](../behaviors/SettingsCloseSavesSystemFile.md) | what closing the settings screen writes | Closing the settings screen requests a settings save, and the save rewrites the SYSTEM save file with the settings and the save manager's bytes +656..+895, among them the game-cleared byte. |
| [TextNodeDrawGate](../behaviors/TextNodeDrawGate.md) | UI text nodes (GUITextNode_Draw) | GUITextNode_Draw returns before drawing unless a byte at node +0xCC is non-zero, a byte at +0x91 is zero, the string size at +0xE8 is non-zero and a font-table / font-set lookup returns true. |
| [TitleAndSaveListScreens](../behaviors/TitleAndSaveListScreens.md) | title screens, Continue / Load Game save list | The screens between launch and a loaded game, the keys they take, and how the save list is built, as seen live. |
| [TitleBackdropAndInputFlag](../behaviors/TitleBackdropAndInputFlag.md) | the title screen behind another screen | Hiding the title add-on hides its backdrop; input reaches an add-on only when its byte +47 is clear. |
| [TitleMenuRows](../behaviors/TitleMenuRows.md) | which rows the Enhanced title menu shows and how they are laid out | The Enhanced title menu shows 3 to 6 rows chosen by the save state and the cleared flag; the layout file has a state for each count. |
| [TitleMenuRowStorage](../behaviors/TitleMenuRowStorage.md) | where the title add-on keeps its rows and what lies after them | The title add-on stores six 24-byte rows at +72; the count, current row, last input tick and flags follow at +216..+230, and no instruction of the title code touches +231..+239, so a seventh row would overlap those fi... |
| [UIAddonBaseEventRouting](../behaviors/UIAddonBaseEventRouting.md) | how a screen's events reach its handlers | Every add-on's event handler calls UIAddon_OnEventBase first; input reaches the add-on's slot 12 only when its id is not excluded, byte +47 is clear and slot 3 allows it. |
| [UIStateClock](../behaviors/UIStateClock.md) | every UIB state (timeline) | How the clock of a UI state runs: real elapsed time per UI frame (never less than 1/60 s), summed in single precision, frame = time * 60.0 as a float; the end or a loop resets frame and time and drops the overshoot. |
| [UiTableColumnsNeverRead](../behaviors/UiTableColumnsNeverRead.md) | engine (table readers) | No code reads the first dword of UIKeyAssign, UIPadDefine, Icon, SystemBonusEntitlement, UIButtonGuide, BattleVoiceGroupRate and the other UI rows read here; the tables DebugMap (78) and DebugFIdSound (89) are never f... |
| [WidgetRootsAreLayers](../behaviors/WidgetRootsAreLayers.md) | every UI widget (the Job Tree, the finger cursor, the footer guides) | Every widget's root component is drawn into its own layer record, whether or not it has an effect: the renderer's feature byte at r+606621 is 1 from the initialiser and the widget byte at +83 is 1 for all 51 widgets o... |
| [WorldMapLocationsAndBattleEntry](../behaviors/WorldMapLocationsAndBattleEntry.md) | world map free roam, Locations list, travel to a battleground, battle deployment | How a battle is entered from the world map, and which screens and memory fields show it, as seen live. |
| [WorldMapObjectiveLineIsTheNearestCaptionRow](../behaviors/WorldMapObjectiveLineIsTheNearestCaptionRow.md) | engine (world map) | The objective line of the world map is the caption of the current progress row, or of the nearest earlier row of the same first key whose sets_objective byte is set. |
| [WorldMapRoutesAndLocationsFollowProgress](../behaviors/WorldMapRoutesAndLocationsFollowProgress.md) | engine (world map) | Routes are shown, hidden and greyed by the story progress row; a route grows between its two end points, forward or reversed; locations go into three lists by locations_list and are positioned by map_x / map_y. |
| [ZodiacStoneBoardShowsStonesByHeldState](../behaviors/ZodiacStoneBoardShowsStonesByHeldState.md) | engine (Zodiac Stone screen) | Each of the 13 stones shows the row with the highest second key whose user_situation is met; the owner-timeline column decides whether the stone is shown held, or as not yet acquired with the owner's portrait state. |

## Tables (234)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [BattlePanelNumbersActor](../tables/BattlePanelNumbersActor.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the battle unit panel, actor side (HP and MP with maxima, Wt, At, level, experience). |
| [BattlePanelNumbersTarget](../tables/BattlePanelNumbersTarget.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the battle unit panel, target side. |
| [BattleSceneWindowColours](../tables/BattleSceneWindowColours.md) | Executable |  | 6 rows of 20 bytes | Corner colours (four per row) of the battle scene window gradients. |
| [BattleSceneWindowTemplatesDefault](../tables/BattleSceneWindowTemplatesDefault.md) | Executable |  | 920 bytes of window records | Window records (rectangles, flags, pointers) of the battle scene screen, default for other languages. |
| [BattleSceneWindowTemplatesLang0](../tables/BattleSceneWindowTemplatesLang0.md) | Executable |  | 800 bytes of window records | Window records (rectangles, flags, pointers) of the battle scene screen, text language 0. |
| [CharGridOrder](../tables/CharGridOrder.md) | Executable |  | 97 rows of 1 bytes | Which symbol each cell of the 97-cell character selection grid shows. |
| [EaseCurvesSetA](../tables/EaseCurvesSetA.md) | Executable |  | 56 rows of 4 bytes | Easing curve set for legacy screen animations: 6 curves of 9 samples (linear up, linear down, ease up, ease down, bump, constant 1.0) plus a short tail. |
| [EaseCurvesSetB](../tables/EaseCurvesSetB.md) | Executable |  | 44 rows of 4 bytes | Easing curve set b: 44 samples in 9-sample curves (five-step ramps, S-curves and two bumps). |
| [EaseCurvesSetC](../tables/EaseCurvesSetC.md) | Executable |  | 20 rows of 4 bytes | Easing curve set c: 20 samples of small step curves (0, 0x800, 0x1000 ramps). |
| [EaseCurvesSetD](../tables/EaseCurvesSetD.md) | Executable |  | 36 rows of 4 bytes | Easing curve set d: 36 samples (4 curves of 9: ramp, S-curve, bumps). |
| [EaseCurvesSetE](../tables/EaseCurvesSetE.md) | Executable |  | 72 rows of 4 bytes | Easing curve set e: 72 samples (8 curves of 9), the shapes of set a plus a decay curve. |
| [EaseCurvesSetF](../tables/EaseCurvesSetF.md) | Executable |  | 120 rows of 4 bytes | Easing curve set f: 120 samples, curves of 33 steps (long ramps and S-curves) for slower animations. |
| [EaseCurvesSetG](../tables/EaseCurvesSetG.md) | Executable |  | 6 rows of 8 bytes | Six start and end factors (0 to 1.0, 1.0 to 0, ...) used as ramp endpoints. |
| [EaseCurvesSetH](../tables/EaseCurvesSetH.md) | Executable |  | 5 rows of 12 bytes | Short 3-sample curves; the 0x80-byte object ends with a list of byte pairs (cell step offsets) that this reader does not use. |
| [EquipPanelCellsLanguage0V0](../tables/EquipPanelCellsLanguage0V0.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 0, variant 0 (19 cells). |
| [EquipPanelCellsLanguage0V1](../tables/EquipPanelCellsLanguage0V1.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 0, variant 1 (19 cells). |
| [EquipPanelCellsLanguage0V2](../tables/EquipPanelCellsLanguage0V2.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 0, variant 2 (19 cells). |
| [EquipPanelCellsLanguage0V3](../tables/EquipPanelCellsLanguage0V3.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 0, variant 3 (19 cells). |
| [EquipPanelCellsLanguage2V0](../tables/EquipPanelCellsLanguage2V0.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 2, variant 0 (19 cells). |
| [EquipPanelCellsLanguage2V1](../tables/EquipPanelCellsLanguage2V1.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 2, variant 1 (19 cells). |
| [EquipPanelCellsLanguage2V2](../tables/EquipPanelCellsLanguage2V2.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 2, variant 2 (19 cells). |
| [EquipPanelCellsLanguage2V3](../tables/EquipPanelCellsLanguage2V3.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 2, variant 3 (19 cells). |
| [EquipPanelCellsLanguage3V0](../tables/EquipPanelCellsLanguage3V0.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 3, variant 0 (19 cells). |
| [EquipPanelCellsLanguage3V1](../tables/EquipPanelCellsLanguage3V1.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 3, variant 1 (19 cells). |
| [EquipPanelCellsLanguage3V2](../tables/EquipPanelCellsLanguage3V2.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 3, variant 2 (19 cells). |
| [EquipPanelCellsLanguage3V3](../tables/EquipPanelCellsLanguage3V3.md) | Executable (initialised data) |  | 19 rows of 12 bytes | Sprite cells of the equip screen panel, language 3, variant 3 (19 cells). |
| [EquipPanelColourPairs](../tables/EquipPanelColourPairs.md) | Executable (initialised data) |  | 11 rows of 4 bytes | Gradient colour pairs of the result panel, one colour per variant. |
| [EquipPanelRects](../tables/EquipPanelRects.md) | Executable (initialised data) |  | 10 rows of 8 bytes | The panel origins and VRAM staging rectangles of the equip screen panels: two palette row rectangles, then screen rectangles and two texture strip rectangles. |
| [EquipScreenPalette](../tables/EquipScreenPalette.md) | Executable (initialised data) |  | 256 rows of 2 bytes | UI palette block (four rows of 64 colours) the equipment screen uploads to the CLUT area of VRAM. Verdict: designer-data. |
| [EventMenuNodesDefault](../tables/EventMenuNodesDefault.md) | Executable (initialised data) |  | 63 rows of 88 bytes | Legacy menu node array of the event task group, default language. |
| [EventMenuNodesLanguage0](../tables/EventMenuNodesLanguage0.md) | Executable (initialised data) |  | 63 rows of 88 bytes | Legacy menu node array of the event task group, language 0 (63 nodes of 88 bytes, mutable at run time). |
| [EventMenuNodesLanguage2](../tables/EventMenuNodesLanguage2.md) | Executable (initialised data) |  | 63 rows of 88 bytes | Legacy menu node array of the event task group, language 2. |
| [EventMenuNodesLanguage3](../tables/EventMenuNodesLanguage3.md) | Executable (initialised data) |  | 63 rows of 88 bytes | Legacy menu node array of the event task group, language 3. |
| [FrameSetsDefault](../tables/FrameSetsDefault.md) | Executable |  | 142 rows of 8 bytes | Sprite frame sets of the widget animations, the default (language 1) variant. |
| [FrameSetsLanguage0](../tables/FrameSetsLanguage0.md) | Executable |  | 142 rows of 8 bytes | Sprite frame sets of the widget animations, language 0 variant. |
| [FrameSetsLanguage2](../tables/FrameSetsLanguage2.md) | Executable |  | 142 rows of 8 bytes | Sprite frame sets of the widget animations, language 2 variant. |
| [FrameSetsLanguage3](../tables/FrameSetsLanguage3.md) | Executable |  | 142 rows of 8 bytes | Sprite frame sets of the widget animations, language 3. |
| [GradientWindowVertexPalette](../tables/GradientWindowVertexPalette.md) | Executable |  | 12 rows of 1 bytes | Which palette colour each of the 12 vertices of a gradient window takes. |
| [GridArrowCells](../tables/GridArrowCells.md) | Executable (initialised data) |  | 5 rows of 12 bytes | Five sprite cells of the grid screen (arrows and page markers). |
| [GridAvailableTemplate](../tables/GridAvailableTemplate.md) | Executable (initialised data) |  | 54 rows of 1 bytes | Initial availability flags of the grid screen entries. |
| [GridHelpRowsDefault](../tables/GridHelpRowsDefault.md) | Executable (initialised data) |  | 31 rows of 24 bytes | Cursor rows of the grid screen text helper, default language. |
| [GridHelpRowsLanguage0](../tables/GridHelpRowsLanguage0.md) | Executable (initialised data) |  | 31 rows of 24 bytes | Cursor rows of the grid screen text helper, language 0. |
| [GridMenuNodesDefault](../tables/GridMenuNodesDefault.md) | Executable (initialised data) |  | 5 rows of 88 bytes | Legacy menu nodes of the grid screen, default language. |
| [GridMenuNodesLanguage0](../tables/GridMenuNodesLanguage0.md) | Executable (initialised data) |  | 5 rows of 88 bytes | Legacy menu nodes of the grid screen, language 0. |
| [ItemListScriptLanguage0](../tables/ItemListScriptLanguage0.md) | Executable (initialised data) |  | 1 script of 198 bytes | The UI script that lays out and runs the item list screen's widgets, language 0 (198 bytes, then a block of rectangles). |
| [ItemListScriptLanguage1](../tables/ItemListScriptLanguage1.md) | Executable (initialised data) |  | 1 script of 198 bytes | The UI script that lays out and runs the item list screen's widgets, language 1 (198 bytes, then a block of rectangles). |
| [ItemListScriptLanguage2](../tables/ItemListScriptLanguage2.md) | Executable (initialised data) |  | 1 script of 198 bytes | The UI script that lays out and runs the item list screen's widgets, language 2 (198 bytes, then a block of rectangles). |
| [ItemListScriptLanguage3](../tables/ItemListScriptLanguage3.md) | Executable (initialised data) |  | 1 script of 198 bytes | The UI script that lays out and runs the item list screen's widgets, language 3 (198 bytes, then a block of rectangles). |
| [JobLearnListScriptLang1](../tables/JobLearnListScriptLang1.md) | Executable |  | 1 script of 493 bytes | UI script (layout of the job learn list) for text language 1. |
| [JobLearnListScriptLang2](../tables/JobLearnListScriptLang2.md) | Executable |  | 1 script of 493 bytes | UI script (layout of the job learn list) for text language 2. |
| [JobLearnListScriptLang3](../tables/JobLearnListScriptLang3.md) | Executable |  | 1 script of 493 bytes | UI script (layout of the job learn list) for text language 3. |
| [JobUnitRowsScriptLang0](../tables/JobUnitRowsScriptLang0.md) | Executable |  | 1 script of 217 bytes | UI script (layout of the job screen's unit rows) for text language 0. |
| [JobUnitRowsScriptLang1](../tables/JobUnitRowsScriptLang1.md) | Executable |  | 1 script of 217 bytes | UI script (layout of the job screen's unit rows) for text language 1. |
| [JobUnitRowsScriptLang2](../tables/JobUnitRowsScriptLang2.md) | Executable |  | 1 script of 217 bytes | UI script (layout of the job screen's unit rows) for text language 2. |
| [JobUnitRowsScriptLang3](../tables/JobUnitRowsScriptLang3.md) | Executable |  | 1 script of 217 bytes | UI script (layout of the job screen's unit rows) for text language 3. |
| [LegacyAbilityMenuSkillsetByTab](../tables/LegacyAbilityMenuSkillsetByTab.md) | Executable |  | 4 rows of 1 byte | Four skillset ids, one per tab of the legacy ability menu; the same object continues with two 7-entry dword tables (run starts 0, 6 ... 36 and 0, 60 ... 360) that cut the page art into per-page ranges. |
| [LegacyBounceProfile](../tables/LegacyBounceProfile.md) | Executable |  | 11 rows of 2 bytes | Symmetric 11-sample arc used to animate a cursor or row; the rest of the 0xBA-byte object holds small cell records. |
| [LegacyButtonIconGroupStartsLang0](../tables/LegacyButtonIconGroupStartsLang0.md) | Executable |  | 15 rows of 1 byte | Cumulative piece start index of each button icon group for text language 0; language 1 (default), 2 and 3 share another list (LegacyButtonIconGroupStartsLang1). |
| [LegacyButtonIconGroupStartsLang1](../tables/LegacyButtonIconGroupStartsLang1.md) | Executable |  | 15 rows of 1 byte | Piece start indexes of the button icon groups for text languages 1, 2 and 3 (80 pieces; three identical copies at 0x140691D00, 0x140691CF0 and 0x140691A60). |
| [LegacyButtonIconPiecesLang0](../tables/LegacyButtonIconPiecesLang0.md) | Executable |  | 81 rows of 12 bytes | Texture rectangle and draw offset of each button icon piece, text language 0 (81 pieces; the other languages have 80). |
| [LegacyButtonIconPiecesLang1](../tables/LegacyButtonIconPiecesLang1.md) | Executable |  | 80 rows of 12 bytes | Texture rectangle and draw offset of each button icon piece, text language 1. |
| [LegacyButtonIconPiecesLang2](../tables/LegacyButtonIconPiecesLang2.md) | Executable |  | 80 rows of 12 bytes | Texture rectangle and draw offset of each button icon piece, text language 2. |
| [LegacyButtonIconPiecesLang3](../tables/LegacyButtonIconPiecesLang3.md) | Executable |  | 80 rows of 12 bytes | Texture rectangle and draw offset of each button icon piece, text language 3. |
| [LegacyButtonIconScalesLang0](../tables/LegacyButtonIconScalesLang0.md) | Executable |  | 81 rows of 4 bytes | Scale pair of each button icon piece for text language 0. |
| [LegacyButtonIconScalesLang1](../tables/LegacyButtonIconScalesLang1.md) | Executable |  | 80 rows of 4 bytes | Scale pair of each button icon piece for text languages 1, 2 and 3 (three identical copies); language 0 has its own with 81 rows (LegacyButtonIconScalesLang0). |
| [LegacyCellRects](../tables/LegacyCellRects.md) | Executable (initialised data) |  | 5 rows of 20 bytes | Five 20-byte rectangle records (size, texture position and flag bytes) of legacy item page cells; the rest of the 0xD0-byte object holds pointers and floats. |
| [LegacyCursorPalette](../tables/LegacyCursorPalette.md) | Executable (initialised data) |  | 24 rows of 2 bytes | Palette words of the legacy cursor highlight (a pale ramp). |
| [LegacyCursorPositions](../tables/LegacyCursorPositions.md) | Executable |  | 31 rows of 2 bytes | Cursor (x, y) positions of the legacy item pages (from +0x10) and a 5-byte group list at +0; the tail of the 0x90-byte object holds three save file name strings. |
| [LegacyCursorRowsLang0](../tables/LegacyCursorRowsLang0.md) | Executable (initialised data) |  | about 33 rows of 24 bytes | Cursor row table of a legacy menu, language 0 variant: 24-byte rows holding the cursor x, y and a key; the candidate address is the third halfword of the first row (base + 4). |
| [LegacyCursorRowsLangOther](../tables/LegacyCursorRowsLangOther.md) | Executable (initialised data) |  | about 33 rows of 24 bytes | Cursor row table of the same legacy menu for the languages other than 0; 30 bytes differ from the language 0 table. |
| [LegacyItemCursorTemplates](../tables/LegacyItemCursorTemplates.md) | Executable |  | 5 rows of 8 bytes | Five pointer slots (first empty) to the cursor window templates of the legacy item pages. |
| [LegacyItemListBodyGridA](../tables/LegacyItemListBodyGridA.md) | Executable (initialised data) |  | 1 grid (0x1280 bytes) | Cell code grid of a large legacy list body (variant a). |
| [LegacyItemListBodyGridB](../tables/LegacyItemListBodyGridB.md) | Executable (initialised data) |  | 1 grid (0xBA0 bytes) | Cell code grid of a large legacy list body (variant b). |
| [LegacyItemListLayoutLang0](../tables/LegacyItemListLayoutLang0.md) | Executable (initialised data) |  | 1 script (0x190 bytes) | Layout script of the item list page of the legacy party menu, language 0 variant. |
| [LegacyItemListLayoutLang1](../tables/LegacyItemListLayoutLang1.md) | Executable (initialised data) |  | 1 script (0x190 bytes) | Layout script of the item list page of the legacy party menu, language 1 variant. |
| [LegacyItemListLayoutLang2](../tables/LegacyItemListLayoutLang2.md) | Executable (initialised data) |  | 1 script (0x190 bytes) | Layout script of the item list page of the legacy party menu, language 2 variant. |
| [LegacyItemListLayoutLang3](../tables/LegacyItemListLayoutLang3.md) | Executable (initialised data) |  | 1 script (0x190 bytes) | Layout script of the item list page of the legacy party menu, language 3 variant. |
| [LegacyItemUseLayoutLang0](../tables/LegacyItemUseLayoutLang0.md) | Executable (initialised data) |  | 1 script (0x100 bytes) | Layout script of the item use page of the legacy party menu (using an item on a unit), language 0 variant. |
| [LegacyItemUseLayoutLang1](../tables/LegacyItemUseLayoutLang1.md) | Executable (initialised data) |  | 1 script (0x100 bytes) | Layout script of the item use page of the legacy party menu (using an item on a unit), language 1 variant. |
| [LegacyItemUseLayoutLang2](../tables/LegacyItemUseLayoutLang2.md) | Executable (initialised data) |  | 1 script (0x100 bytes) | Layout script of the item use page of the legacy party menu (using an item on a unit), language 2 variant. |
| [LegacyItemUseLayoutLang3](../tables/LegacyItemUseLayoutLang3.md) | Executable (initialised data) |  | 1 script (0x100 bytes) | Layout script of the item use page of the legacy party menu (using an item on a unit), language 3 variant. |
| [LegacyJobChoiceLayoutLang0](../tables/LegacyJobChoiceLayoutLang0.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Layout script of the job choice page of the legacy party menu (the page that lists a unit's jobs and applies a change), language 0 variant. |
| [LegacyJobChoiceLayoutLang1](../tables/LegacyJobChoiceLayoutLang1.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Layout script of the job choice page of the legacy party menu (the page that lists a unit's jobs and applies a change), language 1 variant. |
| [LegacyJobChoiceLayoutLang2](../tables/LegacyJobChoiceLayoutLang2.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Layout script of the job choice page of the legacy party menu (the page that lists a unit's jobs and applies a change), language 2 variant. |
| [LegacyJobChoiceLayoutLang3](../tables/LegacyJobChoiceLayoutLang3.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Layout script of the job choice page of the legacy party menu (the page that lists a unit's jobs and applies a change), language 3 variant. |
| [LegacyJobDetailLayoutLang0](../tables/LegacyJobDetailLayoutLang0.md) | Executable (initialised data) |  | 1 script (0x1F0 bytes) | Layout script of the job detail page of the legacy party menu (four pages of the chosen job), language 0 variant. |
| [LegacyJobDetailLayoutLang1](../tables/LegacyJobDetailLayoutLang1.md) | Executable (initialised data) |  | 1 script (0x1F0 bytes) | Layout script of the job detail page of the legacy party menu (four pages of the chosen job), language 1 variant. |
| [LegacyJobDetailLayoutLang2](../tables/LegacyJobDetailLayoutLang2.md) | Executable (initialised data) |  | 1 script (0x1F0 bytes) | Layout script of the job detail page of the legacy party menu (four pages of the chosen job), language 2 variant. |
| [LegacyJobDetailLayoutLang3](../tables/LegacyJobDetailLayoutLang3.md) | Executable (initialised data) |  | 1 script (0x280 bytes) | Layout script of the job detail page of the legacy party menu (four pages of the chosen job), language 3 variant. |
| [LegacyJobScreenLayoutLang0](../tables/LegacyJobScreenLayoutLang0.md) | Executable (initialised data) |  | 1 record (0x19B0 bytes) | Language 0 variant of the legacy page layout: a header of row sizes and a grid of cell codes (the other languages are smaller blocks). |
| [LegacyListPageRangesLang0](../tables/LegacyListPageRangesLang0.md) | Executable (initialised data) |  | 120 rows of 2 bytes | Cumulative start ids that cut a long entry list (names of the legacy list page) into categories; language 0 variant. |
| [LegacyListPageRangesLang1](../tables/LegacyListPageRangesLang1.md) | Executable (initialised data) |  | 120 rows of 2 bytes | Cumulative start ids that cut a long entry list (names of the legacy list page) into categories; language 1 variant. |
| [LegacyListPageRangesLang2](../tables/LegacyListPageRangesLang2.md) | Executable (initialised data) |  | 120 rows of 2 bytes | Cumulative start ids that cut a long entry list (names of the legacy list page) into categories; language 2 variant. |
| [LegacyListRowSlot](../tables/LegacyListRowSlot.md) | Executable |  | 48 rows of 1 byte | Sparse byte map from a list row code to a slot number; nearly all entries are 0. |
| [LegacyMenuNodesDefault](../tables/LegacyMenuNodesDefault.md) | Executable (initialised data, written at run time) |  | 63 rows of 88 bytes | Legacy menu tree, language 1 (default). |
| [LegacyMenuNodesLanguage0](../tables/LegacyMenuNodesLanguage0.md) | Executable (initialised data, written at run time) |  | 63 rows of 88 bytes | Legacy battle / scene menu tree, language 0: 63 nodes of 88 bytes; mutable at run time. |
| [LegacyMenuNodesLanguage2](../tables/LegacyMenuNodesLanguage2.md) | Executable (initialised data, written at run time) |  | 63 rows of 88 bytes | Legacy menu tree, language 2. |
| [LegacyMenuNodesLanguage3](../tables/LegacyMenuNodesLanguage3.md) | Executable (initialised data, written at run time) |  | 63 rows of 88 bytes | Legacy menu tree, language 3. |
| [LegacyMenuRowCounts](../tables/LegacyMenuRowCounts.md) | Executable |  | 48 rows of 1 byte | Number of rows of each legacy menu (the list is LegacyMenuRowListPointers). |
| [LegacyMenuRowIcons](../tables/LegacyMenuRowIcons.md) | Executable |  | 16 rows of 1 bytes | A run of 16 consecutive row codes followed by a table of 88 u16 cell ids: menu row decoration data of the legacy menus. |
| [LegacyMenuRowListPointers](../tables/LegacyMenuRowListPointers.md) | Executable |  | 48 rows of 8 bytes | Pointers to the byte lists of row ids of each legacy menu; the matching row counts are LegacyMenuRowCounts. |
| [LegacyMenuRowResults](../tables/LegacyMenuRowResults.md) | Executable (initialised data) |  | 31 rows of 16 bytes | Per legacy menu, the result code of each row (and which menus remember the row per unit). |
| [LegacyMenuTaskSetups](../tables/LegacyMenuTaskSetups.md) | Executable |  | 4 rows of 48 bytes | Per menu state, the three pane tasks of the legacy menu with their task ids and owner ids. |
| [LegacyOptionsDefaultChoices](../tables/LegacyOptionsDefaultChoices.md) | Executable (initialised data) |  | 12 rows of 4 bytes | Default choice of each of the 12 options of the legacy options screen. |
| [LegacyOptionsTextBases](../tables/LegacyOptionsTextBases.md) | Executable (initialised data) |  | 12 rows of 4 bytes | Per option of the legacy options screen, the message id of its first choice label. |
| [LegacyRowCellDescriptors](../tables/LegacyRowCellDescriptors.md) | Executable |  | 9 rows of 24 bytes (from this address) | Sprite cell descriptors of the item list row drawer, 24 bytes each. |
| [LegacyTask10CellsSlot0](../tables/LegacyTask10CellsSlot0.md) | Executable (initialised data) |  | 28 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 0, variant 0. |
| [LegacyTask10CellsSlot1](../tables/LegacyTask10CellsSlot1.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 0, variant 1. |
| [LegacyTask10CellsSlot10](../tables/LegacyTask10CellsSlot10.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 2, variant 2. |
| [LegacyTask10CellsSlot11](../tables/LegacyTask10CellsSlot11.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 2, variant 3. |
| [LegacyTask10CellsSlot12](../tables/LegacyTask10CellsSlot12.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 3, variant 0. |
| [LegacyTask10CellsSlot13](../tables/LegacyTask10CellsSlot13.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 3, variant 1. |
| [LegacyTask10CellsSlot14](../tables/LegacyTask10CellsSlot14.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 3, variant 2. |
| [LegacyTask10CellsSlot15](../tables/LegacyTask10CellsSlot15.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 3, variant 3. |
| [LegacyTask10CellsSlot2](../tables/LegacyTask10CellsSlot2.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 0, variant 2. |
| [LegacyTask10CellsSlot3](../tables/LegacyTask10CellsSlot3.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 0, variant 3. |
| [LegacyTask10CellsSlot4](../tables/LegacyTask10CellsSlot4.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 1, variant 0. |
| [LegacyTask10CellsSlot5](../tables/LegacyTask10CellsSlot5.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 1, variant 1. |
| [LegacyTask10CellsSlot6](../tables/LegacyTask10CellsSlot6.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 1, variant 2. |
| [LegacyTask10CellsSlot7](../tables/LegacyTask10CellsSlot7.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 1, variant 3. |
| [LegacyTask10CellsSlot8](../tables/LegacyTask10CellsSlot8.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 2, variant 0. |
| [LegacyTask10CellsSlot9](../tables/LegacyTask10CellsSlot9.md) | Executable (initialised data) |  | 24 rows of 12 bytes | Sprite cell list of the legacy scene task 10, language 2, variant 1. |
| [LegacyTask12CommandsA](../tables/LegacyTask12CommandsA.md) | Executable (initialised data) |  | 1 block (0x1E0 bytes) | Command row block of the legacy scene task 12 (text labels and live pointers). |
| [LegacyTask12CommandsB](../tables/LegacyTask12CommandsB.md) | Executable (initialised data) |  | 1 block (length unknown) | Command row block of the legacy scene task 12 for the other mode. |
| [LegacyTask12LayoutLang0](../tables/LegacyTask12LayoutLang0.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Cell list of the legacy scene task 12, language 0 variant. |
| [LegacyTask12LayoutLang1](../tables/LegacyTask12LayoutLang1.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Cell list of the legacy scene task 12, language 1 variant. |
| [LegacyTask12LayoutLang2](../tables/LegacyTask12LayoutLang2.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Cell list of the legacy scene task 12, language 2 variant. |
| [LegacyTask12LayoutLang3](../tables/LegacyTask12LayoutLang3.md) | Executable (initialised data) |  | 1 script (0x110 bytes) | Cell list of the legacy scene task 12, language 3 variant. |
| [LegacyTask13LayoutMode13](../tables/LegacyTask13LayoutMode13.md) | Executable (initialised data) |  | 1 block (0x1C0 bytes) | Layout block of the legacy scene task 13 for mode 13. |
| [LegacyTask13LayoutOther](../tables/LegacyTask13LayoutOther.md) | Executable (initialised data) |  | 1 block (0x1C0 bytes) | Layout block of the legacy scene task 13 for every other mode. |
| [LegacyTitleMenuOffsets](../tables/LegacyTitleMenuOffsets.md) | Executable |  | 6 rows of 2 bytes | Six signed offsets applied to the opening menu slots; the same 0x30-byte object continues with a float (0.01), a list of cell ids and two 5-byte lists. |
| [MessageWindowTagCellsDefault](../tables/MessageWindowTagCellsDefault.md) | Executable (initialised data) |  | 20 rows of 12 bytes | Message window decoration cells, default (language 1) variant. |
| [MessageWindowTagCellsLanguage0](../tables/MessageWindowTagCellsLanguage0.md) | Executable (initialised data) |  | 20 rows of 12 bytes | Message window decoration cells, language 0 variant. |
| [MessageWindowTagCellsLanguage2](../tables/MessageWindowTagCellsLanguage2.md) | Executable (initialised data) |  | 20 rows of 12 bytes | Sprite cells (4 per window kind 5..9) decorating message windows, language 2 variant. |
| [MessageWindowTagCellsLanguage3](../tables/MessageWindowTagCellsLanguage3.md) | Executable (initialised data) |  | 20 rows of 12 bytes | Message window decoration cells, language 3 variant. |
| [NxdDataConfigCategory](../tables/NxdDataConfigCategory.md) | NXD file | 249 | 16 rows of 16 bytes | Settings menu categories: the item ids each contains and a UI text key for the title. |
| [NxdDataConfigItem](../tables/NxdDataConfigItem.md) | NXD file | 250 | 61 rows of 76 bytes | Settings menu rows (61): pad list, name and description UI text keys and value-kind parameters. |
| [NxdDataConfigItemButtonType](../tables/NxdDataConfigItemButtonType.md) | NXD file | 288 | 2 rows of 12 bytes | Option values for the button-style setting. |
| [NxdDataConfigItemCursorMoveType](../tables/NxdDataConfigItemCursorMoveType.md) | NXD file | 268 | 2 rows of 20 bytes | Option values for the cursor-movement setting. |
| [NxdDataConfigItemEnableDOF](../tables/NxdDataConfigItemEnableDOF.md) | NXD file | 271 | 3 rows of 12 bytes | Option values for the depth-of-field setting. |
| [NxdDataConfigItemForwardEnabledType](../tables/NxdDataConfigItemForwardEnabledType.md) | NXD file | 323 | 3 rows of 12 bytes | Option values for the fast-forward enable setting, with UI text keys. |
| [NxdDataConfigItemResolution](../tables/NxdDataConfigItemResolution.md) | NXD file | 252 | 9 rows of 8 bytes | Option list of the resolution setting (nine rows pointing at Resolution). |
| [NxdDataConfigItemScreenMode](../tables/NxdDataConfigItemScreenMode.md) | NXD file | 251 | 3 rows of 12 bytes | Option values for the screen-mode setting. |
| [NxdDataConfigItemTextLanguage](../tables/NxdDataConfigItemTextLanguage.md) | NXD file | 260 | 7 rows of 12 bytes | Option values for the text-language setting (seven languages). |
| [NxdDataConfigItemVoiceLanguage](../tables/NxdDataConfigItemVoiceLanguage.md) | NXD file | 259 | 2 rows of 12 bytes | Option values for the voice-language setting (two). |
| [NxdDataConfigPadAssign](../tables/NxdDataConfigPadAssign.md) | NXD file | 270 | 4 rows of 20 bytes | Pad button assignment presets keyed by two ids. |
| [NxdDataConfigPadList](../tables/NxdDataConfigPadList.md) | NXD file | 273 | 4 rows of 20 bytes | Four pad lists used by settings rows. |
| [NxdDataCursorMoveType](../tables/NxdDataCursorMoveType.md) | NXD file | 267 | 2 rows of 8 bytes | Two cursor movement types. |
| [NxdDataDifficultyLevel](../tables/NxdDataDifficultyLevel.md) | NXD file | 111 | 3 rows of 28 bytes | The three play modes: UI text key and numeric parameters. |
| [NxdDataFloorCursorSpeed](../tables/NxdDataFloorCursorSpeed.md) | NXD file | 262 | 4 rows of 8 bytes | Four cursor speeds. |
| [NxdDataForwardEnabledType](../tables/NxdDataForwardEnabledType.md) | NXD file | 324 | 3 rows of 8 bytes | Three fast-forward permission types. |
| [NxdDataIcon](../tables/NxdDataIcon.md) | NXD file | 118 | 1400 rows of 16 bytes | Icon id to image file path (1400 rows). |
| [NxdDataIconGroup](../tables/NxdDataIconGroup.md) | NXD file | 29 | 75 rows of 12 bytes | Icon group parameters (75 rows). |
| [NxdDataLanguage](../tables/NxdDataLanguage.md) | NXD file | 261 | 7 rows of 12 bytes | The seven game languages. |
| [NxdDataMessageWindowAnimationType](../tables/NxdDataMessageWindowAnimationType.md) | NXD file | 245 | 9 rows of 28 bytes | Message window animation parameters (nine types). |
| [NxdDataSystemParam](../tables/NxdDataSystemParam.md) | NXD file | 84 | 71 rows of 12 bytes | System parameter values (71). |
| [NxdDataUIAbilityIcon](../tables/NxdDataUIAbilityIcon.md) | NXD file | 31 | 55 rows of 8 bytes | Ability icon variants (55). |
| [NxdDataUIAddon](../tables/NxdDataUIAddon.md) | NXD file | 24 | 264 rows of 36 bytes | UI add-on definitions (264): UI file path and flags. |
| [NxdDataUIAddonPriority](../tables/NxdDataUIAddonPriority.md) | NXD file | 81 | 8 rows of 12 bytes | UI add-on priorities (8). |
| [NxdDataUIAnnounce](../tables/NxdDataUIAnnounce.md) | NXD file | 68 | 123 rows of 28 bytes | Announcement banner definitions (123). |
| [NxdDataUIButton](../tables/NxdDataUIButton.md) | NXD file | 322 | 21 rows of 12 bytes | UI button definitions (21). |
| [NxdDataUIButtonGuide](../tables/NxdDataUIButtonGuide.md) | NXD file | 33 | 1152 rows of 40 bytes | Button guide footer layouts keyed by screen and slot (1152). |
| [NxdDataUIColor](../tables/NxdDataUIColor.md) | NXD file | 20 | 201 rows of 12 bytes | Named UI colours (201). |
| [NxdDataUIDialog](../tables/NxdDataUIDialog.md) | NXD file | 34 | 241 rows of 60 bytes | Dialog definitions (241): text and option UI text keys. |
| [NxdDataUIEquipAbilitySlot](../tables/NxdDataUIEquipAbilitySlot.md) | NXD file | 62 | 12 rows of 16 bytes | Equipment screen ability slot layout (12). |
| [NxdDataUIEquipDetailNumParam](../tables/NxdDataUIEquipDetailNumParam.md) | NXD file | 198 | 9 rows of 12 bytes | Equipment detail number fields, keyed by field and variant. |
| [NxdDataUIFilePathExchange](../tables/NxdDataUIFilePathExchange.md) | NXD file | 125 | 5 rows of 12 bytes | UI file replacement mapping (5). |
| [NxdDataUIFontSet](../tables/NxdDataUIFontSet.md) | NXD file | 21 | 100 rows of 100 bytes | Font sets (100) as groups of font type ids. |
| [NxdDataUIFontType](../tables/NxdDataUIFontType.md) | NXD file | 27 | 19 rows of 24 bytes | Font types (19) with file path. |
| [NxdDataUILoadTexturePath](../tables/NxdDataUILoadTexturePath.md) | NXD file | 143 | 32 rows of 8 bytes | Loading screen texture paths (32). |
| [NxdDataUIMenuButtonLeft](../tables/NxdDataUIMenuButtonLeft.md) | NXD file | 180 | 8 rows of 32 bytes | Left menu buttons (8). |
| [NxdDataUIMenuSortList](../tables/NxdDataUIMenuSortList.md) | NXD file | 43 | 33 rows of 16 bytes | Menu sort option lists keyed by menu and slot. |
| [NxdDataUIMenuTab](../tables/NxdDataUIMenuTab.md) | NXD file | 95 | 6 rows of 8 bytes | Menu tabs keyed by menu and slot (6). |
| [NxdDataUIModal](../tables/NxdDataUIModal.md) | NXD file | 333 | 27 rows of 24 bytes | Modal window definitions (27). |
| [NxdDataUIMouseCollision](../tables/NxdDataUIMouseCollision.md) | NXD file | 329 | 21 rows of 12 bytes | UI mouse pick boxes (21). |
| [NxdDataUISubMenu](../tables/NxdDataUISubMenu.md) | NXD file | 139 | 3 rows of 20 bytes | Sub menu definitions (3). |
| [NxdDataUISubTab](../tables/NxdDataUISubTab.md) | NXD file | 61 | 59 rows of 16 bytes | Sub tabs keyed by tab group and slot (59). |
| [NxdDataUISystemParam](../tables/NxdDataUISystemParam.md) | NXD file | 23 | 301 rows of 8 bytes | UI system parameter values (301). |
| [NxdDataUIUnitStatusNumParam](../tables/NxdDataUIUnitStatusNumParam.md) | NXD file | 197 | 19 rows of 16 bytes | Unit status number fields (19). |
| [OpeningSpriteLists](../tables/OpeningSpriteLists.md) | Executable (initialised data) |  | 152 rows of 8 bytes | Per-language pointer sets of the opening sprite cell lists: four sets of 12 pointers, then four sets of 26. |
| [OpeningStepMaps](../tables/OpeningStepMaps.md) | Executable |  | 40 rows of 1 bytes | Byte step maps of the opening sequence plus three resource path strings (the title texture and two message texture files). |
| [PanelCellGroupPointers](../tables/PanelCellGroupPointers.md) | Executable (initialised data) |  | 32 rows of 8 bytes | Pointers to the sprite cell groups of the status window frame (four languages of eight modes). |
| [PanelScreenPalette](../tables/PanelScreenPalette.md) | Executable (initialised data) |  | 256 rows of 2 bytes | UI palette block of the second panel screen; the first 62 bytes equal EquipScreenPalette. |
| [PanelSlideCurve](../tables/PanelSlideCurve.md) | Executable |  | 12 rows of 2 bytes | Easing curve (symmetric, peak 144) a battle unit panel uses to slide a part of the panel in and out. |
| [PanelStateOffsets](../tables/PanelStateOffsets.md) | Executable |  | 16 rows of 1 bytes | A short list of signed offsets a unit panel row builder adds to a position; the bytes 0x2E, 0, 0, 0, 0, 0, 13, 13, 31, 31, 0, 0, -2, -1, -1, -1. |
| [SceneMenuNodesADefault](../tables/SceneMenuNodesADefault.md) | Executable (initialised data) |  | 7 rows of 88 bytes | Seven legacy menu nodes of the scene menus, first group, default language. |
| [SceneMenuNodesALanguage0](../tables/SceneMenuNodesALanguage0.md) | Executable (initialised data) |  | 7 rows of 88 bytes | Seven legacy menu nodes of the scene menus, first group, language 0. |
| [SceneMenuNodesBDefault](../tables/SceneMenuNodesBDefault.md) | Executable (initialised data) |  | 7 rows of 88 bytes | Seven legacy menu nodes of the scene menus, second group, default language. |
| [SceneMenuNodesBLanguage0](../tables/SceneMenuNodesBLanguage0.md) | Executable (initialised data) |  | 7 rows of 88 bytes | Seven legacy menu nodes of the scene menus, second group, language 0. |
| [ScreenTaskSets](../tables/ScreenTaskSets.md) | Executable |  | 9 rows of 64 bytes | The window tasks started together for each legacy screen set (four handlers, their slot numbers, their expected tags). |
| [SpriteAnimScripts](../tables/SpriteAnimScripts.md) | Executable |  | 18 rows of 8 bytes | Eighteen sprite animation frame lists of the opening / title sprites: each frame is a cell group index and a number of ticks. |
| [UiCoreNameKeys](../tables/UiCoreNameKeys.md) | Executable |  | 43 rows of 8 bytes | The 43 fixed names the UI system registers first: widget events (Show, Hide, Enable, Disable, FocusIn, FocusOut, CursorOver, CursorOut, Click, Check, Open, Close, gauge and scroll events, In / Out), widget part names ... |
| [UiEquipScreenNodeNames](../tables/UiEquipScreenNodeNames.md) | Executable |  | 9 rows of 8 bytes | Names of the nodes and animations of the HD equipment screen. |
| [UiEventCommandNames](../tables/UiEventCommandNames.md) | Executable |  | 8 rows of 8 bytes | Command words of the event window markup (forced, wait, cursor, cursor end, no set, value set, time, branch). |
| [UiEventWindowFontAndNameNodeRun](../tables/UiEventWindowFontAndNameNodeRun.md) | Executable |  | 2 rows of 8 bytes at the head (the sweep run holds 182 slots) | Head list of 2 node name pointers (Normalfont, TextName); the run continues into class vtables (13 class vtables: event, common parts, gil and character number, notice dialog, main menu parts, horoscope affinity, job ... |
| [UiGlyphCodeTriples](../tables/UiGlyphCodeTriples.md) | Executable |  | 73 rows of 3 bytes | Scan list used to turn a character code 1..72 into a glyph slot (row index). |
| [UiGuideTipPageNamesRun](../tables/UiGuideTipPageNamesRun.md) | Executable |  | 6 rows of 8 bytes at the head (the sweep run holds 896 slots) | Head list of 6 node name pointers (page01 to page06); the run continues into class vtables (54 class vtables: guide, bar (profit, gossip, main list), menu base, shop, end slate, classic band / loading / subtitles, end... |
| [UiLauncherButtonOrder](../tables/UiLauncherButtonOrder.md) | Executable |  | 8 rows of 4 bytes (7 used) | Button ids of the start launcher in focus order. |
| [UiLauncherControllerGuideLabelsRun](../tables/UiLauncherControllerGuideLabelsRun.md) | Executable |  | 15 rows of 8 bytes at the head (the sweep run holds 25 slots) | Head list of 15 node name pointers (Controller button label nodes (L2, L1, select, d-pad, left stick, L3, R2, R1, right buttons, right stick, R3, start)); the run continues into class vtables (UIAddonFFTOLauncher (sec... |
| [UiLauncherFocusNeighborsAlt](../tables/UiLauncherFocusNeighborsAlt.md) | Executable |  | 7 rows of 24 bytes | Directional focus neighbours of the seven buttons of the start launcher, alternate layout (the default layout of the same shape is at 0x14070A8D0). |
| [UiLauncherModeNamesRun](../tables/UiLauncherModeNamesRun.md) | Executable |  | 2 rows of 8 bytes at the head (the sweep run holds 99 slots) | Head list of 2 node name pointers (EnhancedMode and ClassicMode node names); the run continues into class vtables (6 class vtables: launcher, title cushion, launcher agent, start config (two) and its agent). |
| [UiLegacyLayoutScriptOps](../tables/UiLegacyLayoutScriptOps.md) | Executable |  | 22 rows of 8 bytes | Handlers of the 22 opcodes of the legacy layout script (the record language of the job choice, job detail and other legacy pages: {opcode, length, arguments} until opcode 22). |
| [UiLegacyWindowCellLayoutBase](../tables/UiLegacyWindowCellLayoutBase.md) | Executable |  | about 81 rows of 12 bytes | Cell records (kind, size, offset) of a legacy list window, base set. |
| [UiLegacyWindowColourSetsLang1](../tables/UiLegacyWindowColourSetsLang1.md) | Executable |  | colour dwords (about 1888 bytes) | Colour set of a legacy list window, text language 1. |
| [UiLegacyWindowColourSetsLang2](../tables/UiLegacyWindowColourSetsLang2.md) | Executable |  | colour dwords (about 2000 bytes) | Colour set of a legacy list window, text language 2. |
| [UiLegacyWindowColourSetsLang3](../tables/UiLegacyWindowColourSetsLang3.md) | Executable |  | colour dwords (about 1632 bytes) | Colour set of a legacy list window, text language 3. |
| [UiLegacyWindowGroupStartsLang0](../tables/UiLegacyWindowGroupStartsLang0.md) | Executable |  | 12 rows of 1 byte (+4 padding) | Cumulative start indexes of 12 cell groups of a legacy list window, text language 0. |
| [UiLegacyWindowGroupStartsLang1](../tables/UiLegacyWindowGroupStartsLang1.md) | Executable |  | 12 rows of 1 byte (+4 padding) | Cumulative start indexes of 12 cell groups of a legacy list window, text language 1. |
| [UiLegacyWindowGroupStartsLang2](../tables/UiLegacyWindowGroupStartsLang2.md) | Executable |  | 12 rows of 1 byte (+4 padding) | Cumulative start indexes of 12 cell groups of a legacy list window, text language 2. |
| [UiLegacyWindowGroupStartsLang3](../tables/UiLegacyWindowGroupStartsLang3.md) | Executable |  | 12 rows of 1 byte (+4 padding) | Cumulative start indexes of 12 cell groups of a legacy list window, text language 3. |
| [UiPartyMemberPartNodeNamesRun](../tables/UiPartyMemberPartNodeNamesRun.md) | Executable |  | 6 rows of 8 bytes at the head (the sweep run holds 353 slots) | Head list of 6 node name pointers (six party member part nodes (parts, parts00 to parts04)); the run continues into class vtables (19 class vtables: save / load, system top, subtitles, novel, brave story (Darlavon, tr... |
| [UiRadioButtonNodeNamesRun](../tables/UiRadioButtonNodeNamesRun.md) | Executable |  | 4 rows of 8 bytes at the head (the sweep run holds 659 slots) | Head list of 4 node name pointers (RadioButton01 to RadioButton04); the run continues into class vtables (39 class vtables: system message, battle command, warning, announce, battle (continuous, dialog, flytext, join,... |
| [UiStartupScreenNodeNamesRun](../tables/UiStartupScreenNodeNamesRun.md) | Executable |  | 3 rows of 8 bytes at the head (the sweep run holds 557 slots) | Head list of 3 node name pointers (ShowEnFrDe, ShowJa, ShowTitle); the run continues into class vtables (41 class vtables: startup, text input, poach, employ and item screens, guide). |
| [UiStoryButtonNodeNamesRun](../tables/UiStoryButtonNodeNamesRun.md) | Executable |  | 10 rows of 8 bytes at the head (the sweep run holds 451 slots) | Head list of 10 node name pointers (ButtonArazlamL00..L02, S00..S03, Darlavon00..02); the run continues into class vtables (27 class vtables: brave story top, achievement notifications, novel manager callback, world m... |
| [UiTabButtonNodeNamesRun](../tables/UiTabButtonNodeNamesRun.md) | Executable |  | 3 rows of 8 bytes at the head (the sweep run holds 237 slots) | Head list of 3 node name pointers (TabButton01 to TabButton03); the run continues into class vtables (16 class vtables: brave story glossary, work history, zodiac stone, journal, collection, books). |
| [UnitEditorRangesA](../tables/UnitEditorRangesA.md) | Executable (initialised data) |  | 22 rows of 8 bytes | Value ranges of the 22 editable fields of the unit editor screen, mode A (level 1..99, brave / faith 0..100, three ability id ranges 144..171, 172..207, 208..239, ...). |
| [UnitEditorRangesB](../tables/UnitEditorRangesB.md) | Executable (initialised data) |  | 22 rows of 8 bytes | Value ranges of the unit editor, mode B: rows 0..13 equal mode A, rows 14..18 each allow 1..356 where mode A allows 1..187 twice and then three ranges 428..453, 454..485, 486..509, rows 19..21 equal mode A. Verdict: d... |
| [UnitEditorWidgetsDefault](../tables/UnitEditorWidgetsDefault.md) | Executable (initialised data) |  | 22 rows of 24 bytes | Widget records of the 22 editable fields of the unit editor screen, every other language. |
| [UnitEditorWidgetsLanguage0](../tables/UnitEditorWidgetsLanguage0.md) | Executable (initialised data) |  | 22 rows of 24 bytes | Widget records of the 22 editable fields of the unit editor screen, text language 0. |
| [UnitPageNumberFieldsA](../tables/UnitPageNumberFieldsA.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Number fields of the second unit page, first panel. |
| [UnitPageNumberFieldsB](../tables/UnitPageNumberFieldsB.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Number fields of the second unit page, second panel. |
| [UnitPanelCellsLanguage0](../tables/UnitPanelCellsLanguage0.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the unit status page, language 0 (18 cells). |
| [UnitPanelCellsLanguage1](../tables/UnitPanelCellsLanguage1.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the unit status page, language 1 (18 cells). |
| [UnitPanelCellsLanguage2](../tables/UnitPanelCellsLanguage2.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the unit status page, language 2 (18 cells). |
| [UnitPanelCellsLanguage3](../tables/UnitPanelCellsLanguage3.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the unit status page, language 3 (18 cells). |
| [UnitPanelNumberFieldsA](../tables/UnitPanelNumberFieldsA.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Number fields (Move, Jump, Wt, weapon powers, At, Def, Ar, Av and their magic pairs) of the unit status page, first panel. |
| [UnitPanelNumberFieldsB](../tables/UnitPanelNumberFieldsB.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Number fields of the unit status page, second panel. |
| [UnitPanelScriptBlock0](../tables/UnitPanelScriptBlock0.md) | Executable (initialised data) |  | 1 rectangle and 1 script block | A panel window rectangle followed by a UI script block of the unit panel page (block 0). |
| [UnitPanelScriptBlock1](../tables/UnitPanelScriptBlock1.md) | Executable (initialised data) |  | 1 rectangle and 1 script block | A panel window rectangle followed by a UI script block of the unit panel page (block 1). |
| [UnitPanelScriptBlock2](../tables/UnitPanelScriptBlock2.md) | Executable (initialised data) |  | 1 rectangle and 1 script block | A panel window rectangle followed by a UI script block of the unit panel page (block 2). |
| [UnitPanelScriptBlock3](../tables/UnitPanelScriptBlock3.md) | Executable (initialised data) |  | 1 rectangle and 1 script block | A panel window rectangle followed by a UI script block of the unit panel page (block 3). |
| [WindowCurvePointers](../tables/WindowCurvePointers.md) | Executable |  | 5 rows of 8 bytes | Pointers to the five window open / close animation step lists. |
| [WindowGrowSteps](../tables/WindowGrowSteps.md) | Executable |  | 12 rows of 1 bytes | Per-frame edge movement of the window grow animation for each window style. |
| [WindowPatternTiles](../tables/WindowPatternTiles.md) | Executable (initialised data) |  | 2088 rows of 2 bytes | Line patterns of the legacy window frames (borders and gradient rows) as 16-bit words, in a block of 2088 words. |
