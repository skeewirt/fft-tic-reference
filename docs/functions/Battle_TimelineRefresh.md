# Battle_TimelineRefresh

- **Address:** `0x140215E54`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void __fastcall Battle_TimelineRefresh(void)`
- **Callers:** `Battle_TimelineFocusCamera` (`0x140209738`), `sub_140210AF0` (0x140213B21); one data reference at 0x143D37B10
- **Callees:** `sub_1402607C0`, `Battle_TimelineBuildList`, `sub_14010BD20`, `TurnPanel_SetTag` (`0x140215540`), `sub_1400E5814`, `sub_14010BA54`, `sub_1400E5A44`, `sub_1400E5A8C`, `sub_14022AA88`, `sub_1400E4C48`, `sub_140214134`, `sub_1400E4CD0`, `sub_1400E4D5C`, `sub_1400E4DE8`, `sub_1400E4E74`, `sub_1400E56A0`, `sub_1400E5708`, `Battle_UnitStatusFill`, `sub_1400E4FD0`, `sub_1400E5058`, `sub_1400E5448`, `sub_1400E4EE8`, `sub_1400E4F5C`, `CharaName_GetDisplayName`, `sub_1400E54BC`, `sub_1400E5544`, `sub_1400E55B8`, `sub_1400E562C`, `BattleUnit_BuildJobRecord`, `BattleMain_SetPanelJobRecord`, `sub_1400E577C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Refreshes the Combat Timeline panel: builds the forecast, copies it into `g_TurnList`, and fills the visible rows
(portrait, name, HP/MP, CT) and the scroll position.

## Behavior

- V: when the panel is not in timeline mode (`dword_140D4058C != -1`) it calls `Battle_UnitStatusFill` for slots 0..20 and
  returns. Before that, an early-out (`dword_140D4058C` set to 0, return) applies when the unit record found by `sub_1402607C0` has its
  byte +0x1EC above 10, `dword_140D40594` is 19, `g_BattleState` is 39 and the turn result is 768 or 1280.
- V: calls `Battle_TimelineBuildList` (`0x1402333E8`) with a local 40-entry array; the returned count and the flags
  decide the scroll: with the layout word at `g_CharaRenderMgr+13420` equal to 1 or 2 the scroll is the count minus 3
  (a four-row window); with 0 it is the count minus 8; either is clamped to 31.
- V: copies the 40 entries (160 bytes) into `g_TurnList` `0x140D40490` (`0x140215Fxx`, the `qmemcpy` of `v127`).
- V: it calls `TurnPanel_SetTag(tag, listIndex, unit, entryByte0, entryByte1)` for tags 1..9 (nine body rows) and, depending
  on the scroll case, tag 0 and tag 10 for the edge rows
  (`sub_140215540`) which paints portrait/name/HP/MP/ability name.
- V: the panel header widgets get `sub_14022AA88` (unit portrait/name), HP/max HP (`+0x30`/`+0x32`), MP/max MP
  (`+0x34`/`+0x36`), and the CT field; the CT shown is 100 when the unit's `+0x1B8` active flag is non-zero,
  otherwise the unit byte `+0x41` (the status fill's `wt` field; `sub_140226CA0` fills it from unit `+0x41`, or
  100 when `+0x1B8` is set) (`sub_1400E4E74`, I for the exact widget).
- V: reads `g_BattleState` (`0x140C6B1CC`) twice: value 39 is part of the entry early-out, and value 91 (the focus camera) skips the per-unit header refresh. The normal timeline screens 90 and 97 reach this refresh through the main loop.

## State touched

- Calls: [Battle_TimelineBuildList](Battle_TimelineBuildList.md), [TurnPanel_SetTag](TurnPanel_SetTag.md), [sub_14022AA88](sub_14022AA88.md), [sub_140214134](sub_140214134.md), [Battle_UnitStatusFill](Battle_UnitStatusFill.md), [CharaName_GetDisplayName](CharaName_GetDisplayName.md), [BattleUnit_BuildJobRecord](BattleUnit_BuildJobRecord.md), [BattleMain_SetPanelJobRecord](BattleMain_SetPanelJobRecord.md)

## Referenced by

- Appears in flows: [BattleTimelineCameraFlow](../flows/BattleTimelineCameraFlow.md)
- Called by: [Battle_TimelineFocusCamera](Battle_TimelineFocusCamera.md)

## Notes

The timeline is rebuilt from live state on every refresh, not cached. The list it copies is the same format `TurnList_InsertEntry` and `TurnPanel_SetTag` use.

## Open questions

Resolved 2026-11-22: 90, 91 and 97 are `g_BattleState` dispatch ids, not timeline layouts or zoom levels. 91 is the focus-camera screen run by `Battle_TimelineFocusCamera`; 90 and 97 are the two timeline-screen variants `sub_140209218` selects from the battle control bytes at +70 and +74. What those two flags mean is still open.
