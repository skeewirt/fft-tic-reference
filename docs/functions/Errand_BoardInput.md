# Errand_BoardInput

- **Address:** `0x1402ED540`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void Errand_BoardInput(int *state)`
- **Callers:** ClassicMenu_RunScreenStack
- **Callees:** Errand_SelectBoardEntry, WorldMenu_RunTopOpenHook, sub_14019DF88, Errand_Recall, sub_14019DCD4, sub_1402D541C, sub_1401A1D28, Errand_ComputeRewards, sub_14036FCB8, sub_14036CB1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The tavern errand board's input step: dispatch a chosen errand, collect a returned one, recall one, or leave.

## Behavior

- V: after a closing message, either picks the board entry under the cursor (Errand_SelectBoardEntry with the entry's 11-bit id from g_ErrandBoardList) or goes back (WorldMenu_RunTopOpenHook).
- V: reads the board widget's request (sub_14019DF88) and switches on it: 0x0D collects the selected returned errand (finds its active slot by the errand byte, then Errand_ComputeRewards and sub_14036FCB8), 0x18 recalls it (Errand_Recall), 6 calls sub_14036CB1C, others set screen states.

## State touched

- Calls: [Errand_SelectBoardEntry](Errand_SelectBoardEntry.md), [WorldMenu_RunTopOpenHook](WorldMenu_RunTopOpenHook.md), [Errand_Recall](Errand_Recall.md), [Errand_ComputeRewards](Errand_ComputeRewards.md)

## Notes

Name is ours (was sub_1402ED540).

## Open questions

? what sub_14036CB1C (request 6) opens.
