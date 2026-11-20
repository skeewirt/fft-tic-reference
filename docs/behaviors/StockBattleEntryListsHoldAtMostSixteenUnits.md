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
- V: an OverrideEntryData row can only clear an entry (row byte +0x8D clears entry byte 0), never fill an empty one, so these counts are upper bounds; the entry budget (EntryUnitsShareADistinctLookBudget) and event actors that start off the field lower them further.
- M: key 432 (events 284..287, the 12-entry two-area battle): presence bits (entry byte +24 & 0xC0) are 0x80 'placed' on entries 0..4, 0x00 'off the field' on 5..8 and 0xC0 'built, not placed' on 9..11, so 5 of its 12 units start on the field.
- ?: units that event scripts add after the start (Battle_JoinUnitAndLoad from event commands) are not counted here.

## Open questions

? the largest number of units on the field at once in any stock battle, once event joins and departures are counted.
