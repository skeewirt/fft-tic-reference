# SortieScreen_ShowAreaBoxes

- **Address:** `0x140147C24`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void SortieScreen_ShowAreaBoxes(UIAddonFFTOBattleSortie2 *screen, int area0Count, int area1Count)`
- **Callers:** sub_1401EF0D8
- **Callees:** UIName_Key, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows as many portrait boxes in each area of the deployment screen as the area's count, by playing the Team component's states.

## Behavior

- V: returns when the screen's +0x48 is 0. For area0Count 1..5 it plays the Team state 'Team01_<n>' (none for another value); then 'ShowTeam02' when area1Count > 0, else 'HideTeam02'; then 'Team02_<n>' for area1Count 1..4.
- V: the states show or hide the box parts T01_k / T02_k through their visibility tracks (the parts' enabled byte +144); a box that no state names keeps its own byte.
- V: called once by sub_1401EF0D8 right after the capacity (+0x40) is set, with the two areas' count bytes.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Referenced by

- Observed behaviours: [DeploymentPortraitColumnBoxes](../behaviors/DeploymentPortraitColumnBoxes.md)

## Open questions

None recorded.
