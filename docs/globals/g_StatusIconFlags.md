# g_StatusIconFlags

- **Kind:** global
- **Address:** `0x1406735D0`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint32[]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The per-status flag words the status panel update reads: index status+1, no bound check. Entries past 40 exist, so a forty-first status reads a meaningful but unintended value.

## Behavior

- V: the status update switches on the id and reads this table in its default case.

## Referenced by

- Described by tables: [StatusIconFlags](../tables/StatusIconFlags.md)
- Read by: [sub_1401FB064](../functions/sub_1401FB064.md)

## Open questions

None recorded.
