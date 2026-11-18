# ScenarioSetupRecordFeedsTheBattleSceneVariables

- **Kind:** observed behaviour
- **Scope:** engine (scene entry of an event or battle)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md), [Scenario_CheckBattleRecord](../functions/Scenario_CheckBattleRecord.md), [SceneVar_Write](../functions/SceneVar_Write.md), [BattleLoad_StepFresh](../functions/BattleLoad_StepFresh.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

When a scene starts, the routine that applies the scenario setup record finds the record of the current event number (scene variable 39) in the 24-byte table of 887 records and writes the scene variables the battle load reads: the battle map id (variable 51) from a signed byte at +2, the entry key (50), up to two deployment area ids (53, 54) and their count (52).

## Behavior

- V: the search is linear over at most 887 records and ends at the first record whose event number (u16 at +0) is 0; 713 stock records are used (event numbers 1..743) and 174 are free.
- V: the map id is the signed byte at +2; the byte at +3 is a separate field (high nibble to variable 48, low nibble to variable 35), so the two bytes are not one 16-bit map word.
- V: SceneVar_Write stores a negative value reduced to its low byte, so a map byte of 128..255 reaches variable 51 as 128..255; variable 51 is a 32-bit cell and the scene entry copies it into the 32-bit battle map id.
- V: the u16 at +7 is the entry key (variable 50) and is written only when it is not 0; the u16 at +9 and +11 are deployment area ids (variables 53 and 54), variable 52 counts the non-zero ones, and the signed byte at +17 goes to variable 511 only when the one at +9 is not 0.
- V: the u16 at +22 is a key of the table EnhancedBattleEvent; the routine returns before writing variable 51 when that key has no row, when the key has 16 or more entries, or when the collected list reaches 512 words.
- V: Scenario_CheckBattleRecord continues a battle only for a record whose byte +20 is exactly 0x80 (144 stock records); 65 records hold 0x81 and 20 hold 0x82.
- V: the per-event words built from bytes +18..+20 fill an array of 887 words indexed by event number, which the battle capture copies whole (0x6EE bytes): event numbers stay below 887.

## Notes

Event 93 keeps the current value of variable 51 instead of the record's map byte. In the resume case (scene mode 1) the routine reads the record of the saved event number.

## Open questions

? the meaning of byte +20 values 0x81 and 0x82; ? bytes +5, +6, +13, +14 and +15..+16; ? whether the 59 stock records whose key at +22 has no EnhancedBattleEvent row are ever started.
