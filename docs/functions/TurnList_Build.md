# TurnList_Build

- **Address:** `0x14030FFC4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int __fastcall TurnList_Build(uint8_t *list, int mode, int fillCurrent)`
- **Callers:** `Battle_TimelineBuildList` (`0x1402333E8`), `sub_14030DD8C`, `sub_14030E368`, `BTurn_ForecastIndex`, `BTurn_ForecastUnitAt`, `BTurn_PreviewAction`, `sub_14032437C`, `sub_140364A50`
- **Callees:** `TurnList_InsertEntry` (`0x140310490`), `sub_14030FE18`, `AbilityAction_GetRecord`, `sub_1402607C0`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 40-entry turn-order forecast: simulates each unit's CT until it reaches 100, inserts entries sorted by
time, and adds the entries of pending (charging) actions.

## Behavior

- V: clears 40 entries to `0xFFFFFFFF`.
- V: unless `mode == 2` or `fillCurrent == 1`, inserts the unit currently marked active (`+0x1B8 != 0`) at time 0.
- V: for each of the 21 records (`g_BattleUnitTable`, stride 512): skips units for which `sub_14030FE18` returns
  true (dead/removed/statuses); reads the unit's `+0x64`/`+0x65` status bits and its `+0x6C`/`+0x71` modifier
  bytes to raise the effective speed, and skips units flagged `+0x61 & 2`.
- V: the time simulation: `ct = unit[0x41]`, `speed = max(unit[0x40], 1)`; while `ct < 100` add speed (halved by
  Slow via `+0x64 & 4`, x1.5 by Haste via `+0x64 & 8`), incrementing a tick counter; after the tick, `ct %= 100`
  and the entry time is `(tick << 8) - ct + 100`. Up to 40 entries and 255 ticks per unit.
- V: a pending action (`+0x18D != 0`) adds an entry with `0x40`, its ability low byte and the charge time from
  `AbilityAction_GetRecord(ability)[12] & 0x7F`, at `tick + charge`; the ability id's bit 8 goes to flag `0x80`.
- V: mode 3 (`a3 == 1`) is the AI prediction: it sets `g_BattleSimulating = 2` around the call (saved/restored by the
  callers `BTurn_PreviewAction` and `Battle_AITurnRun`); mode 0 is the normal timeline.
- V: the tail is filled with copies of the last entry so all 40 slots are valid.
- V: returns `-1` when nothing was inserted, else 0.

## State touched

- Calls: [TurnList_InsertEntry](TurnList_InsertEntry.md), [sub_14030FE18](sub_14030FE18.md), [AbilityAction_GetRecord](AbilityAction_GetRecord.md)

## Referenced by

- Called by: [BTurn_PreviewAction](BTurn_PreviewAction.md), [Battle_TimelineBuildList](Battle_TimelineBuildList.md)

## Notes

The IDB/exported name is `TurnList_Build` (kept: `symbols/functions.json` and the `TurnList_InsertEntry` sheet already
use it; renaming to a `BTurn_*` name would break those references). The low 5 bits of entry byte 0 are the unit slot; 31 (0x1F) ends the list.

## Open questions

The exact tie-break of equal times (the insertion is a stable "first time above" shift, so equal times append after).
