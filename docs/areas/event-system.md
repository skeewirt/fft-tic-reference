# Event system

The event variable store, the cooperative task and thread scheduler, the event interpreter with its script loader and scanners, the dialogue, sprite, colour and camera tasks, and the helpers the event opcodes share.

Functions: 162, Structures: 1, Globals: 5, Observed behaviours: 3.

## Functions (162)

| Name | Address | Purpose |
|---|---|---|
| [EventAngle_Quantize](../functions/EventAngle_Quantize.md) | `0x140240408` | Stores a copy of an angle rounded down to a multiple of 4096 in a global, for angles from -16384 to 16383. |
| [EventBlock_ApplyOperands](../functions/EventBlock_ApplyOperands.md) | `0x1402355E0` | The callback installed by opcode 0x28: resolves the unit named by its operands and gives it a 128-byte block, a doubled count and a fixed value, using a block helper. |
| [EventCamera_MoveTask](../functions/EventCamera_MoveTask.md) | `0x1402401A8` | The task started by event opcode 0x1B: moves the camera from its current state to six target values over a number of frames. |
| [EventChannel_BindStepTask](../functions/EventChannel_BindStepTask.md) | `0x1402421AC` | The task started by event opcode 0x6B: releases a keyed object, binds or selects its channel, then runs the same frame loop as opcode 0x6A. |
| [EventChannel_StepTask](../functions/EventChannel_StepTask.md) | `0x14024223C` | The task started by event opcode 0x6A: runs a per-frame refresh of a keyed object's channel for a set number of frames, then releases or keeps the key. |
| [EventCharaSprite_SetTable256Entry](../functions/EventCharaSprite_SetTable256Entry.md) | `0x1400D1B74` | Loads a table-256 entry into a sub-object of the unit sprite renderer and sets how long the change takes. |
| [EventColor_Task](../functions/EventColor_Task.md) | `0x14023FA14` | The task started by event opcode 0x1A: applies a screen colour change and waits out its duration. |
| [EventColorPath_Task](../functions/EventColorPath_Task.md) | `0x14023FB30` | The task started by event opcode 0x3E: moves three values in a straight line from a start triple to an end triple, two frames per step, passing each step to `sub_1402F4618` with the operand's value byte, then ends. |
| [EventControl_ApplyCarry](../functions/EventControl_ApplyCarry.md) | `0x14021EEC4` | When an event script starts, restores auto-advance and fast-forward from the previous event if the new event's EventId row allows it. |
| [EventControl_CarryToNextEvent](../functions/EventControl_CarryToNextEvent.md) | `0x14021F14C` | When an event script ends, saves whether auto-advance and fast-forward were on so a chained event can start with them. |
| [EventControl_IsAutoAdvancing](../functions/EventControl_IsAutoAdvancing.md) | `0x1401DB498` | True when dialogue auto-advance should act this frame: the overlay is in its running state, auto is on and no fast-forward hold is in progress. |
| [EventControl_PausedTick](../functions/EventControl_PausedTick.md) | `0x1401DB978` | Paused frame of the event overlay: accepts the completed hold as a skip (state 3) or resumes on the pause / back action. |
| [EventControl_Reset](../functions/EventControl_Reset.md) | `0x1401DB370` | Clears the event pause overlay state on frames where no event script tick ran. |
| [EventControl_RunningTick](../functions/EventControl_RunningTick.md) | `0x1401DB6C4` | The unpaused frame of the event overlay: toggles dialogue auto-advance on action 91 and runs the fast-forward hold (actions 89 / 90) with its press gate and its one-second ramp. |
| [EventControl_ShowFastForwardLabel](../functions/EventControl_ShowFastForwardLabel.md) | `0x1401DBD14` | Shows or hides the fast-forward indicator of the dialogue window and remembers it in EventControl +44. |
| [EventControl_TryOpenPause](../functions/EventControl_TryOpenPause.md) | `0x1401DBC24` | Opens the event pause overlay on the pause action and picks its button hints: with Skip when EventSkip_IsAvailable is true, without it otherwise. |
| [EventControl_Update](../functions/EventControl_Update.md) | `0x1401DB3CC` | Per-frame state machine of the event pause overlay (state 0 off, 1 running, 2 paused, 3 skip chosen). |
| [EventControl_UpdateGuide](../functions/EventControl_UpdateGuide.md) | `0x1401DBD54` | Chooses the button guide shown under an event: 503 while fast-forward is held or running, 504 in auto-advance, otherwise 501 / 506 for five seconds after an input. |
| [EventCounter_Task](../functions/EventCounter_Task.md) | `0x14023FA9C` | The task started by event opcode 0x41: runs without returning on its own, adding to the shared 16-bit counter on a repeating frame cycle until the skip test ends it. |
| [EventDataLoad_Poll](../functions/EventDataLoad_Poll.md) | `0x140274324` | A state machine that starts a table-selected game data read for the current track index and reports busy until the read and a timed delay have finished; it is the busy test that opcode 0x8A waits on, through MultiStr_... |
| [EventEndSlate_ShowTask](../functions/EventEndSlate_ShowTask.md) | `0x14021EB40` | The task started by event opcode 0xEC: adds the end-slate UI add-on, plays its language-keyed state and its Show state, waits until the state ends or the skip test passes, then removes the add-on. |
| [EventFlagWait_Task](../functions/EventFlagWait_Task.md) | `0x14023589C` | The task started by event opcode 0x8B: waits frame by frame until the global dword_140CDB824 becomes zero, then ends. |
| [EventMapTitle_DrawSweep](../functions/EventMapTitle_DrawSweep.md) | `0x140302318` | Builds four 184-byte map-title draw records for one sweep value into a 736-byte buffer and links them into the draw list; the layout argument (0 or 1) chooses the record variant and the link order. |
| [EventMapTitle_LoadTexture](../functions/EventMapTitle_LoadTexture.md) | `0x140302B68` | Loads the map-title texture file chosen by scene variable 51 (maptitle_%03d.tex) into a 10,240-byte buffer, unless the enhanced-build test says it is not needed; the 0x91 handler calls it before starting the sweep task. |
| [EventMapTitle_SweepTask](../functions/EventMapTitle_SweepTask.md) | `0x14030299C` | The task started by event opcode 0x91: runs three sweeps of a 0-to-255 value over frames (up, hold at 255, sweep again with the second layout), one draw and one frame per value, using the operand 3 step, and ends earl... |
| [EventMessage_Scripted](../functions/EventMessage_Scripted.md) | `0x1402DB09C` | The dialogue-window task used by the first task table: it shows a scripted event message, pages through the text and waits for the player. |
| [EventMessage_Task](../functions/EventMessage_Task.md) | `0x1402238C4` | The dialogue-window task: it shows an event message in a speech window, pages through the text and waits for the player. |
| [EventMode_DispatchTask](../functions/EventMode_DispatchTask.md) | `0x14023354C` | The task started by event opcode 0x78: clears a global and hands the task's mode and argument to the mode dispatcher, which starts one of several helper tasks. |
| [EventMoveTargets_Rewrite](../functions/EventMoveTargets_Rewrite.md) | `0x1402404CC` | Rewrites the operands of the next opcode 0x19 from the vectors of two units and, in mode 0, adds an angle target equal to the current angle plus the shortest turn to a fixed angle table. |
| [EventMusic_LoadTrack](../functions/EventMusic_LoadTrack.md) | `0x1401D7450` | Starts background music track number `track` on channel `channel` of the global sound object, which is the body of opcode 0x84 with channel 9: a cache hit is handed to a replay helper, and a miss replaces that channel... |
| [EventNode_PlayShow](../functions/EventNode_PlayShow.md) | `0x14013BA64` | When a global byte is set, marks a UI node and plays its Show state. |
| [EventNode_SetFromTable224](../functions/EventNode_SetFromTable224.md) | `0x14013B9D4` | Finds the table-224 entry for two keys and passes its text offset to the GUI target of a UI node. |
| [EventObject_MoveTask](../functions/EventObject_MoveTask.md) | `0x140240100` | The task started by event opcode 0x6E: tags itself as a move task and runs the movement worker for the object named in its operands. |
| [EventObject_MoveWorker](../functions/EventObject_MoveWorker.md) | `0x14023FC54` | Movement worker for opcode 0x6E: moves a unit record from its current position to three 16-bit targets over a number of frame steps, shaped by a curve mode. |
| [EventPad_UpdateRepeat](../functions/EventPad_UpdateRepeat.md) | `0x1402EBDE0` | Updates the held-button auto-repeat state used while the event system runs; only the scheduler slot (task index 16) does the work. |
| [EventPanel_PickRow](../functions/EventPanel_PickRow.md) | `0x14033D5C4` | The second half of the 0x7D task: reads the row number the task stored in its block, picks that row of a language-dependent panel table and runs the branch for the row kind. |
| [EventPanel_QueueAndWait](../functions/EventPanel_QueueAndWait.md) | `0x14033D4C0` | The kind-1 branch of EventPanel_PickRow: queues the value 50 in a two-entry queue, waits until the queue is released, then calls the callback sub_1402B1F08 with 1 and changes the global dword_1411A7D08 from 1 to 2. |
| [EventPanel_ShowTask](../functions/EventPanel_ShowTask.md) | `0x140233E64` | The task started by event opcode 0x7D: takes a turn in the shared sequencer, then shows a panel chosen by its operand from a language-dependent table and waits for that panel's work to finish. |
| [EventPanel_ShowWaitTask](../functions/EventPanel_ShowWaitTask.md) | `0x140221564` | The task started by event opcode 0xAB when the enhanced flag is set: shows the UI table row named by its operand on the panel and waits until the panel closes or the skip test passes. |
| [EventPreviewUnit_StageSlot](../functions/EventPreviewUnit_StageSlot.md) | `0x140214284` | Finds a preview-unit slot for a 16-bit reference, copies its 512-byte record into the staging buffer and sets the staged flag. |
| [EventPreviewUnits_RunFrames](../functions/EventPreviewUnits_RunFrames.md) | `0x140214A70` | Runs the per-frame preview-unit update for opcode 0xC1: it applies flagged preview-unit slots and, when any were flagged, waits while the UI reports busy. |
| [EventRef_ResolveSlot](../functions/EventRef_ResolveSlot.md) | `0x140226A18` | Turns a script reference id into the slot number of the object it names. |
| [EventScene_QueueHelpText](../functions/EventScene_QueueHelpText.md) | `0x1402C08C0` | Prepares a unit preview scene task: it builds the preview sprite record for the selected party unit, queues the shared help-text id as render command 12 and starts the event task. |
| [EventScript_FindInstruction](../functions/EventScript_FindInstruction.md) | `0x1402425D0` | Scans the loaded event script for an instruction with a given opcode (or an alternative opcode) whose first operand byte has a given value. |
| [EventScript_FindOpcode](../functions/EventScript_FindOpcode.md) | `0x1402426BC` | Scans the loaded event script from a byte offset for the next instruction with a given opcode and returns its offset. |
| [EventScript_InstructionLength](../functions/EventScript_InstructionLength.md) | `0x1402CBE2C` | Returns the length in bytes of the event script instruction at a pointer: one opcode byte plus its operand bytes. |
| [EventScript_IsSkipStop](../functions/EventScript_IsSkipStop.md) | `0x14021F1B4` | Decides whether a given opcode counts as a stopping point when the interpreter skips forward through a script. |
| [EventScript_LoadCurrent](../functions/EventScript_LoadCurrent.md) | `0x14023F37C` | Loads the event the game is currently on, if it is not already loaded. |
| [EventScript_LoadFile](../functions/EventScript_LoadFile.md) | `0x1402F3BC4` | Loads one event script file from the game's script folder into a caller buffer. |
| [EventScript_LoadIntoBuffer](../functions/EventScript_LoadIntoBuffer.md) | `0x1402340A4` | Loads an event script into the shared 10,240-byte event buffer and substitutes a variant for a few special events. |
| [EventScript_ReadDword](../functions/EventScript_ReadDword.md) | `0x1402F0C48` | Reads a 4-byte little-endian operand from script memory. |
| [EventScript_Run](../functions/EventScript_Run.md) | `0x14023A868` | The event interpreter: it walks the loaded event script one instruction at a time and carries out each opcode. |
| [EventScript_SkipTick](../functions/EventScript_SkipTick.md) | `0x14023987C` | The event fast-forward tick: while the skip action is held it raises the skip state that makes the event text advance. |
| [EventScript_TaskMain](../functions/EventScript_TaskMain.md) | `0x14023A830` | The entry function of the event interpreter task: loads the current event, adjusts one global flag, and runs the interpreter. |
| [EventSequence_RecordTask](../functions/EventSequence_RecordTask.md) | `0x140233558` | The task started by event opcode 0x76: takes a turn in the shared sequencer, then records two values per frame into a history until the task is stopped. |
| [EventSequencer_TakeTurn](../functions/EventSequencer_TakeTurn.md) | `0x1402334FC` | Waits for the shared sequencer to be free, claims it by writing the caller's tag, waits until it is released, and ends the caller when the flag word at word_140D408F8 is 1. |
| [EventSkip_IsAvailable](../functions/EventSkip_IsAvailable.md) | `0x140239834` | Says whether the running event script may be skipped now. |
| [EventSkip_IsViewerEvent](../functions/EventSkip_IsViewerEvent.md) | `0x1402397F8` | The second way an event becomes skippable: event variable 508 set (an event started from a viewer path), with the event number outside 410..425 and a blocking flag clear. |
| [EventSoundEntry_Append](../functions/EventSoundEntry_Append.md) | `0x1401D7AF8` | The body of opcode 0xA6: looks the id up in data table 280 and then, through a value in that row, in data table 279; when both rows are valid it creates a 56-byte sound resource that carries the id and appends it to t... |
| [EventSoundEntry_SetStateById](../functions/EventSoundEntry_SetStateById.md) | `0x1401D7CF0` | The body of opcode 0xA7: for every entry in the sound object's entry list whose id equals the operand, stops its resource if one is held, and sets the entry's state byte to 4. |
| [EventSprite_LoadTask](../functions/EventSprite_LoadTask.md) | `0x140233EA0` | The task started by event opcode 0x58: loads the sprite data for an event character into memory for one of two display sides, then ends. |
| [EventState_MoveTask](../functions/EventState_MoveTask.md) | `0x14023F520` | The task started by event opcode 0x19: moves up to seven state-block values toward the operand targets over the operand step count, then writes the final values and ends. |
| [EventStateTrack_RunTask](../functions/EventStateTrack_RunTask.md) | `0x140234E04` | The task started by event opcode 0x1D: turns the 0x19 instructions of the block up to the next 0x1E into seven piecewise tracks, one per state value, and plays them frame by frame until the last track ends or the skip... |
| [EventSubquestPanel_Run](../functions/EventSubquestPanel_Run.md) | `0x140214CEC` | Shows a sub-quest UI panel that holds the opcode 0xAC operand, blocks until one of the input keys 0x15, 0x1A or 0x1B is active, then hides and releases the panel. |
| [EventSubScript_RunTask](../functions/EventSubScript_RunTask.md) | `0x1402358C8` | The task started by event opcode 0x2A: runs the instructions after 0x2A up to 0x2B as a parallel script, dispatching each opcode to unit, scene-variable and wait helpers, and ends when the block ends or the skip test ... |
| [EventTable226_FindRecord](../functions/EventTable226_FindRecord.md) | `0x140245A2C` | Looks up one record of table 226 by key and stores the record pointer in the output slot. |
| [EventTask_Start](../functions/EventTask_Start.md) | `0x1402BA5AC` | Starts a task in the first task table: resets the slot's block, marks it runnable and records its entry function. |
| [EventTask_Terminate](../functions/EventTask_Terminate.md) | `0x1402BA698` | Ends the current event task. |
| [EventTask_WaitFrame](../functions/EventTask_WaitFrame.md) | `0x1402F2C14` | The event system's wait-one-frame primitive: moves on to the next runnable task, refreshes the held-button repeat state, then yields. |
| [EventTasks_Init](../functions/EventTasks_Init.md) | `0x1402EA2F0` | Initialises the first task group: points its task table, variable store and event buffer at their storage. |
| [EventText_FindMessage](../functions/EventText_FindMessage.md) | `0x1402DDBC8` | Finds an event message in memory from its packed 16-bit reference and returns a pointer to the start of its text. |
| [EventText_NextChar](../functions/EventText_NextChar.md) | `0x140221404` | Advances through an event message byte stream by one position, following the stream's back-reference codes. |
| [EventThread_ReturnToEntry](../functions/EventThread_ReturnToEntry.md) | `0x1402F3710` | Restarts the calling event task thread from its saved entry context. |
| [EventThread_Yield](../functions/EventThread_Yield.md) | `0x1402F377C` | Hands control from the calling event task back to the scheduler and sleeps until that task is resumed. |
| [EventUnitBlock_RunTask](../functions/EventUnitBlock_RunTask.md) | `0x140235D38` | The task started by event opcode 0x49: runs the instructions after 0x49 up to 0x4A once, handling the unit opcodes 0x45 and 0x82 and skipping the rest, then ends. |
| [EventUnitMove_Task](../functions/EventUnitMove_Task.md) | `0x1402400C0` | The task started by event opcode 0x3B: moves a unit's three-value vector from its current value to three operand targets over the operand step count, then ends. |
| [EventUnitObject_ApplyId](../functions/EventUnitObject_ApplyId.md) | `0x140136798` | Looks up a 4-byte id in table 87 and applies the matching text to the UI sub-object of the object at [[qword_143CD9DA8+16]+104], closing its panel first. |
| [EventUnitStatus_ApplyTask](../functions/EventUnitStatus_ApplyTask.md) | `0x14024189C` | The task started by event opcode 0x92: resolves a unit id, applies a mode-dependent update to the unit's preview row and status bits, runs the unit-end callback, waits the given frames, then ends. |
| [EventUnitStatus_RefreshNode](../functions/EventUnitStatus_RefreshNode.md) | `0x14027294C` | The unit-end callback installed by the 0x92 status paths: finds the unit node for a slot and passes it to sub_1401FAF54, which refreshes that unit's flag words and state. |
| [EventUnitStatus_RunMembers](../functions/EventUnitStatus_RunMembers.md) | `0x1402416C8` | For each unit the reference selects, refreshes its per-unit block from its preview row and runs the unit-end callback for it, then waits 0, 40 or 80 frames; when flag is zero it finishes with the group-end callback su... |
| [EventUnitStatus_SetBit](../functions/EventUnitStatus_SetBit.md) | `0x140241BD0` | For one unit reference, clears two 5-byte bitmaps in the unit's preview row, sets one bit in one of them, and sends mode 2 of the scene callback dispatch for that row. |
| [EventVar_Alu](../functions/EventVar_Alu.md) | `0x1402EC038` | The event variable arithmetic unit: applies one operation to the destination variable using either a literal or another variable as the operand, and stores the result back into the packed store. |
| [EventVar_Read](../functions/EventVar_Read.md) | `0x1402E9898` | Reads one event variable by index. |
| [EventVar_ResolveSlot](../functions/EventVar_ResolveSlot.md) | `0x1402EC298` | Maps an event variable index to the address of the dword in the store that holds it. |
| [EventVar_Write](../functions/EventVar_Write.md) | `0x1402E9918` | Writes one event variable by index. |
| [EventVoice_PlayTask](../functions/EventVoice_PlayTask.md) | `0x140221488` | The task started by event opcode 0xC2 when the enhanced flag is set: starts a table entry for its id, keeps it in the list while it is present, and stops it when the object or the skip test says so. |
| [GameData_ReadSectors](../functions/GameData_ReadSectors.md) | `0x1402F40C4` | The game's general data read entry point, expressed in the original disc layout: it reads a run of 2048-byte sectors of one kind of game file, and sends event scripts (kind 17) to EventScript_LoadFile. |
| [IdRemap_Lookup](../functions/IdRemap_Lookup.md) | `0x1402BA9C8` | Remaps an id above 0xA7 through the 406-row table `g_IdRemapPairs` (7 pairs of two dwords per row, 56 bytes); returns the replacement, or the id itself when it is not in the table. |
| [SceneCallback_Dispatch](../functions/SceneCallback_Dispatch.md) | `0x1402F7D1C` | Calls the callback in the global function pointer `qword_140D40940` for modes 0 to 6. |
| [SceneGroup_ResolveId](../functions/SceneGroup_ResolveId.md) | `0x140240888` | Reads an operand id and decides whether it names one unit or a group: ids 1 to 255 are resolved to a unit id, and ids 0 and 256 and up select a group mode for SceneUnit_TestGroupMember. |
| [SceneGroup_SetFlag04](../functions/SceneGroup_SetFlag04.md) | `0x140241F54` | The shared body of opcodes 0x6C and 0x6D: sets or clears bit 0x04 of byte +143 of each unit selected by the operand. |
| [SceneMsgTask_Run](../functions/SceneMsgTask_Run.md) | `0x140231D7C` | Scene task that reads the current scene's message word and dispatches a message descriptor built from it. |
| [SceneObject_FindBySlot](../functions/SceneObject_FindBySlot.md) | `0x140260A98` | Finds the object list node for a slot number. |
| [SceneObject_SnapFieldBands](../functions/SceneObject_SnapFieldBands.md) | `0x140272B6C` | Walks the linked list at qword_140D3A410 and sets a 16-bit field of each entry from that entry's low 12 bits of another field; EventScript_Run calls it at the start of the 0xE3 transition path. |
| [ScenePad_UpdateRepeat](../functions/ScenePad_UpdateRepeat.md) | `0x14023970C` | Updates the held-button repeat for the second task table. |
| [ScenePlacement_WriteGroup](../functions/ScenePlacement_WriteGroup.md) | `0x140241FF0` | Writes a 7-byte placement record for each unit of a unit or group that passes the group test against the 21 keys, each record headed from a cell position given by the operands. |
| [ScenePlacement_WritePair](../functions/ScenePlacement_WritePair.md) | `0x140240D5C` | Writes 7-byte placement records for a pair of units: the second unit for each valid, different unit that passes the group test, and the first unit too when flag is 0, with headings computed from the two units' positio... |
| [ScenePreview_ClaimForUnit](../functions/ScenePreview_ClaimForUnit.md) | `0x1402731E8` | For one unit: sets its state words at +0x0E and +0x1F8 to 1 and claims its preview entry. |
| [ScenePreview_FindEntry](../functions/ScenePreview_FindEntry.md) | `0x14027260C` | Finds a preview-unit record by a one-byte key and reports how it was found through the status pointer. |
| [ScenePreview_IndexOfSlot](../functions/ScenePreview_IndexOfSlot.md) | `0x140273064` | Returns the preview index of the object in a slot: byte +444 of the object's preview data, or -1 when the slot has no object or no preview data. |
| [ScenePreview_ShowEntry](../functions/ScenePreview_ShowEntry.md) | `0x14027313C` | Shows the preview-table entry for a slot: clears the preview globals, claims the entry and queues a draw entry built from the record's fields. |
| [ScenePreview_SlotOfIndex](../functions/ScenePreview_SlotOfIndex.md) | `0x140273090` | The reverse of ScenePreview_IndexOfSlot: finds the object whose preview index is the given value and returns its slot number. |
| [SceneTask_FindFree](../functions/SceneTask_FindFree.md) | `0x1402424DC` | Finds a free slot in the second task table for a task that the caller is about to start with SceneTask_Start. |
| [SceneTask_FindTag](../functions/SceneTask_FindTag.md) | `0x140242588` | Finds a running task in the second table by its tag. |
| [SceneTask_Start](../functions/SceneTask_Start.md) | `0x1402F7DE4` | Starts a task in the second task table: resets the slot's block, marks it runnable and records its entry function so its thread begins there. |
| [SceneTask_Terminate](../functions/SceneTask_Terminate.md) | `0x1402F7EC8` | Ends the current task in the second task table; the error trap and the normal exit for scene and event-script tasks. |
| [SceneTask_WaitFrame](../functions/SceneTask_WaitFrame.md) | `0x1402F7CAC` | The wait-one-frame primitive for the second task table; over 100 routines call it to wait. |
| [SceneTasks_Init](../functions/SceneTasks_Init.md) | `0x140235F1C` | Initialises the second task group: clears its task table and points its table, variable store and event buffer at their storage. |
| [SceneTransition_CheckTables](../functions/SceneTransition_CheckTables.md) | `0x1402391C4` | Runs a transition check over the scene group tables and, in one case, writes scene variable 39; the value it returns is not used by its caller in EventScript_Run. |
| [SceneUnit_AddPosition](../functions/SceneUnit_AddPosition.md) | `0x140272F04` | Adds a three-word delta to the position words of the unit node for a slot. |
| [SceneUnit_ApplyFlagRow](../functions/SceneUnit_ApplyFlagRow.md) | `0x140240C9C` | Sets or clears a flag on one unit, writes its 7-byte row when the slot is 0 to 20, and calls two scene helpers with the slot and operand values. |
| [SceneUnit_ApplyModeAndAction](../functions/SceneUnit_ApplyModeAndAction.md) | `0x140241DF8` | Applies a mode byte to the flag byte of each unit that an id names, then passes an action code to the state helper, and waits for frames when the code is 83, 84 or 85. |
| [SceneUnit_BuildPalette](../functions/SceneUnit_BuildPalette.md) | `0x14026C858` | The body of opcode 0xA8: when the unit exists, builds 16 packed 15-bit words from the table 302 row selected by the unit's byte +343 and passes them to `sub_1402F7594` with the index 3. |
| [SceneUnit_BuildPoint](../functions/SceneUnit_BuildPoint.md) | `0x140272BD0` | Builds the three-word world point (x, height, z) of a unit from its live record. |
| [SceneUnit_CallbackSend19](../functions/SceneUnit_CallbackSend19.md) | `0x140273810` | The callback that opcode 0x98 installs in the global qword_140D40940: for one unit key it sends the value 0x13 to the unit's sub-record and returns whether the unit exists. |
| [SceneUnit_CopyField4C](../functions/SceneUnit_CopyField4C.md) | `0x14022697C` | Copies three 16-bit words from a unit node into a caller buffer, used by the opcode 0x53 and 0x69 bodies. |
| [SceneUnit_MeasureRange](../functions/SceneUnit_MeasureRange.md) | `0x1403130C4` | The callback that opcode 0x87 installs in the global qword_140D40940: it measures a scaled distance from a source unit to a target unit, or to a fixed three-word point when no target unit has a preview index, and retu... |
| [SceneUnit_Oscillate120](../functions/SceneUnit_Oscillate120.md) | `0x140240A78` | Runs a 120-frame sequence on one unit: a callback, a helper call, two SceneUnit_ResetAndQueue4 calls with +31 and then -31, waits of 10, 50 and 60 frames, and a final clear of two bytes of the unit's preview record. |
| [SceneUnit_ReleasePartner](../functions/SceneUnit_ReleasePartner.md) | `0x1401FB398` | When the unit node's low status bits equal 1, clears the unit's and its partner's status fields and calls the release routine for both. |
| [SceneUnit_ResetAndQueue4](../functions/SceneUnit_ResetAndQueue4.md) | `0x140270864` | Resets a unit's state bytes and words and queues an action (code 4) with the given values through sub_1402F7C20. |
| [SceneUnit_ResetFields](../functions/SceneUnit_ResetFields.md) | `0x140272E98` | Resets the state fields of one unit node and calls the partner release routine on it. |
| [SceneUnit_RunPlacement](../functions/SceneUnit_RunPlacement.md) | `0x140269074` | Runs the placement setup for one scene object record, using the record's bytes 8 to 11 to choose a table entry and a position table. |
| [SceneUnit_SetFlag12C](../functions/SceneUnit_SetFlag12C.md) | `0x14026CA00` | The body of opcode 0xA9: clears bit 0x40 of the unit's byte +0x12C (300) and sets it again to bit 0 of byte +8 of the table 305 row selected by the unit's byte +345, when that row exists. |
| [SceneUnit_SetFlag156](../functions/SceneUnit_SetFlag156.md) | `0x14027322C` | Marks a unit's flag byte at +0x156 as set (0 during event 54) and clears two of its state words. |
| [SceneUnit_TestGroupMember](../functions/SceneUnit_TestGroupMember.md) | `0x1402408F0` | Tests whether unit key 'key' (0 to 20 in the callers' loops) is a member of the group selected by *groupMode. |
| [SceneUnit_UpdateNearFlag](../functions/SceneUnit_UpdateNearFlag.md) | `0x140273838` | Sets or clears one flag byte of a unit node by comparing two values from sub_140262808, only when the global mode dword_140782A94 equals 386. |
| [SceneUnit_ZeroPosAndReset](../functions/SceneUnit_ZeroPosAndReset.md) | `0x1402356B0` | Zeroes the three position words of the unit named by its operands and then calls the unit reset routine on it, with one preview-table byte set to 6 for the duration of that call. |
| [SceneVar_Alu](../functions/SceneVar_Alu.md) | `0x140242700` | The second task group's event variable arithmetic unit. |
| [SceneVar_Read](../functions/SceneVar_Read.md) | `0x1402332D8` | Reads one event variable by index through the second task group's copy of the variable system. |
| [SceneVar_ResolveSlot](../functions/SceneVar_ResolveSlot.md) | `0x140242984` | Maps an event variable index to the address of its dword in the second task group's variable store. |
| [SceneVar_Write](../functions/SceneVar_Write.md) | `0x140233368` | Writes one event variable by index through the second task group's copy of the variable system. |
| [SoundCue_Play](../functions/SoundCue_Play.md) | `0x1402BAA30` | Plays a sound cue on the first free sound channel of 13..19: remaps the cue with IdRemap_Lookup, drops it when the result is above 0x2B1, and returns the channel used or -1. |
| [sub_1401365AC](../functions/sub_1401365AC.md) | `0x1401365AC` | Gives the input focus to one of the two option nodes of a choice window: the node the message window task calls "the cursor line" while a story choice waits. |
| [sub_140136654](../functions/sub_140136654.md) | `0x140136654` | Shows the finger cursor over the focused option of a choice window once the window's nodes are all built. |
| [sub_1401DEC14](../functions/sub_1401DEC14.md) | `0x1401DEC14` | Walks the inline text of an event instruction: it steps byte by byte, handles the three control codes it knows, measures each text run and advances to the next instruction. |
| [sub_1401DF120](../functions/sub_1401DF120.md) | `0x1401DF120` | Answers whether a text needs two or more lines at a given width: it decodes the text, measures it and divides the measurement by the width. |
| [sub_1401E1618](../functions/sub_1401E1618.md) | `0x1401E1618` | One step of the event command task: it starts the task, runs one queued command per step, and tears the task down when the script ends. |
| [sub_14024138C](../functions/sub_14024138C.md) | `0x14024138C` | Applies or clears a status on a preview unit from an event command, then refreshes the unit's status display. |
| [sub_1402C6514](../functions/sub_1402C6514.md) | `0x1402C6514` | One of the scene-task bodies event opcode 0x78 starts (mode 5): it places the units of the scene, shows their speech balloons and unit markers, and runs until the task is stopped. |
| [sub_1402C72B8](../functions/sub_1402C72B8.md) | `0x1402C72B8` | One of the scene-task bodies event opcode 0x78 starts (mode 6): a unit-display scene that also drives the desertion marker, built on the same balloon and unit-marker task skeleton as mode 5. |
| [sub_1402DF374](../functions/sub_1402DF374.md) | `0x1402DF374` | Builds and runs an event message scene: it resolves the message text, places the speaking units and their sprites, and waits frame by frame until the message ends. |
| [sub_1402F2C70](../functions/sub_1402F2C70.md) | `0x1402F2C70` | Dispatches one of the six scene text commands: the command number picks a branch and the branch forwards the remaining arguments to the handler whose address sits in the slot at 0x14184B3B0. |
| [sub_1402F8684](../functions/sub_1402F8684.md) | `0x1402F8684` | Scene task that carries out one scripted scene instruction: it registers a task record, waits frames, and builds the sprites and text the instruction asks for. |
| [sub_1402FB7C8](../functions/sub_1402FB7C8.md) | `0x1402FB7C8` | Fills battle snapshot block B from game-data table rows and repairs the live save arrays from it; it is the only writer of that block. |
| [sub_140300768](../functions/sub_140300768.md) | `0x140300768` | Event unit-block task that paints one scene unit: it reads the shape byte of the unit's job row and drives the sprite and text setup. |
| [sub_140300D74](../functions/sub_140300D74.md) | `0x140300D74` | Second event unit-block painter: the same job-row read as sub_140300768 plus sector reads from the game data files. |
| [sub_1403015A4](../functions/sub_1403015A4.md) | `0x1403015A4` | Builds an event or message record from a text id, choosing a different id range depending on the text id's kind. |
| [sub_140301ED8](../functions/sub_140301ED8.md) | `0x140301ED8` | Builds the text of an event message. |
| [sub_140338A28](../functions/sub_140338A28.md) | `0x140338A28` | Second scene-instruction task of the same family as sub_1402F8684: it registers a task slot, runs a frame loop and builds sprites and text. |
| [sub_14033F8C0](../functions/sub_14033F8C0.md) | `0x14033F8C0` | Event task that opens a UI panel: it drops the pending input bit, reads the panel selector and starts the panel task with a fixed text id. |
| [sub_1403456D4](../functions/sub_1403456D4.md) | `0x1403456D4` | Event task that runs a scripted message window: it resolves the message, waits for the player's input and writes the outcome to the event variables. |
| [sub_140371550](../functions/sub_140371550.md) | `0x140371550` | Paints a three-cell text line: it resolves a message through the text table and writes the three u16 cells at 0x14078D9C0. |
| [sub_140372F9C](../functions/sub_140372F9C.md) | `0x140372F9C` | Runs one pass of a script: it walks the instruction stream, calls EventCmd_Run for each command and advances the cursor. |
| [sub_140373BB0](../functions/sub_140373BB0.md) | `0x140373BB0` | Builds the 0x8800 text row used by the script layer: it writes the row's cells and hands them to the layout helpers. |
| [sub_140373DE8](../functions/sub_140373DE8.md) | `0x140373DE8` | Second builder for the 0x8800 text row: it computes the ids and passes them to the text dispatcher sub_1402F2C70. |
| [sub_14037D4BC](../functions/sub_14037D4BC.md) | `0x14037D4BC` | Builds a 0xC800 text row: it writes the row descriptor and calls the layout helpers for the cells. |
| [sub_14037E1E8](../functions/sub_14037E1E8.md) | `0x14037E1E8` | Opening-sequence step that builds a 0xB800 text row and advances the opening script. |
| [sub_1403980AC](../functions/sub_1403980AC.md) | `0x1403980AC` | Third scene-instruction task of the sub_1402F8684 family: it registers a task slot, runs a frame loop and builds sprites and text. |
| [sub_14039DA58](../functions/sub_14039DA58.md) | `0x14039DA58` | Advances the calendar held in event variables 0x67 (year), 0x2E (month) and 0x2F (day) by a number of days and updates the 64 date-keyed bytes and records beside it. |
| [UserSituation_IsMet](../functions/UserSituation_IsMet.md) | `0x1400FF8A4` | Answers whether a UserSituation condition (nxd table 90, keyed by situation and entry) holds; the UI asks it to show or lock features. |
| [UserSituation_SetValue](../functions/UserSituation_SetValue.md) | `0x1400FF660` | Sets one situation counter and tells the registered listeners. |
| [UserSituation_TestCheck](../functions/UserSituation_TestCheck.md) | `0x1400FFAF0` | One check of a UserSituation row against the situation store (qword_143CD9DE0): a flag byte, a counter compare or a scene variable. |

## Structures (1)

| Name | Size (bytes) | Summary |
|---|---|---|
| [EventControl](../structs/EventControl.md) | 64 | ffto::Game::Event::EventControl (vtable 0x140713658), the singleton at g_EventControl: the event-script pause overlay and its hold-to-skip. |

## Globals (5)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_EventKeepAutoLatch](../globals/g_EventKeepAutoLatch.md) | `0x140C6AD73` | `uint8` | 1 after auto-advance was switched on with action 91 while the setting enableEventKeepAuto is on; EventControl_RunningTick then switches auto on again in the next event; 0 after auto is switched off. |
| [g_EventScriptBuffer](../globals/g_EventScriptBuffer.md) | `0x140D3CD50` | `uint8[10240]` | The 0x2800-byte event-script file image the script loader fills and the event interpreter runs. |
| [g_EventWorkPtr](../globals/g_EventWorkPtr.md) | `0x14078DCE8` | `ptr` | Pointer to the event work block at 0x140D40060; the event tasks reach their work area through it. |
| [g_ScreenFade](../globals/g_ScreenFade.md) | `0x142FF9E08` | `uint64` | The fade and skip state: the low dword is the fade alpha, the high dword the skip state (0 none, 1 requested, 2 skipping). |
| [g_SkipRequestSource](../globals/g_SkipRequestSource.md) | `0x142FF9EF4` | `uint64` | The skip-request source: its high dword is copied into the fade/skip state by the event runner. |

## Observed behaviours (3)

| Name | Scope | Summary |
|---|---|---|
| [SceneSkipState](../behaviors/SceneSkipState.md) | every skippable story scene: event scripts (world map, town, battle) and movies | Whether the scene on screen can be skipped with the pause overlay + hold, and which kind of scene it is, read from memory without any input. |
| [SoundCuesAreRemappedBeforeTheyPlay](../behaviors/SoundCuesAreRemappedBeforeTheyPlay.md) | engine | Every sound cue goes through SoundCue_Play, which first remaps it with IdRemap_Lookup (table g_IdRemapPairs, 406 rows of 7 from/to pairs) and drops any result above 0x2B1. |
| [StoryChoiceBalloon](../behaviors/StoryChoiceBalloon.md) | story scenes: a dialogue balloon with several selectable lines | A choice balloon is an ordinary message whose text contains the control code 0xFB (options start on this line) and 0xFC (run the choice). |
