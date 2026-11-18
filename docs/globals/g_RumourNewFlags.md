# g_RumourNewFlags

- **Kind:** global
- **Address:** `0x1411A7299`
- **Type:** `event system`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint8[64][2]: per rumour id, {new, new arrival}; set to {1, 1} by the new-game reset (sub_14033FB84), cleared by TavernMenu_OnCommand when a rumour is read, tested by TavernRumours_BuildList and Tavern_HasNewEntries. Part of the menu-new block at 0x1411A7280 (+25) that the save stores as bar.uwasa.menu_new[64].

## Referenced by

- Observed behaviours: [RumourNewFlagsAreIndexedByTheLowByteOfTheId](../behaviors/RumourNewFlagsAreIndexedByTheLowByteOfTheId.md)

## Open questions

None recorded.
