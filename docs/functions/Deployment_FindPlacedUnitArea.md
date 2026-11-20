# Deployment_FindPlacedUnitArea

- **Address:** `0x1401F3E3C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool Deployment_FindPlacedUnitArea(DeploymentState *state, int slot, int *area, int *order)`
- **Callers:** sub_1401F16F4 (the unit under the tile cursor)
- **Callees:** Deployment_AreaOfPlacedUnit, sub_1403033CC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds which deployment area a placed party unit (by its battle slot) stands in, and its order among the placed units of that area.

## Behavior

- V: walks the first 5 placed party indices (+68..+87); for each one that is not -1 it gets the entry's area (Deployment_AreaOfPlacedUnit) and its battle record (sub_1403033CC by party index), and counts the entries of area 0 and of area 1 met before the one whose record slot byte equals `slot`.
- V: found: *area = its area, *order = the count of earlier entries in that area, returns 1; not found among the 5: *area = -1, *order = -1, returns 0.

## State touched

- Calls: [Deployment_AreaOfPlacedUnit](Deployment_AreaOfPlacedUnit.md)

## Referenced by

- Observed behaviours: [DeploymentAcceptsOneToFivePlacedUnits](../behaviors/DeploymentAcceptsOneToFivePlacedUnits.md)

## Notes

A sixth placed entry is never looked at (the loop stops at 5).

## Open questions

None recorded.
