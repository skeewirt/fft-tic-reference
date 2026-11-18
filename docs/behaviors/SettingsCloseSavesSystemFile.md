# SettingsCloseSavesSystemFile

- **Kind:** observed behaviour
- **Scope:** what closing the settings screen writes
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [UIAddonFFTOConfig_OnClose](../functions/UIAddonFFTOConfig_OnClose.md), [sub_1400B5E24](../functions/sub_1400B5E24.md), [g_ConfigData](../globals/g_ConfigData.md), [g_SaveManager](../globals/g_SaveManager.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Closing the settings screen requests a settings save, and the save rewrites the SYSTEM save file with the settings and the save manager's bytes +656..+895, among them the game-cleared byte.

## Behavior

- V: `g_ConfigData` (0x140C69690, a pointer) +224 = a settings save requested, +225 = settings changed; 0x1400B5E24 (its per-frame step) does, when +224: if +225 and no save request is busy, `Options_ApplyBlock(g_SaveManager, block)` (0x1400C3814) with the settings and `g_SaveManager` +656..+895 (the game-cleared byte +888 among them), then +224 = +225 = 0; without +225 only +224 is cleared. `Options_ApplyBlock` names the 'SYSTEM' save (string xref 0x1400C3962). I: this writes the system save file.
- V: the General Options on-close handler sets +224 = 1 unconditionally (0x140189057).
- V (seen live 2026-11-13): closing the screen rewrote the system save file within the same second, with the cleared byte as it was in memory (so +225 was set then; what set it was not read).

## Open questions

None recorded.
