# DeploymentGrid_CommenceCheck

- **Address:** `0x1401EE890`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int DeploymentGrid_CommenceCheck(uint8_t *grid)`
- **Callers:** sub_1401F16F4, sub_1401F22D0
- **Callees:** SceneVar_Read, Deployment_SelectArea, sub_1401EE6AC, sub_1401EE830, BattleMsg_SetKind1

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides whether the deployment screen may start the battle with the units placed: returns a result code, 1 meaning go.

## Behavior

- V: returns 0 when the placed-unit count (dword at +64) is not 1..5; 3 when sub_1401EE6AC finds nothing placed.
- V: reads the number of deployment areas (scene variable 52), takes the area sizes through Deployment_SelectArea(0) and, for two areas, (1), and asks sub_1401EE830 per area; an area with no unit sends a kind-1 battle message and returns 6; with two areas and the second one empty it sends the message with 7 or 8 depending on how the counts compare.
- V: scans the placed party indices (dword array at +68): an entry below -1 returns 0; an entry equal to 0 (party member 0) sets a flag.
- V: returns 1 when scene variable 511 is 0 or party member 0 is placed, otherwise 2 (Ramza must be deployed).

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [Deployment_SelectArea](Deployment_SelectArea.md), [BattleMsg_SetKind1](BattleMsg_SetKind1.md)

## Referenced by

- Observed behaviours: [DeploymentAcceptsOneToFivePlacedUnits](../behaviors/DeploymentAcceptsOneToFivePlacedUnits.md), [DeploymentStateLayout](../behaviors/DeploymentStateLayout.md), [ScenarioRamzaRequiredRule](../behaviors/ScenarioRamzaRequiredRule.md), [TwoDeploymentAreasShareOneCapacity](../behaviors/TwoDeploymentAreasShareOneCapacity.md)

## Open questions

? the exact meaning of the result codes 3, 6, 7 and 8 beyond the messages.
