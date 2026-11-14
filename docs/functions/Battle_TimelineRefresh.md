# Battle_TimelineRefresh

- **Address:** `0x140215E54`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char __fastcall Battle_TimelineRefresh(int a1, int a2, int a3)`
- **Callers:** `Battle_TimelineFocusCamera` (`0x140209738`), `sub_140210AF0`
- **Callees:** `sub_1402607C0`, `Battle_TimelineBuildList`, `sub_14010BD20`, `TurnPanel_SetTag` (`0x140215540`), `sub_1400E5814`, `sub_14010BA54`, `sub_1400E5A44`, `sub_1400E5A8C`, `sub_14022AA88`, `sub_1400E4C48`, `sub_140214134`, `sub_1400E4CD0`, `sub_1400E4D5C`, `sub_1400E4DE8`, `sub_1400E4E74`, `sub_1400E56A0`, `sub_1400E5708`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Refreshes the Combat Timeline panel: builds the forecast, copies it into `g_TurnList`, and fills the visible rows
(portrait, name, HP/MP, CT) and the scroll position.

## Behavior

- V: bails out to the per-unit tag refresh when the panel is not in timeline mode (`dword_140D4058C != -1`).
- V: calls `Battle_TimelineBuildList` (`0x1402333E8`) with a local 40-entry array; the returned count and the flags
  decide the scroll (`v12` = first visible row, max 31/39).
- V: copies the 40 entries (160 bytes) into `g_TurnList` `0x140D40490` (`0x140215Fxx`, the `qmemcpy` of `v127`).
- V: for the 10 visible rows calls `TurnPanel_SetTag(tag, listIndex, unit, entryByte0, entryByte1)`
  (`sub_140215540`) which paints portrait/name/HP/MP/ability name.
- V: the panel header widgets get `sub_14022AA88` (unit portrait/name), HP/max HP (`+0x30`/`+0x32`), MP/max MP
  (`+0x34`/`+0x36`), and the CT field; the CT shown is 100 when the unit's `+0x1B8` active flag is non-zero,
  otherwise `unit[0x65]` (`sub_1400E4E74`, I for the exact widget).
- V: uses the global UI mode `dword_140C6B1CC` (39/90/91/97) to decide whether the timeline is the active screen.

## State touched

- Calls: [Battle_TimelineBuildList](Battle_TimelineBuildList.md), [TurnPanel_SetTag](TurnPanel_SetTag.md), [sub_14022AA88](sub_14022AA88.md), [sub_140214134](sub_140214134.md)

## Notes

The timeline is rebuilt from live state on every refresh, not cached. The list it copies is the same format `TurnList_InsertEntry` and `TurnPanel_SetTag` use.

## Open questions

The exact meaning of the `dword_140C6B1CC` values 90/91/97 (different timeline layouts or zoom levels).
