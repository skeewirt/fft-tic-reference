# UnitEventFlagWord

- **Kind:** observed behaviour
- **Scope:** engine (battle unit table)
- **Area:** [Unit data](../areas/unit-data.md)
- **Affects:** [OverrideEntry_FillUnitEntry](../functions/OverrideEntry_FillUnitEntry.md), [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md), [Battle_TurnEngine](../functions/Battle_TurnEngine.md), [BattleObjective_ShowsTarget](../functions/BattleObjective_ShowsTarget.md), [EventPreviewUnits_RunFrames](../functions/EventPreviewUnits_RunFrames.md), [sub_14036099C](../functions/sub_14036099C.md), [sub_1401EA2F0](../functions/sub_1401EA2F0.md), [sub_1401EE9B4](../functions/sub_1401EE9B4.md), [sub_1401F5AFC](../functions/sub_1401F5AFC.md), [sub_14013F71C](../functions/sub_14013F71C.md), [sub_140214404](../functions/sub_140214404.md), [sub_140214610](../functions/sub_140214610.md), [UnitWorkRecord](../structs/UnitWorkRecord.md), [UnitEventFlagBit](../registries/UnitEventFlagBit.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle unit's dword +504 holds one bit per OverrideEntryData flag byte (bits 0..10) and bit 11 from the equipment build. Each bit switches a presentation or ordering rule; the one-line meaning of each bit is in the registry UnitEventFlagBit.

## Behavior

- V: OverrideEntry_FillUnitEntry sets bit n for each non-zero flag byte +0x8E .. +0x97 (bits 0..9) and +0x99 (bit 10); Battle_PlaceEntryUnits stores the word at unit +504.
- V: bits 5, 6 and 7 are one-shot: the preview-units event opcode runs the announcement and clears the bit it just used, so the announcement plays once per unit.
- V: bit 10 is one-shot too: Battle_TurnEngine clears it when it gives the unit the first turn.
- V: bit 0 changes the side category (sub_14036099C returns 3 for it unless the unit's side bits are 0x10) and is read by the turn panel and the tile marker code; the exact panel and marker calls are listed in the registry.
- I: the three target bits (2, 3, 4) all add a stop to the objective camera tour, but only bit 2 depends on the BattleObjective row's show_targets column.

## Open questions

? the role of bits 1, 8 and 9.
