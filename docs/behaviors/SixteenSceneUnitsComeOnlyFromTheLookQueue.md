# SixteenSceneUnitsComeOnlyFromTheLookQueue

- **Kind:** observed behaviour
- **Scope:** engine (battle unit drawing)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md), [LookPool_ResetForBattleLoad](../functions/LookPool_ResetForBattleLoad.md), [SceneUnits_SaveRestore](../functions/SceneUnits_SaveRestore.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle unit is drawn through one of 16 scene-unit records, and only SceneUnit_BuildFromQueueEntry creates them, from the 16-entry look queue; with all 16 in use the next unit gets no scene unit.

## Behavior

- V: the scene-unit records are 16 x 1352 bytes (in-use dword at 0x140D30030, g_SceneUnitSlots at +8); SceneUnit_BuildFromQueueEntry takes the requested record below 16 or the first free one and returns null when none is free.
- V: SceneUnit_BuildFromQueueEntry has one caller, CharaPalette_ReloadForShape, which runs from the battle load (BattleLoad_StepFresh), the mid-battle join (Battle_JoinUnitAndLoad), sub_14023A0B4 and sub_14030476C.
- V: five functions address the in-use dwords: LookPool_ResetForBattleLoad, SceneUnit_BuildFromQueueEntry, SceneUnits_SaveRestore, sub_1401D4544 and sub_14033D6B0.
- I: entry units are kept only while their count is below 16 minus scene variable 57 (EntryUnitsShareADistinctLookBudget), and the placed party takes up to 5 more; whether variable 57 reserves scene units for the party is not settled.

## Open questions

? the value of scene variable 57 in stock battles (a live read per battle); ? when a scene unit is released (KO, crystal, leaving).
