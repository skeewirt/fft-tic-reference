# Deployment_CompactPlaced

- **Address:** `0x1401EE6DC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Deployment_CompactPlaced(DeploymentState *state)`
- **Callers:** sub_1401F22D0, sub_1401F3128, sub_1401F358C and one more caller in the deployment code
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves the placed party indices of the deployment state to the front of their array.

## Behavior

- V: does nothing when the capacity (+64) is above 5; otherwise copies the 5 dwords from +68 to the stack, sets all 5 to -1 and writes back the ones that are not -1 in order.

## Referenced by

- Observed behaviours: [DeploymentAcceptsOneToFivePlacedUnits](../behaviors/DeploymentAcceptsOneToFivePlacedUnits.md)

## Open questions

None recorded.
