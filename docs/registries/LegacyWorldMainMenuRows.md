# LegacyWorldMainMenuRows

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [LegacyWorldMenu_MainMenuTask](../functions/LegacyWorldMenu_MainMenuTask.md), [LegacyMenu_ConfirmRow](../functions/LegacyMenu_ConfirmRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The rows of node 4 of the old world menu (the old main world menu): row -> next node -> what it opens. The row list is at 0x140789388. Only row 1 can be reached: the node's task confirms row 1 and nothing else.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="node 6"></a>0 | `node 6` | `LegacyMenu_BuildLocationList` | V | The old location list. |
| <a id="node 7"></a>1 | `node 7` | `LegacyWorldMenu_RequestRoster` | V | The roster: word 0x143749F28, run by LegacyWorldMenu_StepRosterRequest. The only reachable row. |
| <a id="node 11"></a>2 | `node 11` | `sub_1402B3DE4` | V | Word 0x143749F34 -> state mask 0x100 -> ClassicMenu_HubStep opens kind 28. |
| <a id="node 14"></a>3 | `node 14` | `sub_1402B3C54` | V | Word 0x143749F2C -> state mask 0x100000 -> kind 43. |
| <a id="node 12"></a>4 | `node 12` | `sub_1402B3BF0` | V | Word 0x143749F30 -> LegacyWorldMenu_StepRow4Request (sub_14021A030(1)). |
| <a id="node 5"></a>5 | `node 5` | `sub_1402B3B90` | V | Starts sub_1402B3B88 in the slot below, then sub_1402BA718 and sub_1402B8690. |
| <a id="node 18"></a>6 | `node 18` | `sub_1402B3F20` | V | Puts the cancel bit in the input and starts sub_1402B3E48 in the slot below. |
| <a id="node 16"></a>7 | `node 16` | `LegacyMenu_NumberEntryTask` | V | Map number 1..200, then LegacyWorldMenu_StartTestBattle (test battle, variable 510 = 1). |
| <a id="node 15"></a>8 | `node 15` | `LegacyWorldMenu_RequestEventVarEditor` | V | Word 0x143749F38 -> state mask 0x800000 -> EventVarEditor_Open. |
| <a id="node 17"></a>9 | `node 17` | `LegacyWorldMenu_RequestPartyLoader` | V | Word 0x143749F3C -> state mask 0x1000000 -> PartyLoader_OpenPrompt -> MenuCtl_Entry52 -> Party_RebuildFromBattleEntry. |
| <a id="node 20"></a>10 | `node 20` | `EventMenu_NodeListTask` | I | A small window titled by text 0x5012 whose rows all close one level. Whether the list has this row: see behaviour. |

## Behavior

- V: LegacyWorldMenu_MainMenuTask calls LegacyMenu_ConfirmRow only with row 1, and only when a roster request code (1000 or 2000 at g_CharaRenderMgr +13448) waits.
- V: rows 2, 3, 8 and 9 set request words that LegacyWorldMenu_FrameStep turns into state masks of dword 0x141D32E14 (0x100, 0x100000, 0x800000, 0x1000000) read by ClassicMenu_HubStep; row 4 sets word 0x143749F30, which LegacyWorldMenu_StepRow4Request runs without any mask.
- I: the row count: the list's eleventh word (20) is also the first word of node 19's row list at 0x14078939C; the words after it (0, 1, 200, -1, -1, then the bytes of a code pointer) belong to node 19's list and to the range record at 0x1407893A0. If those positions were rows, 0 and 1 would open nodes 0 and 1, and 200 would index past the 21 nodes (garbage).

## Open questions

None recorded.
