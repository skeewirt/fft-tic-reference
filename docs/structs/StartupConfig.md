# StartupConfig

- **Kind:** structure
- **Area:** [Application and startup](../areas/app-startup.md)
- **Size:** 280 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 280-byte block that Game_Main fills from the process arguments and the startup parser, then Application_Initialize copies into the application object at +1200. Only the fields a switch or a reader was seen to use are listed.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="arg_count"></a>`0x0` | arg_count | `int32` | V | Argument count (set by sub_14002C1FC). |
| <a id="arg_vector"></a>`0x8` | arg_vector | `char **` | V | Argument vector (set by sub_14002C1FC). |
| <a id="window_width"></a>`0x14` | window_width | `int32` | I | 0x8000 means 'not given'; GameWindow_FillCreateParams takes the pair at +0x14 / +0x18 as the window size otherwise. No switch writes it. |
| <a id="window_height"></a>`0x18` | window_height | `int32` | I | The second dword of the size pair. |
| <a id="window_y"></a>`0x1C` | window_y | `int32` | V | /windowpos Y; 0x8000 when not given. |
| <a id="window_x"></a>`0x20` | window_x | `int32` | V | /windowpos X; 0x8000 when not given. |
| <a id="cpu_decompression_threads"></a>`0x24` | cpu_decompression_threads | `int32` | V | /buildin_cpu_decompression_threads N. |
| <a id="ignore_config"></a>`0x37` | ignore_config | `uint8` | V | /ignore_config. |
| <a id="memory_limit_bytes"></a>`0xA0` | memory_limit_bytes | `uint64` | V | /memory_limit in bytes; 0 when absent. |
| <a id="exceptionoff"></a>`0xBF` | exceptionoff | `uint8` | I | /exceptionoff; no reader. |
| <a id="console"></a>`0xC0` | console | `uint8` | I | /console; no reader. |
| <a id="cmd"></a>`0xC1` | cmd | `uint8` | I | /cmd; no reader. |
| <a id="allocator_option"></a>`0xC7` | allocator_option | `uint8` | ? | Passed to the system allocator's init by Memory_InitAllocators and read from the application copy (g_Application+1399) by sub_14002B364; no switch sets it. |
| <a id="windowtopmost"></a>`0xCD` | windowtopmost | `uint8` | V | /windowtopmost. |
| <a id="enable_memory_save"></a>`0xD7` | enable_memory_save | `uint8` | V | /enable_memory_save. |
| <a id="disable_tty"></a>`0xDE` | disable_tty | `uint8` | I | /disable_tty; no reader. |
| <a id="disable_gpu_decompression"></a>`0xE2` | disable_gpu_decompression | `uint8` | V | /disable_gpu_decompression. |
| <a id="disable_gpu_decompression_metacommand"></a>`0xE3` | disable_gpu_decompression_metacommand | `uint8` | V | /disable_gpu_decompression_metacommand. |
| <a id="enable_builtin_cpu_decompression"></a>`0xE4` | enable_builtin_cpu_decompression | `uint8` | V | /enable_builtin_cpu_decompression. |
| <a id="disable_direct_device"></a>`0xE5` | disable_direct_device | `uint8` | V | /disable_direct_device (also sets the next byte). |
| <a id="disable_direct_destination"></a>`0xE6` | disable_direct_destination | `uint8` | V | /disable_direct_destination. |
| <a id="disable_file_buffering"></a>`0xE7` | disable_file_buffering | `uint8` | V | /disable_file_buffering. |
| <a id="disable_file_cache"></a>`0xE8` | disable_file_cache | `uint8` | V | /disable_file_cache. |
| <a id="boot_option"></a>`0xEB` | boot_option | `uint8` | ? | Read as g_Application+1435 by Boot_Update when it opens the startup screen; no switch sets it. |
| <a id="razor_gpu_friendly"></a>`0xEC` | razor_gpu_friendly | `uint8` | I | /razor_gpu_friendly; no reader. |
| <a id="razor_cpu_friendly"></a>`0xED` | razor_cpu_friendly | `uint8` | I | /razor_cpu_friendly; no reader. |
| <a id="disable_directstorage"></a>`0xFE` | disable_directstorage | `uint8` | I | /disable_directstorage; no reader. |
| <a id="startup_flag_262"></a>`0x106` | startup_flag_262 | `uint8` | ? | Read by Application_InitPlatformServices (decides a failure); no switch sets it. |
| <a id="startup_flag_263"></a>`0x107` | startup_flag_263 | `uint8` | ? | Passed to sub_14002F060 by Application_InitPlatformServices; no switch sets it. |
| <a id="disable_nxd_allocator"></a>`0x10A` | disable_nxd_allocator | `uint8` | I | /disable_nxd_allocator; no reader. |
| <a id="return_switch"></a>`0x10E` | return_switch | `uint8` | V | /return. |
| <a id="ouncenx_upgrade"></a>`0x10F` | ouncenx_upgrade | `uint8` | I | /ouncenx_upgrade; no reader. |

## Behavior

- V: Game_Main clears 0x118 bytes, sub_14002C1FC sets the defaults, Startup_ParseLaunchSwitches applies the switches, and Application_Initialize copies the block (0x118 bytes) to g_Application+1200.
- V: the defaults that are not zero are 0x8000 at +0x14, +0x18, +0x1C and +0x20 and a few small constants in fields no switch touches.

## Notes

Offsets are hexadecimal in this table; the switch descriptions give the same numbers in decimal.

## Open questions

? the remaining fields' roles (the defaults routine writes a few more non-zero constants).
