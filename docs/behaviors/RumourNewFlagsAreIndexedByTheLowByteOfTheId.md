# RumourNewFlagsAreIndexedByTheLowByteOfTheId

- **Kind:** observed behaviour
- **Scope:** engine (tavern rumours)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [TavernRumours_BuildList](../functions/TavernRumours_BuildList.md), [Tavern_HasNewEntries](../functions/Tavern_HasNewEntries.md), [TavernMenu_OnCommand](../functions/TavernMenu_OnCommand.md), [g_RumourNewFlags](../globals/g_RumourNewFlags.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every reader and the writer of the rumour new flags guards the index with a test of the LOW BYTE of the id (taken as a signed byte, it must be 0..63, and that byte is the index), so an id whose low byte is 0..63 indexes the 64 pairs whatever its upper bits are.

## Behavior

- V: four places address the pairs: the builder's read (0x14036EED3), two reads in Tavern_HasNewEntries (0x140345270, 0x1403453FA), the clear in TavernMenu_OnCommand (0x14019D76A, through the base 0x1411A7280 + 0x19); and the reset loop of sub_14033FB84 (64 pairs set to {1, 1}).
- V: the save stores the pairs by its field schema from the fixed block at 0x1411A7280 (bar.uwasa.menu_new[64] at +25), not through these instructions.
- V (seen live): moving the cursor onto a rumour in the list clears its new flag.

## Open questions

None recorded.
