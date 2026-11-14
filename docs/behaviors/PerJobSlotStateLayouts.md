# PerJobSlotStateLayouts

- **Kind:** observed behaviour
- **Scope:** engine (party, battle and save unit records)
- **Area:** [Unit data](../areas/unit-data.md)
- **Affects:** [Job_IdToIndex](../functions/Job_IdToIndex.md), [Unit_CollectJobSkillsets](../functions/Unit_CollectJobSkillsets.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per-job state (learned flags, level nibbles, JP, total JP) sits in several unit layouts at different offsets, indexed by the job slot that Job_IdToIndex returns.

## Behavior

- I (the offsets and counts are not re-read by us): the save record (0x258 bytes) keeps learned flags at +0x32 (3 bytes a slot), level nibbles at +0x74, JP words at +0x80 and total JP words at +0xAE, with 23 slots (0 to 22) in each array; the party-menu copy (0x280 bytes) keeps learned flags at +0x7B + 3 * slot, level nibbles at +0xBD, JP words at +0xCA and total JP words at +0xF8; a battle unit (0x200 bytes at 0x141853CE0) keeps learned flags at +0xA2 = (slot + 0x36) * 3, level nibbles at +0xE4, JP words at +0xF0 and total JP words at +0x11E.
- I: the job level thresholds come from the 'generaljob' NXD table (rows 0 to 19, nine thresholds each: 0, 100, 200, 400, 700, 1100, 1600, 2200, 3000); slots 20 and above have no row, so JobLevelJp read garbage for them.
- I: slots 20 and 21 are the hidden Dark Knight and Onion Knight (jobs 160 and 161) and are not always empty in a stock save.
- V (live 2026-11-13, a party unit on slot 49, world map): the save-record offsets +0x74 / +0x80 / +0xAE and the party-menu copy's +0xBD / +0xCA / +0xF8 hold (current JP words identical in both); the party copies sit behind the pointer table at 0x141800F50 (the unit's save slot at copy +44; two copies for one unit). Writing only the level nibbles (8) in both does not last: on the unit's next menu screen the party copy's nibbles were back to the levels its total JP gives. With the total JP words at 3000 (the Lv. 8 threshold) in the save record and both copies, the Change Job grid and the Job Tree showed Lv. 8 after the unit's Status was opened again (not while the screens stayed open).

## Open questions

None recorded.
