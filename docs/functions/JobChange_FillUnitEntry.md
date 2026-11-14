# JobChange_FillUnitEntry

- **Address:** `0x14033751C`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `void JobChange_FillUnitEntry(void *entry, char slot, void *a3, char current)`
- **Callers:** sub_140337DA0 (job-change screen events), sub_140336F5C
- **Callees:** sub_1400C6178, sub_1400B1D24, sub_14028662C, sub_1400F72F0, Item_CountTotal, Inventory_AddCount, sub_140289FAC, sub_1400FBB7C, JobRecord_FillIconAndGenericFlag, sub_1400FB8E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills one 704-byte unit entry of the job-change screen: unit name, job list state, the current JobRecord/icon and the five equipped ability ids.

## Behavior

- V: stores the slot at entry+693; reads the viewed unit g_PartyUnits[word_141811428] and writes its name (party record unit+376+88*slot) via sub_1400C6178 / sub_1400B1D24.
- V: sets entry+164 = 2, then walks the job ids returned by sub_14028662C(unitIndex, &list, 0); when sub_1400F72F0(id, unitJob) is true it sets entry+164 = 0 and adopts that id.
- V: clears five 16-byte slots at entry+180 and five 88-byte slots at entry+332, then marks a slot 2 when the candidate job fails the Item_CountTotal / Inventory_AddCount / sub_140289FAC availability checks.
- V: builds a unit snapshot (job row +189, levels +202, flags +112, job id +36), calls JobRecord_FillIconAndGenericFlag(entry+156, ...), copies five job ids to entry+172 (16-byte stride) and five ability records to entry+252 (88-byte stride, sub_1400FB8E4).
- V: when `current` is set it renders the unit preview (sub_140103C50 / sub_1402C1628 / sub_1400ED124), otherwise clears it (sub_140115148).

## State touched

- Calls: [Item_CountTotal](Item_CountTotal.md), [Inventory_AddCount](Inventory_AddCount.md), [JobRecord_FillIconAndGenericFlag](JobRecord_FillIconAndGenericFlag.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Observed behaviours: [JobListBuilderCallersHold24Words](../behaviors/JobListBuilderCallersHold24Words.md)

## Notes

The caller hands the 704-byte entry to sub_140115CC8 / sub_140117BEC; only the writes above are verified.

## Open questions

Full layout of the 704-byte entry and the meaning of the five slot state values.
