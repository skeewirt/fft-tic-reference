# BattleMain_SetPanelJobRecord

- **Address:** `0x14010141C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 BattleMain_SetPanelJobRecord(__int64 screen, int which, __int64 rec)`
- **Callers:** Battle_UnitStatusFill, Battle_UnitStatusFillAlt, Battle_TimelineRefresh, sub_1402DF374
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores a job record (the first 92 bytes) into one of the battle main screen's two unit panel blocks.

## Behavior

- V: the screen object is read at +64 of the argument; nothing happens when it is null.
- V: `which` 0, 2 or 3 selects the second block (+212); any other value the first; the record is copied to screen +65464 (+212) as 5 x 16 bytes, 8 bytes and a dword.
- V: the panel fill later passes each 212-byte block to sub_140291490 (UIAddonFFTOBattleMain4 vfunc 14).
- V (traced live 2026-11-17): called from Battle_UnitStatusFillAlt with the record BattleUnit_BuildJobRecord had just built for the unit under the cursor.

## Referenced by

- Observed behaviours: [BattlePanelJobLineShowsDashesAtLevelZero](../behaviors/BattlePanelJobLineShowsDashesAtLevelZero.md)

## Notes

Name is ours.

## Open questions

None recorded.
