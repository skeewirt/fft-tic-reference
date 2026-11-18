# Battle

Battle logic outside the formulas: AI decisions and evaluation, action checks, ranges and targets, action resolution and execution, the turn engine (charge time, turn order, the timeline), the live unit table, status effects, the battle command menu and presentation, the ability and item lists, and the results and learning after a battle.

Functions: 315, Structures: 65, Globals: 48, Registries: 1, Flows: 5, Observed behaviours: 45, Tables: 89.

## Functions (315)

| Name | Address | Purpose |
|---|---|---|
| [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md) | `0x140320504` | Turns one packed four-byte action entry into the game's current-action block at `0x1418716A0`: it resolves the command, fills the action's range and presentation fields from the ability or item data, and for the item ... |
| [Action_PickTargetEquipment](../functions/Action_PickTargetEquipment.md) | `0x1403065C4` | Chooses which equipment slot a steal or break action aims at, from the target unit's hand and body slots, and reports the chosen slot and item to the action builder. |
| [Action_SetWeaponItem](../functions/Action_SetWeaponItem.md) | `0x1403098CC` | Fills the weapon item id of a battle action from the acting unit's equipped weapon, with 255 standing for empty hands and zero written for an empty or out-of-range id. |
| [Ai_ActionWorthOnUnit](../functions/Ai_ActionWorthOnUnit.md) | `0x14038B34C` | Tells the AI whether the action in g_AiCurrentAction is worth trying on unit `slot`: 0 no, 1 yes, 2 yes (a stronger case). |
| [Ai_StatusLastsTurns](../functions/Ai_StatusLastsTurns.md) | `0x14038BAB4` | Tells the battle AI whether a unit has a status and will still have it after the given number of its turns. |
| [Ai_SurveyTargets](../functions/Ai_SurveyTargets.md) | `0x14031FD40` | Before planning, goes over every unit and every action in the acting unit's action list and notes what those actions could do to each unit (hurt it, help it), then marks which of its own actions are worth planning with. |
| [Ai_UnitTurnStep](../functions/Ai_UnitTurnStep.md) | `0x14031F130` | Runs one step of an AI-controlled unit's decision (several frames per turn) and, when it is done, writes the chosen move and action. |
| [BannerWord_Draw](../functions/BannerWord_Draw.md) | `0x140227AD8` | Builds the gradient quads of one banner word image from its run of sprite cells. |
| [Battle_ActorResultLevels](../functions/Battle_ActorResultLevels.md) | `0x14030C704` | Applies the acting unit's action result and returns, in four bytes, what the level-up banners need: two result bytes, the new unit level and the new job level. |
| [Battle_AITurnPrepare](../functions/Battle_AITurnPrepare.md) | `0x14031F534` | Fills the per-unit AI table (visibility, HP/MP ratios, flags) and then runs one AI turn. |
| [Battle_AITurnRun](../functions/Battle_AITurnRun.md) | `0x14038A468` | Runs one AI trial: applies the candidate action on the preview unit table, lets the turn engine play on (up to 255 steps), scores the outcome and restores the engine state. |
| [Battle_ApplyActionResult](../functions/Battle_ApplyActionResult.md) | `0x14030A488` | Applies the pending action result of one unit to that unit: HP/MP damage and healing, stat changes, Brave/Faith changes, EXP/level changes, status sets/clears and the death check. |
| [Battle_ApplyActionResults](../functions/Battle_ApplyActionResults.md) | `0x140206758` | Applies the resolved action to every target and starts each target's hit animation; this is the step that turns the formula result into live HP/MP/status changes and visible hits. |
| [Battle_AwardActorJp](../functions/Battle_AwardActorJp.md) | `0x14030C7C4` | Gives the acting battle unit its JP for the current job and reports whether its job level changed (for the level-up message). |
| [Battle_AwardUnitJp](../functions/Battle_AwardUnitJp.md) | `0x14028338C` | Awards job JP to a battle unit after an action: it validates the unit, resolves its job index and JP amount, applies the award and reports the amount. |
| [Battle_BuildRosterTeam](../functions/Battle_BuildRosterTeam.md) | `0x140270CE4` | Fills the live 21-slot battle unit table (`g_BattleUnitTable`, `0x141853CE0`, stride 512) from a 5-entry spawn list, one team at a time. |
| [Battle_CommandTask](../functions/Battle_CommandTask.md) | `0x140202B08` | The per-frame player battle command task: advances the turn engine, claims the active unit, and puts up the command menu (Move / Abilities / Wait / Status) or hands the unit to the AI. |
| [Battle_ExecuteAction](../functions/Battle_ExecuteAction.md) | `0x140206A0C` | Executes the acting unit's pending action: resolves it against every target, selects the visual effect, and hands off to the result-apply loop or to the "no effect" branch. |
| [Battle_Init](../functions/Battle_Init.md) | `0x14020EF10` | Allocates and resets the battle singletons when a battle starts: BattleControl, post-battle calculator, a 3008-byte battle object, the map-view camera manager, markers and the command menu. |
| [Battle_InitScene](../functions/Battle_InitScene.md) | `0x1402C8818` | The battle scene initialiser started by event opcode 0x78 mode 7: it builds the battle UI, places the units and their markers, shows the cursor and waits for the battle to end. |
| [Battle_IsTileOccupied](../functions/Battle_IsTileOccupied.md) | `0x140282A7C` | Tests a map tile for the targeting cursor: bounds, terrain passability, the unit standing there and the large-monster exception for jobs 94..96. |
| [Battle_MenuClose](../functions/Battle_MenuClose.md) | `0x1402100F4` | Closes the command menu for the acting unit. |
| [Battle_MenuHidePage](../functions/Battle_MenuHidePage.md) | `0x140154308` | Hides the page for a menu id (or all six pages when `menuId == -1`). |
| [Battle_MenuOpen](../functions/Battle_MenuOpen.md) | `0x140210184` | Opens the command menu for the acting unit. |
| [Battle_MenuPageOfCommand](../functions/Battle_MenuPageOfCommand.md) | `0x140154248` | Maps a battle command/menu id to one of the six `BattleMenu` page numbers. |
| [Battle_MenuShowPage](../functions/Battle_MenuShowPage.md) | `0x140154624` | Shows one of the six command-menu pages and binds its radio buttons, icon and title. |
| [Battle_MoveRange_Build](../functions/Battle_MoveRange_Build.md) | `0x14027B2F0` | Builds the move range of one unit: sets up the scratch block, seeds the unit's tile with its Move budget, spreads the budget tile by tile and jump by jump, then commits the tiles the unit can stop on. |
| [Battle_MoveRange_CeilingAbove](../functions/Battle_MoveRange_CeilingAbove.md) | `0x14027C348` | The lowest underside, over both map layers of one column, that lies above a given height on one edge; 127 when there is none. |
| [Battle_MoveRange_CheckMount](../functions/Battle_MoveRange_CheckMount.md) | `0x14027C218` | For a target tile holding a mountable ally: records in the tile's mark byte 3 the budget with which the unit could get onto the mount. |
| [Battle_MoveRange_CheckSource](../functions/Battle_MoveRange_CheckSource.md) | `0x14027BAC4` | Prepares leaving the current tile in one direction: the height of the edge being left, the headroom above it and the budget record to spend from; returns non-zero when the tile cannot be left that way. |
| [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md) | `0x14027BD0C` | Tests one target of a step or jump (variant bit 0 = map layer, variant >= 2 = onto the unit standing there) and, when the unit can get there with a better budget, stores the budget and flags the tile as frontier. |
| [Battle_MoveRange_Commit](../functions/Battle_MoveRange_Commit.md) | `0x14027B7F0` | Turns the budgets into the lit set: decides for each of the 512 tiles whether the unit can stop there, counts them and writes the result to the tile table (bit 0x20 of tile byte +5) or to the marking table. |
| [Battle_MoveRange_Expand](../functions/Battle_MoveRange_Expand.md) | `0x14027C138` | Spreads the budget from the current frontier tile to its four neighbours. |
| [Battle_MoveRange_ExpandJump](../functions/Battle_MoveRange_ExpandJump.md) | `0x14027C5E0` | Spreads the budget from the current frontier tile by horizontal jumps: in each of the four straight lines, over 1 up to Jump / 2 tiles. |
| [Battle_MoveRange_GapBlocked](../functions/Battle_MoveRange_GapBlocked.md) | `0x14027C3DC` | Whether a column stops a horizontal jump that passes over it at a given height: anything (tile body or enemy) overlapping the band from the height to height + body blocks, and so does a column that is entirely above. |
| [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md) | `0x14027B530` | Clears the range marks, gives every tile its movement flag byte (slope, standable, blocked), stamps the other units onto their tiles and seeds the unit's own tile with Move + 1. |
| [Battle_MoveRange_OutOfBounds](../functions/Battle_MoveRange_OutOfBounds.md) | `0x14027BA88` | True when the target coordinates in the scratch (two signed words) are outside the map. |
| [Battle_MoveRange_WeatherCost](../functions/Battle_MoveRange_WeatherCost.md) | `0x14027AD6C` | The movement cost of the weather-dependent terrains: 1, 2 or 3 from event variable 35 and two bits of dword_140D3A830. |
| [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md) | `0x14027ADB8` | Prepares the globals the move-range expansion reads: it copies the acting unit move, jump, stance and status data into the range scratch block and fills the sixteen-entry blocker table. |
| [Battle_PreviewUnitAction](../functions/Battle_PreviewUnitAction.md) | `0x140282BDC` | Rebuilds the preview of the action a battle unit currently holds: it resets the per-unit target flags, resolves the action mode and range, and refills the preview block. |
| [Battle_ResolveAction](../functions/Battle_ResolveAction.md) | `0x1403099B0` | Resolves one action request against one target: selects the formula from the action type / ability, runs the formula handler and leaves a 40-byte result record for the apply step. |
| [Battle_ResolveReaction](../functions/Battle_ResolveReaction.md) | `0x140283C00` | Resolves a reaction or secondary action: it copies the action, rebuilds the preview and range, calls the action resolver and then the reaction bookkeeping. |
| [Battle_ResolveTargets](../functions/Battle_ResolveTargets.md) | `0x140281CE8` | Builds the target set for one action request and resolves the request against every target, producing one result record per target plus a summary of the whole action. |
| [Battle_ResultResetStatusSets](../functions/Battle_ResultResetStatusSets.md) | `0x14030A43C` | Clears the two pending status sets of an action-result block (and a five-byte scratch copy in the battle formula state). |
| [Battle_ShowJobLevelUp](../functions/Battle_ShowJobLevelUp.md) | `0x1402041D8` | Shows the job level-up banner over the acting unit when its action raised its job level. |
| [Battle_ShowUnitLevelUp](../functions/Battle_ShowUnitLevelUp.md) | `0x14020401C` | Shows the level-up banner over the acting unit when its action raised its unit level. |
| [Battle_StatusApply](../functions/Battle_StatusApply.md) | `0x14030CAA8` | Converts the pending status sets of one unit's action result block into applied status bits, after filtering them against the unit's innate/immunity sets. |
| [Battle_StatusRefresh](../functions/Battle_StatusRefresh.md) | `0x14030CA00` | Applies the pending status clears of a unit and recomputes the effective 40-bit status set. |
| [Battle_StatusResolve](../functions/Battle_StatusResolve.md) | `0x14030C87C` | Applies the pending status adds and removes of one battle unit: filters them, clears, sets, then settles the effects that depend on the new set. |
| [Battle_TimelineBuildList](../functions/Battle_TimelineBuildList.md) | `0x1402333E8` | Builds the 40-entry timeline list for the UI and overlays the acting unit's current command preview. |
| [Battle_TimelineRefresh](../functions/Battle_TimelineRefresh.md) | `0x140215E54` | Refreshes the Combat Timeline panel: builds the forecast, copies it into `g_TurnList`, and fills the visible rows (portrait, name, HP/MP, CT) and the scroll position. |
| [Battle_TurnEngine](../functions/Battle_TurnEngine.md) | `0x14030F030` | The battle turn state machine: ticks CT, picks the next unit, starts and finishes turns, and resolves charged actions. |
| [Battle_TurnStep](../functions/Battle_TurnStep.md) | `0x1402029DC` | Runs one step of the turn engine on the player path and dispatches the returned action code to the scene/UI. |
| [Battle_UnitStatusFill](../functions/Battle_UnitStatusFill.md) | `0x1402158F4` | Fills the battle status panel's view record (and the addon's cached fields) from the live unit table. |
| [BattleAct_SetupEffect](../functions/BattleAct_SetupEffect.md) | `0x1402060F4` | Selects the visual effect for an ability: builds the list of units on screen, reads the ability's charge byte from `g_AbilityAnim`, combines it with the ability element and calls the effect-number selector. |
| [BattleAction_ApplyRequest](../functions/BattleAction_ApplyRequest.md) | `0x140281434` | Wrapper that takes a request whose first byte is a unit slot, points at that unit action block, and applies the request; on success in the normal battle state it also refreshes the unit action. |
| [BattleAction_BuildUnitRequest](../functions/BattleAction_BuildUnitRequest.md) | `0x140283280` | Writes a command and action word into a unit action block, optionally marks the ring, and applies the request through the common wrapper. |
| [BattleAction_GetRangeInfo](../functions/BattleAction_GetRangeInfo.md) | `0x140281C24` | Chooses how an action acquires its range and area: the item path for the item-like command kinds and the ability record path otherwise, filling the caller flags and returning the range result. |
| [BattleAction_RunScript](../functions/BattleAction_RunScript.md) | `0x140234B3C` | The driver task for the battle presentation programs: reads the current script id from scene block 1, starts up to four sub-tasks defined by that script's 64-byte record, waits for them and repeats, then ends. |
| [BattleAction_StartScript](../functions/BattleAction_StartScript.md) | `0x140234A94` | Starts one of the seven battle presentation programs (the "scene script" table) and records the acting unit and target for the tasks that program starts. |
| [BattleAnim_SelectMotion](../functions/BattleAnim_SelectMotion.md) | `0x140269988` | Chooses the battle motion (animation id) for an ability: weapon attack, cast/ranged special, or a fixed motion from the per-ability table, then starts it on the unit. |
| [BattleAnim_SelectWeaponMotion](../functions/BattleAnim_SelectWeaponMotion.md) | `0x140269790` | Chooses the motion of a plain weapon attack from the attacker's weapon animation type and, for some types, from how high the target stands, then starts it. |
| [BattleAnim_StartMotion](../functions/BattleAnim_StartMotion.md) | `0x140268E04` | Starts a motion on a battle unit's scene object: stores the animation number and the facing value the unit's animation will use. |
| [BattleCommand_BuildMenu](../functions/BattleCommand_BuildMenu.md) | `0x1402EAD14` | The battle command task: it reads the cell text of the command menu, starts the list and screen tasks, and runs the menu until the unit action is chosen. |
| [BattleCommand_BuildScreen](../functions/BattleCommand_BuildScreen.md) | `0x1402E600C` | Builds the battle command/ability screen: the unit panels, the job record, the ability list entries and the equip detail panel the player navigates during a turn. |
| [BattleCommand_BuildUnitList](../functions/BattleCommand_BuildUnitList.md) | `0x1402EB174` | Builds the command list for the active unit: it asks the list builder for the commands, resolves their text and writes the cell words the menu reads. |
| [BattleCommand_CommitCursor](../functions/BattleCommand_CommitCursor.md) | `0x1402EB874` | Closes a battle command list: normalises its entries and stores the cursor row. |
| [BattleCommand_StoreCursorRow](../functions/BattleCommand_StoreCursorRow.md) | `0x1402EB828` | Remembers the cursor row of the current battle command menu for the acting unit. |
| [BattleControl_FrameUpdate](../functions/BattleControl_FrameUpdate.md) | `0x1401EA110` | Per-frame update of the battle control object; its first part sets the fast-forward level in battle straight from the held buttons. |
| [BattleLabel_ShowReactionSignal](../functions/BattleLabel_ShowReactionSignal.md) | `0x14014BFFC` | Draws a plain text label (a BattleSignal title) over a unit, in the TextReaction node. |
| [BattleLabel_ShowStatusSignal](../functions/BattleLabel_ShowStatusSignal.md) | `0x14014B87C` | Draws a styled status label over a unit: the BattleSignal row's title with the icon of the status that names the row. |
| [BattleMain_SetPanelJobRecord](../functions/BattleMain_SetPanelJobRecord.md) | `0x14010141C` | Stores a job record (the first 92 bytes) into one of the battle main screen's two unit panel blocks. |
| [BattleMenu_ConfirmRow](../functions/BattleMenu_ConfirmRow.md) | `0x140237B18` | Acts on a confirmed battle command menu row: picks the follow-up screen code and starts the scene task that shows it. |
| [BattleMenu_RunStep](../functions/BattleMenu_RunStep.md) | `0x1402381C4` | Runs one step of the battle menu step table: sets the current menu and starts the step's task. |
| [BattleMsg_Dispatch](../functions/BattleMsg_Dispatch.md) | `0x1402387C4` | Fills the battle message record from an event: it switches on the message kind, writes the kind and id of the record entries, starts the message scene task and resets the action-list widget state. |
| [BattleMsg_ResolveEntry](../functions/BattleMsg_ResolveEntry.md) | `0x1401EBBF4` | Renders one battle message record entry: reads its kind and id, resolves the text for that kind and returns the entry's text buffer. |
| [BattleMsg_SetCellText](../functions/BattleMsg_SetCellText.md) | `0x1402EBA70` | Reads a 2-byte word from the published unit list and writes it as the message id, with the fixed kind 6, into the battle message object the HUD draws. |
| [BattleMsg_SetKind1](../functions/BattleMsg_SetKind1.md) | `0x1401FA5C4` | Sets one battle message entry to kind 1 and stores its id. |
| [BattleMsg_SetKind6](../functions/BattleMsg_SetKind6.md) | `0x1401FA61C` | Sets one battle message record entry to kind 6 and stores its id. |
| [BattleMsg_UnitTurnScene](../functions/BattleMsg_UnitTurnScene.md) | `0x140237494` | Scene task that refreshes the battle message when a unit's turn starts: writes the acting unit's command or ability into record entry 0, starts the message scene tasks and resets the action-list widget states. |
| [BattlePreview_BuildAction](../functions/BattlePreview_BuildAction.md) | `0x140282234` | Builds the battle preview block for the action a unit is about to take: the preview word, the ability or item id, the target and the flags the cursor and forecast read. |
| [BattleRange_ApplyShape](../functions/BattleRange_ApplyShape.md) | `0x14027FFE8` | Applies the range shape and the effect area of an action to the cursor mask: it resolves the action record or the item path, marks the reachable tiles and then hands the effect area to the area marker. |
| [BattleRange_ClearWithin2](../functions/BattleRange_ClearWithin2.md) | `0x14027EB40` | Clears mark byte 0 (both layers) of every tile within Manhattan distance 2 of (x, y): the minimum range of the 'direct' weapons. |
| [BattleRange_FlagTargetTiles](../functions/BattleRange_FlagTargetTiles.md) | `0x14027FDD8` | Copies the range marks into the tile table: sets tile byte +5 bit 0x40 on every marked, targetable tile of both layers and returns how many it set. |
| [BattleRange_MarkArcReach](../functions/BattleRange_MarkArcReach.md) | `0x14027EE40` | The bow shape: tiles at Manhattan distance 3 or more whose distance, shortened by a quarter of the height the unit stands above them, is within the weapon range. |
| [BattleRange_MarkArea](../functions/BattleRange_MarkArea.md) | `0x140280B40` | Marks every tile of an action effect area: it reads the ability action record, builds the area offsets for the shape, and sets them relative to the target tile. |
| [BattleRange_MarkAttack](../functions/BattleRange_MarkAttack.md) | `0x14027FD2C` | Builds the target tiles of the Attack command (and of command kind 10): clears the range-mark array, marks the weapon's reach of the acting unit, removes the unit's own tile and flags the targetable tiles in the tile ... |
| [BattleRange_MarkRing](../functions/BattleRange_MarkRing.md) | `0x14027FE20` | Marks the outer ring of tiles an action can reach, from the twenty-byte action block, and returns the range value the range display uses. |
| [BattleRange_MarkStrikeOrLunge](../functions/BattleRange_MarkStrikeOrLunge.md) | `0x14027F0D0` | The melee shapes: the four adjacent tiles (flag 0x80), or two tiles in the four straight lines (flag 0x40 alone), each kept only inside a height band around the unit's reach height. |
| [BattleRange_MarkTileInBand](../functions/BattleRange_MarkTileInBand.md) | `0x14027F1D4` | Sets mark byte 0 = 1 for a map tile, separately in each layer, when that layer's target height is inside [max(lo, 0), hi]. |
| [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md) | `0x14027EFC0` | Marks in the range-mark array the tiles one unit's weapon reaches from its tile: picks the weapon, seeds the unit's tile and runs one of three shape routines chosen by the weapon's flag byte. |
| [BattleRange_SpreadDiamond](../functions/BattleRange_SpreadDiamond.md) | `0x14027EBF8` | Spreads the seeded marks outward one tile per pass for range passes, so every tile within Manhattan distance range of a seed gets a non-zero mark byte 0; heights are not looked at. |
| [BattleTask_Slot13Entry](../functions/BattleTask_Slot13Entry.md) | `0x140229D24` | One battle scene task, started as slot 13 by the battle program records 2, 3 and 6: refreshes scene state and runs the battle event/message runner that ends the task. |
| [BattleUnit_BuildCursorRecord](../functions/BattleUnit_BuildCursorRecord.md) | `0x140281248` | Builds the seven-byte cursor record a unit contributes to the targeting display: slot and flags, level, terrain height and the tile the cursor should sit on. |
| [BattleUnit_SetStatusVisual](../functions/BattleUnit_SetStatusVisual.md) | `0x1401FB064` | Sets or clears a status's visual bits on the unit's scene object: the tint / pose word or the sprite-change word. |
| [BTurn_FinishUnit](../functions/BTurn_FinishUnit.md) | `0x140310650` | Ends one unit's turn: clears the active flag and applies the post-turn CT bonus. |
| [BTurn_IsUnitDone](../functions/BTurn_IsUnitDone.md) | `0x140310704` | Decides whether the active unit has nothing left to do this turn, including the two-unit (partner) case. |
| [BTurn_MarkActionDone](../functions/BTurn_MarkActionDone.md) | `0x1403105B0` | Records that a unit has used its action and ends the turn if the move was already used. |
| [BTurn_MarkMoveDone](../functions/BTurn_MarkMoveDone.md) | `0x140310548` | Records that a unit has finished its move (and/or given up its action) and ends the turn when everything required is done. |
| [BTurn_OnTurnStartStatus](../functions/BTurn_OnTurnStartStatus.md) | `0x14030F9A0` | Runs the per-turn status roll at the moment a unit is selected (after `CT % 100`): decides whether the turn is consumed by a status and queues the pending status effects for the action block at `unit + 0x1BE`. |
| [BTurn_PreviewAction](../functions/BTurn_PreviewAction.md) | `0x14030FE60` | Previews what a unit's pending action does to the turn order: applies the request in simulation mode, builds the timeline and puts the unit back as it was. |
| [BTurn_QueueInvisibilityEnd](../functions/BTurn_QueueInvisibilityEnd.md) | `0x14030C240` | Queues the removal of Invisibility from a unit whose turn has ended, when the other conditions hold. |
| [BTurn_QueueTerrainPoison](../functions/BTurn_QueueTerrainPoison.md) | `0x14030C2C0` | Queues Poison for a unit that stands on a harmful terrain tile and passes the filter of the status rules. |
| [BTurn_StatusFlags](../functions/BTurn_StatusFlags.md) | `0x14030FB9C` | Returns the turn-scheduling flags of one unit work record: whether it can act at all, and whether Haste/Slow modify its CT increment. |
| [BUi_BattleMenuWindowsCtor](../functions/BUi_BattleMenuWindowsCtor.md) | `0x1401012A0` | Creates the two addons of the battle menu-windows agent: the battle HUD (`BattleMain4`) and the command menu (`BattleCommand`). |
| [BUi_BattleMenuWindowsSetPage](../functions/BUi_BattleMenuWindowsSetPage.md) | `0x1401015FC` | The command menu's show/hide entry point: maps a caller's state to a page show or hide. |
| [BUi_CommandAddonCtor](../functions/BUi_CommandAddonCtor.md) | `0x140153020` | Constructs the 5640-byte command-menu addon: vtable, sub-objects and idle field values. |
| [Effect_ClearCurrent](../functions/Effect_ClearCurrent.md) | `0x14031A7E0` | Clears the running effect: resets its bookkeeping and sets the current effect number to -1. |
| [Effect_PatchPolygonSeams](../functions/Effect_PatchPolygonSeams.md) | `0x140381834` | Nudges the texture coordinates of a few primitives of five stock effects by one or two units, keyed by the effect number. |
| [Effect_RunStateMachine](../functions/Effect_RunStateMachine.md) | `0x140319DA4` | Per-frame state machine of one battle effect: waits for the file load, uploads the texture, sets up the effect sections and runs the effect to its end. |
| [Effect_SelectForAbility](../functions/Effect_SelectForAbility.md) | `0x140319B50` | Picks the effect number for an effect word and starts the effect. |
| [Effect_TintByNxdScale](../functions/Effect_TintByNxdScale.md) | `0x1403845C0` | Updates one effect node: copies its position and angle into the node record and sets its colour, scaled by the effect number's table row. |
| [EffectAnchor_GetPoint](../functions/EffectAnchor_GetPoint.md) | `0x140384240` | Gives an effect's caster (index -1) or target (index 0..) position: a unit's scene position or a tile's centre. |
| [EffectEmitter_Spawn](../functions/EffectEmitter_Spawn.md) | `0x1403847D8` | Spawns the particles of one effect emitter at time t: count, position, velocity, mass, forces, life, homing and children from its 196-byte record. |
| [EffectFile_GetTrackRow](../functions/EffectFile_GetTrackRow.md) | `0x1402742CC` | Returns the two numbers that locate the data file of one battle effect: its file number in the game pack and its size in bytes. |
| [EffectFile_ResetBasePointers](../functions/EffectFile_ResetBasePointers.md) | `0x1402741BC` | Points every entry of the 512-slot effect base array at the one shared effect buffer. |
| [EffectFile_UploadTexture](../functions/EffectFile_UploadTexture.md) | `0x1402741E0` | Registers the two palettes and copies the picture stored at the end of the loaded effect file into the 1024 by 512 video page. |
| [EffectFlash_Start](../functions/EffectFlash_Start.md) | `0x140313F34` | Sequence kind 4 handler: the screen flash effect that tints the view with an element colour. |
| [EffectNxd_HasFlag24](../functions/EffectNxd_HasFlag24.md) | `0x1400D2AB8` | Reports whether the RefinedVFXTexture row of an effect has its byte at +24 set. |
| [EffectNxd_HasFlag25](../functions/EffectNxd_HasFlag25.md) | `0x1400D2B4C` | Reports whether the RefinedVFXTexture row of an effect has its byte at +25 set. |
| [EffectNxd_HasFlag28](../functions/EffectNxd_HasFlag28.md) | `0x1400D2BE0` | Reports whether the RefinedVFXTexture row of an effect has its byte at +28 set. |
| [EffectNxd_LoadRow](../functions/EffectNxd_LoadRow.md) | `0x1400D258C` | Reads the Enhanced parameter row of the current effect from the RefinedVFXTexture table (id 202) and applies it to the effect renderer and to the loaded effect data. |
| [EffectPalette_Step](../functions/EffectPalette_Step.md) | `0x140315620` | Sequence kind 18 handler: a full screen palette effect that starts from six seed colours. |
| [EffectParticle_StepPhysics](../functions/EffectParticle_StepPhysics.md) | `0x140388170` | Moves every effect particle one step: position by velocity, velocity by gravity, drag and force, force by its change or by homing. |
| [EffectScript_OpCallCallback](../functions/EffectScript_OpCallCallback.md) | `0x14031AC98` | Effect script opcode: runs one effect callback at once. |
| [EffectScript_OpLoadPhysics](../functions/EffectScript_OpLoadPhysics.md) | `0x14031B9DC` | Effect script opcode 0x27: loads the effect's gravity and drag from the header of section 3. |
| [EffectScript_OpRunTimeline](../functions/EffectScript_OpRunTimeline.md) | `0x14031C2DC` | Effect script opcode 0x28: runs one step of the effect's timeline (emitter tracks, colour tracks, sound tracks, camera tracks) and counts the frame. |
| [EffectScript_OpSetCallback](../functions/EffectScript_OpSetCallback.md) | `0x14031AC30` | Effect script opcode: attaches one of the effect callbacks to a live callback slot. |
| [EffectScript_OpUpdateParticles](../functions/EffectScript_OpUpdateParticles.md) | `0x14031B768` | Effect script opcode 0x25: moves every particle of the effect, draws it, runs its child emitters and removes it when its life ends. |
| [EffectScript_Run](../functions/EffectScript_Run.md) | `0x14031D658` | Runs the opcodes of one effect script until it yields or ends. |
| [EffectScript_RunColourTracks](../functions/EffectScript_RunColourTracks.md) | `0x14031BE2C` | Runs the colour-fade tracks of the effect timeline: palette fades on the screen, the caster and the targets. |
| [EffectScript_RunEmitterTracks](../functions/EffectScript_RunEmitterTracks.md) | `0x14031BC8C` | Runs the five emitter tracks of the effect timeline: each track is a list of phases, and the emitter of the running phase is asked to spawn particles. |
| [EffectSequence_Run](../functions/EffectSequence_Run.md) | `0x14031A3DC` | Per frame driver of the effect sequence entries: runs the handler of every active entry and retires finished ones. |
| [EffectSprite_EmitPieces](../functions/EffectSprite_EmitPieces.md) | `0x140380878` | Turns an effect sprite's current frame pieces into textured quads at the sprite's position. |
| [EffectSprite_StepAnimation](../functions/EffectSprite_StepAnimation.md) | `0x140387B70` | Steps one effect sprite's animation script and, on a frame change, points the sprite at the new frame's pieces; then draws it. |
| [EffectSprites_Spawn](../functions/EffectSprites_Spawn.md) | `0x140313210` | Creates the sprites of one effect sprite group when the effect is inside the group's frame window. |
| [EventUnitStatus_DispatchActiveIcons](../functions/EventUnitStatus_DispatchActiveIcons.md) | `0x140241080` | For one preview unit of an event scene, sends the status icon updater a message for every status the unit currently has. |
| [EventUnitStatus_SaveAndHide](../functions/EventUnitStatus_SaveAndHide.md) | `0x140241128` | For an event scene, saves the status state of a unit into the event unit store and clears the statuses the scene must not show. |
| [ItemAction_SetAmount](../functions/ItemAction_SetAmount.md) | `0x140306BD0` | The formula handler for the MP-restoring consumables: it rebuilds the used item's id, reads that item's chemist row and writes the item's amount into the battle result block. |
| [Job_ReadLearnedBitsForBattle](../functions/Job_ReadLearnedBitsForBattle.md) | `0x14020D190` | Walks the skillset of a work record's current job and tests each slot's learned bit (3 bytes at C +162 + 3*index). |
| [Map_LoadBattleData](../functions/Map_LoadBattleData.md) | `0x140251584` | Loads the per-map data of a battle map: its Move-Find row, its draw-index lists and its 4096-byte map block. |
| [MapAnim_Load](../functions/MapAnim_Load.md) | `0x1400C6D64` | Reads the map's anim file when the RefinedBgAnim rows ask for one. |
| [MapAnim_ReadRows](../functions/MapAnim_ReadRows.md) | `0x1400C795C` | Copies the RefinedBgAnim rows of a map into the anim set's per-entry table; returns 0 when any row's kind is 0. |
| [MapBlock_ApplyLayerCommand](../functions/MapBlock_ApplyLayerCommand.md) | `0x1402523B0` | Applies one layer's records of the loaded map block to the draw tables and, for layer 0 in the enhanced graphics mode, starts the map mesh, texture and anim loads. |
| [MapBlock_RunCommand](../functions/MapBlock_RunCommand.md) | `0x1402509E8` | Runs one command record of the loaded map block (layers, camera, palettes, lights) and dispatches the layer commands to MapBlock_ApplyLayerCommand. |
| [MapDrawLists_Load](../functions/MapDrawLists_Load.md) | `0x140249CB8` | Fills the two map draw-index bitsets from the per-map index lists of the current battle map. |
| [MapMesh_ApplyPolygonRows](../functions/MapMesh_ApplyPolygonRows.md) | `0x1400C9DCC` | Rebuilds the per-polygon override arrays from the RefinedBgMeshPolygon rows of the loaded map whenever the battle state value or the loaded map changed. |
| [MapMesh_FindNodeRows](../functions/MapMesh_FindNodeRows.md) | `0x1400D5934` | Finds the RefinedBgMeshNode rows of one map and variation: a pointer to the first row and the row count (0, 0 when there are none). |
| [MapMesh_InitNodeFlags](../functions/MapMesh_InitNodeFlags.md) | `0x1400C89F0` | Sets the 32 node slots of the mesh set to their start flags from the node rows, marks the nodes the mesh references, and applies the per-map stock offsets. |
| [MapMesh_Load](../functions/MapMesh_Load.md) | `0x1400C7F54` | Reads the map's mesh file into the mesh set and sets up its node rows; 0 = built, 1 = nothing built. |
| [MapMesh_Reset](../functions/MapMesh_Reset.md) | `0x1400CA258` | Clears the mesh set: node arrays, layer data and counts. |
| [MapMesh_StockNodeOffset](../functions/MapMesh_StockNodeOffset.md) | `0x1400C8D94` | A hard-coded list of position offsets for single nodes of nine stock maps; 0 for every other map and node. |
| [MapRenderer_ApplyMapRow](../functions/MapRenderer_ApplyMapRow.md) | `0x1400D5374` | Tears down a mesh set that belongs to another map or variation, then applies the chosen variation of the map's Map row to the renderer's post-effect settings. |
| [MapRenderer_ReuseLoadedMesh](../functions/MapRenderer_ReuseLoadedMesh.md) | `0x1400D55C4` | Re-runs the node setup of an already loaded mesh set (a second battle on the same map). |
| [MapRow_SelectVariation](../functions/MapRow_SelectVariation.md) | `0x140254B8C` | Chooses which variation struct of a map's Map row applies now, and a kind code, from four scene variables. |
| [MapTextures_LoadMapSlots](../functions/MapTextures_LoadMapSlots.md) | `0x1400CA690` | Requests the map's colour and lighting textures from the RefinedBgTexture rows, deduplicating equal names. |
| [MapTextures_LoadSystemSlots](../functions/MapTextures_LoadSystemSlots.md) | `0x1400CA47C` | Requests the 8 system textures of the map: names from RefinedBgSystemTexture, default colour table when there is none. |
| [MapTextures_NameOfFrame](../functions/MapTextures_NameOfFrame.md) | `0x1400CAA54` | Builds the file name of one frame of one slot of the map's textures; null when there is none. |
| [MapTextures_Reset](../functions/MapTextures_Reset.md) | `0x1400CA95C` | Releases every map and system texture of the texture set and sets its id fields to none. |
| [MapTextures_SlotVariantCode](../functions/MapTextures_SlotVariantCode.md) | `0x1400CACDC` | Returns the per-variation integer of a texture row minus one (0 when the entry is 0 or the row is absent). |
| [MessageWindow_OpenMode0](../functions/MessageWindow_OpenMode0.md) | `0x1402E092C` | Opens the legacy unit info message window for the acting unit with level and experience (mode 0). |
| [MessageWindow_OpenMode1](../functions/MessageWindow_OpenMode1.md) | `0x1402E09DC` | Opens the legacy unit info message window for the acting unit with the hit chance, after a preview of the action (mode 1). |
| [MessageWindow_OpenMode2](../functions/MessageWindow_OpenMode2.md) | `0x1402E0C2C` | Opens the legacy unit info message window for the target unit with the hit chance (mode 2). |
| [MessageWindow_OpenMode3](../functions/MessageWindow_OpenMode3.md) | `0x1402E098C` | Opens the legacy unit info message window for the target unit with level and experience (mode 3). |
| [MoveFind_ApplyTrap](../functions/MoveFind_ApplyTrap.md) | `0x14030C39C` | Applies the trap of a unit's tile to the unit as an action result. |
| [MoveFind_ProbeTile](../functions/MoveFind_ProbeTile.md) | `0x140271D80` | Reports what a battle tile hides: another unit, a Move-Find item not yet taken and a trap kind. |
| [MoveFind_TakeItem](../functions/MoveFind_TakeItem.md) | `0x140271CA8` | Gives a unit the Move-Find item of its tile: rolls common against rare by Brave and marks the tile taken. |
| [ResultLabel_QueueFromUnit](../functions/ResultLabel_QueueFromUnit.md) | `0x14026801C` | Fills a unit's label task from the unit's action-result block: which number and text labels to show, and the queue of status labels (BattleSignal ids) for the statuses the action added or removed. |
| [ResultLabel_ShowNext](../functions/ResultLabel_ShowNext.md) | `0x140266A68` | Shows the next pending label over a unit: a number (HP / MP / stat change), a fixed text, or the next queued status label. |
| [Scenario_CheckBattleRecord](../functions/Scenario_CheckBattleRecord.md) | `0x14020DFA8` | Finds the scenario setup record of the current event and lets the battle set-up continue only for a battle record. |
| [StatsPanel_Build](../functions/StatsPanel_Build.md) | `0x14022AC18` | Builds the detailed stats panel (display script 6): draws its numbers into VRAM and places its sprite cells. |
| [StatsScreen_Task](../functions/StatsScreen_Task.md) | `0x1402E1890` | Task of the legacy stats screen: builds its eighteen cell primitives and the stat number strips, then waits for a close. |
| [Status_ListCategory](../functions/Status_ListCategory.md) | `0x1400FAAB4` | Returns the list category of a status from its UIStatusEffect text row: 1 a gain, 2 an ailment, anything else not listed. |
| [Status_ListSortKey](../functions/Status_ListSortKey.md) | `0x1400FAB3C` | Returns the sort key of a status in the Status screen lists, from its UIStatusEffect text row. |
| [StatusList_BuildFromResultBlock](../functions/StatusList_BuildFromResultBlock.md) | `0x1402791FC` | Lists the statuses a result block adds and removes, as one byte per status, sorted by display priority. |
| [StatusList_BuildFromSet](../functions/StatusList_BuildFromSet.md) | `0x1402792B0` | Lists the statuses set in a five-byte status set, one byte per status, sorted by display priority. |
| [StatusScreen_BuildLists](../functions/StatusScreen_BuildLists.md) | `0x140112A04` | Fills the Status screen's two status lists (gains, ailments) from a five-byte status set, sorts them and draws them. |
| [StatusScreen_DrawLists](../functions/StatusScreen_DrawLists.md) | `0x140112B48` | Draws the Status screen's status list: one list item per gain, then per ailment, and the caption of the first. |
| [StatusScreen_SetCaption](../functions/StatusScreen_SetCaption.md) | `0x140113388` | Shows the caption (the help text) of the selected status on the Status screen. |
| [StatusScreen_SetEntry](../functions/StatusScreen_SetEntry.md) | `0x140112E84` | Sets one entry of the Status screen list: the status icon and the status name. |
| [sub_1400E615C](../functions/sub_1400E615C.md) | `0x1400E615C` | A guarded variant of the item-row text setter: it forwards an item id and four caller values to the item-row builder, but only when three UI subsystems are alive and the caller's kind is the one it serves. |
| [sub_140109134](../functions/sub_140109134.md) | `0x140109134` | Refreshes a battle-side panel object from a packed text id or from the panel's own selection fields. |
| [sub_140109F0C](../functions/sub_140109F0C.md) | `0x140109F0C` | A smaller sibling of sub_140109134: it finds one named text part of a UI object and fills it from a packed text id, choosing item, ability or a third source by the text kind. |
| [sub_1401560D0](../functions/sub_1401560D0.md) | `0x1401560D0` | Fills the four command radio buttons of a command screen: each button gets the icon and the title of the skillset named by its text token (name token 0xB000 \| set), so it is the one place a skillset's name is read str... |
| [sub_1401EC01C](../functions/sub_1401EC01C.md) | `0x1401EC01C` | Walks the forty battle message entries and resolves each one through the shared resolver. |
| [sub_1401F92A8](../functions/sub_1401F92A8.md) | `0x1401F92A8` | Fills the 106 rows of the PostBattleCalc object, one per formula id: the 12 formulas with an after-damage rule get a hook row, every other row holds the do-nothing marker. |
| [sub_1401F9CC4](../functions/sub_1401F9CC4.md) | `0x1401F9CC4` | A small preview of an item's effect amount: it repeats the HP-item formula's arithmetic but only when the battle state is in an item-preview phase, and writes the result into the same result block. |
| [sub_14020261C](../functions/sub_14020261C.md) | `0x14020261C` | Posts a battle message that depends on the current map, then marks the unit's action as done. |
| [sub_14020327C](../functions/sub_14020327C.md) | `0x14020327C` | Confirm handler for a battle command: it stores the chosen value in the command request and starts battle program 3. |
| [sub_140203450](../functions/sub_140203450.md) | `0x140203450` | The unit-targeting confirm handler: it stores the chosen value in the command request and starts battle program 3 for a found unit node. |
| [sub_14020435C](../functions/sub_14020435C.md) | `0x14020435C` | Runs the first pending tile event of the flag word dword_142FCE878 (set when a unit has stopped on a tile): crystal or chest pickup, map item, trap and the other terrain events. |
| [sub_140204B78](../functions/sub_140204B78.md) | `0x140204B78` | Runs one battle command page: it toggles the unit's status flags, posts a message and leaves through the command task. |
| [sub_14020558C](../functions/sub_14020558C.md) | `0x14020558C` | Drains one entry of the deferred battle message queue and hands it to the dispatcher. |
| [sub_1402055FC](../functions/sub_1402055FC.md) | `0x1402055FC` | Pushes one deferred battle message onto the sixteen-entry queue. |
| [sub_1402059AC](../functions/sub_1402059AC.md) | `0x1402059AC` | The end-of-action notification task: it reads the action's presentation row, pushes the message and then retires. |
| [sub_140206344](../functions/sub_140206344.md) | `0x140206344` | Runs a battle reaction notification and reads the inventory, so a reaction that consumes an item can be shown. |
| [sub_140206C14](../functions/sub_140206C14.md) | `0x140206C14` | Maps an ability's charge type to a charge motion through the charge-motion pair table. |
| [sub_140206CE8](../functions/sub_140206CE8.md) | `0x140206CE8` | Releases a charged action: it turns the unit toward its target, takes the charge pose and starts the action script. |
| [sub_140206F90](../functions/sub_140206F90.md) | `0x140206F90` | Validates and commits the chosen ability command, then puts the unit into its charge pose. |
| [sub_14020A7F0](../functions/sub_14020A7F0.md) | `0x14020A7F0` | One of the battle command handlers: it reads the command request and runs the chosen row, ending the turn for the wait/auto ids. |
| [sub_14020AD64](../functions/sub_14020AD64.md) | `0x14020AD64` | The auto-battle style command handler: it finishes the unit without a player choice and hands the turn over. |
| [sub_14020B90C](../functions/sub_14020B90C.md) | `0x14020B90C` | Finishes a unit's move and then looks for a tile event where it stopped. |
| [sub_14020BCF0](../functions/sub_14020BCF0.md) | `0x14020BCF0` | The turn-end facing prompt: the player turns the unit with the d-pad and confirms to finish its turn. |
| [sub_14020BFD4](../functions/sub_14020BFD4.md) | `0x14020BFD4` | Per-frame function of battle state 21 (the crystal / chest / item pickup state): applies the player's choice once it has been made, runs the pickup effects, and calls sub_14020435C again for the next pending flag. |
| [sub_14020C704](../functions/sub_14020C704.md) | `0x14020C704` | The cast handler: it sets the effect word and the charge pose for the action the unit is about to take. |
| [sub_14020CC50](../functions/sub_14020CC50.md) | `0x14020CC50` | The hit sequence of an action: it picks the impact animation and voice from the effect word and starts the notification. |
| [sub_140210AF0](../functions/sub_140210AF0.md) | `0x140210AF0` | The battle state machine: one step per frame from command input through action resolution to the next turn. |
| [sub_140217630](../functions/sub_140217630.md) | `0x140217630` | For a party unit given by its save index, builds the unit's battle command byte list on a scratch unit and answers the first command whose list holds a usable entry (the twin of sub_14030E010, which builds the live me... |
| [sub_140226E44](../functions/sub_140226E44.md) | `0x140226E44` | Refreshes the battle unit panel when an item is selected, checking the item's record category and then its weapon sub-record to decide what the panel shows. |
| [sub_14022EFF4](../functions/sub_14022EFF4.md) | `0x14022EFF4` | Refreshes a battle help panel from the currently selected 16-bit word. |
| [sub_140233588](../functions/sub_140233588.md) | `0x140233588` | A battle scene task that shows a message with three arguments and a kind-3 message entry. |
| [sub_1402371F8](../functions/sub_1402371F8.md) | `0x1402371F8` | Builds the rows of the battle command page and pushes each row's label and state into the list widget. |
| [sub_140237CD0](../functions/sub_140237CD0.md) | `0x140237CD0` | Turns the cursor's list cell into a kind-6 battle message entry. |
| [sub_140237FA4](../functions/sub_140237FA4.md) | `0x140237FA4` | Commits the highlighted command-list cell into the selection message words. |
| [sub_140238444](../functions/sub_140238444.md) | `0x140238444` | Posts the action-name banner for a unit, with a job-pair special case. |
| [sub_140248E08](../functions/sub_140248E08.md) | `0x140248E08` | Converts a packed map record into the runtime battle tile table. |
| [sub_140269554](../functions/sub_140269554.md) | `0x140269554` | Picks the weapon animation for a battle action from the item in the unit's weapon slot and its record category. |
| [sub_140269BBC](../functions/sub_140269BBC.md) | `0x140269BBC` | Applies the action's look word to the acting unit's scene object. |
| [sub_14026A508](../functions/sub_14026A508.md) | `0x14026A508` | Decides whether an action's effect word means no ability, treating both 0 and 512 as empty. |
| [sub_140271AC0](../functions/sub_140271AC0.md) | `0x140271AC0` | Builds the flag word (dword_142FCE878) of tile events that apply to a unit that has just stopped, for sub_14020435C to work through. |
| [sub_140271EFC](../functions/sub_140271EFC.md) | `0x140271EFC` | Rolls which abilities a unit learns from the unit on the tile it names; fills the result block at dword_1411A6AB0 and returns its address. |
| [sub_1402722D8](../functions/sub_1402722D8.md) | `0x1402722D8` | Applies the outcome of a crystal or chest pickup to the picking unit's record: a chest item goes to the inventory, a crystal restores HP and MP, or the rolled abilities are learned. |
| [sub_1402723EC](../functions/sub_1402723EC.md) | `0x1402723EC` | Chooses the item a chest unit gives to the unit that steps on it. |
| [sub_140274DB0](../functions/sub_140274DB0.md) | `0x140274DB0` | Builds ten 5-byte status masks (one bit per status 0..39) from the flag bytes of the status property table. |
| [sub_140278CF0](../functions/sub_140278CF0.md) | `0x140278CF0` | Sets or clears the countdown of a timed status on a unit record. |
| [sub_140279110](../functions/sub_140279110.md) | `0x140279110` | Sort comparator: orders two status ids by byte 2 of their status property entries. |
| [sub_140279150](../functions/sub_140279150.md) | `0x140279150` | Returns a code for the highest-priority status present in two 5-byte status sets of a unit state. |
| [sub_14027F270](../functions/sub_14027F270.md) | `0x14027F270` | Computes the reachable-tile highlight for a unit, extending the base movement/jump by the best Jump-command abilities in its skillset. |
| [sub_14027F974](../functions/sub_14027F974.md) | `0x14027F974` | Marks the tiles of an action's area (the range marks) for a request; ability 220 gets four extra directional marks. |
| [sub_140280170](../functions/sub_140280170.md) | `0x140280170` | Builds the weapon part of a battle action: which item is in the acting unit's hands, what damage it does, and which animation it uses. |
| [sub_140280850](../functions/sub_140280850.md) | `0x140280850` | Marks the units that satisfy the two Arithmeticks mask abilities of an action; returns the number marked, -1 when invalid. |
| [sub_140281488](../functions/sub_140281488.md) | `0x140281488` | Validates a candidate action per command type and, when a3 asks for it, consumes the item or MP; returns -1 invalid, else a small result code (0..3). |
| [sub_140281A64](../functions/sub_140281A64.md) | `0x140281A64` | Collects target units for a preview action by action id (440, 444, 446 special-cased). |
| [sub_1402828E4](../functions/sub_1402828E4.md) | `0x1402828E4` | Returns a small action-mode code for a unit from its command flags and its current ability, special-casing ability 367 and job 93. |
| [sub_140282E38](../functions/sub_140282E38.md) | `0x140282E38` | Walks the 21 preview units and starts each one's pending action. |
| [sub_14028531C](../functions/sub_14028531C.md) | `0x14028531C` | Copies the selected party unit's five equipment words into a battle unit record and mirrors the two hand words into the save row, all raw. |
| [sub_1402855F0](../functions/sub_1402855F0.md) | `0x1402855F0` | Fills a 72-byte local record from the selected party unit's words, including the five equipment words copied raw into +0x1A..+0x1E and +0x20..+0x26. |
| [sub_1402C4D1C](../functions/sub_1402C4D1C.md) | `0x1402C4D1C` | One of the battle unit panel builders: it fills the panel rows for a unit's equipment from the unit's item slots. |
| [sub_1402DE564](../functions/sub_1402DE564.md) | `0x1402DE564` | A battle unit panel builder, the twin of the one at sub_1402C4D1C: it fills a unit's equipment rows from the unit's item slots. |
| [sub_1402EA58C](../functions/sub_1402EA58C.md) | `0x1402EA58C` | The second item command list builder: it assembles the list of items a unit may use in battle and labels each entry with its count. |
| [sub_1402FE1D0](../functions/sub_1402FE1D0.md) | `0x1402FE1D0` | A battle unit panel builder that also handles the small per-slot status icons next to each equipment row. |
| [sub_140304F44](../functions/sub_140304F44.md) | `0x140304F44` | Answers what a map tile contains: it bounds-checks a tile coordinate and returns the element/terrain flags packed for that tile. |
| [sub_1403052DC](../functions/sub_1403052DC.md) | `0x1403052DC` | Filters the pending add / remove status sets of the current action against the target's immunities and the status property table; returns how many bits remain. |
| [sub_1403067D0](../functions/sub_1403067D0.md) | `0x1403067D0` | Post-dispatch step for the physical formulas (id below 7): it filters the pending status set, checks the defender's state and flags the result. |
| [sub_140308C30](../functions/sub_140308C30.md) | `0x140308C30` | The formula handler for the HP-restoring consumables: it derives the amount from the used item's chemist row and hands the result to the shared healing step. |
| [sub_140308C98](../functions/sub_140308C98.md) | `0x140308C98` | The formula handler for the revive consumable: it decides whether the target can be revived, then sets the amount of HP restored from the item's chemist row and a random roll. |
| [sub_1403095E4](../functions/sub_1403095E4.md) | `0x1403095E4` | Executes a reaction ability: builds the result record the reaction causes from the reaction id in the word at 0x14186AFF0, or refuses an id it does not handle. |
| [sub_1403099B0](../functions/sub_1403099B0.md) | `0x1403099B0` | Resolves one battle action: copies the 20-byte action, sets up per-command data, dispatches the formula and runs the post steps. |
| [sub_14030A11C](../functions/sub_14030A11C.md) | `0x14030A11C` | Finishes the result block of one resolved action: either drops the whole result when the acting unit's own state forbids it, or runs the per-formula post hook, clamps the numbers to 999 and decides whether a follow-up... |
| [sub_14030AFEC](../functions/sub_14030AFEC.md) | `0x14030AFEC` | A post-resolution reaction helper: after an action resolves it can queue one of a small set of reaction abilities for the acting unit, under a set of command, unit-flag and item-category conditions. |
| [sub_14030B1A0](../functions/sub_14030B1A0.md) | `0x14030B1A0` | The preview twin of sub_1402828E4: works out the MP cost of the action under the cursor and the same refusal codes, without paying. |
| [sub_14030B278](../functions/sub_14030B278.md) | `0x14030B278` | Checks whether the unit can answer with an automatic item: it picks one of the two item words the unit carries, tests that the item is a usable weapon-slot item, and queues the fixed ability `0x1BF` when the test passes. |
| [sub_14030B4F0](../functions/sub_14030B4F0.md) | `0x14030B4F0` | Reaction and auto-item path: it picks an item or weapon reaction, builds the action for it and applies it without consuming the item. |
| [sub_14030BE18](../functions/sub_14030BE18.md) | `0x14030BE18` | The Brave roll that decides whether a reaction fires; on success it stores the reaction id and the amount the reaction acts on in the action block. |
| [sub_14030BE68](../functions/sub_14030BE68.md) | `0x14030BE68` | The second reaction helper: the same Brave roll as sub_14030BE18, only for a unit with status bit 0x01 at +0x63, and it stores the reaction id without copying the HP result. |
| [sub_14030BF04](../functions/sub_14030BF04.md) | `0x14030BF04` | Handles a break or destroy effect on a piece of equipment: it finds the item, checks whether it can break, and removes it from the slot. |
| [sub_14030CAA8](../functions/sub_14030CAA8.md) | `0x14030CAA8` | Applies a unit's pending status bits (bitset at unit-state +29..+33) to its status state, subject to immunity and conflict checks. |
| [sub_14030CD08](../functions/sub_14030CD08.md) | `0x14030CD08` | Finds a unit that learns the current ability from the action, rolling the learn chance; returns the unit index or -1. |
| [sub_14030CFB8](../functions/sub_14030CFB8.md) | `0x14030CFB8` | Clears every pending status on a unit and refreshes the status icons. |
| [sub_14030D1CC](../functions/sub_14030D1CC.md) | `0x14030D1CC` | Builds and submits an item request for a reaction, temporarily marking the item as not consumed. |
| [sub_14030DD8C](../functions/sub_14030DD8C.md) | `0x14030DD8C` | Builds a unit's usable ability list for skillset a2 (ids plus cost, value, flag and availability arrays); sibling of sub_14030E368. |
| [sub_14030E010](../functions/sub_14030E010.md) | `0x14030E010` | Builds the battle command list for a unit: it reads the two command-set bytes, maps each command to its kind and lets the per-kind builder fill the list. |
| [sub_14030E174](../functions/sub_14030E174.md) | `0x14030E174` | Per-kind list builder: it dispatches on the menu selector to the item list, the throw list, the Arithmeticks list and four more per-command builders. |
| [sub_14030E368](../functions/sub_14030E368.md) | `0x14030E368` | Builds the list of ability ids (with cost and availability arrays) a unit has for command/skillset a2; the shared worker of the per-command list functions. |
| [sub_14030E94C](../functions/sub_14030E94C.md) | `0x14030E94C` | For a unit whose command is 21 (Arithmeticks), lists its ability ids whose kind5 mask intersects a4, 0xFFFF terminated. |
| [sub_14030EC48](../functions/sub_14030EC48.md) | `0x14030EC48` | Builds the usable list for a battle command: it checks the command kind and writes one text cell per entry for the menu. |
| [sub_14030FCDC](../functions/sub_14030FCDC.md) | `0x14030FCDC` | Finds the position of a unit's status in the 40-entry status display list and returns it, or one of the negative codes for the missing cases. |
| [sub_14030FE18](../functions/sub_14030FE18.md) | `0x14030FE18` | Answers whether a unit can take its turn: a short predicate over four status flags and the display-list gate. |
| [sub_1403166C0](../functions/sub_1403166C0.md) | `0x1403166C0` | Resets the shared text-cell buffer and rebuilds the action-name row of every unit in the preview table. |
| [sub_1403167E4](../functions/sub_1403167E4.md) | `0x1403167E4` | Rebuilds one unit's action row in the shared text buffer: it collects the unit's candidate actions and writes their packed words. |
| [sub_140316B04](../functions/sub_140316B04.md) | `0x140316B04` | Seeds a unit's candidate action slots for its current command before the action row is written. |
| [sub_140316D24](../functions/sub_140316D24.md) | `0x140316D24` | Adds a unit's candidate action slots for command a2 (one entry per usable ability, or a fixed set for Throw / Items / Jump) to the AI slot table at word_141872598. |
| [sub_1403170CC](../functions/sub_1403170CC.md) | `0x1403170CC` | Answers whether a unit may use one ability id: it checks the unit's availability flag and then the learned bit for that id. |
| [sub_140323D1C](../functions/sub_140323D1C.md) | `0x140323D1C` | Runs the crystal / chest window: lists the abilities the roll chose, asks the player to learn them or restore HP and MP (or announces a chest item) and stores the answer in dword_140D40958. |
| [sub_140324658](../functions/sub_140324658.md) | `0x140324658` | Opens one of three battle panels for a message-script command: mode 0 a panel through sub_140324970, mode 1 a 19-row list panel (sub_140321DB8), mode 2 the crystal / chest window. |
| [sub_14032B1A4](../functions/sub_14032B1A4.md) | `0x14032B1A4` | A battle/result panel that copies the 0x141876E90 block into the 0x14078DDD0 render area and draws the unit's equipment summary. |
| [sub_14032EDB8](../functions/sub_14032EDB8.md) | `0x14032EDB8` | The flag-aware equip panel task. |
| [sub_14032F410](../functions/sub_14032F410.md) | `0x14032F410` | A two-row equip panel variant: it reads five display words at carrier +0x2E, not the five hand words, and draws them in two groups. |
| [sub_14032F9F8](../functions/sub_14032F9F8.md) | `0x14032F9F8` | The equip detail panel: it reads the five hand words at 0x141876EB4 and a second five-word array at 0x141876EBE, and draws both rows without extracting the top two bits. |
| [sub_14033A37C](../functions/sub_14033A37C.md) | `0x14033A37C` | A battle unit panel variant, the third of the five builders, with the same hand-slot loop and the same top-two-bit flag read as the other flagged variant. |
| [sub_14033B420](../functions/sub_14033B420.md) | `0x14033B420` | A battle unit panel builder that fills the unit's equipment rows and the small slot markers next to them. |
| [sub_14033E394](../functions/sub_14033E394.md) | `0x14033E394` | Selects a battle record from the table at 0x141D3B7A0 and copies its +0x30..+0x6F slice to the battle panel block at 0x141D3B880, which puts the record's hand words at block +0x24. |
| [sub_140364408](../functions/sub_140364408.md) | `0x140364408` | The second battle item panel initialiser, the twin of sub_140323D1C: it sets up the panel for a unit and its current item. |
| [sub_140388EB4](../functions/sub_140388EB4.md) | `0x140388EB4` | AI search pass: tries the abilities of four skillsets with action-record flag 0x40 against combinations of two sub-abilities. |
| [sub_140389D84](../functions/sub_140389D84.md) | `0x140389D84` | AI targeting step: it picks a target area, calls the ring-range helper and returns the chosen cells. |
| [sub_14038ABA4](../functions/sub_14038ABA4.md) | `0x14038ABA4` | Evaluates an action's targets: resolves the target list and accumulates score fields per hit unit using the ability's flags4. |
| [sub_14038BC00](../functions/sub_14038BC00.md) | `0x14038BC00` | AI-side action builder: it turns the chosen action into the packed action word and evaluates its target. |
| [sub_14038BF34](../functions/sub_14038BF34.md) | `0x14038BF34` | AI: picks the concrete action for the chosen candidate; for command type 3 draws a random usable ability, otherwise selects targets. |
| [sub_14038C47C](../functions/sub_14038C47C.md) | `0x14038C47C` | AI targeting for the Arithmeticks path: it walks the tiles around a point and returns the ones in range. |
| [sub_14038C8F8](../functions/sub_14038C8F8.md) | `0x14038C8F8` | Small AI wrapper: it builds the current action and hands it to the shared candidate evaluator. |
| [sub_14038D1EC](../functions/sub_14038D1EC.md) | `0x14038D1EC` | AI candidate builder: it builds an action from a candidate slot and sets up its target state. |
| [sub_14038D65C](../functions/sub_14038D65C.md) | `0x14038D65C` | AI action evaluation: it builds the action, evaluates its target set and stores the chosen target. |
| [sub_14039651C](../functions/sub_14039651C.md) | `0x14039651C` | Copies the unit's hands into a preview record so the equip preview shows the same items the unit carries. |
| [sub_140399A64](../functions/sub_140399A64.md) | `0x140399A64` | The battle-side flag-aware equip panel. |
| [TurnList_Build](../functions/TurnList_Build.md) | `0x14030FFC4` | Builds the 40-entry turn-order forecast: simulates each unit's CT until it reaches 100, inserts entries sorted by time, and adds the entries of pending (charging) actions. |
| [TurnList_InsertEntry](../functions/TurnList_InsertEntry.md) | `0x140310490` | Inserts one 4-byte entry into a 40-entry turn-order list, sorted by its time key; a pending-action entry also carries the unit's ability (9 bits). |
| [TurnPanel_FillUnitEntry](../functions/TurnPanel_FillUnitEntry.md) | `0x14010C1FC` | Fills one entry (448 bytes at panel + 448 x index) of a battle turn panel: the unit's numbers, name and its status byte list. |
| [TurnPanel_SetTag](../functions/TurnPanel_SetTag.md) | `0x140215540` | Fills one tag of the turn-order panel from a list entry: the unit's portrait data and, for a pending action, the ability name. |
| [TurnPanel_SetUnitPanel](../functions/TurnPanel_SetUnitPanel.md) | `0x140214FB4` | Fills the unit panel shown for a turn-order entry, with the pending ability's name when the entry is an action. |
| [Unit_BuildInnateStatuses](../functions/Unit_BuildInnateStatuses.md) | `0x140278688` | Builds the three innate status groups of a unit from its job row, its equipment attributes and its permanent extra set, restores the battle-applied set, and refreshes the status display. |
| [Unit_ChangeBattleStat](../functions/Unit_ChangeBattleStat.md) | `0x14030C080` | Applies one stat change of an action result to a unit stat byte, clamped, and keeps the stat total in step. |
| [Unit_GetReachHeight](../functions/Unit_GetReachHeight.md) | `0x14027EDA4` | The height (in half-steps) the weapon reach rules measure from: the unit's own tile without its water depth, raised when the unit is mounted or floating, with the depth added back for some movement flags. |
| [Unit_HasStatusGroup](../functions/Unit_HasStatusGroup.md) | `0x140278FA8` | Tests whether a unit carries any status of one of the ten party-wide status groups by ANDing its five status bytes against that group's five-byte mask. |
| [Unit_InitBattleStatusState](../functions/Unit_InitBattleStatusState.md) | `0x140278E0C` | Sets up the status state of a unit that has just been built into the battle: the applied set, the countdowns and the KO counter. |
| [Unit_ListItemCommandItems](../functions/Unit_ListItemCommandItems.md) | `0x14030E680` | Builds the item list for the Item command: it takes the usable ability list of the command's skill set and rewrites each of the fourteen item abilities into the item id the command offers. |
| [Unit_ListThrowableItems](../functions/Unit_ListThrowableItems.md) | `0x14030E7B4` | Builds the candidate list for the Throw command: the item ids in the unit's inventory that the game considers throwable, ordered for the menu. |
| [Unit_ReinitStatusCountdowns](../functions/Unit_ReinitStatusCountdowns.md) | `0x140278600` | Re-initialises the countdown bytes of a unit after its innate status set has been rebuilt: it merges the saved innate status bytes into the effective set and starts a duration for every battle-applied status that has ... |
| [Unit_SetChargeStateBits](../functions/Unit_SetChargeStateBits.md) | `0x140279370` | Sets which of the four action states Readying, Jumping, Evading, Performing (statuses 4..7) a unit is in, and the charge counter that goes with it. |
| [UnitInfo_FillFromBattleUnit](../functions/UnitInfo_FillFromBattleUnit.md) | `0x1402CBCA0` | Fills the unit information record a battle panel draws (the deployment carousel's unit card, an event's unit preview) from a battle unit record: its job line, face, level, HP / MP / CT, Brave and Faith. |
| [UnitPage_Task](../functions/UnitPage_Task.md) | `0x1402FAA28` | Task of the legacy unit page: builds the cells and the fifteen number fields of the unit page. |
| [UnitPanel_FillEffectLine](../functions/UnitPanel_FillEffectLine.md) | `0x140227CF8` | Fills the effect line of the unit status panel (the panel beside the action preview and the AI's target panel) from the current target's result block: damage, recovery, a stat change, or the statuses the action would ... |
| [UnitPanel_FillJobLine](../functions/UnitPanel_FillJobLine.md) | `0x14029B5CC` | Fills the job line of a unit panel from a 148-byte job record: the job icon, the job level, the JP and the JP to the next level. |
| [UnitPanel_SetSignalList](../functions/UnitPanel_SetSignalList.md) | `0x14010A284` | Turns a status list (ids, bit 0x80 = removed) into the panel's list of BattleSignal ids. |
| [UnitPanel_SetStatusBytes](../functions/UnitPanel_SetStatusBytes.md) | `0x14010A42C` | Fills a battle unit panel's status byte list (the icons on the panel) from a five-byte status set. |
| [VramPage_CopyRect](../functions/VramPage_CopyRect.md) | `0x14025FA60` | Copies a rectangle of 16-bit pixels into the 1024 by 512 video page (g_SaveYoxPage) and marks that area for upload. |

## Structures (65)

| Name | Size (bytes) | Summary |
|---|---|---|
| [ActionEntryWord](../structs/ActionEntryWord.md) | 2 | The 16-bit word of a four-byte action entry (the AI and preview form): the action id in bits 0..9 and the acting unit slot in bits 10..15. |
| [ActionResult](../structs/ActionResult.md) | 48 | The result of one action on one target, filled by the formula handler and read by the result applier, the preview and the messages. |
| [AiCommandEntry](../structs/AiCommandEntry.md) | 4 | One candidate action of the AI's command table: the ability word (id \| unit slot << 10), the command (skillset) byte it comes from and a flag byte. |
| [BannerWordRange](../structs/BannerWordRange.md) | 4 | One row of the BannerWordRanges table. |
| [BattleMenuRowScreenCode](../structs/BattleMenuRowScreenCode.md) | 1 | One row of the BattleMenuRowScreenCodes table. |
| [BattleMenuStepRow](../structs/BattleMenuStepRow.md) | 32 | One row of the command menu step tables (same shape as the stock menu step table). |
| [BattleMsgDescriptor](../structs/BattleMsgDescriptor.md) | 16 | The 4-dword descriptor the banner takes: class, subtype, kind and a message word. |
| [BattleMsgEntry](../structs/BattleMsgEntry.md) | 524 | One slot of the battle message store: the kind, the kind-dependent argument, a message id and a 512-byte text buffer. |
| [BattleMsgRecord](../structs/BattleMsgRecord.md) |  | The record the message object holds at +8: the values the argument filler reads for a message. |
| [BattlePanelHandWord](../structs/BattlePanelHandWord.md) | 2 | One hand word as the flag-aware panels read it: the item id in bits 0..8 and a two-bit value in bits 14..15. |
| [BattleRangeMarkRecord](../structs/BattleRangeMarkRecord.md) | 5 | One record of g_BattleRangeMarks, parallel to BattleTileRecord (512 records, layer 1 at +0x500). |
| [BattleTileRecord](../structs/BattleTileRecord.md) | 8 | One tile of the battle map in g_BattleTileTable: 256 records per layer, two layers (layer 1 at +0x800), index x + y * width. |
| [CommandKindMessageOffset](../structs/CommandKindMessageOffset.md) | 1 | One row of the CommandKindMessageOffsets table. |
| [CommandKindParam](../structs/CommandKindParam.md) | 4 | One row of the CommandKindParams table. |
| [CornerColour](../structs/CornerColour.md) | 4 | One row of the BannerWordColours table. |
| [CrystalRollResult](../structs/CrystalRollResult.md) | 1393 | The block Unit_RollAbilityLearning fills at dword_1411A6AB0 (1393 bytes, the next data starts at 0x1411A7024) when a unit stops on a crystal or chest. |
| [EffectBlendWeightsRow](../structs/EffectBlendWeightsRow.md) | 7 | One row of the EffectBlendWeights table. |
| [EffectFileLocatorRow](../structs/EffectFileLocatorRow.md) | 8 | One row of EffectFileLocatorsLangOther. |
| [EffectFlashProfilesRow](../structs/EffectFlashProfilesRow.md) | 14 | One row of the EffectFlashProfiles table. |
| [EffectKindRecordsRow](../structs/EffectKindRecordsRow.md) | 4 | One row of the EffectKindRecords table. |
| [EffectLabelRectRow](../structs/EffectLabelRectRow.md) | 4 | One row of BattleEffectLabelRectsLang0. |
| [EffectNumberPseudoRow](../structs/EffectNumberPseudoRow.md) | 2 | One row of the EffectNumberPseudo table. |
| [EffectPaletteSeedsRow](../structs/EffectPaletteSeedsRow.md) | 3 | One row of the EffectPaletteSeeds table. |
| [EffectSpriteSpawnRecordsRow](../structs/EffectSpriteSpawnRecordsRow.md) | 46 | One row of the EffectSpriteSpawnRecords table. |
| [ElementColoursRow](../structs/ElementColoursRow.md) | 3 | One row of the ElementColours table. |
| [ElementMaskOrderRow](../structs/ElementMaskOrderRow.md) | 1 | One row of the ElementMaskOrder table. |
| [EquipPanelBlock](../structs/EquipPanelBlock.md) | 64 | A 64-byte copy of a party or battle record's bytes +0x30..+0x6F, kept at 0x141876E90 for the field equip screens and at 0x141D3B880 for the battle panels. |
| [FormatArgRecord](../structs/FormatArgRecord.md) | 264 | One argument of a formatted UI text string: a 256-byte text area and a type dword at +0x100. |
| [FormulaBlock](../structs/FormulaBlock.md) | 72 | The state of the one action being resolved: Battle_ResolveAction fills it per target and every formula handler reads and writes it. |
| [ItemListCells](../structs/ItemListCells.md) |  | The static item-list cell store: 82 two-byte cells (kind tag in bits 15..11, id in bits 10..0) and the parallel per-cell arrays beside them. |
| [LayoutPointer](../structs/LayoutPointer.md) | 8 | One row of the StatusPanelLayoutsLanguage0 table. |
| [MenuCursorDefault](../structs/MenuCursorDefault.md) | 16 | One row of the MenuCursorDefaults table. |
| [MoveBlockerRecord](../structs/MoveBlockerRecord.md) | 7 | One entry of g_MoveBlockers: another unit on the map as the move-range builder sees it. |
| [MoveFindRow](../structs/MoveFindRow.md) | 24 | One row of the MoveFindItems table. |
| [MoveRangeScratch](../structs/MoveRangeScratch.md) | 128 | The move-range builder's scratch block at g_MoveRangeScratch, filled by Battle_MoveRangeSetup from the unit record. |
| [NxdDataBattleEventOpcodeRow](../structs/NxdDataBattleEventOpcodeRow.md) | 8 | One row of the nxd.battle_event_opcode table (data table). |
| [NxdDataBattleObjectiveRow](../structs/NxdDataBattleObjectiveRow.md) | 16 | One row of the nxd.battle_objective table (English text table; the other languages share the layout). |
| [NxdDataBattleRow](../structs/NxdDataBattleRow.md) | 4 | One row of the nxd.battle table (data table). |
| [NxdDataBattleSignalRow](../structs/NxdDataBattleSignalRow.md) | 16 | One row of the nxd.battle_signal table (English text table; the other languages share the layout). |
| [NxdDataC_Mes_Id_SampleRow](../structs/NxdDataC_Mes_Id_SampleRow.md) | 24 | One row of the nxd.battle_message_text table (English text table; the other languages share the layout). |
| [NxdDataContinuousBattleTimelineRow](../structs/NxdDataContinuousBattleTimelineRow.md) | 8 | One row of the nxd.continuous_battle_timeline table (data table). |
| [NxdDataContinuousSortieConfirmRow](../structs/NxdDataContinuousSortieConfirmRow.md) | 108 | One row of the nxd.continuous_sortie_confirm table (data table). |
| [NxdDataEntryAreaRow](../structs/NxdDataEntryAreaRow.md) | 8 | One row of the nxd.entry_area table (data table). |
| [NxdDataEntryNoRow](../structs/NxdDataEntryNoRow.md) | 28 | One row of the nxd.entry_no table (data table). |
| [NxdDataGameModeTypesRow](../structs/NxdDataGameModeTypesRow.md) | 24 | One row of the nxd.game_mode_types table (data table). |
| [NxdDataMapRow](../structs/NxdDataMapRow.md) | 32 | One row of the nxd.map table (data table). |
| [NxdDataMapVariationEventRow](../structs/NxdDataMapVariationEventRow.md) | 20 | One row of the nxd.map_variation_event table (data table). |
| [NxdDataMapVariationRandomBattleRow](../structs/NxdDataMapVariationRandomBattleRow.md) | 8 | One row of the nxd.map_variation_random_battle table (data table). |
| [NxdDataOverrideEntryDataRow](../structs/NxdDataOverrideEntryDataRow.md) | 160 | One row of the nxd.override_entry_data table (data table). |
| [NxdDataPauseRow](../structs/NxdDataPauseRow.md) | 24 | One row of the nxd.pause table (data table). |
| [NxdDataSortieConfirmRow](../structs/NxdDataSortieConfirmRow.md) | 48 | One row of the nxd.sortie_confirm table (data table). |
| [PaletteCyclePair](../structs/PaletteCyclePair.md) | 4 | One row of the EquipPanelPaletteCycle table. |
| [PaletteIdWord](../structs/PaletteIdWord.md) | 2 | One row of the StatusPanelPaletteIds table. |
| [PopupBounceStep](../structs/PopupBounceStep.md) | 2 | One row of the PopupBounceCurve table. |
| [PostBattleCalc](../structs/PostBattleCalc.md) | 3400 | The per-formula post-processing object of a battle: a virtual function table pointer and 106 rows of 32 bytes, one per formula id, that sub_14030A11C runs after a formula handler. |
| [PostBattleCalcRow](../structs/PostBattleCalcRow.md) | 32 | One row of PostBattleCalc: an entry thunk, its argument, and the callback the thunk jumps to. |
| [RangeRowMasksRow](../structs/RangeRowMasksRow.md) | 2 | One row of the RangeRowMasks table. |
| [ScriptedActorPresetsRow](../structs/ScriptedActorPresetsRow.md) | 8 | One row of the ScriptedActorPresets table. |
| [StatusIconFlagMaskRow](../structs/StatusIconFlagMaskRow.md) | 4 | One row of BattleStatusIconFlagMasks. |
| [StatusPanelFrameLine](../structs/StatusPanelFrameLine.md) | 7 | One row of the StatusPanelFrameLines table. |
| [StatusPropertyRow](../structs/StatusPropertyRow.md) | 16 | Properties of one status. |
| [SurfacePairConstant](../structs/SurfacePairConstant.md) | 2 | One row of the SurfacePairConstants table. |
| [TerrainPropertiesRow](../structs/TerrainPropertiesRow.md) | 1 | One byte of a TerrainProperties block (two blocks of 64). |
| [UiNumberField](../structs/UiNumberField.md) | 32 | One row of the StatusNumbersActorA table and the tables that share its shape. |
| [WeaponHitSoundCuesRow](../structs/WeaponHitSoundCuesRow.md) | 1 | One row of BattleWeaponHitSoundCues. |

## Globals (48)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_AbilityMpCost](../globals/g_AbilityMpCost.md) | `0x1407B078E` | `uint8` | The MP cost of the action being started or previewed: the action row's cost byte, halved for a unit with the halving passive; zero when no cost applies. |
| [g_ActionItemIdByte](../globals/g_ActionItemIdByte.md) | `0x1407B077E` | `uint8` | The item-id byte the battle action resolver leaves for the item formulas: the item id's low byte plus 0x10, so the formulas rebuild the id by adding 0xF0. |
| [g_AiCommandTable](../globals/g_AiCommandTable.md) | `0x141872598` | `AiCommandEntry[16][34]` | The AI's candidate action table: 16 rows (one per AI unit) of 34 four-byte entries; each entry is an ability word and the command (skillset) byte it came from. |
| [g_BattleActingUnit](../globals/g_BattleActingUnit.md) | `0x14186AF68` | `ptr` | Pointer to the unit record the current battle action is worked out on: the TARGET of the action (the unit hit), although the name says acting; its byte at +0x97 carries the reaction flags and its byte at +0x61 the ite... |
| [g_BattleActionBlock](../globals/g_BattleActionBlock.md) | `0x14186AF70` | `ActionResult *` | Pointer to the result block of the current action on its target: unit +0x1BE of the target's slot (the formula handlers' R). |
| [g_BattleCasterResult](../globals/g_BattleCasterResult.md) | `0x14186AF60` | `ActionResult *` | Pointer to the caster's own result block of the action being resolved: a static ActionResult at 0x14186AFC0, apart from the unit records. |
| [g_BattleCasterUnit](../globals/g_BattleCasterUnit.md) | `0x14186AF78` | `uint8 *` | Pointer to the unit record of the one who does the action, as the formula handlers read it: the entry of g_PreviewUnitTable chosen by byte 0 of the request. |
| [g_BattleCommandBytes](../globals/g_BattleCommandBytes.md) | `0x140D40838` | `uint8[8]` | The battle command menu's byte list for the unit whose menu is open: the command (skillset) byte of each row, 0xFF-terminated. |
| [g_BattleCommandBytesB](../globals/g_BattleCommandBytesB.md) | `0x14184B2C0` | `uint8[8]` | The second copy of the battle command menu's byte list, built by the same builder for the other command menu (BattleCommand_BuildUnitList), 0xFF-terminated. |
| [g_BattleCommandKinds](../globals/g_BattleCommandKinds.md) | `0x14184A9A8` | `uint8[8]` | The command kind of each entry of the byte list just built: g_CommandKind[command byte] & 0x0F. |
| [g_BattleCommandRequest](../globals/g_BattleCommandRequest.md) | `0x142FD35A0` | `uint8[20]` | The twenty-byte battle command request: the command byte at +1, the chosen 16-bit value at +2 and +8 (kept equal), and the ability word at +6. |
| [g_BattleContextGate](../globals/g_BattleContextGate.md) | `0x14186AF80` | `uint32` | Battle context gate: while it is non-zero the reaction and secondary-action paths refuse to run, which is how those actions avoid refunding or repeating. |
| [g_BattleControl](../globals/g_BattleControl.md) | `0x143CD9EF0` | `BattleControl *` | Singleton ffto::Game::Battle::BattleControl (vtable 0x140714058); BattleControl_FrameUpdate is its per-frame update; its destructor clears the fast-forward level and mode. |
| [g_BattleLineAbility](../globals/g_BattleLineAbility.md) | `0x142FD3590` | `uint32` | The ability, cut to 9 bits, that the battle-line task turns into a text id (0xA800 OR the ability) when a unit speaks a line for an action. |
| [g_BattleMapId](../globals/g_BattleMapId.md) | `0x140D3A838` | `int` | 32-bit battle map id: set from scene variable 51 or from the signed event words 0x140D40924 / 0x140D40928, passed to the map task (BattleLoad_StepFresh, the load task) and copied whole by the battle capture; the battl... |
| [g_BattleMapWords](../globals/g_BattleMapWords.md) | `0x140D3F950` | `uint16[]` | The runtime per-EVENT word table (887 words): one word per story event number, built by ScenarioSetup_ApplyRecord from the scenario setup records at every scene start; the battle message, skip and event code read it b... |
| [g_BattleModeFlag](../globals/g_BattleModeFlag.md) | `0x141853C08` | `int` | 32-bit mode global the main loop sets around battles and the scene start; 1 while a random-encounter battle loads (seen live: 0 on the world map, 1 at the title card and deployment); MapRow_SelectVariation takes its r... |
| [g_BattleMsgObject](../globals/g_BattleMsgObject.md) | `0x143CDA388` | `ptr` | Pointer to the battle message object. |
| [g_BattleMsgQueue](../globals/g_BattleMsgQueue.md) | `0x142FCF870` | `uint8[256]` | The deferred battle message queue: sixteen entries of sixteen bytes (id byte, unit byte, qword value). |
| [g_BattleMsgQueueCount](../globals/g_BattleMsgQueueCount.md) | `0x142FCF864` | `int` | The number of entries in the deferred battle message queue, at most sixteen. |
| [g_BattleState](../globals/g_BattleState.md) | `0x140C6B1CC` | `int` | The battle state word the battle state machine switches on. |
| [g_BattleStateGate](../globals/g_BattleStateGate.md) | `0x14186AF9C` | `uint32` | Battle state word that suspends the reaction helper while it is non-zero. |
| [g_BattleTileTable](../globals/g_BattleTileTable.md) | `0x140D8DCB0` | `uint8[4096]` | The battle map tile table: 512 records of 8 bytes (flags and movement cost), filled by the map setup from the packed level record and read by the map code. |
| [g_BattleUnitTable](../globals/g_BattleUnitTable.md) | `0x141853CE0` | `uint8[10752]` | The live battle unit table: 21 records of 512 bytes. |
| [g_CMesIdTable](../globals/g_CMesIdTable.md) | `0x143CDA340` | `ptr` | The cached result of the NXD registry lookup for table 172, the battle message text table. |
| [g_CommandKind](../globals/g_CommandKind.md) | `0x14067E010` | `uint8[256]` | Command id to command kind, one byte per row: 256 stock rows indexed by the command (skillset) byte. |
| [g_CurrentActionBlock](../globals/g_CurrentActionBlock.md) | `0x1418716A0` | `uint8[?]` | The current-action block Action_BuildCurrentAction fills for the AI and the action preview: command at +0, packed action word at +2, item id at +6, flags at +0x10 and the ability aux flags further in. |
| [g_CurrentMapId](../globals/g_CurrentMapId.md) | `0x140784478` | `int` | 32-bit id of the map being loaded or in play, stored by the map load task before it calls Map_LoadBattleData; MapResource_Read indexes the per-map resource pointer tables with it; 0x77777777 means no map; the other re... |
| [g_FastForwardStateTable](../globals/g_FastForwardStateTable.md) | `0x142FCF730` | `uint8[256]` | Per battle state (index g_BattleState): non-zero = fast-forward allowed. |
| [g_FormulaBlock](../globals/g_FormulaBlock.md) | `0x1407B0770` | `uint8[16]` | The block the action resolver and the formula handlers share, 0x48 bytes from 0x1407B0770: the request's action type, the ability being worked out (the word at +8, address 0x1407B0778), the weapon or item word, the in... |
| [g_LoadedMapId](../globals/g_LoadedMapId.md) | `0x142FF9EB8` | `int` | 32-bit id of the map the loader last accepted (a map with a block); read by the battle setup and the scene update, which compare it with stock map numbers; cleared by the scene reset |
| [g_MessageDescriptor](../globals/g_MessageDescriptor.md) | `0x140783210` | `uint8[?]` | The current battle message descriptor: the message word at +0, the item id at +4 and the text id at +8. |
| [g_MoveBlockers](../globals/g_MoveBlockers.md) | `0x141882680` | `uint8[112]` | Up to 16 entries of 7 bytes, one per other unit on the map (record MoveBlockerRecord); an unused entry has id 0xFF. |
| [g_MoveFindTakenBits](../globals/g_MoveFindTakenBits.md) | `0x1411A7680` | `data` | uint8[128]: taken bits of the Move-Find hidden tiles, four per map, two maps per byte, byte = scene variable 51 / 2, bit 0x80 >> (tile slot + 4 x (id & 1)); saved and restored whole; directly followed by g_PoachersDen... |
| [g_MoveFindWorkingRow](../globals/g_MoveFindWorkingRow.md) | `0x140D8DC90` | `data` | 24 bytes: the Move-Find row of the loaded map (four hidden tiles of 6 bytes), copied from the table by Map_LoadBattleData and saved with the battle capture |
| [g_MoveRangeScratch](../globals/g_MoveRangeScratch.md) | `0x141882600` | `uint8[128]` | Scratch block of the move-range builder, filled by Battle_MoveRangeSetup: Jump, horizontal jump, Move, the unit's tile, movement mode and flags, body height (record MoveRangeScratch). |
| [g_MoveRangeTileCount](../globals/g_MoveRangeTileCount.md) | `0x1418827B0` | `uint16` | Number of tiles the last move-range build lit (Battle_MoveRange_Commit). |
| [g_MoveTerrainCost](../globals/g_MoveTerrainCost.md) | `0x141882700` | `uint8[64]` | Movement cost per terrain type for the unit being built (0xFF = cannot enter), copied by Battle_MoveRangeSetup from one of the six sets of g_MoveTerrainCostSets and adjusted for weather and abilities. |
| [g_MoveTerrainCostSets](../globals/g_MoveTerrainCostSets.md) | `0x14067F5B0` | `uint8[6][64]` | Six constant cost sets by terrain type: walking, open (Fly / Teleport), float, water (two modes), one more water mode, lava walking. |
| [g_MoveTileFlags](../globals/g_MoveTileFlags.md) | `0x141882880` | `uint8[512]` | Per-tile flag byte of the move-range builder: 0x01 frontier, 0x02 one-axis slope, 0x04 occupied, 0x08 unit that can be stepped onto, 0x10 standable, 0x20 mountable ally, 0x40 steep, 0x80 blocked. |
| [g_PostBattleCalc](../globals/g_PostBattleCalc.md) | `0x143CDA750` | `PostBattleCalc *` | Pointer to the PostBattleCalc object of the running battle: 106 per-formula post-processing rows. |
| [g_ReactionGateTable](../globals/g_ReactionGateTable.md) | `0x14067F730` | `uint8[32]` | One byte per reaction id 422..453: the reaction executor refuses (returns 0 at once) an id whose byte has 1 in its low two bits. |
| [g_SceneTaskSlots](../globals/g_SceneTaskSlots.md) | `0x14114B150` | `uint8[1512]` | Nine scene-task data records of 0xA8 bytes, parsed from u16 token streams during the battle map setup and captured in a kind-1 snapshot. |
| [g_StatusGroupMasks](../globals/g_StatusGroupMasks.md) | `0x1411A6A70` | `uint8[10][5]` | The ten party-wide status group masks, five bytes each: a group test ANDs these bytes against the unit status bytes at +0x61..+0x65. |
| [g_StatusIconFlags](../globals/g_StatusIconFlags.md) | `0x1406735D0` | `uint32[]` | The per-status flag words the status panel update reads: index status+1, no bound check. |
| [g_TextCommandSlot](../globals/g_TextCommandSlot.md) | `0x140D40940` | `ptr` | The callback slot the battle text command installs: sub_140243390 is stored here and every branch of the text dispatcher calls it. |
| [xmmword_141876E90](../globals/xmmword_141876E90.md) | `0x141876E90` | `EquipPanelBlock` | The field equip screens' 64-byte copy of the selected party record bytes +0x30..+0x6F; its hand words at +0x24 are a raw copy of g_PartyUnits +0x54..+0x5C. |
| [xmmword_141D3B880](../globals/xmmword_141D3B880.md) | `0x141D3B880` | `EquipPanelBlock` | The battle module's copy of the same 64-byte record slice (+0x30..+0x6F), with its five hand words at +0x24; read by the battle panel sub_140399A64. |

## Registries (1)

| Name | Summary |
|---|---|
| [BattleMsgKindBase](../registries/BattleMsgKindBase.md) | The message-id base per descriptor kind for class 0 subtype 2: id = 1000 x kind + (word & 0x7FF). |

## Flows (5)

| Name | Summary |
|---|---|
| [BattleMessageBanner](../flows/BattleMessageBanner.md) | How a message descriptor becomes text in the battle's centre banner: a battle handler calls the banner function, which resolves the descriptor to a message id and a template, fills the format arguments, sets the text ... |
| [CrystalAbilityLearning](../flows/CrystalAbilityLearning.md) | A unit that stops on a Crystal or Chest unit's tile triggers a roll of the abilities the dead unit had learned in jobs the picker has unlocked, a window where a player-controlled unit chooses between learning them and... |
| [EquipPanelBlockFill](../flows/EquipPanelBlockFill.md) | How the five hand words travel from a unit record to the two panel blocks and what the two flag-aware panels do with them. |
| [MapRendererBuildPath](../flows/MapRendererBuildPath.md) | How the Enhanced renderer builds the terrain of a battle map: from the map id to the requests for the mesh, the textures and the anim, and which data table rows steer each step. |
| [StatusLabelOverAHitUnit](../flows/StatusLabelOverAHitUnit.md) | How a status an action added or removed is shown over the hit unit (the styled name with its icon): the unit's label task queues one BattleSignal id per status from the result block's two 40-bit sets, then pops and dr... |

## Observed behaviours (45)

| Name | Scope | Summary |
|---|---|---|
| [AbilityAboveStockBoundaryHasNoMpCheckOrCost](../behaviors/AbilityAboveStockBoundaryHasNoMpCheckOrCost.md) | engine (action start and preview) | The MP check and payment (sub_1402828E4) and its preview twin (sub_14030B1A0) only look at ids up to 0x16F (367): an ability id above that boundary pays no MP, has no MP check and shows no cost. |
| [AFailedMeshLoadSkipsEveryLaterRendererStep](../behaviors/AFailedMeshLoadSkipsEveryLaterRendererStep.md) | engine (map renderer) | When MapMesh_Load returns anything but 0 (missing file, oversize, wrong header, ids 15 and 33) the texture, system-texture and anim steps are not run and the mesh set's loaded-id field stays at none; the map block's t... |
| [AfterDamageReactionChain](../behaviors/AfterDamageReactionChain.md) | engine (battle action result) | At the end of Battle_ApplyActionResult the unit held in g_BattleActingUnit is tested for passive reactions in a fixed order; the first one present goes to a Brave-roll helper, and the reaction executor then handles on... |
| [AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable](../behaviors/AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable.md) | engine | An AI-controlled unit weighs statuses in two places, both limited to the 40 statuses of the five status bytes: the test of whether an action is worth trying on a unit compares the action's status bytes (from its infli... |
| [AttackWeaponReach](../behaviors/AttackWeaponReach.md) | battle: the tiles the Attack command can target, from the equipped weapon or bare hands | Which tiles a unit's basic Attack can target: one weapon is chosen, its flag byte picks one of four shapes (strike, lunge, direct, arc), heights are compared in half-steps, the unit's own tile and some flagged tiles a... |
| [BattleCommandMenuCarriesSetsAsBytes](../behaviors/BattleCommandMenuCarriesSetsAsBytes.md) | engine | The battle command menu works with skillset ids as single bytes at every step: the unit's two set bytes, the byte lists the menu builders write, the kind array, the AI's command table and the command byte of the 20-by... |
| [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md) | engine | A battle effect is one self-contained file per effect number (0..511): EffectFile_GetTrackRow gives its pack file and size, the loader reads it into one shared buffer and the effect runs from offsets inside the file. |
| [BattleEntryDataIsFiveFilesByKey](../behaviors/BattleEntryDataIsFiveFilesByKey.md) | engine (battle unit entries) | The entry key (variable 50) selects 16 entries of 40 bytes: keys 1..127 read from file 224, 128..255 from 225, 256..383 from 226, 384..511 from 227 (81,920 bytes each, 128 keys), and keys 512..591 from file 892 (51,20... |
| [BattleForkDeterminism](../behaviors/BattleForkDeterminism.md) | a battle resumed from one autosave and driven by the same scripted input in two runs | A battle can be forked only at a save point: the autosave restores the world work copy and a battle image, but not the random stream, the frame counters, the input state or the thread/GPU state. |
| [BattleMapIdPathsAndTheirWidths](../behaviors/BattleMapIdPathsAndTheirWidths.md) | engine (battle map id storage) | The battle map id travels as a 32-bit global (0x140D3A838) set from scene variable 51 or from one of two signed 16-bit event words (-1 means none); the current-map global used for resources is another 32-bit global (0... |
| [BattlePanelJobLineShowsDashesAtLevelZero](../behaviors/BattlePanelJobLineShowsDashesAtLevelZero.md) | engine | The job line of a battle unit panel shows 'Lv. |
| [BattleStatChangeAndCtGainSteps](../behaviors/BattleStatChangeAndCtGainSteps.md) | engine | Unit_ChangeBattleStat changes PA / MA / Speed at the base +0x38..+0x3A with the totals +0x3E..+0x40; Move / Jump are at +0x42 / +0x43; the Haste / Slow CT step is in phase 0 of Battle_TurnEngine; Protect and Shell sca... |
| [BattleUnitOnFieldByte](../behaviors/BattleUnitOnFieldByte.md) | battle unit +0x1B5 | Battle unit byte +0x1B5 (437): 1 placed on the field, 0 not placed (benched), 0xFF an empty slot. |
| [BattleUnitTableListsEnemyRowsThatAreNotOnTheField](../behaviors/BattleUnitTableListsEnemyRowsThatAreNotOnTheField.md) | engine (battle unit table, random battle start) | In a random battle the unit table holds up to nine enemy rows from the start, but only the rows with the slot byte (+0x01) equal to their own slot and the on-field byte (+0x1B5) equal to 1 stand on the field; the othe... |
| [CrystalRollMarksAbilitiesBySlotAndId](../behaviors/CrystalRollMarksAbilitiesBySlotAndId.md) | engine | A crystal's roll marks each rolled ability by its skillset slot (that is what is learned) and, for the pickup window, by its id in two 512-bit sets; an id above 0x1FF is learned but not listed. |
| [EnhancedBattleMapFilesAreNamedByMapId](../behaviors/EnhancedBattleMapFilesAreNamedByMapId.md) | engine (enhanced renderer map load) | The enhanced renderer loads the battle map's mesh and animation by file name built from the map id (three digits at least), and reads one row of the data table 'Map' (registry table 60, keys 0..128) by the map id for ... |
| [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md) | The 106 ability formula handlers and the blocks they call | What a formula handler may assume and has to leave behind, read from the stock handlers and from Battle_ResolveAction: the frame it is called in, how it says 'no effect', which result fields go together, why it must n... |
| [FormulaPostHooksAreKeyedByFormulaId](../behaviors/FormulaPostHooksAreKeyedByFormulaId.md) | engine | After a formula handler runs, sub_14030A11C looks the formula byte up in a 106-row hook table (PostBattleCalc) and runs the row's callback, if any: twelve formulas have an Undead rule there. |
| [HitLabelsAndThePanelEffectLineAreSeparateLists](../behaviors/HitLabelsAndThePanelEffectLineAreSeparateLists.md) | engine | The status label over a unit hit by an action and the effect line of the unit status panel are two different lists. |
| [KoLeavesSomeStatusesOnTheUnit](../behaviors/KoLeavesSomeStatusesOnTheUnit.md) | engine | KO does not end every status: its property row (status 2) cancels the action states 4..7, Confusion, Vampire, Float, Invisibility, Berserk, Critical and every status 23..39, and leaves Undead, Stone, Traitor, Blindnes... |
| [MapDrawListRowsAreSearchedLinearlyToABoundOfFifty](../behaviors/MapDrawListRowsAreSearchedLinearlyToABoundOfFifty.md) | engine (battle map draw lists) | MapDrawLists_Load clears two 513-byte bitsets, then searches the 50 rows of the draw-list table for the row whose 16-bit map id equals the loaded map and sets, for each 0xFFFF-terminated list the row points at, the bi... |
| [MapLoaderIndexesThreeTablesByASixteenBitMapId](../behaviors/MapLoaderIndexesThreeTablesByASixteenBitMapId.md) | engine (battle map load) | Map_LoadBattleData takes the battle map id as a 16-bit value and uses it, with no bound, as the row of three tables: the Move-Find rows (24 bytes), the map-block file numbers of the two text-language copies (4 bytes),... |
| [MapMeshAndAnimFilesCarryTheirOwnMapId](../behaviors/MapMeshAndAnimFilesCarryTheirOwnMapId.md) | engine (map mesh and anim files) | The mesh file and the anim file of a battle map hold the map id in their header, and the loaders refuse a file whose id is not the one requested. |
| [MapRendererTableRowFallbacks](../behaviors/MapRendererTableRowFallbacks.md) | engine (map renderer tables) | What each renderer table gives the build when a map has no row: nodes get default flags (visible), polygon overrides do nothing, system textures use the stock default file, map textures are an empty set, the anim file... |
| [MapResourceFilesAreFileNumberAndSizePairsPerMap](../behaviors/MapResourceFilesAreFileNumberAndSizePairsPerMap.md) | engine (battle map resources) | MapResource_Read reads one resource file of the current map: a request record either carries a file number and a size itself, or carries the marker value 0xFEEDBACC (as a 32-bit number) and a pair number, which select... |
| [MapTextureRowsAreReadOnlyForMapIdsUpToOneTwentySeven](../behaviors/MapTextureRowsAreReadOnlyForMapIdsUpToOneTwentySeven.md) | engine (map texture set) | The loader of the map's colour and lighting textures reads the RefinedBgTexture rows only when the map id is 127 or less; for a larger id it requests no map texture at all. |
| [MapTextureRowsPairEveryNameWithAFrameCount](../behaviors/MapTextureRowsPairEveryNameWithAFrameCount.md) | engine (map texture rows) | A RefinedBgTexture row has two name lists and, beside each, a list of frame counts stored as plain signed 32-bit integers. |
| [MoveFindTakenBitsAreFourPerMapInA128ByteArray](../behaviors/MoveFindTakenBitsAreFourPerMapInA128ByteArray.md) | engine (Move-Find state) | Which hidden tiles of a map have been taken is kept as four bits per map, two maps per byte, in a 128-byte array indexed by scene variable 51 (the current map id): map ids 0..255 fit, and the bytes after the array bel... |
| [MoveRangeRules](../behaviors/MoveRangeRules.md) | battle: the tiles lit when the Move command opens (and the same builder for the AI and for another unit's range) | Which tiles a unit can stop on: a budget of Move + 1 spreads from its tile by steps and straight jumps under height, headroom, terrain-cost and occupancy rules; a final pass keeps the tiles it may stop on. |
| [PlaceNameOfABattleComesFromTheMapRowOfTheLoadedId](../behaviors/PlaceNameOfABattleComesFromTheMapRowOfTheLoadedId.md) | engine (battle title card, pause menu, save list) | The title card, the objective header of the pause menu and the place label of the save list all show the place name belonging to the loaded map id's Map row, and a mid-battle autosave resumes the battle on the saved id. |
| [PlaceTextOfAMapIdComesFromTheMapRowAndTheTownRow](../behaviors/PlaceTextOfAMapIdComesFromTheMapRowAndTheTownRow.md) | engine (battle HUD, save list, title card) | The battle's place text reads the place-name id at row +8 of the Map row of variable 51; the save list reads row +12 (else +8) of the Map row of the low byte of the map id for a battle save, and the Town row of the lo... |
| [PlayerDeploymentAreaTableHasSevenHundredSixtyEightRows](../behaviors/PlayerDeploymentAreaTableHasSevenHundredSixtyEightRows.md) | engine (battle deployment) | The origin of the player's deployment grid comes from a 12-byte-row table of 768 rows in the executable (row number in the u16 at +10), indexed by the deployment area ids in variables 53 and 54 with no bound check; th... |
| [PoisonAndRegenActAtTheEndOfTheUnitsTurn](../behaviors/PoisonAndRegenActAtTheEndOfTheUnitsTurn.md) | engine | Poison and Regen change HP when the turn of the unit ends: Battle_TurnEngine phase 19 writes max HP / 8 as damage (Poison) or as a heal (Regen, only when not poisoned) into the result block of the unit, which the game... |
| [PseudoEffectWordIsASixteenBitEventOperand](../behaviors/PseudoEffectWordIsASixteenBitEventOperand.md) | engine (effect selection) | An effect word of 512 or more selects a row of the 37-word pseudo effect table (row = word - 512, row 0 when 37 or more) and the effect number is masked to 9 bits; event command class 0x18 sets the word, which the eve... |
| [RandomBattleModeSelectsTheLightingVariantOfAMapsTextures](../behaviors/RandomBattleModeSelectsTheLightingVariantOfAMapsTextures.md) | engine (map variation, map textures) | A battle started from a random encounter runs MapRow_SelectVariation in its 'random battle' branch, which always yields a kind code from 1 to 6, and the name builder then reads the second name array of each texture ro... |
| [RandomEncounterRowByte22IsTheBattleMapId](../behaviors/RandomEncounterRowByte22IsTheBattleMapId.md) | engine (random battle start) | A random battle at a battleground takes its battle map from byte 22 of the encounter row, not from a scenario setup record: the row's byte 22 becomes variable 51 when the world-map screen ends, the chosen formation by... |
| [ScenarioSetupRecordFeedsTheBattleSceneVariables](../behaviors/ScenarioSetupRecordFeedsTheBattleSceneVariables.md) | engine (scene entry of an event or battle) | When a scene starts, the routine that applies the scenario setup record finds the record of the current event number (scene variable 39) in the 24-byte table of 887 records and writes the scene variables the battle lo... |
| [SpawnRecordPassiveWords](../behaviors/SpawnRecordPassiveWords.md) | engine | A battle spawn record's reaction / support / movement word below 0x1FE names an ability and 0x1FE or above asks for a random one of the unit's skillset slots 16..21. |
| [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md) | engine | The effective set +0x61 of a unit is written at the end of a fixed group of functions; the applied set is written only from the pending sets, from its own saved copy or derived from +0x61; the game removes a status on... |
| [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md) | engine | A unit's statuses are 40-bit sets (status s = bit 0x80 >> (s & 7) of byte s >> 3) kept in eight regions of the battle unit record: innate a, innate b, the effective set, the applied set, the pending add and remove pai... |
| [StatusLoopsInflictCopyAndBattleTableLifetime](../behaviors/StatusLoopsInflictCopyAndBattleTableLifetime.md) | engine | The status pipeline (Battle_StatusResolve) runs a filter, a refresh and an apply loop over the status ids in order; the inflict copy of a result is read only by formula 56; the battle task clears the unit table at its... |
| [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md) | engine | The battle Status screen lists a unit's statuses in two dword lists (gains, ailments) and reads each one's name, category, sort key and caption from its UIStatusEffect row (key id + 1); the icon path s_%03d is formatt... |
| [StatusVisualMasks](../behaviors/StatusVisualMasks.md) | scene unit status visuals | A scene unit carries set and clear masks for status visuals; SceneUnit_ApplyStatusVisuals applies them and redraws the pose, and a scene unit build zeroes the words. |
| [TurnOrderEntryKeepsNineBitsOfTheAbility](../behaviors/TurnOrderEntryKeepsNineBitsOfTheAbility.md) | engine | A turn-order entry keeps 9 bits of the pending ability (byte 1 plus bit 7 of byte 0 for 256), so the combat timeline names an ability of 512 or more by the stock ability 256 + its low byte (512 = Vengeance). |
| [UsableAbilityListLearnedBitGroup](../behaviors/UsableAbilityListLearnedBitGroup.md) | engine | The usable-ability list reads a unit's learned bits per job group. |

## Tables (89)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [BannerWordCells](../tables/BannerWordCells.md) | Executable (initialised data) |  | 204 rows of 12 bytes | Sprite cells that build the 64 banner word images. |
| [BannerWordColours](../tables/BannerWordColours.md) | Executable (initialised data) |  | 4 rows of 4 bytes | Corner colours of the banner word gradient. |
| [BannerWordRanges](../tables/BannerWordRanges.md) | Executable |  | 65 rows of 4 bytes | For each of 64 banner word images, which run of sprite cells builds it. |
| [BattleEffectLabelRectsLang0](../tables/BattleEffectLabelRectsLang0.md) | Executable |  | 60 rows of 4 bytes | Texture rectangles of the effect label pictures for text language 0. |
| [BattleEffectLabelRectsLang1](../tables/BattleEffectLabelRectsLang1.md) | Executable |  | 60 rows of 4 bytes | Texture rectangles of the effect label pictures for text language 1. |
| [BattleEffectLabelRectsLang2](../tables/BattleEffectLabelRectsLang2.md) | Executable |  | 60 rows of 4 bytes | Texture rectangles of the effect label pictures for text language 2. |
| [BattleEffectLabelRectsLang3](../tables/BattleEffectLabelRectsLang3.md) | Executable |  | 60 rows of 4 bytes | Texture rectangles of the effect label pictures for text language 3. |
| [BattleMenuRowScreenCodes](../tables/BattleMenuRowScreenCodes.md) | Executable |  | 24 rows of 1 bytes | Per battle-menu row id, the screen or message code its confirm opens. |
| [BattleStatusIconFlagMasks](../tables/BattleStatusIconFlagMasks.md) | Executable |  | 40 rows of 4 bytes (42 to the next symbol) | Per status id the bit mask that marks the status on the battle scene object (drawing side). |
| [BattleTiles](../tables/BattleTiles.md) | Executable (filled at run time) |  | 512 records of 8 bytes | The battle map tile table: flags and movement cost per tile, filled by the map setup from the map's level record. |
| [BattleUnits](../tables/BattleUnits.md) | Executable (filled at run time) |  | 21 records of 512 bytes | The live battle unit table: hit points, magic points, tile, facing, charge time and action words. |
| [BattleWeaponHitSoundCues](../tables/BattleWeaponHitSoundCues.md) | Executable |  | 3 rows of 32 bytes | Sound cue (+1) played when an attack effect hits, per weapon type, in three variants. |
| [C_Mes_Id_Sample](../tables/C_Mes_Id_Sample.md) | NXD file | 172 |  | The battle message text table: CMesId_GetText reads one row by message id and the registry result is cached in g_CMesIdTable. |
| [CommandKindMessageOffsets](../tables/CommandKindMessageOffsets.md) | Executable |  | 24 rows of 1 bytes | Offset of the screen / message code of each battle command kind (code = 0x1000 + offset). |
| [CommandKindParams](../tables/CommandKindParams.md) | Executable (initialised data) |  | 16 rows of 4 bytes | Two small values for each battle command kind; the same 16 rows sit in front of the stock menu step table. |
| [CommandMenuSteps](../tables/CommandMenuSteps.md) | Executable (initialised data) |  | 61 rows of 32 bytes | The 61 rows of the stock battle menu step table with the task pointer of the command menu task. |
| [EffectBlendWeights](../tables/EffectBlendWeights.md) | Executable |  | 5 rows of 7 bytes | Four ramps of seven 0..255 blend weights for the flash effect and a fifth row listing five palette slots. |
| [EffectFileLocatorsLang0](../tables/EffectFileLocatorsLang0.md) | Executable |  | 512 rows of 8 bytes | Pack file number and size of every battle effect file (text language 0). |
| [EffectFileLocatorsLangOther](../tables/EffectFileLocatorsLangOther.md) | Executable |  | 512 rows of 8 bytes | Pack file number and size of every battle effect file (text language 1, 2 or 3 (and when no language record exists)). |
| [EffectFlashProfiles](../tables/EffectFlashProfiles.md) | Executable |  | 4 rows of 14 bytes | Seven parameter words per screen flash profile (timing and strength values; the high byte of the last word picks a blend weight row). |
| [EffectKindRecords](../tables/EffectKindRecords.md) | Executable |  | 22 rows of 4 bytes | One row per effect kind: the sequence handler kind that runs it and a parameter word. |
| [EffectNumberPseudo](../tables/EffectNumberPseudo.md) | Executable |  | 37 rows of 2 bytes | Effect number per pseudo effect word. |
| [EffectPaletteSeeds](../tables/EffectPaletteSeeds.md) | Executable |  | 6 rows of 3 bytes | Six 5-bit RGB colours packed into the effect palette at the start of the palette effect. |
| [EffectSpriteSpawnRecords](../tables/EffectSpriteSpawnRecords.md) | Executable |  | 12 rows of 46 bytes | One record per effect sprite group: sprite definition index, frame window, live limit, parameter block and the number of sprites to create. |
| [ElementColours](../tables/ElementColours.md) | Executable |  | 9 rows of 3 bytes | RGB tint per element for effect flashes. |
| [ElementMaskOrder](../tables/ElementMaskOrder.md) | Executable |  | 9 rows of 1 byte | The element bit mask of each element slot of ElementColours: 0 (none), then the bits 0x80, 0x04, 0x08, 0x10, 0x02, 0x01, 0x20, 0x40. |
| [EquipPanelCellsLanguage0A](../tables/EquipPanelCellsLanguage0A.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Sprite cells of the equipment / ability status panel, language 0, variant a. |
| [EquipPanelCellsLanguage0B](../tables/EquipPanelCellsLanguage0B.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 0, variant b. |
| [EquipPanelCellsLanguage2A](../tables/EquipPanelCellsLanguage2A.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 2, variant a. |
| [EquipPanelCellsLanguage2B](../tables/EquipPanelCellsLanguage2B.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 2, variant b. |
| [EquipPanelCellsLanguage3A](../tables/EquipPanelCellsLanguage3A.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 3, variant a. |
| [EquipPanelCellsLanguage3B](../tables/EquipPanelCellsLanguage3B.md) | Executable (initialised data, written at run time) |  | 19 rows of 12 bytes | Equipment panel cells, language 3, variant b. |
| [EquipPanelPaletteCycle](../tables/EquipPanelPaletteCycle.md) | Executable (initialised data) |  | 19 rows of 4 bytes | Two-phase palette ids of the 19 equipment panel cells (a blinking highlight). |
| [EventUnitNumbersA](../tables/EventUnitNumbersA.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields (hp, hpmax, mp, mpmax, wt, wtmax, at, atmax, level, exp) of the legacy dialogue unit panel, first unit. |
| [EventUnitNumbersB](../tables/EventUnitNumbersB.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the legacy dialogue unit panel, second unit. |
| [FastForwardStates](../tables/FastForwardStates.md) | Executable (filled at run time) |  | 256 bytes | Whether fast-forward is allowed in each battle state; filled from the GameModeTypes NXD table. |
| [GameModeTypes](../tables/GameModeTypes.md) | NXD file | 88 |  | Per game-mode flags. |
| [MenuCursorDefaults](../tables/MenuCursorDefaults.md) | Executable (initialised data) |  | 31 rows of 16 bytes | Menu numbers with a pointer to the default record of each battle command menu. |
| [MoveBlockers](../tables/MoveBlockers.md) | Executable (filled at run time) |  | 112 entries of 1 byte | Up to 16 entries of 7 bytes, one per other unit on the map (record MoveBlockerRecord); an unused entry has id 0xFF. |
| [MoveFindItems](../tables/MoveFindItems.md) | Executable (initialised data, written at run time) |  | 128 rows of 24 bytes | Move-Find Item and trap data: per map, up to four hidden tiles with a trap kind and a common and a rare item. |
| [MoveTerrainCost](../tables/MoveTerrainCost.md) | Executable (filled at run time) |  | 64 entries of 1 byte | Movement cost per terrain type for the unit being built (0xFF = cannot enter), copied by Battle_MoveRangeSetup from one of the six sets of g_MoveTerrainCostSets and adjusted for weather and abilities. |
| [MoveTerrainCostSets](../tables/MoveTerrainCostSets.md) | Executable (constant) |  | 6 rows of 64 entries of 1 byte | Six constant cost sets by terrain type: walking, open (Fly / Teleport), float, water (two modes), one more water mode, lava walking. |
| [MoveTileFlags](../tables/MoveTileFlags.md) | Executable (filled at run time) |  | 512 entries of 1 byte | Per-tile flag byte of the move-range builder: 0x01 frontier, 0x02 one-axis slope, 0x04 occupied, 0x08 unit that can be stepped onto, 0x10 standable, 0x20 mountable ally, 0x40 steep, 0x80 blocked. |
| [NxdDataBattle](../tables/NxdDataBattle.md) | NXD file | 83 | 713 rows of 4 bytes | Index of battle ids: the rows carry no data column besides the DLC gate; other tables key off these ids. |
| [NxdDataBattleEventOpcode](../tables/NxdDataBattleEventOpcode.md) | NXD file | 221 | 40 rows of 8 bytes | Index of the battle event opcode numbers (40 rows); rows carry only a designer comment slot. |
| [NxdDataBattleObjective](../tables/NxdDataBattleObjective.md) | NXD file | 47 | 69 rows of 16 bytes, text in 7 languages | Win-condition captions shown in the battle system menu, with a flag marking protect-the-unit objectives. |
| [NxdDataBattleSignal](../tables/NxdDataBattleSignal.md) | NXD file | 214 | 71 rows of 16 bytes, text in 7 languages | Short in-battle banner texts (titles) with a flag for evasion messages. |
| [NxdDataContinuousBattleTimeline](../tables/NxdDataContinuousBattleTimeline.md) | NXD file | 231 | 46 rows of 8 bytes | Timeline steps for chained battles (46 rows). |
| [NxdDataContinuousSortieConfirm](../tables/NxdDataContinuousSortieConfirm.md) | NXD file | 230 | 27 rows of 108 bytes | Sortie confirmation parameters for chained battles, keyed by battle and part. |
| [NxdDataEntryArea](../tables/NxdDataEntryArea.md) | NXD file | 244 | 2519 rows of 8 bytes | Deployment areas: per battle and slot, a position value. |
| [NxdDataEntryNo](../tables/NxdDataEntryNo.md) | NXD file | 109 | 512 rows of 28 bytes | Per entry number (512): link to the sortie confirmation row plus parameters. |
| [NxdDataMap](../tables/NxdDataMap.md) | NXD file | 60 | 129 rows of 32 bytes | Per map (129): parameters; map content lives in map files. |
| [NxdDataMapVariationEvent](../tables/NxdDataMapVariationEvent.md) | NXD file | 207 | 14 rows of 20 bytes | Map variations tied to events (14). |
| [NxdDataMapVariationRandomBattle](../tables/NxdDataMapVariationRandomBattle.md) | NXD file | 208 | 7 rows of 8 bytes | Map variations for random battles (7). |
| [NxdDataOverrideEntryData](../tables/NxdDataOverrideEntryData.md) | NXD file | 96 | 516 rows of 160 bytes | Per-battle unit entry overrides (516 rows, keyed by battle and slot): sprite, job, skills, gear, level and facing. |
| [NxdDataPause](../tables/NxdDataPause.md) | NXD file | 282 | 13 rows of 24 bytes | Pause overlay settings (13) with a sound event link. |
| [NxdDataSortieConfirm](../tables/NxdDataSortieConfirm.md) | NXD file | 54 | 375 rows of 48 bytes | Sortie confirmation screens (375): map link, UI text keys for event, max units and threat rating. |
| [PopupBounceCurve](../tables/PopupBounceCurve.md) | Executable |  | 13 rows of 2 bytes | Arc of offsets for a bouncing pop-up over 13 frames. |
| [RangeRowMasks](../tables/RangeRowMasks.md) | Executable |  | 8 rows of 2 bytes | Bit-run masks (a triangle) used to build the diamond of the range overlay; 8 distances. |
| [ReactionGates](../tables/ReactionGates.md) | Executable |  | 32 bytes | One byte per reaction id: the reaction executor refuses an id whose byte has 1 in its low two bits. |
| [SceneTaskSlots](../tables/SceneTaskSlots.md) | Executable (filled at run time) |  | 1512 entries of 1 byte | Nine scene-task data records of 0xA8 bytes, parsed from u16 token streams during the battle map setup and captured in a kind-1 snapshot. |
| [ScriptedActorPresets](../tables/ScriptedActorPresets.md) | Executable |  | 6 rows of 8 bytes | Scripted unit presets of one scene: a null-terminated list of 6 record pointers copied into the sprite palette and pose tables. |
| [StatsNumbersLive](../tables/StatsNumbersLive.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Eight stat number fields (At, Atmagic, Def, Defmgc, Ar, Armagic, Av, Avmagic) of a legacy screen. |
| [StatsNumbersUnitA](../tables/StatsNumbersUnitA.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Fifteen number fields of the legacy unit page, variant a. |
| [StatsNumbersUnitB](../tables/StatsNumbersUnitB.md) | Executable (initialised data) |  | 15 rows of 32 bytes | Fifteen number fields of the legacy unit page, variant b (two labels differ). |
| [StatsPanelCellsDefault](../tables/StatsPanelCellsDefault.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Detailed stats panel cells, language 1 / default. |
| [StatsPanelCellsLanguage0](../tables/StatsPanelCellsLanguage0.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Sprite cells of the detailed stats panel (Move, Jump, weapon power, At / Def / Ar / Av), language 0. |
| [StatsPanelCellsLanguage2](../tables/StatsPanelCellsLanguage2.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Detailed stats panel cells, language 2. |
| [StatsPanelCellsLanguage3](../tables/StatsPanelCellsLanguage3.md) | Executable (initialised data) |  | 18 rows of 12 bytes | Detailed stats panel cells, language 3. |
| [StatsPanelNumbers](../tables/StatsPanelNumbers.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Number fields of the detailed stats panel (attack, defence, evasion pairs). |
| [StatusGroupMasks](../tables/StatusGroupMasks.md) | Executable (constant) |  | 10 rows of 5 entries of 1 byte | The ten party-wide status group masks, five bytes each: a group test ANDs these bytes against the unit status bytes at +0x61..+0x65. |
| [StatusIconFlags](../tables/StatusIconFlags.md) | Executable (constant) |  |  | The per-status flag words the status panel update reads: index status+1, no bound check. |
| [StatusNumbersActorA](../tables/StatusNumbersActorA.md) | Executable (initialised data, written at run time) |  | 7 rows of 32 bytes | Number fields of the acting unit's status panel (variant A). |
| [StatusNumbersActorB](../tables/StatusNumbersActorB.md) | Executable (initialised data) |  | 6 rows of 32 bytes | Number fields of the acting unit's status panel (variant B, no AT). |
| [StatusNumbersTargetA](../tables/StatusNumbersTargetA.md) | Executable (initialised data, written at run time) |  | 7 rows of 32 bytes | Number fields of the target unit's status panel (variant A). |
| [StatusNumbersTargetB](../tables/StatusNumbersTargetB.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Number fields of the target unit's status panel with the hit chance (variant B). |
| [StatusPanelFrameLines](../tables/StatusPanelFrameLines.md) | Executable |  | 8 rows of 7 bytes | Eight one-pixel shaded border lines of the battle status panel (light and dark pairs). |
| [StatusPanelLayoutsDefault](../tables/StatusPanelLayoutsDefault.md) | Executable (initialised data) |  | 8 rows of 8 bytes | Per status panel kind, its layout block, for text languages 1 and every language that has no table of its own. |
| [StatusPanelLayoutsLanguage0](../tables/StatusPanelLayoutsLanguage0.md) | Executable (initialised data) |  | 8 rows of 8 bytes | Per status panel kind, its layout block, language 0. |
| [StatusPanelLayoutsLanguage2](../tables/StatusPanelLayoutsLanguage2.md) | Executable (initialised data) |  | 8 rows of 8 bytes | Per status panel kind, its layout block, text language 2. |
| [StatusPanelLayoutsLanguage3](../tables/StatusPanelLayoutsLanguage3.md) | Executable (initialised data) |  | 8 rows of 8 bytes | Per status panel kind, its layout block, text language 3. |
| [StatusPanelPaletteIds](../tables/StatusPanelPaletteIds.md) | Executable (initialised data) |  | 22 rows of 2 bytes | Palette ids of the battle status panel parts. |
| [StatusProperties](../tables/StatusProperties.md) | Executable |  | 40 rows of 16 bytes | Per status: priority, countdown, group flags, the statuses it cancels and the statuses that block it. |
| [SurfacePairConstants](../tables/SurfacePairConstants.md) | Executable |  | 63 rows of 2 bytes | Per surface type, two bytes that are 25 everywhere; their two destination words have no other reader. |
| [TerrainProperties](../tables/TerrainProperties.md) | Executable |  | 2 blocks of 64 bytes | Two 64-byte blocks indexed by terrain type: the ability id the terrain gives and a flag byte whose bit 0x80 marks harmful terrain. |
| [UnitStatusNumbersMode0](../tables/UnitStatusNumbersMode0.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the legacy unit info message window, actor with level and experience. |
| [UnitStatusNumbersMode1](../tables/UnitStatusNumbersMode1.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Number fields of the legacy unit info message window, actor with hit chance. |
| [UnitStatusNumbersMode2](../tables/UnitStatusNumbersMode2.md) | Executable (initialised data) |  | 8 rows of 32 bytes | Number fields of the legacy unit info message window, target with hit chance. |
| [UnitStatusNumbersMode3](../tables/UnitStatusNumbersMode3.md) | Executable (initialised data) |  | 10 rows of 32 bytes | Number fields of the legacy unit info message window, target with level and experience. |
