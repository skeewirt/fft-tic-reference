# Battle_TimelineBuildList

- **Address:** `0x1402333E8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool __fastcall Battle_TimelineBuildList(int *count, uint8_t *list)`
- **Callers:** `Battle_TimelineRefresh` (`0x140215F68`)
- **Callees:** `TurnList_Build` (`0x14030FFC4`), `BTurn_PreviewAction` (`0x14030FE60`)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 40-entry timeline list for the UI and overlays the acting unit's current command preview.

## Behavior

- V: when the renderer mode `*(int*)(g_CharaRenderMgr + 13420)` is 1 or 2, it updates the scroll words
  (`xmmword_142FD35A0`) from the timeline list at `qword_14184A9B0` and the current unit's index.
- V: calls `TurnList_Build(list, 0, 1)` (`0x14030FFC4` with `a2=0`, `a3=1`) and returns its result in `*count`.
- V: otherwise (renderer mode 0) it builds the forecast and then calls `BTurn_PreviewAction(unit, ..., list, 1)`
  (`sub_14030FE60`) to overwrite the current unit's entry with the action it is about to take (used while the
  command menu is up).
- V: returns whether the scroll word changed.

## State touched

- Calls: [TurnList_Build](TurnList_Build.md), [BTurn_PreviewAction](BTurn_PreviewAction.md)

## Referenced by

- Appears in flows: [BattleTimelineCameraFlow](../flows/BattleTimelineCameraFlow.md)
- Called by: [Battle_TimelineRefresh](Battle_TimelineRefresh.md)

## Notes

`a3 = 1` in `TurnList_Build` means "do not insert the active unit at time 0"; the preview overlay puts it back
with its chosen action.

## Open questions

The renderer-mode 1/2 path was only read at the field level.
