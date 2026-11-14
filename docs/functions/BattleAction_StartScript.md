# BattleAction_StartScript

- **Address:** `0x140234A94`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleAction_StartScript(int scriptId, int actorSlot, int targetSlot)`
- **Callers:** ~30 battle/menu/event functions, including `sub_140202F34`, `sub_14020327C`,
- **Callees:** `sub_140226C2C`, `SceneTask_Start` (`0x140234B10`)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts one of the seven battle presentation programs (the "scene script" table) and records the acting
unit and target for the tasks that program starts.

## Behavior

- V: returns immediately when `word_140D4080C == 1` (a battle/menu lock).
- V: stores `byte_140672134[scriptId]` in `dword_142FEC534`.
- V: when `actorSlot != 0xFF`: stores it in the high half of `dword_1407DCF98` (`+2`) and in
  `word_1407832AA`.
- V: when `targetSlot != 0xFF`: stores it in `word_1407DCFAA` and `word_14078332A`.
- V: if scene slot 2 is free (`[off_140783088 + 0x1090] == 0`), calls
  `SceneTask_Start(2, sub_140234B3C)` at `0x140234B10`.
- V: writes the script id at scene block 1 offset 0 (`[off_140783088 + 0x1000]`), then zeroes block 1
  offsets +8 and +16.
- V: the driver (`sub_140234B3C`) reads that id to select the 64-byte record at `0x140672210`.

## State touched

- Calls: [SceneTask_Start](SceneTask_Start.md)

## Referenced by

- Called by: [sub_14020327C](sub_14020327C.md), [sub_140203450](sub_140203450.md)

## Notes

The program table and the seven records are documented in `docs/reference/battle-actions.md`. Script 3
is started by the three action-confirm functions; script 2 by the turn-start state machine.

## Open questions

- The meaning of the per-script byte table `byte_140672134` (values 1..8) stored in `dword_142FEC534`.
