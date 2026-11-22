# WorldEncounter_StartBattle

- **Address:** `0x140248254`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void WorldEncounter_StartBattle(void *task)`
- **Callers:** sub_1402473EC, sub_1402482F8
- **Callees:** sub_1402B8690, EventVar_Write, sub_1402CC2E0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the random battle WorldEncounter_Roll picked: writes the scene variables the battle load reads (the entry, one deployment area and its row) and clears the story event number.

## Behavior

- V: EventVar_Write(50, the picked formation), EventVar_Write(52, 1) (one deployment area), EventVar_Write(53, dword_140D49468 = 0x200 + the encounter row's byte 1, the deployment row), EventVar_Write(39, 0); clears dword_141856710 and calls sub_1402CC2E0(0).
- V: no scenario setup record is applied for the battle, so Deployment_PrepareCandidates sets scene variable 57 to that row's count byte (seen live: 5 at Mandalia Plain, row 554).

## State touched

- Calls: [EventVar_Write](EventVar_Write.md)

## Referenced by

- Observed behaviours: [DeploymentRowsOfEachBattle](../behaviors/DeploymentRowsOfEachBattle.md)

## Open questions

None recorded.
