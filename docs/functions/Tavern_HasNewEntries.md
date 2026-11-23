# Tavern_HasNewEntries

- **Address:** `0x140344B68`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool Tavern_HasNewEntries(...)`
- **Callers:** WorldMap_ScreenInput, sub_1402D50E4, sub_140345FE4
- **Callees:** TavernRumour_IsAvailable, sub_1401DF5B4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

I: tells whether the tavern has an entry still marked new (rumours and errands), for the marker of the town menu.

## Behavior

- V: one loop walks rumour ids 0..63 and, for each, the towns 0..42, calling TavernRumour_IsAvailable(id, town); an available id whose new flag (low-byte guard as in TavernRumours_BuildList) differs from r12b (0) makes it return.
- V: a second loop walks rumour ids 0..63 for the current town and tests the same flag the same way.
- V: two further loops read the errand new flags (g_ErrandNewFlags) the same way.

## State touched

- Calls: [TavernRumour_IsAvailable](TavernRumour_IsAvailable.md)

## Referenced by

- Called by: [WorldMap_ScreenInput](WorldMap_ScreenInput.md)
- Observed behaviours: [RumourNewFlagsAreIndexedByTheLowByteOfTheId](../behaviors/RumourNewFlagsAreIndexedByTheLowByteOfTheId.md), [ScreenMusicComesFromBGMTransitionRows](../behaviors/ScreenMusicComesFromBGMTransitionRows.md)

## Notes

Only the rumour loops were read in full.

## Open questions

? the meaning of sub_1401DF5B4(town) in the first loop (a town test before the availability call).
