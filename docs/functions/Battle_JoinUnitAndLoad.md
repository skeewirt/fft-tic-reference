# Battle_JoinUnitAndLoad

- **Address:** `0x1401F2E4C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void Battle_JoinUnitAndLoad(void *a1)`
- **Callers:** not recorded
- **Callees:** Battle_AddJoinedUnit, CharaPalette_ReloadForShape

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The mid-battle join: runs Battle_AddJoinedUnit, then the look loader once per frame until it returns 0.

## Behavior

- V: the loader is CharaPalette_ReloadForShape.

## State touched

- Calls: [CharaPalette_ReloadForShape](CharaPalette_ReloadForShape.md)

## Referenced by

- Observed behaviours: [MidBattleJoinLoadsLooks](../behaviors/MidBattleJoinLoadsLooks.md)

## Open questions

None recorded.
