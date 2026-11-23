# TavernRumours_BuildList

- **Address:** `0x14036EE50`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void TavernRumours_BuildList(void)`
- **Callers:** the tavern screen's task (through the task table)
- **Callees:** TavernRumour_IsAvailable, UITable_GetRowByKey, sub_14019DCD4, sub_1402D541C, Input_ActionBit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the tavern's Rumors list: walks rumour ids 0..63, keeps the ones the current town may show, and pushes each into the list widget with its new marker.

## Behavior

- V: the loop runs over ids 0..63 (an unsigned compare of the counter with 64) and calls TavernRumour_IsAvailable(id, current town) for each id; the current town is the dword at 0x140D493E8.
- V: for an available id it stores the word id - 14336 into the shared list of the tavern pages (g_ErrandBoardList) at the next position, with a range check of the byte offset, and 0 into g_PageListFlags.
- V: it pushes a 16-byte entry into the list widget's vector (the widget at [[[0x143CD9DA8]+16]+328]+112, vector at +992): the id as a dword at +0, the Gossip row's fields +4 and +8 at +4 and +8, the new marker at +12, 1 at +13.
- V: the new marker is the first byte of the id's pair in g_RumourNewFlags, read only when the low byte of the id, taken as a signed byte, is 0..63 (the test looks at the low byte, not the whole id); otherwise the marker is the value held in the low byte of rbp.
- V: when the Gossip row's field +4 is nonzero, byte +13 of the entry is set to whether the progress value of that situation is below the row's field +8 (a quest rumour not yet taken).
- V (seen live, Gariland): the list showed The Corpse Brigade, King Ondoria III and The Fifty Years' War with their blue new markers, and the markers cleared as the cursor passed over each entry.

## State touched

- Calls: [TavernRumour_IsAvailable](TavernRumour_IsAvailable.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Called by: [Tavern_RumorTextWait](Tavern_RumorTextWait.md)
- Observed behaviours: [RumourNewFlagsAreIndexedByTheLowByteOfTheId](../behaviors/RumourNewFlagsAreIndexedByTheLowByteOfTheId.md), [TavernRumoursListGossipRowsByIdTownMaskAndUnlockVariable](../behaviors/TavernRumoursListGossipRowsByIdTownMaskAndUnlockVariable.md)

## Notes

The text, title and icon of an entry come from the nxd Gossip row whose key is the id (table 181), read by the widget when it draws.

## Open questions

? what sub_14019DCD4(widget, 2) does to the list (sort or redraw).
