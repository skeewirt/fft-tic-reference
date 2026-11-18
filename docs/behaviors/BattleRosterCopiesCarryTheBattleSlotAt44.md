# BattleRosterCopiesCarryTheBattleSlotAt44

- **Kind:** observed behaviour
- **Scope:** engine (battle party records)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [PartyUnit_FillFromWorkRecord](../functions/PartyUnit_FillFromWorkRecord.md), [UnitWork_BuildForSlot](../functions/UnitWork_BuildForSlot.md), [JobScreen_RefreshAfterChange](../functions/JobScreen_RefreshAfterChange.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

In battle the party records are copies of battle unit records: PartyUnit_FillFromWorkRecord fills the battle roster records from the battle unit table, writing the unit's battle slot at +44 and its save slot at +0x1E, and UnitWork_BuildForSlot (battle modes 101 and 104) copies the roster into the party records with one memmove, so there +44 is a battle slot, not the save slot it names outside battle.

## Behavior

- V (disassembly): PartyUnit_FillFromWorkRecord stores work +2 at +0x1E, work +1 at +0x22 and again at +0x2C (44), and the work record's job byte (+3) as the job word (+0x24).
- V (decompiled): UnitWork_BuildForSlot in modes 101 / 104 calls the roster builder (sub_140360780, which fills one 640-byte record per standing unit from the battle unit table) and copies the records whole into the party record array, then points the party pointer table at them.
- V (seen live 2026-11-17, a resumed battle): party record 8 held +44 = 16 and +0x1E = 0 for the unit of battle slot 16 whose save slot is 0; save slot 16 was empty.
- V (seen live): the battle Status screen and its header are built from these copies (JobScreen_RefreshAfterChange copies the selected one into the preview record).

## Open questions

None recorded.
