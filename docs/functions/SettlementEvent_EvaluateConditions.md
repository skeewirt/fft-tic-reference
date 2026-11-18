# SettlementEvent_EvaluateConditions

- **Address:** `0x140343AF8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int SettlementEvent_EvaluateConditions(unsigned int row, unsigned int mask)`
- **Callers:** sub_14015B970, sub_1401DF5B4, sub_140247E8C
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdTable_GetEntryCount, NxdTable_GetEntryByKeys3, the 44 condition handlers

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Evaluates the condition lists of one row of the settlement event data table (table 199) and reports whether the settlement's event may start.

## Behavior

- V: finds the table 199 in the data registry and the row by id, then walks the row's entries; each entry's condition list is a run of 16-bit opcode words below 44 followed by their arguments.
- V: for each opcode word it calls the handler from the 44-entry condition handler table (0x140684E90); handlers read event variables (equal to, below a value, gil at least n x 10 ...) and set bit 1 of a fail flag when the test fails.
- V: the mask argument selects which result bits matter (the callers pass 8 to ask whether an event is active).
- I: the lists belong to the settlement events (the callers are the town status text and the location availability test).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdTable_GetEntryCount](NxdTable_GetEntryCount.md), [NxdTable_GetEntryByKeys3](NxdTable_GetEntryByKeys3.md)

## Referenced by

- Reads tables: [NxdDataEnhancedWorldEvent](../tables/NxdDataEnhancedWorldEvent.md)

## Notes

Read: the head and the handler loop; the result assembly was not followed.

## Open questions

?: the full meaning of the returned value; the entry types 1 and 34 of the rows.
