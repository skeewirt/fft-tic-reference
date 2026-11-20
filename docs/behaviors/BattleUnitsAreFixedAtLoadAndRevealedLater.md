# BattleUnitsAreFixedAtLoadAndRevealedLater

- **Kind:** observed behaviour
- **Scope:** engine (battle unit records over a battle)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md), [BattleUnit_RevealOnField](../functions/BattleUnit_RevealOnField.md), [ScenePreview_ShowEntry](../functions/ScenePreview_ShowEntry.md), [ScenePreview_ClaimForUnit](../functions/ScenePreview_ClaimForUnit.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle's unit records are set at load (the 16 entries) and at deployment (the party); afterwards event scripts only reveal records that are off the field and take units off, so the most units a battle can show is bounded by its entry list plus the party. Each entry's presence bits say how it starts.

## Behavior

- V: presence (entry byte +24 & 0xC0, applied by Battle_PlaceEntryUnits): 0x80 placed; 0x40 placed or not by one random bit; 0x00 built but left off the field (parked: no look queued); 0xC0 built and its look queued but not placed and not counted (drawn, not on the field). An OverrideEntryData row's Present column replaces the bits unless it is 255.
- V: the exact load order per entry (Battle_PlaceEntryUnits): an empty entry (byte 0 = 0) gets slot 0xFF and on-field 0xFF; otherwise the record is built; a parked entry (0x00, or 0x40 losing its random bit) gets slot 0xFF and on-field 0 and is checked against nothing; a placed (0x80, 0x40 winning) or hidden (0xC0) entry is checked in order: Unit_CheckSpawnTile (fail: slot 0xFF, on-field 0xFF), then the sprite budget EntryUnits_CheckLookBudget(9 - variable 57) (fail: slot 0xFF, on-field 0 = parked), then a hidden entry has its look queued without being counted, and a placed entry is kept and its look queued only while the kept count is below 16 - variable 57 (else slot 0xFF, on-field 0xFF).
- V: so the sprite budget counts placed and hidden entries, the unit budget counts placed entries only, and parked entries are counted by neither; an entry the sprite budget refuses becomes parked (on-field 0), which BattleUnit_RevealOnField accepts, so a script can later bring it in.
- V: BattleUnit_RevealOnField is the only code found that puts an existing off-field record on the field; ScenePreview_ShowEntry also queues the look of a parked record (a new scene unit), ScenePreview_ClaimForUnit takes a drawn but unplaced one.
- V (seen live, random battle at Mandalia Plain, entry key 165): the 9 entries are entry 0 placed (0x80) and entries 1..8 random (0x40), in pairs that share a tile; 3 stood on the field (records 0, 1, 7), records 2..6 were built and left off (no scene unit), and record 8 was dropped (+0x1B5 = 0xFF). Only the 3 placed records had scene units (3 of 16), and the look pool held 2 records.
- I: record 8 was dropped because record 7, its pair, had taken the tile (Unit_CheckSpawnTile refuses a tile held by a lower record); not traced.
- M: key 432 (events 284..287) places entries 0..4, parks 5..8 (0x00) and builds 9..11 drawn but unplaced (0xC0); its override rows keep those bits (Present 255).
- ?: which event commands reveal which entries in each battle, and when (the event files hold more blocks than the main script; their layout is not decoded).

## Open questions

? the event file layout beyond the main script; ? the opcode that owns the take-off case at 0x14023BFA0.
