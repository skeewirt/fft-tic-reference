# BUi_BattleMenuWindowsCtor

- **Address:** `0x1401012A0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 sub_1401012A0(agent, ...)`
- **Callers:** agent construction (registered in the UI agent table at `sub_1400EC678`)
- **Callees:** Mem_Alloc, `sub_140102F20`, `sub_140153020`, `sub_1401D16C4`, `sub_1401D1A00`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the two addons of the battle menu-windows agent: the battle HUD (`BattleMain4`) and the command menu (`BattleCommand`).

## Behavior

- V: allocates 66680 bytes, initializes it with `sub_140102F20`, attaches it and registers it as addon type **120**; stores the pointer at agent `+64`.
- V: allocates 5640 bytes, initializes it with `sub_140153020`, attaches it and registers it as type **101**; stores it at agent `+72`.
- V: sets agent `+80 = 1`.

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md)

## Notes

`sub_140102F20` is the 11.5 KB `BattleMain4` constructor: it binds the HUD nodes (`MapInfo`, `AttackInfo`, `UnitInfoLeft/Right`, `ATBar`, `TextBoardSurvey`, ...) and registers the 100 UI state keys at +57192 (`sub_14010E1FC`).

## Open questions

? what agent+80 selects.
