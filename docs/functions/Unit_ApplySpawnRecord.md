# Unit_ApplySpawnRecord

- **Address:** `0x14027612C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Unit_ApplySpawnRecord(uint8_t *work, const uint8_t *entry, ...)`
- **Callers:** Unit_BuildFromRecord
- **Callees:** UnitWork_BuildFromGuestOrPartyRecord (sub_1402766C8), Skillset_GetAbility, sub_1401E8C9C, SceneVar_Read, sub_140279328

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies a 40-byte spawn entry to a unit work record before the job and stat build: copies the side and presence byte, picks the save-record path for party and guest units, and sets level, birthday, Brave and Faith with their random rules.

## Behavior

- V: work +4 = entry +23; work +5 and work +494 = entry +24 (the whole byte is copied; the side bits 0x30 and presence bits 0xC0 are read from it by other functions).
- V: entry +1 bit 3 set: UnitWork_BuildFromGuestOrPartyRecord builds the unit from a guest save record; if that fails and event variable 508 is 0 the function returns -1 (Unit_BuildFromRecord then returns -1: no unit). With variable 508 set it falls through to the entry path.
- V: without bit 3, an entry whose marker (entry +0) is 1..3 and whose entry +4 is 0 updates the first party save record whose marker is 0..3 (the marker, the job byte for the reset jobs, the three special ability bits of the old and the new job's skillsets through Skillset_GetAbility 151 / 153 / 154 and sub_1401E8C9C), then builds from it with UnitWork_BuildFromGuestOrPartyRecord.
- V: copies 7 bytes of g_CurrentSpawnEntry (entry +33..+39) to work +407..+413.
- V: marker 0x80 / 0x81 / 0x82 force work +6 bits 0xE0 to 0x80 / 0x40 / 0x20 (values reached by shifts of the marker, not as immediates), keeping the low 5 bits of entry +1.
- V: work +6 = entry +1 (adjusted), work +0 = entry +0, work +2 = 0xFF (no save record).
- V: level (work +41) from entry +3: 0 or 0xFE (tested as (value + 2) & 0xFD == 0) = random from H - H/8 to H, where H is the highest save-record level capped at 99 (the byte at 0x140D405AB, set by Battle_PlaceEntryUnits); 100..253 = value - 100 + H; the result is clamped to 1..99.
- V: birthday from entry +4 (month 1..12) and +5 (day 1..31), otherwise a random day of 365; sub_140279328 turns it into the zodiac nibble of work word +8; job 0x97 (entry +10) forces zodiac 0xC.
- V: Brave: work +43 and +42 = entry +6, a value above 100 replaced by 45 + Rng(30). Faith: work +45 and +44 = entry +7, same rule.
- V: work +40 = entry +28 (above 99 = Rng(100)); work dword +508 = entry +2 (the name byte, replaced later by UnitWork_SetNameKey when the OverrideEntryData row names a key).

## State touched

- Calls: [UnitWork_BuildFromGuestOrPartyRecord](UnitWork_BuildFromGuestOrPartyRecord.md), [Skillset_GetAbility](Skillset_GetAbility.md), [SceneVar_Read](SceneVar_Read.md)
- Reads: [g_CurrentSpawnEntry](../globals/g_CurrentSpawnEntry.md), [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Referenced by

- Called by: [Unit_BuildFromRecord](Unit_BuildFromRecord.md)

## Notes

Reads entry +0..+7, +10, +23, +24, +28, +33..+39, the party save records and the byte at 0x140D405AB; writes work +0, +2, +4..+6, +8, +40..+45, +407..+413, +494, +508.

## Open questions

? what the special-ability bit copy of the party-record path is for (the three skillset abilities 151 / 153 / 154 were not identified).
