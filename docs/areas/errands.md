# Errands

The timed dispatch system: records, scoring, rewards, start and finish.

Functions: 25, Structures: 1, Globals: 2, Observed behaviours: 2, Tables: 2.

## Functions (25)

| Name | Address | Purpose |
|---|---|---|
| [BarTop_Setup](../functions/BarTop_Setup.md) | `0x14019F330` | Sets up the tavern's top menu (rumors, errands): the errand row is open only when situation 3220 holds. |
| [DateBits_Store9](../functions/DateBits_Store9.md) | `0x1402CD274` | Stores a date (month, day) as 9 bits at position 9 * index of a bit array: the errand finish dates and the treasure find dates. |
| [Errand_ApplyResult](../functions/Errand_ApplyResult.md) | `0x140370054` | Applies a finished errand's result to the save: event flags, gil, loot, JP and the active list. |
| [Errand_BoardInput](../functions/Errand_BoardInput.md) | `0x1402ED540` | The tavern errand board's input step: dispatch a chosen errand, collect a returned one, recall one, or leave. |
| [Errand_BuildActiveList](../functions/Errand_BuildActiveList.md) | `0x140370F38` | Fills the board list with the errands that are away (dispatched and not yet back) for the legacy list window. |
| [Errand_BuildBoard](../functions/Errand_BuildBoard.md) | `0x1402ED078` | Builds the list of errands the tavern board shows: one entry per errand record, marked as available, dispatched or returning, with the preview of the units on a dispatched errand. |
| [Errand_BuildBoardEntry](../functions/Errand_BuildBoardEntry.md) | `0x1402EE0F0` | Decides whether an errand that is not dispatched goes on the tavern board and fills its board entry. |
| [Errand_ComputeRewards](../functions/Errand_ComputeRewards.md) | `0x1402D29C0` | Computes JP and gil rewards, the grade and the bonus loot for one active errand when it ends. |
| [Errand_Finish](../functions/Errand_Finish.md) | `0x14036FF30` | Ends an active errand: totals the gil, queues a result entry and applies the result. |
| [Errand_IsAvailable](../functions/Errand_IsAvailable.md) | `0x1402CCE20` | Decides whether an errand is offered at a town right now. |
| [Errand_IsOffered](../functions/Errand_IsOffered.md) | `0x1402EE0A4` | Whether an errand is offered at a town now: not dispatched, not completed, no delay left, and available there. |
| [Errand_LoadRecord](../functions/Errand_LoadRecord.md) | `0x1402CCDC4` | Copies one 23-byte errand (dispatch) definition out of the executable's errand data block into 23 16-bit words, resolving the two fee fields. |
| [Errand_ReactionPose](../functions/Errand_ReactionPose.md) | `0x1402D2CEC` | Chooses which reaction pose a unit shows in the errand result scene from its Brave, Faith and sex. |
| [Errand_Recall](../functions/Errand_Recall.md) | `0x1402EE1C8` | Calls off the dispatched errand selected on the board: its units come back and the errand is offered again. |
| [Errand_RollBonusLoot](../functions/Errand_RollBonusLoot.md) | `0x1402D3120` | On a successful errand (grade 0) picks a treasure or a random bonus and adds its JP and gil to the result. |
| [Errand_ScoreParty](../functions/Errand_ScoreParty.md) | `0x1402D2DB0` | Scores the 1 to 3 units sent on an errand and sets the party grade (0 best, 2 worst). |
| [Errand_SelectBoardEntry](../functions/Errand_SelectBoardEntry.md) | `0x1402ED7E0` | Opens the detail of a board errand: the tavern keeper's line, the record, and the legacy message window. |
| [Errand_Start](../functions/Errand_Start.md) | `0x14036A7D8` | Starts an errand from the prepared board selection: pays the fee, creates the active record and marks the errand started. |
| [Errand_TreasureMilestone](../functions/Errand_TreasureMilestone.md) | `0x1402D3520` | After a successful errand, reports whether the number of treasures found has reached a milestone. |
| [sub_14016E60C](../functions/sub_14016E60C.md) | `0x14016E60C` | Event handler of an errand screen: on event 0x10001 shows the two treasure-progress gauges (milestone counts). |
| [sub_1401A161C](../functions/sub_1401A161C.md) | `0x1401A161C` | The menu screen's decide step: it counts the entries in a list owned by the screen, reads the selected record's kind and switches the screen to the matching sub-state or help page. |
| [sub_1402CCEE0](../functions/sub_1402CCEE0.md) | `0x1402CCEE0` | Checks the errand state on a world tick: it reads the active errand slots and their delay bytes, ages the eggs, and posts the result message when an errand is due. |
| [sub_14036A294](../functions/sub_14036A294.md) | `0x14036A294` | Errand board painter: it seeds the board object, fills the 0x5C-byte board record and lays out the title, counter and per-errand text cells. |
| [Tavern_TopInput](../functions/Tavern_TopInput.md) | `0x1402D5210` | The tavern top screen's input step: rumors, errands, or leave. |
| [TownMenu_BuildItems](../functions/TownMenu_BuildItems.md) | `0x1403449B0` | Lists the town menu items of a settlement (Outfitter, Tavern, Warriors' Guild, Poachers' Den). |

## Structures (1)

| Name | Size (bytes) | Summary |
|---|---|---|
| [ErrandActiveSlot](../structs/ErrandActiveSlot.md) | 9 | One of the eight active errand slots at g_ErrandActive (9 bytes each, count g_ErrandActiveCount): a dispatch in progress or back, its errand, its days, the town it left from and up to three units. |

## Globals (2)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_ErrandActive](../globals/g_ErrandActive.md) | `0x1411A71A0` | `uint8[8][9]` | The eight active errand slot records, nine bytes each: flags, errand id, town and the three dispatched unit ids. |
| [g_ErrandDelay](../globals/g_ErrandDelay.md) | `0x1411A7140` | `uint8[96]` | The per-errand delay byte, one per errand id 0..95, saved with the game. |

## Observed behaviours (2)

| Name | Scope | Summary |
|---|---|---|
| [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md) | engine | An errand is an index 0..95 into five stores: its 23-byte record, a 4-bit state nibble in the event variables (864 + id), a delay byte, 9 bits of finish date and two new flags, plus the eight active slots that name it... |
| [TavernErrandsOpenAtSituationCounter450](../behaviors/TavernErrandsOpenAtSituationCounter450.md) | engine | The tavern's errand row is open only when UserSituation 3220 holds: situation counter 0 (the dword at g_UserSituation +24, or +104 with the bank bit) is at least 450, which event opcode 0xE9 raises with the story. |

## Tables (2)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [ErrandActive](../tables/ErrandActive.md) | Executable memory (saved with the game) |  | 8 rows of 9 entries of 1 byte | The eight active errand slot records, nine bytes each: flags, errand id, town and the three dispatched unit ids. |
| [ErrandDelay](../tables/ErrandDelay.md) | Executable memory (saved with the game) |  | 96 entries of 1 byte | The per-errand delay byte, one per errand id 0..95, saved with the game. |
