# Application and startup

Entry, frame loop, message pump, clock, exception handling and the startup debug/capture gates.

Functions: 71, Structures: 4, Globals: 2, Registries: 1, Flows: 9, Observed behaviours: 7, Tables: 3.

## Functions (71)

| Name | Address | Purpose |
|---|---|---|
| [App_LaunchClassic](../functions/App_LaunchClassic.md) | `0x1401DDB5C` | Starts the Classic executable and ends this one. |
| [App_ProcessMessages](../functions/App_ProcessMessages.md) | `0x14002F728` | Drains up to ten Win32 messages per call. |
| [App_RunFrame](../functions/App_RunFrame.md) | `0x14002A1F0` | One iteration of the game's application loop: frame pacing, the debug/capture gate, Steam callbacks, the UI/render/audio update chain and the secondary frame-rate wait. |
| [Application_Initialize](../functions/Application_Initialize.md) | `0x1400296BC` | First virtual step of the application object: copies the startup block into the object, brings up the platform services and decides whether the splash window is shown. |
| [Application_InitPlatformServices](../functions/Application_InitPlatformServices.md) | `0x14002DEFC` | Gathers process and machine facts into the application object, starts COM and the exception handling, and applies the low-memory and file-cache switches. |
| [BonusEntitlement_IsOwned](../functions/BonusEntitlement_IsOwned.md) | `0x1401006F4` | Answers whether the bonus entitlement of a SystemBonusEntitlement row is owned. |
| [BonusEntitlements_Setup](../functions/BonusEntitlements_Setup.md) | `0x1400FFE14` | Builds the application's entitlement list from the SystemBonusEntitlement table and collects the bonus content paths of each entitlement. |
| [Boot_CloseUI](../functions/Boot_CloseUI.md) | `0x1401DE0C4` | Removes the boot UI when the boot launcher is left: the startup add-on, the title cushion, the launcher and the second system agent's add-on. |
| [Boot_EnterState4](../functions/Boot_EnterState4.md) | `0x1401E7C0C` | Enters boot state 4, first handing its four values to the render-command submitter and, when /return was given, storing 256 in a boot field. |
| [Boot_Frame](../functions/Boot_Frame.md) | `0x1400B5A7C` | One frame of the boot sequence: the per-frame dispatcher for boot states 0..4. |
| [Boot_SetState](../functions/Boot_SetState.md) | `0x1401E79A0` | Changes the boot state. |
| [Boot_StartThreads](../functions/Boot_StartThreads.md) | `0x140256EF0` | Creates the game's 17 task threads and installs the game-thread entry in the task scheduler. |
| [Boot_Update](../functions/Boot_Update.md) | `0x1401DE164` | The boot launcher: a local state machine on the boot UI object. |
| [Boot_UpdateVideo](../functions/Boot_UpdateVideo.md) | `0x1402561D0` | The per-frame handler of boot state 2. |
| [BuildReport_InitAll](../functions/BuildReport_InitAll.md) | `0x14000D844` | Static initialiser: sets up all 256 build report records. |
| [BuildReport_ReadEnvironment](../functions/BuildReport_ReadEnvironment.md) | `0x1400B1AA4` | Clears a large report record's sections and copies three build environment variables into it. |
| [Classic_BuildLaunchArguments](../functions/Classic_BuildLaunchArguments.md) | `0x1401E6354` | Writes the current display, sound and camera settings as a switch string of the second kind (the one Startup_ParseDisplaySwitches reads) into a 256-byte buffer and returns its length. |
| [Cursor_Apply](../functions/Cursor_Apply.md) | `0x14001DC14` | Makes the cursor table's current entry the OS cursor, or hides the cursor. |
| [Cursor_LoadTable](../functions/Cursor_LoadTable.md) | `0x1400103E4` | Loads the game's mouse cursors into the cursor object's table (index -> HCURSOR) and applies the current one. |
| [Debug_DetectCaptureTools](../functions/Debug_DetectCaptureTools.md) | `0x140082894` | Returns 1 when a known graphics-capture/injection layer is loaded, or when a GPU/COM query on `hostObject+3504` succeeds. |
| [DirectStorage_ConfigureManager](../functions/DirectStorage_ConfigureManager.md) | `0x14006FA94` | Applies the DirectStorage switches to the DirectStorage library's configuration block, creates the factory and sets up the manager's queue and request records. |
| [DirectStorage_InitDevice](../functions/DirectStorage_InitDevice.md) | `0x14006B578` | Gets the graphics device for the file system manager, starts DirectStorage when it is enabled and supported, and decides the 'direct destination' flag from the switches. |
| [DrawMode_BuildShaderTable](../functions/DrawMode_BuildShaderTable.md) | `0x1403CECFC` | Fills a 34-entry table that maps a draw mode number to a shader id, a variant number and a flag byte. |
| [Game_LoopReset](../functions/Game_LoopReset.md) | `0x140283FCC` | The one-time reset before the outer loop: it sets the 374x240 screen mode, clears the fade, battle and event state, resets the event counters, calls the scene/UI reset helpers, and seeds the constant block. |
| [Game_Main](../functions/Game_Main.md) | `0x14002BD50` | The game's WinMain body: it rejects a debugger at startup, sets the working directory, creates the splash/window objects, runs the application loop until exit, and tears the objects down. |
| [Game_MainLoop](../functions/Game_MainLoop.md) | `0x1402D3FA0` | The game's outer loop. |
| [Game_MainLoopReset](../functions/Game_MainLoopReset.md) | `0x1402D4A2C` | The 15-byte pre-loop wrapper: it calls the reset helper `sub_140283FCC` and then enters `Game_MainLoop`. |
| [Game_ThreadMain](../functions/Game_ThreadMain.md) | `0x140348658` | The entry installed for the game task thread: on first use it prepares the 4 MB work arena and the 512x272 display state, points every effect base slot at the shared effect buffer, then resets the game state and enter... |
| [GameTasks_RunFrameSteps](../functions/GameTasks_RunFrameSteps.md) | `0x1402574E0` | Runs the game's task threads for one displayed frame: the whole per-frame step is repeated GlobalWork_GetSpeedMultiplier times, which is how fast-forward speeds the game up. |
| [GameWindow_FillCreateParams](../functions/GameWindow_FillCreateParams.md) | `0x140010750` | Listener step that fills the window creation record: class and title text, icon, position, size and style, from the saved settings and the startup switches. |
| [GlobalWork_GetFastForwardMode](../functions/GlobalWork_GetFastForwardMode.md) | `0x1401E8A9C` | Returns the fast-forward mode of the current frame after the 'Fast-forward' setting is applied: 0 none, 1 battle, 2 event script, 3 world map. |
| [GlobalWork_GetSpeedMultiplier](../functions/GlobalWork_GetSpeedMultiplier.md) | `0x1401E8AC4` | The number of game steps per displayed frame: 1 normally, 3 at fast-forward level 1, 5 at level 2. |
| [Mem_CopyChecked](../functions/Mem_CopyChecked.md) | `0x14002630C` | The game's checked copy: copies the smaller of the destination size and the count, and reports a destination too small or a null pointer; every copy of the 20-byte action block (unit +0x1A0) and of the formula block's... |
| [Memory_GetAvailableBytes](../functions/Memory_GetAvailableBytes.md) | `0x140018A2C` | Reports how much memory the game may still use: the operating system's available physical memory, or the /memory_limit figure minus what the allocators hold. |
| [Memory_InitAllocators](../functions/Memory_InitAllocators.md) | `0x1400112F4` | Brings the allocators up (reference counted) and records the memory limit given by /memory_limit. |
| [Opening_EndToTitle](../functions/Opening_EndToTitle.md) | `0x14037DE18` | Ends the opening and resets the scene into the title path: it releases the three opening objects, clears the scene-object bit, calls `Scene_Init(1)` so `TitleScene_Start` pushes task 14, then clears the two scene word... |
| [OpeningMenu_Task](../functions/OpeningMenu_Task.md) | `0x1402F0124` | A four-row scene menu built on sprite rows: it moves a highlighted row, starts the opening text or the title scene on a choice, and leaves the scene loop for the other choices. |
| [OpeningScene_Resume](../functions/OpeningScene_Resume.md) | `0x1402F0848` | Scene task 13: the title's way back into the opening. |
| [OpeningScene_Start](../functions/OpeningScene_Start.md) | `0x1402EFF6C` | The mode-0 scene entry: it loads the opening scene page (or shows the title menu on the shop-gate path), resets the scene flag bits around a movie wait, ends any pending UI fade, then pushes scene task 0 and seeds the... |
| [OpeningSubmenu_Task](../functions/OpeningSubmenu_Task.md) | `0x14037D998` | A three-row scene submenu created by the four-row menu. |
| [OpeningTask_0](../functions/OpeningTask_0.md) | `0x1402F0060` | Scene task 0: the bridge from the mode-0 opening start to the title scene. |
| [OpeningTask_1](../functions/OpeningTask_1.md) | `0x1402F00D4` | Scene task 1: the opening's exit gate. |
| [OpeningTask_10](../functions/OpeningTask_10.md) | `0x14037F1F0` | Scene task 10: the closing task of the alternate scene loop (`SceneLoop_RunAlt`); nothing ties it to the opening scene beyond sharing the opening's task table. |
| [OpeningTask_12](../functions/OpeningTask_12.md) | `0x14037F398` | Table entry 12: a two-way gate for the opening stage chain. |
| [OpeningTask_4](../functions/OpeningTask_4.md) | `0x14037DEA0` | Opening stage 4: the per-frame state machine that turns the opening text/menu into the date selection or the return-to-title shortcut. |
| [OpeningTask_5](../functions/OpeningTask_5.md) | `0x14037E83C` | Opening stage 5: the month/day picker. |
| [OpeningTask_6](../functions/OpeningTask_6.md) | `0x14037EDD4` | Opening stage 6: the date confirmation page. |
| [OpeningTask_7](../functions/OpeningTask_7.md) | `0x140332704` | Opening stage 7: the return-to-title shortcut. |
| [OpeningTask_8](../functions/OpeningTask_8.md) | `0x140332A7C` | Table entry 8: a gate that watches the runnable flag of event-task block 2, can set two skip words once (`word_1437F664C` and the latch `byte_142FEF6DF`) while that task runs, and when the task stops it pops itself an... |
| [OpeningTask_9](../functions/OpeningTask_9.md) | `0x14037F188` | Scene task 9: the first task of the alternate scene loop (`SceneLoop_RunAlt`); nothing ties it to the opening scene beyond sharing the opening's task table. |
| [Scene_Init](../functions/Scene_Init.md) | `0x14037F510` | The scene-global reset: it seeds the scene flags, task stack and page buffer, then starts the title path directly for a non-zero mode or through the opening bootstrap for mode 0. |
| [SceneLoop_Run](../functions/SceneLoop_Run.md) | `0x140331C14` | The normal scene loop: it seeds the scene from the mode argument, dispatches one scene task per frame until scene flag bit 0 clears, then returns the hand-over code the task left in `dword_141876F94`. |
| [SceneLoop_RunAlt](../functions/SceneLoop_RunAlt.md) | `0x14039DCE8` | The alternate scene bootstrap: it performs the scene reset inline (without `Scene_Init`), loads the 0x8800-byte run of data kind 877 starting at sector 101 into the scene buffer, pushes scene task 9, and runs the same... |
| [Shader_GetStateOverrides](../functions/Shader_GetStateOverrides.md) | `0x1403CFA94` | Adjusts a small state record for a shader id (flags that differ from the default for some of the built-in shaders). |
| [ShaderManager_RegisterBuiltinShaders](../functions/ShaderManager_RegisterBuiltinShaders.md) | `0x1403CD018` | Registers the 37 built-in shaders, ids 1000 to 1036, each with a name, a vertex blob and a pixel blob, in the shader manager at qword_140D3AD60+432. |
| [SoundCommand_ProcessQueue](../functions/SoundCommand_ProcessQueue.md) | `0x140501F50` | Sound driver step that pops queued commands and runs them; one command selects a config category layer by name. |
| [Splash_CreateWindow](../functions/Splash_CreateWindow.md) | `0x14002EDC8` | Creates the splash window: loads a bitmap resource, registers a window class and shows a centred window of the bitmap's size. |
| [Startup_InstallExceptionHandling](../functions/Startup_InstallExceptionHandling.md) | `0x14002EC0C` | Installs the top-level unhandled-exception filter and the startup diagnostic state: the self-debug call, the user name, the DebugDump path, the lock-file name and the invalid-parameter handler. |
| [Startup_MatchLaunchSwitch](../functions/Startup_MatchLaunchSwitch.md) | `0x14002C634` | Looks for an argument that is exactly the given switch name and reports whether it is present and at which index. |
| [Startup_ParseDisplaySwitches](../functions/Startup_ParseDisplaySwitches.md) | `0x1401E6650` | Reads a second set of switches (resolution, screen mode, output, focus and cursor options, vsync, brightness, language, sound volumes, camera options) from the argument copy held by the application and fills a 48-byte... |
| [Startup_ParseLaunchSwitches](../functions/Startup_ParseLaunchSwitches.md) | `0x14002C2EC` | Reads the process arguments for the startup switches and sets the matching bytes, words and dwords of the 0x118-byte startup block that `Game_Main` built just before. |
| [Startup_SetDataDirectory](../functions/Startup_SetDataDirectory.md) | `0x14002EA04` | Ensures the process working directory is the executable's `data` directory, so relative `data/` paths resolve when the game is launched from another directory. |
| [Time_GetTimestamp](../functions/Time_GetTimestamp.md) | `0x14006A9B4` | Returns a monotonic timestamp in 1/300000-second units. |
| [TitleScene_DemoReturn](../functions/TitleScene_DemoReturn.md) | `0x14037F354` | Scene task 11: the return from the title's attract demo. |
| [TitleScene_NewGameHandoff](../functions/TitleScene_NewGameHandoff.md) | `0x1402F0C14` | Scene task 15: the title's new-game hand-off. |
| [TitleScene_Start](../functions/TitleScene_Start.md) | `0x1402F0864` | The title scene's start function: it resets the game and party state for a fresh title session, allocates the eight-byte title scene frame, shows the title menu (or seeds the save-return result), and pushes scene task... |
| [TitleScene_Task](../functions/TitleScene_Task.md) | `0x1402F0944` | Scene task id 14: it runs `TitleScene_Update` once per dispatch and turns the result into the next scene task id, or ends the scene for the outer loop. |
| [TitleScene_Update](../functions/TitleScene_Update.md) | `0x1401DE744` | The title scene's state machine. |
| [TopLevelExceptionFilter](../functions/TopLevelExceptionFilter.md) | `0x14002EAE0` | The unhandled-exception filter installed by Startup_InstallExceptionHandling. |
| [WinMain](../functions/WinMain.md) | `0x140010E70` | The process entry the C runtime calls: it takes the Win32 startup arguments, fills in the system and game listener objects, and hands them to `Game_Main`. |
| [WorldMap_UpdateFastForward](../functions/WorldMap_UpdateFastForward.md) | `0x14015C0DC` | On the world map (mode 3) sets the fast-forward level to 1 while action 89 is held, else 0. |

## Structures (4)

| Name | Size (bytes) | Summary |
|---|---|---|
| [EntitlementListNode](../structs/EntitlementListNode.md) | 40 | One node of the application's entitlement list (g_Application +1488), built by BonusEntitlements_Setup. |
| [GlobalWork](../structs/GlobalWork.md) | 136 | ffto::Game::GlobalWork (vtable 0x140713EA8), the singleton at g_GlobalWork. |
| [ImportSlotRow](../structs/ImportSlotRow.md) | 8 | One row of SteamApiImportSlots. |
| [StartupConfig](../structs/StartupConfig.md) | 280 | The 280-byte block that Game_Main fills from the process arguments and the startup parser, then Application_Initialize copies into the application object at +1200. |

## Globals (2)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_FastForwardMultipliers](../globals/g_FastForwardMultipliers.md) | `0x140672018` | `int32[3]` | Game steps per displayed frame by fast-forward level: 1, 3, 5 (GlobalWork_GetSpeedMultiplier). |
| [g_GlobalWork](../globals/g_GlobalWork.md) | `0x143CD9DD0` | `GlobalWork *` | Singleton ffto::Game::GlobalWork (136 bytes, vtable 0x140713EA8, created by sub_1400B532C): fast-forward level +0x58, frame step +0x5C, fast-forward mode +0x60 (record GlobalWork). |

## Registries (1)

| Name | Summary |
|---|---|
| [LaunchSwitches](../registries/LaunchSwitches.md) | The command-line switches the executable recognises: 23 startup switches read by Startup_ParseLaunchSwitches and 10 display-settings switches read by Startup_ParseDisplaySwitches. |

## Flows (9)

| Name | Summary |
|---|---|
| [ApplicationLifecycle](../flows/ApplicationLifecycle.md) | The order from process entry to the first scene. |
| [BootStateMachine](../flows/BootStateMachine.md) | The boot dispatcher's states 0..4 and the 5..7 hand-over codes. |
| [BootToGameThread](../flows/BootToGameThread.md) | The hand-over from boot to the game's task threads: boot state 2 creates 17 task threads, installs the game-thread entry in the task-0 command slot, then stops the boot dispatcher. |
| [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md) | How the process arguments become behaviour: the startup parser fills the startup block, the application object keeps a copy, the memory, window, splash and DirectStorage steps read their bytes, a second parser reads t... |
| [OpeningStages](../flows/OpeningStages.md) | How the opening's later stages advance. |
| [OpeningToTitle](../flows/OpeningToTitle.md) | The opening's route to the title and back. |
| [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md) | The hand-off tasks between the front end's three loops. |
| [SceneTaskDispatch](../flows/SceneTaskDispatch.md) | How the opening and title scenes advance. |
| [TitleSceneFlow](../flows/TitleSceneFlow.md) | How the Enhanced title scene advances from the scene reset to a menu hand-off. |

## Observed behaviours (7)

| Name | Scope | Summary |
|---|---|---|
| [AFaultInAGameTaskFreezesTheGame](../behaviors/AFaultInAGameTaskFreezesTheGame.md) | engine | Game logic runs in task threads that the main thread hands control to each frame (GameTasks_RunFrameSteps waits on them). |
| [BonusEntitlementGroupMatch](../behaviors/BonusEntitlementGroupMatch.md) | engine (bonus entitlements) | The bonus entitlement setup matches the entitlement row's group number against the group number of every DLCPathList row; it does not look the path list up by key. |
| [BuildServerVariablesCopiedAtStartup](../behaviors/BuildServerVariablesCopiedAtStartup.md) | engine (start-up) | Before the game starts, a static initialiser fills 256 report records and copies three build-server environment variables (a job name, a build number and a build address) into each. |
| [FastForwardState](../behaviors/FastForwardState.md) | battle, event scripts (story scenes, battle dialogue) and the world map, enhanced edition | How the fast-forward hold and the dialogue auto-advance toggle become state, how to read 'fast-forward is active now' from memory with no input, what gates a hold, and what the state changes. |
| [QuitLoopExit](../behaviors/QuitLoopExit.md) | how the quit request ends the main loop | Game_Main runs App_RunFrame in a loop and leaves it when it returns 0; App_RunFrame returns whether the quit request byte is 0. |
| [QuitRequest](../behaviors/QuitRequest.md) | how the game ends itself or hands over to the Classic executable | The quit request byte of the application object and every path that sets it. |
| [SoundConfigDebugLayerNames](../behaviors/SoundConfigDebugLayerNames.md) | engine (sound driver) | The sound driver resolves a config category name to a layer number; two names that no config file needs to define have built-in numbers: 'SDebug' is layer -2 and 'SUserConfig' is layer -3. |

## Tables (3)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [FastForwardMultipliers](../tables/FastForwardMultipliers.md) | Executable (constant) |  | 3 entries of 4 bytes | Game steps per displayed frame by fast-forward level: 1, 3, 5 (GlobalWork_GetSpeedMultiplier). |
| [SceneTaskTable](../tables/SceneTaskTable.md) | Executable (constant) |  | 16 entries of 8 bytes (scene task ids 0..15) | The 16-entry table of scene task handlers that the two scene loops call once per frame. |
| [SteamApiImportSlots](../tables/SteamApiImportSlots.md) | Executable |  | 11 rows of 8 bytes (the tail of the import table) | Import address slots of eleven functions of the Steam API library (find or create user interface, unregister call result, context init, get user handle, restart app if necessary, API init, register / unregister callba... |
