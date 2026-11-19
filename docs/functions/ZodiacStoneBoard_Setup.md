# ZodiacStoneBoard_Setup

- **Address:** `0x14016C414`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ZodiacStoneBoard_Setup(void *board)`
- **Callers:** the Zodiac Stone screen
- **Callees:** MainTab_BindNodes, MainTab_SelectTab, sub_1402AAB0C, UserSituation_IsMet, Icon_FormatPath, sub_1400F4E74, GUINode_FindState, GUINode_PlayState, GUINode_StopState, GUITextNode_SetTextExpandedTemp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets up the Zodiac Stone board: for each of the 13 stones picks the row to show, plays the stone's state and sets its name.

## Behavior

- V: binds the main tabs (tab 2 selected) and finds the node 'Arazlam'; the node 'Board' plays 'Loop'.
- V: walks ZodiacStone: for each stone (first key) it stores in the board's dword array at +408 (dword index 102) the highest second key whose user_situation (+8) is met (-1 when none) and preloads that row's icon (+0x1C, Icon_FormatPath); it also preloads the icon of row (n, 0) for the 13 stones.
- V: per stone the node 'Zst_%02d' (kind 3) gets node +548 = n + 100 and +557 = 0. No met row: 'HideStone', and 'Loop' is stopped there. Otherwise row +0xC (zodiac_stone_owner_timeline) decides: 0 plays 'ShowStone'; non-zero plays, when the value is not 1, the state named by string +8 of the ZodiacStoneOwnerTimeline row (table 238) with that id, then 'ShowUnacquired'.
- V: the text node 'TextBoardName' (kind 13) gets the name (+0x10).

## State touched

- Calls: [MainTab_BindNodes](MainTab_BindNodes.md), [MainTab_SelectTab](MainTab_SelectTab.md), [UserSituation_IsMet](UserSituation_IsMet.md), [Icon_FormatPath](Icon_FormatPath.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_StopState](GUINode_StopState.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md)

## Referenced by

- Observed behaviours: [ZodiacStoneBoardShowsStonesByHeldState](../behaviors/ZodiacStoneBoardShowsStonesByHeldState.md)

## Notes

The 'Show<owner>' state names come from the owner-timeline table, the 'Hide<owner>' names from its +0xC (reader not looked for).

## Open questions

? what the 'Loop' animation looks like; ? the reader of ZodiacStoneOwnerTimeline +0xC.
