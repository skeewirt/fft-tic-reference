# Unit_ComputeStats

- **Address:** `0x140276EBC`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void Unit_ComputeStats(uint8_t *work, int flags, void *extra)`
- **Callers:** UnitWork_BuildFromSave, sub_140275CA4, sub_140275EF4, Unit_ApplyEquipment
- **Callees:** none (all arithmetic is inline)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns a work record's five 24-bit stat accumulators and the job row's growth pairs into the unit's displayed HP, MP, Speed, PA and MA. Called whenever a work record is built or refreshed.

## Behavior

- V: `work` is the work record (C). The accumulators are 3 bytes each at +123, +126, +129, +132, +135 (order HP, MP, SP, PA, MA); the growth pair for stat i is the C byte at +138+2i and the M byte at +139+2i, copied there from the job row by UnitWork_ApplyJobRow.
- V: each stat is ((accumulator * M) / divisor) >> 14, at least 1. The divisor is 100 for every stat, except that HP and MP use 10 and a cap of 65535 (instead of 999) when bit 2 of work+6 is set (I: the egg/monster flag).
- V: caps: HP and MP 999, SP 50, PA and MA 99. The accumulator itself is clamped to 24 bits and written back.
- V: destinations: HP max +50 and MP max +54 always; current HP +48 and current MP +52 only when `flags` is 0. SP goes to +58, PA to +56, MA to +57, all three skipped when `flags` bit 0 is set.
  - V: the store instructions are `0x140277082` (current HP), `0x140277078` (max HP), `0x140277058` (current MP), `0x14027704E` (max MP), `0x140277011` (SP), `0x140277048` (PA), `0x14027703E` (MA).
- V: when bit 1 of work+155 is set, HP is multiplied by 6/5 after the cap (I: a status or equipment effect).
- V: SP also gets the signed word at extra+128 added when `extra` is non-null and `flags` bit 0 is clear.
- V: when `flags` is 0 and the slot id at work+2 is 0xFE, the accumulators are first re-grown from level 2 up to the level at work+41, using raw += raw / (C - 1 + n) for n = 2..level. A C of 0 counts as 1.
- I: the 0xFE branch rebuilds a generated unit's stats from level 1 values; other units keep the accumulators they already carry.

## Referenced by

- Called by: [Unit_ApplyEquipment](Unit_ApplyEquipment.md), [Unit_BuildFromRecord](Unit_BuildFromRecord.md), [sub_140275EF4](sub_140275EF4.md)
- Observed behaviours: [EntryGrowthBonusesByPlayMode](../behaviors/EntryGrowthBonusesByPlayMode.md)

## Notes

Stat accumulators are 24-bit fixed point: the >> 14 means a stock accumulator near 16384 * 100 / M gives the raw stat. The record offsets here are the work-record (C) layout; the same five accumulators sit at +32..+46 of the save record (A), which Unit_ApplyLevelGrowth edits.

C1 (2026-10-30): the work record C is the **live** battle unit record: `g_BattleUnitTable` (`0x141853CE0`) is an
array of 21 C records (stride 512), not a copy. `UnitWork_BuildFromSaveIndex` calls this function with `flags = 0`,
so a roster build sets current HP/MP equal to max; after that `Battle_ApplyActionResult` (`0x14030A488`) is the only
writer of current HP/MP (`0x14030A62F`, `0x14030A638`). See `docs/reference/battle-units.md` for the field table and
the three independent readers per field.

## Open questions

Meaning of the extra argument's word at +128 (a caller-supplied SP bonus?), and the exact source of the work+155 bit.
