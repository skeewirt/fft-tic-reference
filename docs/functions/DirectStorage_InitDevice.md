# DirectStorage_InitDevice

- **Address:** `0x14006B578`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 DirectStorage_InitDevice(void *files, const uint8_t *startup)`
- **Callers:** sub_14002BA44 (0x14002BA7E)
- **Callees:** D3D12CreateDevice, sub_14006F7B0, sub_14006A67C, sub_140026BD4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gets the graphics device for the file system manager, starts DirectStorage when it is enabled and supported, and decides the 'direct destination' flag from the switches.

## Behavior

- V: copies the device pointer from the render device object (+3504 of g_RenderDevice) into files+2312 and calls the device's virtual slot 1 on it (I: add a reference); when none exists it creates one with D3D12CreateDevice at feature level 12_1.
- V: when the manager byte files+2306 is 1 and the device's capability query (virtual slot at +104, kind 7, value 96) fails or reports at least 96, it runs sub_14006F7B0 with the startup block; on failure it clears files+2306 (returning the error only if it was not 1).
- V: the byte 0x142C81C7A is set to 1 when the byte g_RenderDevice+3464 is not 2, or files+2306 is not 1, or the startup byte +230 (/disable_direct_destination) or +229 (/disable_direct_device) is set.
- I: that byte means 'no direct upload to the GPU'; its many readers are file-reading and texture-descriptor routines, which is why it is tied to the destination switches (rests on the switch names and the reader names).
- V: finally, when files+2304 is non-zero it runs sub_14006A67C; if that fails the function reports an error and returns it.

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)

## Notes

files is the manager qword_143CD9B90; startup is the application's copy at g_Application+1200.

## Open questions

? what sets files+2304 and files+2306.
