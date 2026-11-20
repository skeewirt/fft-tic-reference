# RecordBytesTheGameNeverReads

- **Kind:** observed behaviour
- **Scope:** engine (fixed tables in the executable)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [ScenarioSetupRow](../structs/ScenarioSetupRow.md), [ItemRecord](../structs/ItemRecord.md), [ItemWeaponRecord](../structs/ItemWeaponRecord.md), [AbilityActionRow](../structs/AbilityActionRow.md), [StatusPropertyRow](../structs/StatusPropertyRow.md), [ErrandRecordRow](../structs/ErrandRecordRow.md), [MoveFindRow](../structs/MoveFindRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Bytes and bits of several fixed tables that no function of the game reads, found by listing every code reference to each table, so the stored values decide nothing.

## Behavior

- V: scenario setup record byte +21: read by neither ScenarioSetup_ApplyRecord nor Scenario_CheckBattleRecord, and no other code refers to the record block. 0 on all 713 used stock rows.
- V: item record bytes +4, +6 and +11: no read over the 79 callers of Item_GetRecord (instruction level with operand sizes, and pseudocode level); the pointer is never stored or passed on.
- V: weapon record byte +3: the eight bytes are copied to the current-action weapon record, which is referenced at +0, +1, +2, +4 and +6 only; sub_14030D740 saves and restores the block as a whole.
- V: ability action record bytes +14..+19: the working copy is read at +0..+9, +11, +12 and +13 (33 callers of AbilityAction_GetRecord and 19 of the aux accessor's third out pointer); the 20-byte current-action copy is referenced at +0, +3, +5, +6, +7, +9 and +10, and +12..+19 only inside the 16-byte block save and restore and one dword clear of +16 (Battle_ResolveAction).
- V: status property rows +0 and +1: every reference to the table reads +2 (priority), +3, +4, +5 or +6..+15.
- V: errand record words 3, 13, 14, 15, 18 and 20: over every caller of Errand_LoadRecord (the shared record and the three functions that load into their own buffer) only words 0, 1, 2, 4..12, 16, 17, 19, 21 and 22 are read.
- V: Move-Find row flag bit 0x40 of each tile: MoveFind_ProbeTile, the only reader of the loaded row, tests 0x80, 0x20, 0x10 and 0x0F.
- I: absence of a reader in the code is what is established; a use through data the census could not follow (a table pointer computed at run time) is not excluded.

## Open questions

None recorded.
