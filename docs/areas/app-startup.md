# Application and startup

Entry, frame loop, message pump, clock, exception handling and the startup debug/capture gates.

Functions: 19, Structures: 3, Globals: 2, Observed behaviours: 5, Tables: 2.

## Functions (19)

| Name | Address | Purpose |
|---|---|---|
| [App_LaunchClassic](../functions/App_LaunchClassic.md) | `0x1401DDB5C` | Starts the Classic executable and ends this one. |
| [App_ProcessMessages](../functions/App_ProcessMessages.md) | `0x14002F728` | Drains up to ten Win32 messages per call. |
| [App_RunFrame](../functions/App_RunFrame.md) | `0x14002A1F0` | One iteration of the game's application loop: frame pacing, the debug/capture gate, Steam callbacks, the UI/render/audio update chain and the secondary frame-rate wait. |
| [BonusEntitlement_IsOwned](../functions/BonusEntitlement_IsOwned.md) | `0x1401006F4` | Answers whether the bonus entitlement of a SystemBonusEntitlement row is owned. |
| [BonusEntitlements_Setup](../functions/BonusEntitlements_Setup.md) | `0x1400FFE14` | Builds the application's entitlement list from the SystemBonusEntitlement table and collects the bonus content paths of each entitlement. |
| [Cursor_Apply](../functions/Cursor_Apply.md) | `0x14001DC14` | Makes the cursor table's current entry the OS cursor, or hides the cursor. |
| [Cursor_LoadTable](../functions/Cursor_LoadTable.md) | `0x1400103E4` | Loads the game's mouse cursors into the cursor object's table (index -> HCURSOR) and applies the current one. |
| [Debug_DetectCaptureTools](../functions/Debug_DetectCaptureTools.md) | `0x140082894` | Returns 1 when a known graphics-capture/injection layer is loaded, or when a GPU/COM query on `hostObject+3504` succeeds. |
| [Game_Main](../functions/Game_Main.md) | `0x14002BD50` | The game's WinMain body: it rejects a debugger at startup, sets the working directory, creates the splash/window objects, runs the application loop until exit, and tears the objects down. |
| [GameTasks_RunFrameSteps](../functions/GameTasks_RunFrameSteps.md) | `0x1402574E0` | Runs the game's task threads for one displayed frame: the whole per-frame step is repeated GlobalWork_GetSpeedMultiplier times, which is how fast-forward speeds the game up. |
| [GlobalWork_GetFastForwardMode](../functions/GlobalWork_GetFastForwardMode.md) | `0x1401E8A9C` | Returns the fast-forward mode of the current frame after the 'Fast-forward' setting is applied: 0 none, 1 battle, 2 event script, 3 world map. |
| [GlobalWork_GetSpeedMultiplier](../functions/GlobalWork_GetSpeedMultiplier.md) | `0x1401E8AC4` | The number of game steps per displayed frame: 1 normally, 3 at fast-forward level 1, 5 at level 2. |
| [Mem_CopyChecked](../functions/Mem_CopyChecked.md) | `0x14002630C` | The game's checked copy: copies the smaller of the destination size and the count, and reports a destination too small or a null pointer; every copy of the 20-byte action block (unit +0x1A0) and of the formula block's... |
| [Startup_InstallExceptionHandling](../functions/Startup_InstallExceptionHandling.md) | `0x14002EC0C` | Installs the top-level unhandled-exception filter and the startup diagnostic state: the self-debug call, the user name, the DebugDump path, the lock-file name and the invalid-parameter handler. |
| [Startup_SetDataDirectory](../functions/Startup_SetDataDirectory.md) | `0x14002EA04` | Ensures the process working directory is the executable's `data` directory, so relative `data/` paths resolve when the game is launched from another directory. |
| [sub_1402561D0](../functions/sub_1402561D0.md) | `0x1402561D0` | The top-level per-frame update that keeps the save machinery and the boot/movie transitions moving. |
| [Time_GetTimestamp](../functions/Time_GetTimestamp.md) | `0x14006A9B4` | Returns a monotonic timestamp in 1/300000-second units. |
| [TopLevelExceptionFilter](../functions/TopLevelExceptionFilter.md) | `0x14002EAE0` | The unhandled-exception filter installed by Startup_InstallExceptionHandling. |
| [WorldMap_UpdateFastForward](../functions/WorldMap_UpdateFastForward.md) | `0x14015C0DC` | On the world map (mode 3) sets the fast-forward level to 1 while action 89 is held, else 0. |

## Structures (3)

| Name | Size (bytes) | Summary |
|---|---|---|
| [EntitlementListNode](../structs/EntitlementListNode.md) | 40 | One node of the application's entitlement list (g_Application +1488), built by BonusEntitlements_Setup. |
| [GlobalWork](../structs/GlobalWork.md) | 136 | ffto::Game::GlobalWork (vtable 0x140713EA8), the singleton at g_GlobalWork. |
| [ImportSlotRow](../structs/ImportSlotRow.md) | 8 | One row of SteamApiImportSlots. |

## Globals (2)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_FastForwardMultipliers](../globals/g_FastForwardMultipliers.md) | `0x140672018` | `int32[3]` | Game steps per displayed frame by fast-forward level: 1, 3, 5 (GlobalWork_GetSpeedMultiplier). |
| [g_GlobalWork](../globals/g_GlobalWork.md) | `0x143CD9DD0` | `GlobalWork *` | Singleton ffto::Game::GlobalWork (136 bytes, vtable 0x140713EA8, created by sub_1400B532C): fast-forward level +0x58, frame step +0x5C, fast-forward mode +0x60 (record GlobalWork). |

## Observed behaviours (5)

| Name | Scope | Summary |
|---|---|---|
| [AFaultInAGameTaskFreezesTheGame](../behaviors/AFaultInAGameTaskFreezesTheGame.md) | engine | Game logic runs in task threads that the main thread hands control to each frame (GameTasks_RunFrameSteps waits on them). |
| [BonusEntitlementGroupMatch](../behaviors/BonusEntitlementGroupMatch.md) | engine (bonus entitlements) | The bonus entitlement setup matches the entitlement row's group number against the group number of every DLCPathList row; it does not look the path list up by key. |
| [FastForwardState](../behaviors/FastForwardState.md) | battle, event scripts (story scenes, battle dialogue) and the world map, enhanced edition | How the fast-forward hold and the dialogue auto-advance toggle become state, how to read 'fast-forward is active now' from memory with no input, what gates a hold, and what the state changes. |
| [QuitLoopExit](../behaviors/QuitLoopExit.md) | how the quit request ends the main loop | Game_Main runs App_RunFrame in a loop and leaves it when it returns 0; App_RunFrame returns whether the quit request byte is 0. |
| [QuitRequest](../behaviors/QuitRequest.md) | how the game ends itself or hands over to the Classic executable | The quit request byte of the application object and every path that sets it. |

## Tables (2)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [FastForwardMultipliers](../tables/FastForwardMultipliers.md) | Executable (constant) |  | 3 entries of 4 bytes | Game steps per displayed frame by fast-forward level: 1, 3, 5 (GlobalWork_GetSpeedMultiplier). |
| [SteamApiImportSlots](../tables/SteamApiImportSlots.md) | Executable |  | 11 rows of 8 bytes (the tail of the import table) | Import address slots of eleven functions of the Steam API library (find or create user interface, unregister call result, context init, get user handle, restart app if necessary, API init, register / unregister callba... |
