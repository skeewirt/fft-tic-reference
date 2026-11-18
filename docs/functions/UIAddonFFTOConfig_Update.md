# UIAddonFFTOConfig_Update

- **Address:** `0x140189D54`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOConfig_Update(UIAddonFFTOConfig *addon, float dt)`
- **Callers:** UIAddon_OnEventBase (event 4)
- **Callees:** ConfigMenu_ReadSettings

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame update of the General Options screen (vtable slot 14): queued dialogs, the display change states, the render device check and the sync of shown values with the game settings.

## Behavior

- V: holds the screen's own work only: queued dialogs (0x140193D10), sub-states 4..6 (a display change being applied), the render device check and the sync of the shown values with the game settings (ConfigMenu_ReadSettings every frame, compared with the shown copy at +648).

## State touched

- Calls: [ConfigMenu_ReadSettings](ConfigMenu_ReadSettings.md)

## Notes

Case 7 validates a chosen Text Language code (sub_14002BCE0); see behavior TextLanguage.

## Open questions

None recorded.
