# LaunchSwitchesFromArgumentsToReaders

- **Kind:** flow
- **Area:** [Application and startup](../areas/app-startup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the process arguments become behaviour: the startup parser fills the startup block, the application object keeps a copy, the memory, window, splash and DirectStorage steps read their bytes, a second parser reads the display set later, and the relaunch string reuses the display syntax.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [Game_Main](../functions/Game_Main.md) | V | Returns at once when a debugger is attached; otherwise clears the 0x118-byte startup block and sets its defaults (sub_14002C1FC). |
| <a id="2"></a>2 | [Startup_ParseLaunchSwitches](../functions/Startup_ParseLaunchSwitches.md) | V | Reads the 23 startup switches with Startup_MatchLaunchSwitch. |
| <a id="3"></a>3 | [Memory_InitAllocators](../functions/Memory_InitAllocators.md) | V | Called first by sub_14002BF70: stores the /memory_limit value. |
| <a id="4"></a>4 | [Application_Initialize](../functions/Application_Initialize.md) | V | Copies the block to g_Application+1200 and brings up the platform services and the splash window (skipped with /return). |
| <a id="5"></a>5 | [Application_InitPlatformServices](../functions/Application_InitPlatformServices.md) | V | Reads /enable_memory_save and /disable_file_cache. |
| <a id="6"></a>6 | [Splash_CreateWindow](../functions/Splash_CreateWindow.md) | V | Runs only when /return is absent. |
| <a id="7"></a>7 | [DirectStorage_InitDevice](../functions/DirectStorage_InitDevice.md) | V | Reached from the init chain (sub_14002BA44) with the application's copy: reads the destination switches and starts DirectStorage_ConfigureManager. |
| <a id="8"></a>8 | [GameWindow_FillCreateParams](../functions/GameWindow_FillCreateParams.md) | V | Reads /ignore_config, /windowpos, /windowtopmost and /return when the window record is built. |
| <a id="9"></a>9 | [Startup_ParseDisplaySwitches](../functions/Startup_ParseDisplaySwitches.md) | V | Called from sub_1400B532C: reads the 10 display switches into a block nothing reads. |
| <a id="10"></a>10 | [Boot_EnterState4](../functions/Boot_EnterState4.md) | V | With /return, stores 256 in a boot field that boot state 4 then overwrites with 255 (no lasting effect). |
| <a id="11"></a>11 | [Classic_BuildLaunchArguments](../functions/Classic_BuildLaunchArguments.md) | V | When the player chooses the Classic executable, the display settings are written back as the display set's syntax for the relaunch (App_LaunchClassic). |

## Open questions

? the order of step 9 relative to step 8 (both run during start-up; not traced).
