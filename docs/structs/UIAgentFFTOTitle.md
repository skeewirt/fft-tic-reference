# UIAgentFFTOTitle

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 1448 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The title screens' agent (1448 bytes, `Mem_Alloc(0x5A8)` in `UIAgentManager_CreateAgents` at 0x1401CFA4D; vtable 0x14070A5B0, constructor 0x1401C2AE4). Owns the menu, play mode and saving add-ons and the state machine that moves between them.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="menu_addon"></a>`0x40` | menu_addon | `UIAddonFFTOTitle *` | V | The menu add-on (uiaddon row 244). |
| <a id="playmode_addon"></a>`0x48` | playmode_addon | `UIAddon *` | V | The play mode add-on (row 245). |
| <a id="saving_addon"></a>`0x50` | saving_addon | `UIAddon *` | V | A third add-on (row 256, `ffto_saving.uib`). |
| <a id="state"></a>`0x58` | state | `uint8` | V | Agent state byte (the state machine of UIAgentFFTOTitle_Update). |
| <a id="next_state"></a>`0x59` | next_state | `uint8` | V | The state that follows a fade. |
| <a id="cursor_kind"></a>`0x5A` | cursor_kind | `uint8` | V | The kind of row to put the cursor back on when the menu is rebuilt. |
| <a id="menu_flags"></a>`0x5B` | menu_flags | `uint8[3]` | V | Menu flags at +91, +92 and +93. |
| <a id="resume_records"></a>`0xA4` | resume_records | `uint8[5][264]` | I | Five 264-byte records; the resume descriptors that Continue compares (read in 0x1401C2D60). |
| <a id="chosen_slot"></a>`0x58C` | chosen_slot | `int32` | V | The chosen save slot (+1420). |
| <a id="chosen_is_resume"></a>`0x590` | chosen_is_resume | `uint8` | V | 'The chosen save is a resume descriptor' (+1424). |

## Behavior

- V: UITitle_ShowMenu creates the three add-ons (0x1401CB9B4, 0x1401CBA60, 0x1401CA6C4).

## Notes

Functions: UIAgentFFTOTitle_Update, UIAgentFFTOTitle_OnAddonEvent, UITitle_ShowMenu.

## Open questions

None recorded.
