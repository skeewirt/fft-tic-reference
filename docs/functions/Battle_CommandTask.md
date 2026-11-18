# Battle_CommandTask

- **Address:** `0x140202B08`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_CommandTask(void)`
- **Callers:** `sub_140204B78`, `sub_14020A18C`, `sub_14020A7F0`, `sub_14020BCF0`, `sub_14020DA14`, `sub_14020DAEC`, `sub_140210AF0`
- **Callees:** `sub_140202930`, `Battle_TurnStep` (`0x1402029DC`), `sub_1402366C0`, `sub_1402607C0`, `sub_140202800`, `SceneObject_FindBySlot`, `sub_1401FAF54`, `sub_1400F4BCC`, `sub_1401FAA24`, `sub_1402028D8`, `sub_14020261C`, `sub_140205498`, `sub_140234A94`, `sub_140216ACC`, `sub_1400EB5F4`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The per-frame player battle command task: advances the turn engine, claims the active unit, and puts up the command
menu (Move / Abilities / Wait / Status) or hands the unit to the AI.

## Behavior

- V: IDA's name `_isctype_l` is a wrong FLIRT match (the body is battle code, not CRT); it is the only caller of
  `Battle_TurnStep`.
- V: `sub_140202930()` non-zero short-circuits with menu mode `48` (0x30) (`0x140202B3B`).
- V: otherwise it calls `Battle_TurnStep`, copies `qword_141871698` to `qword_14184A9B0`, resets the panel state and
  looks up the current unit node with `sub_1402607C0`; the node's `+8` byte becomes `dword_140C6AD8C`.
- V: reads the unit's BWorkHolder at `BattleControl + 0x88*slot` (`0x140202D44`/`0x140202D4B`) and calls its voice
  controller when `+0x80` is non-zero.
- V: when the engine result was `0x100` and the unit is a player unit, it runs `sub_140202800`, resets the held-key
  state and shows the command menu: `dword_140C6B1CC = 39` (`0x140202DB3`), `dword_140D3A864 = 1`
  (`0x140202DD5`).
- V: the post-command handler `sub_14020AD64` calls the AI entry `sub_14031F130` when the unit has idled for more
  than 30 frames (`*(uint16*)(node+12) > 0x1E`) and `*(node+466) == 0` (`0x14020ADC6`) — the Auto / idle path (I).
- V: `dword_140D3A868` (last engine code) is only written by this path, in `Battle_TurnStep`.

## State touched

- Calls: [Battle_TurnStep](Battle_TurnStep.md), [sub_1402366C0](sub_1402366C0.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [sub_1400F4BCC](sub_1400F4BCC.md), [sub_14020261C](sub_14020261C.md)

## Referenced by

- Called by: [sub_140204B78](sub_140204B78.md), [sub_14020A7F0](sub_14020A7F0.md), [sub_14020BCF0](sub_14020BCF0.md)

## Notes

This is the function to watch for "the player is being asked to choose": menu mode 39 plus `dword_140D3A864 = 1`.

## Open questions

What `sub_140202930`'s mode 4 (`dword_141853C08 == 4`) means; the exact Auto toggle that makes a player unit take the
`sub_14031F130` branch.
