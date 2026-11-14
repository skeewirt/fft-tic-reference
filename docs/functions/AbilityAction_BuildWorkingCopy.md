# AbilityAction_BuildWorkingCopy

- **Address:** `0x1402BAE24`
- **Area:** [Ability data](../areas/ability-data.md)
- **Prototype:** `void AbilityAction_BuildWorkingCopy(void)`
- **Callers:** AbilityAction_GetRecord
- **Callees:** memmove, sub_1403D325C (registry lookup), sub_1403D3BE4 (row by index), sub_1403D2FD8 (row data pointer)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the writable ability action table: copies the executable's built-in table of 368 records (20 bytes each) and then overwrites fields from the OverrideAbilityActionData nxd table (id 247). This is how nxd data can change ability range, formula, CT or MP cost without touching the executable.

## Behavior

- V: copies 0x1CC0 bytes (368 records x 20) from the built-in table to the working table in one move.
- V: looks up nxd table 247 (cached in a global after the first lookup) and walks its rows by row index, one row per ability id, up to the table's row count.
- V: a field is overwritten only when the override cell is not negative; a negative cell leaves the built-in value.
- V: record layout of the 20 bytes: +0 Range, +1 EffectArea, +2 Vertical, +3..4 first flag list, +5..6 second flag list, +7 Element, +8 Formula, +9 X, +10 Y, +11 InflictStatus, +12 CT, +13 MPCost. The remaining bytes (+14..19) are never written by this function.
- V: the two flag lists are list cells in the nxd row (count at +8 / +16, data offset at +4 / +12); the first two entries of each list become the two bytes.
- I: a live comparison of the built-in table and the working copy showed 47 differing bytes, all in the CT and MPCost columns, matching the stock override rows.

## Referenced by

- Called by: [AbilityAction_GetRecord](AbilityAction_GetRecord.md)
- Reads tables: [AbilityActionRecords](../tables/AbilityActionRecords.md)

## Notes

The working copy (0x14078B2E0) is filled by a memmove (source lea at 0x1402BAE42); the nxd 247 overrides then apply on top. The copy is built lazily on the first AbilityAction_GetRecord call.

About 40 call sites read records through AbilityAction_GetRecord; the formula, range and cost code all read this working copy.

## Open questions

Meaning of the zero bytes at +14..15 and the all-ones bytes at +16..19.
