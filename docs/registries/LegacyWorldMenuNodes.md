# LegacyWorldMenuNodes

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [LegacyWorldMenu_OpenNode](../functions/LegacyWorldMenu_OpenNode.md), [LegacyMenu_ConfirmRow](../functions/LegacyMenu_ConfirmRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The node tree of the old world menu: four tables of 21 node records of 88 bytes, one per text language (tbl_LegacyWorldMenuStateLang0 0x14080CAB0, Lang1 0x14080D1F0, Lang3 0x14080D930, Lang2 0x14080E070). The id is the node number; the value is the task the node runs. Only nodes whose task was read are named here.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="legacymenu_buildlocationlist"></a>2 | `LegacyMenu_BuildLocationList` | `rows: list at 0x140789618` | V | Task of node 2 (also used by node 6). |
| <a id="legacyworldmenu_mainmenutask"></a>3 | `LegacyWorldMenu_MainMenuTask` | `rows: list at 0x140789378 (eight words 0x100D = node 13)` | V | Task of node 3; the same task as node 4. |
| <a id="legacyworldmenu_mainmenutask"></a>4 | `LegacyWorldMenu_MainMenuTask` | `rows: list at 0x140789388; text 0xA010` | V | The old main world menu (LegacyWorldMainMenuRows). |
| <a id="legacymenu_buildlocationlist"></a>6 | `LegacyMenu_BuildLocationList` | `rows: list at 0x140789378 (eight words 0x100D = node 13)` | V | The old location list; row 0 of node 4. WorldMap_OpenLocationsList opens it. |
| <a id="legacyworldmenu_requestroster"></a>7 | `LegacyWorldMenu_RequestRoster` | `row list of node 4` | V | Roster request (word 0x143749F28). |
| <a id="legacyworldmenu_starttestbattle"></a>8 | `LegacyWorldMenu_StartTestBattle` | `row list of node 4` | V | Test battle start; also the function of node 16's range record. |
| <a id="battlecommand_buildscreen"></a>9 | `BattleCommand_BuildScreen` | `rows: list at 0x1407893E0` | V | The generic event-side list task. |
| <a id="legacymenu_loadrowlist"></a>10 | `LegacyMenu_LoadRowList` | `rows: list at 0x1407893B0` | V | Loads a row list and runs the list task. |
| <a id="legacymenu_picklocation"></a>13 | `LegacyMenu_PickLocation` | `row list of node 4` | V | Confirms a location of the old location list. |
| <a id="legacyworldmenu_requesteventvareditor"></a>15 | `LegacyWorldMenu_RequestEventVarEditor` | `row list of node 4` | V | Event variable editor request (word 0x143749F38). |
| <a id="legacymenu_numberentrytask"></a>16 | `LegacyMenu_NumberEntryTask` | `range record 0x1407893A0 (1..200); number word 0x140789374; rows [-2, -1]` | V | Number entry for the test battle map. |
| <a id="legacyworldmenu_requestpartyloader"></a>17 | `LegacyWorldMenu_RequestPartyLoader` | `row list of node 4; range record 0x1407893A0` | V | Party loader request (word 0x143749F3C). |
| <a id="eventmenu_nodelisttask"></a>20 | `EventMenu_NodeListTask` | `row word -1; text 0x5012; saved row 1` | V | A small titled window whose every row closes one level. |

## Behavior

- V: record layout read in the code: +48 task entry (EventTask_Start), +40 next-node word (-15..-1 for every row) or a pointer to a list of 16-bit next-node words per row (LegacyMenu_ConfirmRow), +64 a range record pointer and +72 a value word pointer (number entry nodes, LegacyMenu_NumberEntryTask), +80 the saved row word (LegacyWorldMenu_MainMenuTask, EventMenu_NodeListTask).
- V: the low word of +28 is passed as the title text id to the title drawer (EventMenu_NodeListTask).
- I: the words +0..+23 are the window rectangles (source position, screen offset, size); LegacyWorldMenu_OpenNode adjusts +8..+14.
- V: a next-node word with bit 0x1000 loses that bit first (the change sticks); then a negative word closes that many levels, a word of 256 or more starts nothing (1234 marks the row -1), and any other value is a node number of the same table. Example: the row list of nodes 3 and 6 at 0x140789378 holds eight words 0x100D, each of which starts node 13.
- V: the four tables hold the same task pointers and row lists; the rectangles of some nodes differ by language.
- V: the record after node 20 (+21 * 88) is other data, not a node.

## Notes

Other nodes run tasks with no name yet: 0 and 1 sub_1402B34D0, 5 sub_1402B3B90, 11 sub_1402B3DE4 (request word 0x143749F34), 12 sub_1402B3BF0 (word 0x143749F30), 14 sub_1402B3C54 (word 0x143749F2C), 18 sub_1402B3F20, 19 sub_1402E8E54.

## Open questions

None recorded.
