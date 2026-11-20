# TwoDeploymentAreasShareOneCapacity

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment, two squads)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [DeploymentGrid_CommenceCheck](../functions/DeploymentGrid_CommenceCheck.md), [Deployment_SelectArea](../functions/Deployment_SelectArea.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle with two deployment areas adds the two areas' counts into one capacity, which the commence check still holds to 1..5; stock scenario rows whose two counts add up to 6 or 7 exist but cannot pass that check.

## Behavior

- M: over the scenario setup table (887 rows of 24 bytes at 0x1408ECAB0) 494 rows name a deployment area and 231 name two; the two counts add up to 4 or 5 on the story rows up to event 591, to 6 (3 + 3) on events 600..743 and to 7 (5 + 2) on event 445.
- V: sub_1401EF0D8 sets the capacity to the sum and DeploymentGrid_CommenceCheck returns 0 for a capacity above 5, so a row with a sum of 6 or 7 cannot start its battle through this screen.
- V: after a successful check sub_1401F16F4 walks exactly the 5 records 16..20 (from 0x141855CE0) and numbers the placed units' event-unit byte (+401) from 120.
- ?: whether events 600..743 and 445 are reachable in this version (not checked).

## Open questions

? whether events 600..743 and 445 can be reached; the state fields +1832..+1883 belong to the carousel (DeploymentStateLayout), not to a second squad.
