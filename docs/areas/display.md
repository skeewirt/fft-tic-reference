# Display

Video/window state and resize handling.

Functions: 3, Structures: 5, Tables: 5.

## Functions (3)

| Name | Address | Purpose |
|---|---|---|
| [Video_OnResize](../functions/Video_OnResize.md) | `0x1401E7BA4` | Stores the new backbuffer size for the main window and refreshes the unit-image width factor. |
| [Video_RefreshState](../functions/Video_RefreshState.md) | `0x140255DEC` | Re-applies the video state (mode flags, viewport, aspect factor) after a mode change. |
| [VideoState_InitDefaults](../functions/VideoState_InitDefaults.md) | `0x1402739E0` | Initialises the video/render state globals to their defaults. |

## Structures (5)

| Name | Size (bytes) | Summary |
|---|---|---|
| [NxdDataBrightnessRow](../structs/NxdDataBrightnessRow.md) | 12 | One row of the nxd.brightness table (data table). |
| [NxdDataLoadingSettingsRow](../structs/NxdDataLoadingSettingsRow.md) | 4 | One row of the nxd.loading_settings table (data table). |
| [NxdDataResolutionRow](../structs/NxdDataResolutionRow.md) | 16 | One row of the nxd.resolution table (data table). |
| [NxdDataScreenModeRow](../structs/NxdDataScreenModeRow.md) | 8 | One row of the nxd.screen_mode table (data table). |
| [NxdDataTransitionRow](../structs/NxdDataTransitionRow.md) | 20 | One row of the nxd.transition table (data table). |

## Tables (5)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [NxdDataBrightness](../tables/NxdDataBrightness.md) | NXD file | 137 | 11 rows of 12 bytes | Eleven screen brightness steps and their multiplier. |
| [NxdDataLoadingSettings](../tables/NxdDataLoadingSettings.md) | NXD file | 129 | 11 rows of 4 bytes | Eleven loading screen settings. |
| [NxdDataResolution](../tables/NxdDataResolution.md) | NXD file | 257 | 9 rows of 16 bytes | The nine selectable resolutions (width and height). |
| [NxdDataScreenMode](../tables/NxdDataScreenMode.md) | NXD file | 266 | 3 rows of 8 bytes | Three screen modes. |
| [NxdDataTransition](../tables/NxdDataTransition.md) | NXD file | 100 | 26 rows of 20 bytes | Screen transition parameters (26). |
