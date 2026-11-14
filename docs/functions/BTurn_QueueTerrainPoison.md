# BTurn_QueueTerrainPoison

- **Address:** `0x14030C2C0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 BTurn_QueueTerrainPoison(_BYTE *unit)`
- **Callers:** Battle_TurnEngine
- **Callees:** Battle_ResultReset, Status_FilterPendingSets

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Queues Poison for a unit that stands on a harmful terrain tile and passes the filter of the status rules.

## Behavior

- V: returns 0 when the unit row is empty, or the unit is Crystal, KO or Jumping (mask 0x64 of +97), Stone or Chest (mask 0x81 of +98), or its +0x1B4 bit 0x40 is set.
- V: returns 0 when the unit is Float (bit 0x40 of +99); for a unit whose +0x1B4 is negative the Float test is made on the unit named by the low five bits of +0x1B4 instead.
- V: points g_BattleActingUnit and g_BattleActionBlock at the unit and its result block, resets the result block, then reads the terrain flags of the unit tile (tile table at g_BattleTileTable, layer bit 7 of +81, x +79, y +80) through the 64-entry table at 0x14067F750 + 64; returns 0 when its bit 0x80 is clear.
- V: otherwise sets the pending-add byte at block +32 to 0x80 (Poison, id 24), runs Status_FilterPendingSets(0) and returns 0 when the filter leaves nothing; else sets the result flag at block +39 to 8 and returns 1.
- I: bit 0x80 of that table is the poisonous terrain flag (it is the only gate on the tile).

## Notes

Name is ours. The terrain flag table at 0x14067F750 is reached through an image-base-relative address built in the code, so the address does not appear as an operand.

## Open questions

? which terrain types carry the flag (the table at 0x14067F750 has not been mapped).
