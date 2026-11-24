# LaunchSwitches

- **Kind:** registry
- **Area:** [Application and startup](../areas/app-startup.md)
- **Resolved by:** [Startup_ParseLaunchSwitches](../functions/Startup_ParseLaunchSwitches.md), [Startup_MatchLaunchSwitch](../functions/Startup_MatchLaunchSwitch.md), [Startup_ParseDisplaySwitches](../functions/Startup_ParseDisplaySwitches.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The command-line switches the executable recognises: 23 startup switches read by Startup_ParseLaunchSwitches and 10 display-settings switches read by Startup_ParseDisplaySwitches. The id is the order in which the switch is looked for; the value is the syntax; the text says what the switch sets and which function reads it. A switch is matched exactly and case-sensitively, the first match wins, and a value switch is used only when its values are within the argument count. Switches marked inert set a byte that nothing reads in this executable.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="/exceptionoff"></a>1 | `/exceptionoff` | `flag; startup +191` | I | Inert: the byte is set and no reader was found (none in the functions that use the startup block or the application object). |
| <a id="/windowtopmost"></a>2 | `/windowtopmost` | `flag; +205 -> g_Application+1405` | V | Read by GameWindow_FillCreateParams: ORs the flag 8 into the window record's second style dword. |
| <a id="/memory_limit"></a>3 | `/memory_limit` | `/memory_limit GiB; +160` | V | Value x 1024 shifted left by 20 = bytes, kept by Memory_InitAllocators as the memory limit; Memory_GetAvailableBytes then reports the limit minus the bytes held (I: qword_142F0D960) when the limit does not exceed the machine's memory (I: qword_142E80448). |
| <a id="/razor_gpu_friendly"></a>4 | `/razor_gpu_friendly` | `flag; +236` | I | Inert: no reader. |
| <a id="/razor_cpu_friendly"></a>5 | `/razor_cpu_friendly` | `flag; +237` | I | Inert: no reader. |
| <a id="/disable_directstorage"></a>6 | `/disable_directstorage` | `flag; +254` | I | Inert: no reader (the DirectStorage setup does not test this byte). |
| <a id="/disable_gpu_decompression"></a>7 | `/disable_gpu_decompression` | `flag; +226` | V | Read by DirectStorage_ConfigureManager: sets the configuration block's dword +24 (also set on a graphics vendor id of 0x8086). |
| <a id="/disable_gpu_decompression_metacommand"></a>8 | `/disable_gpu_decompression_metacommand` | `flag; +227` | V | Read by DirectStorage_ConfigureManager: sets the configuration block's dword +20. |
| <a id="/enable_builtin_cpu_decompression"></a>9 | `/enable_builtin_cpu_decompression` | `flag; +228` | V | Read by DirectStorage_ConfigureManager: without it the built-in CPU decompression thread count becomes -1 when no thread count was given. |
| <a id="/buildin_cpu_decompression_threads"></a>10 | `/buildin_cpu_decompression_threads` | `/buildin_cpu_decompression_threads N; +36` | V | Decimal integer; read by DirectStorage_ConfigureManager into the configuration block's dword +4 when non-zero. |
| <a id="/disable_direct_device"></a>11 | `/disable_direct_device` | `flag; +229 and +230` | V | Sets both bytes. DirectStorage_ConfigureManager clears the manager's second flag byte; DirectStorage_InitDevice sets the direct-destination byte 0x142C81C7A. |
| <a id="/disable_direct_destination"></a>12 | `/disable_direct_destination` | `flag; +230` | V | Read by DirectStorage_InitDevice: sets the byte 0x142C81C7A to 1. |
| <a id="/disable_file_buffering"></a>13 | `/disable_file_buffering` | `flag; +231` | V | Read by DirectStorage_ConfigureManager: skips the step that sets the manager flag and two configuration dwords. |
| <a id="/disable_file_cache"></a>14 | `/disable_file_cache` | `flag; +232` | V | Read by Application_InitPlatformServices: sets the application's file-cache byte (+428). |
| <a id="/disable_tty"></a>15 | `/disable_tty` | `flag; +222` | I | Inert: no reader. |
| <a id="/enable_memory_save"></a>16 | `/enable_memory_save` | `flag; +215` | V | Read by Application_InitPlatformServices: forces low-memory mode (the byte at qword_140C69718+617 and the file-cache byte +428 set to 1), as a machine with little memory and few cores gets it automatically. |
| <a id="/cmd"></a>17 | `/cmd` | `flag; +193` | I | Inert: no reader. |
| <a id="/console"></a>18 | `/console` | `flag; +192` | I | Inert: no reader (no console window is created by this executable). |
| <a id="/disable_nxd_allocator"></a>19 | `/disable_nxd_allocator` | `flag; +266` | I | Inert: no reader. |
| <a id="/ignore_config"></a>20 | `/ignore_config` | `flag; +55 -> g_Application+1255` | V | Read by GameWindow_FillCreateParams: skips loading the saved settings file for the window record. |
| <a id="/windowpos"></a>21 | `/windowpos` | `/windowpos X Y; +32 = X, +28 = Y` | V | Decimal integers (I: the conversion routine is taken to be the C runtime's; needs two values). Read by GameWindow_FillCreateParams as the window position; a value at or below -32000 sets a style flag instead. |
| <a id="/return"></a>22 | `/return` | `flag; +270 -> g_Application+1470` | V | Application_Initialize skips Splash_CreateWindow; GameWindow_FillCreateParams leaves the 0x10000000 style toggle alone; no other lasting effect was demonstrated (Boot_EnterState4's store is overwritten at once by boot state 4). |
| <a id="/ouncenx_upgrade"></a>23 | `/ouncenx_upgrade` | `flag; +271` | I | Inert: no reader. |
| <a id="/resolution"></a>24 | `/resolution` | `/resolution W H` | I | Display set (Startup_ParseDisplaySwitches): both above 0 are stored in a global block that nothing else reads, so no effect in this executable. |
| <a id="/screenmode"></a>25 | `/screenmode` | `/screenmode 0..2` | I | Display set: stored in the same unread block. |
| <a id="/output"></a>26 | `/output` | `/output ID A B` | I | Display set: output id and two values; unread block. |
| <a id="/deactiveplay"></a>27 | `/deactiveplay` | `/deactiveplay 0\|1` | I | Display set: unread block. |
| <a id="/cursorclip"></a>28 | `/cursorclip` | `/cursorclip 0\|1` | I | Display set: unread block. |
| <a id="/enablevsync"></a>29 | `/enablevsync` | `/enablevsync 0\|1` | I | Display set: unread block. |
| <a id="/brightness"></a>30 | `/brightness` | `/brightness 0..10` | I | Display set: unread block (default 5). |
| <a id="/language"></a>31 | `/language` | `/language ja\|en\|fr\|de\|cs\|ct\|ko` | I | Display set: index of the code (0..6) into the unread block (default 0). |
| <a id="/sound"></a>32 | `/sound` | `/sound M S V X Y (each 0..100)` | I | Display set: five volume bytes in the unread block (defaults 70, 100, 100, 100, 100). |
| <a id="/camera"></a>33 | `/camera` | `/camera H V` | I | Display set: two flag bytes in the unread block. |

## Behavior

- V: the first 23 rows are read from the startup parser, called from Game_Main before the application object exists; the last 10 are read by a second parser called later from sub_1400B532C against the application's copy of the arguments.
- V: the startup block is copied to g_Application+1200 by Application_Initialize, so a reader of a startup switch uses either the application offset (+1200 + the startup offset) or the startup block passed in.
- V: Classic_BuildLaunchArguments writes exactly the 10 display switches and /windowpos in the same syntax for the relaunch into the game's Classic executable; the enhanced executable never writes /return.
- I: the 'inert' rows rest on a search of the code that touches the startup block and the application object (every reader of a byte at those offsets was inspected); a reader that builds its address some other way would not have shown.
- V: Game_Main returns at once, before any switch is read, when a debugger is attached.
- V: the executable imports no AllocConsole or AttachConsole, and no launch switch reads a console or developer-menu setting.
- ?: RegOpenKeyExW is imported and used by sub_140007C00, sub_1400085F0 and sub_140008800, which were not examined.

## Notes

The startup block's field +235 (g_Application+1435) is read by Boot_Update and Application-level code but no switch writes it. The DirectStorage switches reach their readers through DirectStorage_InitDevice (called from sub_14002BA44).

## Open questions

? what the inert switches were for; ? whether any is read through a computed address.
