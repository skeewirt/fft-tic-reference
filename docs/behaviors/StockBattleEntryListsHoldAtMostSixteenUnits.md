# StockBattleEntryListsHoldAtMostSixteenUnits

- **Kind:** observed behaviour
- **Scope:** engine data (battle unit counts)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md), [Battle_GetEntryBlock](../functions/Battle_GetEntryBlock.md), [Deployment_SelectArea](../functions/Deployment_SelectArea.md), [OverrideEntry_FillUnitEntry](../functions/OverrideEntry_FillUnitEntry.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Counted over the stock data, a battle's entry list (not the units on the field) holds at most 12 units in battles the commence check lets start, 12 plus a deployment of 5 making 17 listed; an entry's presence bits decide which of them start on the field (key 432: 5 of its 12). Random formations list up to 16 entry units, but the entry budget keeps at most 16 minus scene variable 57 of them.

## Behavior

- M: the 713 scenario setup records (691 with an entry key) were read with their entry blocks (16 entries of 40 bytes from game files 224..227 and 892) and their deployment areas' count bytes; an entry counts when its byte 0 is not 0 (the test of Battle_PlaceEntryUnits).
- M: of the 472 records with a deployment area, the entry count is at most 13 (13 entries on 8 records, 12 on 13) and entries + capacity at most 17 for records with a capacity of 5 (events 284..287: 12 + 5); events 684..686 and 734..738 reach 19 (13 + a capacity of 6, which the commence check refuses).
- M: records with no deployment area list up to 16 entries (key 387 on events 3..6 and 586..589, key 308 on events 326..327 with 15).
- M: of the entry keys 1..228 that no scenario record names (I: the random-battle formations), 220 hold units: 20 list 16 entries and 10 list 15.
- V: an OverrideEntryData row clears an entry when its byte +0x8D is set, and otherwise can also fill an empty one: a non-zero row +0x08 is written to entry byte 0 (the marker), +0x10 to the job, +0x48 (unless 255) to the presence bits. M: in the stock data only key 311 (events 330 and 331) fills an empty entry this way (entry 4). This corrects an earlier reading that a row can only clear an entry.
- M: key 432 (events 284..287, the 12-entry two-area battle): presence bits (entry byte +24 & 0xC0) are 0x80 'placed' on entries 0..4, 0x00 'off the field' on 5..8 and 0xC0 'built, not placed' on 9..11, so 5 of its 12 units start on the field.
- M (all 554 scenario records the commence check lets start, overrides applied, at most one unit per tile and layer since Unit_CheckSpawnTile refuses a taken tile, sprites as Unit_ResolvePreviewShape gives them): at the start no battle draws more than 16 units (its placed, random and hidden entries plus its deployment count) and no battle's start looks plus its deployment count exceed 10 (at most 8 looks of its own).
- M: counting every parked unit as brought in, three battles could pass a limit: key 432 (17 drawn), key 387 (13 looks over all its entries) and key 426 (7 looks + 5); the scripts settle them: key 432's events remove the 5 party units and 4 entries (event 285, opcode 0x3D) before bringing units in (event 287), peak 13 drawn; key 426's three parked entries are never brought in by a script; key 387 (Orbonne Monastery) brings in one parked unit in event 4 (10 looks, seen live) and two more in event 6, after the battle.
- V (seen live, Orbonne Monastery from a New Game, pool records 10 and 11 watched): no write to either record through the battle and its closing scene; the battle's drawn units are released when it ends (SceneUnits_ReleaseAll), before event 6 loads its looks.
- V: a battle's units move on and off the field during it only through opcode 0x45 (bring a parked unit in, or release one), opcode 0x44 (a hidden actor onto the field) and opcode 0x3D (remove); scripts are the main instruction stream of each event file, which ends at its first 0xDB (jumps only go forward to a marker before it or back to an earlier one).

## Open questions

? the battle-time trigger rows (EnhancedBattleEvent) and which event each starts (not needed for the unit bounds: the scripts of every event of a battle were counted in event order).
