# LookPool_ResetForBattleLoad

- **Address:** `0x14026F5CC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void LookPool_ResetForBattleLoad(void)`
- **Callers:** sub_14030476C
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears the scene-unit in-use flags and the look pool claims before a battle load, and resets the load state machine.

## Behavior

- V: unless the global at 0x142FF9E2C is 1, sets the in-use dword of each of the 16 scene-unit records and the first byte of each of the 15 look pool records to 0.
- V: clears the list head qword_140D3A410 and the state words at 0x140CE3240 (pass, step, entry index, buffer).
- V (2026-11-08): only byte +0 (the claim) of a pool record is cleared here; byte +1 (the sprite the record holds) and the record's data stay, so CharaPalette_ReloadForShape's pass 2 still finds the record by +1 and skips reading that sprite's classic file. The battle setup sub_140210AF0 clears byte +1 of all 15 records itself, before a resume restore (flow BattleResumeRestoresTheLooks).
- V: clears the scene list head always, and the scene-unit in-use flags and the pool claim bytes +0 only when the load mode (0x142FF9E2C) is not 1: a resumed battle keeps the restored pool records.

## Referenced by

- Called by: [sub_14030476C](sub_14030476C.md)
- Observed behaviours: [LookPoolOfFifteenIsWiredIntoFixedSlots](../behaviors/LookPoolOfFifteenIsWiredIntoFixedSlots.md), [LookSlotsAlreadyInTheGame](../behaviors/LookSlotsAlreadyInTheGame.md), [PoolRecordKeepsItsSpriteAcrossTheReset](../behaviors/PoolRecordKeepsItsSpriteAcrossTheReset.md), [SixteenSceneUnitsComeOnlyFromTheLookQueue](../behaviors/SixteenSceneUnitsComeOnlyFromTheLookQueue.md)

## Notes

Structures: SceneUnitSlot, LookPoolRecord. The name is ours (IDB: sub_14026F5CC).

## Open questions

None recorded.
