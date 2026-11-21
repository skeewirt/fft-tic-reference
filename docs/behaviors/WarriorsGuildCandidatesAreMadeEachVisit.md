# WarriorsGuildCandidatesAreMadeEachVisit

- **Kind:** observed behaviour
- **Scope:** engine (Warriors' Guild recruit list)
- **Area:** [Unit data](../areas/unit-data.md)
- **Affects:** [Recruit_GenerateUnit](../functions/Recruit_GenerateUnit.md), [UnitWork_BuildFromSave](../functions/UnitWork_BuildFromSave.md), [PartyUnit_FillFromWork](../functions/PartyUnit_FillFromWork.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Warriors' Guild's recruit list is 15 candidate records of 564 bytes at 0x1408E6CB0 (the first 564 bytes of a save record's layout), made by Guild_MakeCandidates each time the guild is opened and never saved; hiring one copies it into the save record its display record names, then Guild_RemoveHired moves it to the end of the list.

## Behavior

- V: Guild_MakeCandidates (sub_1402EFBE0) returns at once when no save record is free; otherwise for candidates 0..14 it writes +1 = the first free save record, +3 = 0, calls Recruit_GenerateUnit(candidate, kind) with kind 0 (male) or 1 (female) from one random bit, at most 8 of either kind, clears +7..+13 and calls PartyUnit_BuildFromRecord(candidate, index).
- V: around each Recruit_GenerateUnit call it swaps qword_14184A8E0 with qword_14184A8E8; sub_1402B52E4 fills the buffer that qword points to with every party unit's name bytes (save record +220, 16 bytes each), so the swap gives the candidates a list of their own.
- V: PartyUnit_BuildFromRecord (sub_14028B7D0) builds a unit work from the record (UnitWork_BuildFromSave, slot = record +1), fills g_PartyUnitRecords[640 x index] from it (PartyUnit_FillFromWork), stores the index at its +10 and points g_PartyUnits[index] at it; the guild list and the candidate page draw from these records.
- V: the gate byte 0x142FEC54A is cleared when the guild is opened (sub_1402EECA8, and sub_1402EEC78 on the first opening) and by state 13 of the guild screen (sub_1402EEE30); state 0x2B makes the list only while it is 0, then sets it to 1.
- V: hiring (state 0x18 of sub_1402EEE30) pays the fee, copies the 564 bytes of candidate g_SelectedUnitIndex into the save record whose number is the i16 at +44 of g_PartyUnits[g_SelectedUnitIndex], then calls Guild_RemoveHired.
- V: Guild_RemoveHired (sub_1402EFD00) sets +1 of the hired candidate to 0xFF, gives every other candidate +1 = the next free save record and +292 = the hired record's +292 plus 1, and swaps each later candidate with the one before it, so the hired record ends last and the later ones move down by one.

## Notes

Names are ours: Guild_MakeCandidates = sub_1402EFBE0, Guild_RemoveHired = sub_1402EFD00, PartyUnit_BuildFromRecord = sub_14028B7D0.

## Open questions

? what the guild screen's state 13 is; ? whether +292 is the unit's join order.
