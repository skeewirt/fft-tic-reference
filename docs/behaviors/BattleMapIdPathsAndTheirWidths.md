# BattleMapIdPathsAndTheirWidths

- **Kind:** observed behaviour
- **Scope:** engine (battle map id storage)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [SaveHeader_FillBattleFields](../functions/SaveHeader_FillBattleFields.md), [BattleLoad_StepFresh](../functions/BattleLoad_StepFresh.md), [EventScript_Run](../functions/EventScript_Run.md), [SceneVar_Read](../functions/SceneVar_Read.md), [SceneVar_Write](../functions/SceneVar_Write.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle map id travels as a 32-bit global (0x140D3A838) set from scene variable 51 or from one of two signed 16-bit event words (-1 means none); the current-map global used for resources is another 32-bit global (0x140784478); the battle save header keeps the id in ONE byte.

## Behavior

- V: the battle load passes the 32-bit global (or scene variable 51) to the map task, which stores it into the 32-bit current-map global before calling the map loader (whose argument is 16 bits).
- V: two event words (0x140D40924, 0x140D40928) are compared with -1 and sign-extended when they set the global; the instruction that writes them from script data was not read, so their operand width is ?.
- V: SceneVar_Read returns a 32-bit value and SceneVar_Write takes a 32-bit value; the width of the stored cell behind them was not read (?).
- V: SaveHeader_FillBattleFields stores the low byte of the battle map id at +0x2C of the save header; I: it is for display in the save list; ? the reader of that byte was not found, and whether it also steers a resume.
- V: the battle capture (SceneUnits_SaveRestore) copies the 32-bit global whole.
- V: every other reader found of the two globals compares the id with stock map numbers (6, 8, 14, 15, 22, 23, 26, 33, 50, 52, 53 to 83, 62, 64, 82, 92, 94, 127 appear) or searches a short fixed list keyed by it (five entries); none indexes an array by it other than the tables above, and an id with no match takes the default branch.
- V: one function writes the sentinel 0x77777777 into the current-map global as 'no map'.

## Notes

Together with MoveFindTakenBitsAreFourPerMapInA128ByteArray this is why map ids above 255 are not safe in this build.

## Open questions

? the event command that sets the battle map and its operand width; ? the cell width of scene variable 51 in storage and in saves.
