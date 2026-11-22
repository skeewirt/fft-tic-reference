# Deployment_CountPlaced

- **Address:** `0x1401EE6AC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Deployment_CountPlaced(DeploymentState *state)`
- **Callers:** DeploymentGrid_CommenceCheck, sub_1401F16F4, sub_1401F22D0, sub_1401F3128, sub_1401F3F70, sub_1401F4898, sub_1401F5B64, sub_1401F5CEC and one more caller in the deployment code
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counts the placed party units of the deployment state.

## Behavior

- V: returns 0 when the capacity (+64) is above 5; otherwise the number of entries among the first `capacity` dwords from +68 that are not -1.

## Referenced by

- Called by: [DeploymentGrid_CommenceCheck](DeploymentGrid_CommenceCheck.md)
- Observed behaviours: [DeploymentAcceptsOneToFivePlacedUnits](../behaviors/DeploymentAcceptsOneToFivePlacedUnits.md), [DeploymentPlacedIndicesReaders](../behaviors/DeploymentPlacedIndicesReaders.md)

## Notes

Behavior: DeploymentAcceptsOneToFivePlacedUnits.

## Open questions

None recorded.
