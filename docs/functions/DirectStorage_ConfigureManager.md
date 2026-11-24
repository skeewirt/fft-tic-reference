# DirectStorage_ConfigureManager

- **Address:** `0x14006FA94`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 DirectStorage_ConfigureManager(void *mgr, const uint8_t *startup)`
- **Callers:** sub_14006F7B0 (0x14006F8A5)
- **Callees:** DStorageSetConfiguration1, DStorageGetFactory, sub_140071D94, sub_140070810, sub_14006FD7C, sub_140076B10, sub_140070BD4, sub_140026BD4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the DirectStorage switches to the DirectStorage library's configuration block, creates the factory and sets up the manager's queue and request records.

## Behavior

- V: sets the manager flag bytes at +1190668 = 0 and +1190669 = 1, then clears +1190669 when the startup byte +229 (/disable_direct_device) is set.
- V: unless the startup byte +231 (/disable_file_buffering) is set: when the dword qword_143CD9B90+2320 is not 2 or the next dword +2324 is not 17, it sets mgr+1190668 to 1 and sets two dwords of the configuration block (offsets +12 and +28) to 1.
- V: sets the block dword at +24 to 1 when the render device's dword +4196 is 32902 (0x8086) or the startup byte +226 (/disable_gpu_decompression) is set.
- I: 0x8086 is a graphics vendor id (rests on the number; the field was not named).
- V: block dword +20 is 1 when the startup byte +227 (/disable_gpu_decompression_metacommand) is non-zero.
- V: block dword +4 takes the startup dword +36 (/buildin_cpu_decompression_threads) when it is non-zero; when the startup byte +228 (/enable_builtin_cpu_decompression) is NOT set and the value is 0, it becomes -1.
- V: the block is handed to DStorageSetConfiguration1, the factory is obtained with DStorageGetFactory and stored at mgr+1165808; the dword mgr+1190648 is set to 0x8000000.
- V: creates a status array of 4096 entries named m_storageStatusArray through the factory, queue records through sub_140070810 for the kinds 47, 2 and 14, then initialises 63 queue slots (32 bytes each) and 4096 request records.
- I: the DirectStorage library's meaning of the block's fields is the API's own (rests on the imported call), the code only fills the dwords.

## Notes

The default (no switch) disables the built-in CPU decompression threads (-1).

## Open questions

? the manager's queue and request record layouts (not read here).
