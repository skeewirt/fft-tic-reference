# Deployment_AreaOfPlacedUnit

- **Address:** `0x1401EE734`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Deployment_AreaOfPlacedUnit(DeploymentState *state, int n)`
- **Callers:** sub_1401F3858, Deployment_FindPlacedUnitArea, sub_1401F49EC, sub_1401F5078
- **Callees:** SceneObject_FindByUnitIndex, SceneVar_Read, Deployment_LoadAreaPlacement, Battle_FindUnitNodeAt

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the deployment area (0 or 1) that placed party entry n stands in, or -1.

## Behavior

- V: takes the party index at +68 + 4 n (-1 = none), finds its battle record among records 16..20 only (slot byte not 0xFF, +2 = the party index) and its scene object.
- V: then for each area below scene variable 52 walks the area's 25 placement cells (Deployment_LoadAreaPlacement) and returns the area whose valid cell holds that unit's node (Battle_FindUnitNodeAt).

## State touched

- Calls: [SceneObject_FindByUnitIndex](SceneObject_FindByUnitIndex.md), [SceneVar_Read](SceneVar_Read.md), [Deployment_LoadAreaPlacement](Deployment_LoadAreaPlacement.md)

## Referenced by

- Called by: [Deployment_FindPlacedUnitArea](Deployment_FindPlacedUnitArea.md)
- Observed behaviours: [PartyResultsAreFoundBySaveIndexInAllRecords](../behaviors/PartyResultsAreFoundBySaveIndexInAllRecords.md)

## Open questions

None recorded.
