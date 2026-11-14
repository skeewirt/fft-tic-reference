# Display

Video/window state and resize handling.

Functions: 3.

## Functions (3)

| Name | Address | Purpose |
|---|---|---|
| [Video_OnResize](../functions/Video_OnResize.md) | `0x1401E7BA4` | Stores the new backbuffer size for the main window and refreshes the unit-image width factor. |
| [Video_RefreshState](../functions/Video_RefreshState.md) | `0x140255DEC` | Re-applies the video state (mode flags, viewport, aspect factor) after a mode change. |
| [VideoState_InitDefaults](../functions/VideoState_InitDefaults.md) | `0x1402739E0` | Initialises the video/render state globals to their defaults. |
