# Unit_BuildInnateStatuses

- **Address:** `0x140278688`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Unit_BuildInnateStatuses(void *unit, int reload)`
- **Callers:** sub_140278C1C, sub_14028531C, PartyUnit_ReloadEquipment, sub_14030BF04, sub_14033E4C4, sub_14039651C
- **Callees:** sub_140276DF4, sub_140277C58, Unit_LoadEquipmentAndEvade, sub_1402779EC, sub_14027788C, Unit_ReinitStatusCountdowns, sub_1401FB064

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the three innate status groups of a unit from its job row, its equipment attributes and its permanent extra set, restores the battle-applied set, and refreshes the status display.

## Behavior

- V: the fourth innate source at unit +0x198 is ORed into the group at +0x61 before the job row is copied, matching the fourth group reported in the status model.
- V: the job row is selected from the unit job byte at +3 (with the Mime special case at 0xA1), and its three five-byte status sets are copied over the groups at +0x57, +0x5C and +0x61.
- V: the battle-applied set at +0x1EF is saved on the stack before the copy and restored afterwards.
- V: the equipment attribute apply (sub_1402779EC) then ORs the status bytes of the equipped items into the same groups.
- V: it calls Unit_LoadEquipmentAndEvade and sub_14027788C to rebuild the ability/RSM side, and sub_140276DF4 for the stat block.
- V: Unit_ReinitStatusCountdowns runs at the end for the two reload variants, and sub_1401FB064 refreshes the status icon/flag owner.
- V: the second argument selects the reload path; the six callers include the job-change, equipment-change and save-reload paths.
- I: the fourth group at +0x198 has no identified producer, so the extra innate statuses are only as complete as whatever fills that field.
- ?: whether an equipment status in group 3 survives the first battle refresh; the order of the copy and the restore here does not settle it.
- V: it saves +0x1EF before the rebuild and writes that copy back afterwards (never +0x61 into +0x1EF), and it rewrites Move +0x42 and Jump +0x43 from the job row (+24, +25 & 0x7F) before the equipment bonuses; the PA / MA / Speed bases +0x38..+0x3A are kept (Unit_ComputeStats runs with mode 1 through its callee sub_1402779EC) and only the totals +0x3E..+0x40 are rebuilt (in that callee).

## State touched

- Calls: [Unit_LoadEquipmentAndEvade](Unit_LoadEquipmentAndEvade.md), [sub_1402779EC](sub_1402779EC.md), [Unit_ReinitStatusCountdowns](Unit_ReinitStatusCountdowns.md), [sub_1401FB064](sub_1401FB064.md)
- Reads: [g_JobTable](../globals/g_JobTable.md)
- Writes: [UnitWorkRecord](../structs/UnitWorkRecord.md)

## Referenced by

- Observed behaviours: [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md)

## Notes

Whole function read (612 bytes). The order of the group writes was checked; the source of +0x198 remains open.

## Open questions

None recorded.
