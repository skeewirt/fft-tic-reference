# BattleEffectsAreOneFilePerNumber

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [BattleAct_SetupEffect](../functions/BattleAct_SetupEffect.md), [Effect_SelectForAbility](../functions/Effect_SelectForAbility.md), [EffectFile_GetTrackRow](../functions/EffectFile_GetTrackRow.md), [GameData_ReadSectors](../functions/GameData_ReadSectors.md), [EffectNxd_LoadRow](../functions/EffectNxd_LoadRow.md), [EffectNxd_HasFlag24](../functions/EffectNxd_HasFlag24.md), [EffectNxd_HasFlag25](../functions/EffectNxd_HasFlag25.md), [EffectNxd_HasFlag28](../functions/EffectNxd_HasFlag28.md), [Effect_TintByNxdScale](../functions/Effect_TintByNxdScale.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle effect is one self-contained file per effect number (0..511): EffectFile_GetTrackRow gives its pack file and size, the loader reads it into one shared buffer and the effect runs from offsets inside the file.

## Behavior

- V (code): Effect_SelectForAbility masks the number to 0x1FF; the file table, the 512-entry base pointer array and the NXD readers are the only per-number data outside the file; no stock effect word yields 511 (its file row is empty) and the five hard-coded number tests (33..36, 65, 71, 73, 230, 242, 451, 464, 485) never see it.
- V (code): BattleAct_SetupEffect is called only from BattleAct_Step, which first calls BattleAct_BuildResult with the slot byte +0x1BC of the scene object's unit (+0x148); that function reads the action's ability word at g_BattleUnitTable + slot * 0x200 + 0x1A2; rdi still holds the scene object at the call to Effect_SelectForAbility (0x140206317).
- V (code): EffectNxd_LoadRow writes its effect argument to the renderer slot +88 and nothing reads that field back (two writers, no reader by its displacement 0x24418 from g_CharaRenderer); the flag readers and Effect_TintByNxdScale take the key from their argument or word_141D330BC.

## Open questions

? the blocks between an effect file's header and its texture section are not decoded.
