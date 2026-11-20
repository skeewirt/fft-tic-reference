# Deployment_ResetState

- **Address:** `0x1401EE518`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Deployment_ResetState(DeploymentState *state)`
- **Callers:** sub_1401EE21C, Battle_Init
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets the deployment state: capacity 0, no placed unit, no candidate.

## Behavior

- V: +64 = 0; the five placed indices +68..+87 = -1; +88 and +96 = 0; the 54 candidate entries from +1180 (12 bytes each) get -1; the candidate count +1828 = 0; +1832..+1840 and the nine card slots +1848..+1883 = -1; +1884 = 0; +1888 = 0x1000000.

## Referenced by

- Observed behaviours: [DeploymentStateLayout](../behaviors/DeploymentStateLayout.md)

## Open questions

None recorded.
