# UIAddonFFTOConfig_OnClose

- **Address:** `0x140188FA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOConfig_OnClose(UIAddonFFTOConfig *addon)`
- **Callers:** UIAgent_DetachAddon (vtable slot 5)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

On-close handler of the General Options screen (vtable slot 5): asks for a settings save and, after a display change, restarts the boot sequence.

## Behavior

- V: sets `g_ConfigData` +224 = 1 unconditionally (the byte store at 0x140189057); ConfigData_SaveIfRequested then writes the settings and the system save when +225 is set.
- V: with +57 set it restarts the boot sequence after a display change.
- V (seen live 2026-11-13): closing the screen rewrote the system save file within the same second.

## State touched

- Writes: [g_ConfigData](../globals/g_ConfigData.md)

## Referenced by

- Called by: [UIAgent_DetachAddon](UIAgent_DetachAddon.md)
- Observed behaviours: [SettingsCloseSavesSystemFile](../behaviors/SettingsCloseSavesSystemFile.md)

## Notes

Behavior: SettingsCloseSavesSystemFile.

## Open questions

None recorded.
