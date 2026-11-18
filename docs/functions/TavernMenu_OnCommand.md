# TavernMenu_OnCommand

- **Address:** `0x14019D548`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void TavernMenu_OnCommand(void *menu, void *source, int command, unsigned int id, unsigned int value)`
- **Callers:** the tavern UI add-on (UIAddonFFTOBarGossipMain and the errand page)
- **Callees:** UITable_GetRowByKey, UserSituation_SetValue, EventVar_Write, UIGuide_Show

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

I: the tavern screens' command handler: marks a rumour or an errand as read, takes a quest rumour, and forwards the other commands of the tavern pages.

## Behavior

- V: command 0 from the rumour page: writes 0 to the new flag of rumour `id` (0x1411A7280 + 25 + 2 * id), guarded by a test of the low byte of the id (0..63).
- V: command 0 from the errand page: writes 0 to the errand new flag (0x1411A7280 + 153 + 2 * id) when the low byte of the id is below 0x60.
- V: command 1: when the Gossip row of `id` has a situation (+4) whose progress is below the row's +8, sets that progress and writes the event variables listed by the row's two arrays (+20 variables, +28 values; a variable of 102 multiplies the next value by 10).
- V (seen live): moving the cursor onto a rumour clears its new marker.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [UserSituation_SetValue](UserSituation_SetValue.md), [EventVar_Write](EventVar_Write.md), [UIGuide_Show](UIGuide_Show.md)

## Referenced by

- Observed behaviours: [RumourNewFlagsAreIndexedByTheLowByteOfTheId](../behaviors/RumourNewFlagsAreIndexedByTheLowByteOfTheId.md)

## Notes

Rows 20 and 21 of Gossip (The Haunted Mine, The Cursed Isle of Nelveska) are the stock quest rumours (situations 2 / values 20 and 90).

## Open questions

? the commands 2..8 and 50..53.
