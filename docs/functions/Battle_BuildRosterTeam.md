# Battle_BuildRosterTeam

- **Address:** `0x140270CE4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_BuildRosterTeam(uint8_t *spawnList, int a2)`
- **Callers:** `BattleLoad_StepFresh` (`0x140304741`, battle scene task phase 8), `sub_14030476C` (`0x140304AE7`,
- **Callees:** `UnitWork_BuildFromSaveIndex`, `Unit_ResolvePreviewShape`, `sub_140271178`, `sub_1403041A4`,

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the live 21-slot battle unit table (`g_BattleUnitTable`, `0x141853CE0`, stride 512) from a 5-entry spawn
list, one team at a time. This is the function that places units on the two sides.

## Behavior

- V: `spawnList` holds 5 entries of 8 bytes; byte 0 of each entry is a `g_UnitSaveData` index (0xFF = no unit).
  List bytes 1, 2 and 3 are copied to the record's `+79` (tile X), `+80` (tile Y) and `+81` (facing in bits
  0..3, bits 4..6 kept, bit 7 preserved).
- V: the slot cursor starts at **16** when `a2 == 0` and at **0** when `a2 != 0`; which suggests player-side units at
  16..20 and enemies at 0..4 on the generic sortie path; **contradicted live** for the first battle (player side slots 0..4 and others, enemies 5..9, 12, 13,
  slots 16..20 empty): scripted battles place units through the event tasks. Use the team byte, not the slot.
- V: for each entry: `rec[1] = slot`, `rec[0x1B5] = 1`, `UnitWork_BuildFromSaveIndex(rec, entry[0], 0)`,
  `Unit_ResolvePreviewShape(rec, &pal, rec[3])` -> `rec[0x18F]/0x190`, `rec[0x191] = sprite number`.
  The sprite number counts down from -2 for `a2 != 0` and up from 120 for `a2 == 0`.
- V: an empty entry sets `rec[0x1B5] = 0xFF` and `rec[1] = 0xFF`.
- V: `a2 != 0` additionally sets the word at `+4 = 0x1801` and the team/type byte `+0x1EE = 0x18`
  (`0x140270E59`), i.e. team bits 4..5 = 1 (enemy).
- V: when the spawn entry's byte 3 bit 4 is clear, the unit is registered with `sub_1403041A4(x, y, layer,
  facing, shape, palette, 255, rec, 0)` and reset with `sub_140278E0C(rec, 1)`; bit 4 set leaves
  `rec[0x1B5] = 0`.
- V: for `a2 != 0` only, slots 5..15 are cleared (`+0x1B5 = 0`, `+1 = 0xFF`, `+0x1B4 = 0xFF`).
- I: the failing `sub_140271178` test rejects a unit that cannot be built (e.g. an empty/corrupt save slot).

## State touched

- Calls: [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md)

## Referenced by

- Called by: [BattleLoad_StepFresh](BattleLoad_StepFresh.md), [sub_14030476C](sub_14030476C.md)
- Observed behaviours: [BattleUnitOnFieldByte](../behaviors/BattleUnitOnFieldByte.md), [SceneUnitShapeIsTheQueueWord](../behaviors/SceneUnitShapeIsTheQueueWord.md)

## Notes

This is the authoritative statement that the table is the live battle table, not a preview: it writes the same
records the action resolver reads, and it is called from the battle scene task (phase 8), not from a menu.

## Open questions

What spawn-list byte 3 bit 4 means (a unit that is placed but not present?), and why player units start at 16.
