# Recruit_GenerateUnit

- **Address:** `0x140275310`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Recruit_GenerateUnit(uint8_t *save, unsigned int kind)`
- **Callers:** sub_14027528C (one new recruit, called by GameState_ResetParty and Party_EggUpkeep), Guild_MakeCandidates (the Warriors' Guild's 15 recruit candidates)
- **Callees:** Unit_RollStartingStats, sub_140279328, sub_140279508

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills a fresh save record with a newly generated unit: identity marker, starting job, birth sign, Brave and Faith, stat accumulators, equipment and sprite palette.

## Behavior

- V: `kind` 0 = male generic (marker 0x80, job 74, flag byte +4 = 0x80), 1 = female generic (marker 0x81, flag 0x40), 3 = marker 0x82 with flag 0x20, job 74; any other value becomes 2 = a story unit (marker 1, job 1, flag 0x80).
- V: the starting job is always 74 (Squire) for kinds 0, 1 and 3; it is written before the stats and is not read by the roll.
- V: level byte +29 is 1 (the word at +28 is set to 256); Brave +30 and Faith +31 are each 40 + (31 * rand15 >> 15), so 40 to 70; kind 2 sets both to 70.
- V: birth sign byte +5 is 1 + (365 * rand15 >> 15), then the zodiac sign byte +6 comes from sub_140279328.
- V: Unit_RollStartingStats(accumulators at +32, +35, +38, +41, +44; kind) rolls HP, MP, SP, PA, MA; the row is the kind, so the roll depends on gender and not on the job.
- V: the equipment words at +14..+27 are seven 16-bit words copied from bytes 5..11 of the kind's 12-byte start row: kinds 0 and 1 = 157, 186, 255, 19, 255, 255, 255; kind 2 = 157, 186, 208, 19, 255, 255, 255; kind 3 = all 255 (255 means empty).
- V: when the flag byte +4 has bit 6 or 7 set (kinds 0, 1 and 2), each of the 20 generic jobs gets the same random 100..199 as current JP (word at +128 + 2i) and total JP (word at +174 + 2i), and the level byte +116 + i/2 is set to 0x11 (level 1 for both nibbles); the Bard slot (i = 17) is skipped for flag 0x40 and the Dancer slot (i = 18) for flag 0x80, and the bytes +124 / +125 are then set to 0x10 / 0x01, so a female unit has no Bard level and a male unit no Dancer level.
- I: the dword at +560 is a name id: a base of 256 (male), 512 (female) or 768 (kind 3), 0 for the story kind, plus a random 0..255, redrawn until no live save record with the same marker holds it.
- V: returns the result of sub_140279508 on the record.

## State touched

- Calls: [Unit_RollStartingStats](Unit_RollStartingStats.md)

## Referenced by

- Observed behaviours: [WarriorsGuildCandidatesAreMadeEachVisit](../behaviors/WarriorsGuildCandidatesAreMadeEachVisit.md)
- Resolves registries: [NewUnitStartRows](../registries/NewUnitStartRows.md), [UnitIdentityIds](../registries/UnitIdentityIds.md)

## Notes

Guild_MakeCandidates draws the kind of each candidate from one random bit (0 or 1) and forces the other kind once 8 of one kind are made (V: at most 8 of either sex among the 15). The displayed level-1 stats of a male or female Squire follow from the roll and the Squire row (M = 100, 75, 100, 90, 80): male HP 30 or 31, MP 10 or 11, SP 6, PA 4, MA 3; female HP 28 or 29, MP 11, SP 6, PA 3, MA 4 (computed from the formula in Unit_ComputeStats, not read from a running game).

## Open questions

? the item names of ids 157, 186, 208 and 19 were not looked up.
